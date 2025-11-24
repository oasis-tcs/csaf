#! /usr/bin/env python
"""Validate YAML partial information models against their underlying JSON schema."""
import importlib.util
import json
import os
import pathlib
import sys

if importlib.util.find_spec('jsonpath'):
    import jsonpath as jp
else:
    print('Please install a missing dependency: pip install python-jsonpath')
    sys.exit(2)

ENCODING = 'utf-8'
ENC_ERRS = 'ignore'
COLON = ':'
COMMA = ','
DASH = '-'
DOT = '.'
EQ = '='
HASH = '#'
NL = '\n'
SP = ' '
LS = COMMA + SP

YAML_FCB_ON = '```yaml '
YAML_FCB_OFF = '```'
HC_ON = '<!--'
HC_OFF = '-->'

SomeType = dict[int, list[str]]

CSAF_JSON_SCHEMA = os.getenv('CSAF_JSON_SCHEMA', '../../json_schema/csaf.json')

if not pathlib.Path(CSAF_JSON_SCHEMA).is_file():
    print('Please set environment variable CSAF_JSON_SCHEMA to location of CSAF JSON Schema file')
    sys.exit(2)


def extract_paths(complete_line: str, line_no: int) -> list[str]:
    """Extract the json-path(s) from fenced YAML code block starts."""
    json_paths: list[str] = []
    if complete_line.startswith('```yaml '):
        line = complete_line[8:].strip()
        if line.startswith(HC_ON) and line.endswith(HC_OFF):
            line = line[4:-3]
            if line.startswith('json-path(') and line.endswith(')'):
                if COMMA in line:
                    print(f'ERROR: Line {line_no+1} has multiple paths in json-path/1')
                    raise ValueError(
                        f'Use json-paths/n instead of json-path/1 in "{complete_line}"'
                    )
                json_paths.append(line[10:-1])
                return json_paths

            if line.startswith('json-paths(') and line.endswith(')'):
                line = line[11:-1]
                if COMMA not in line:
                    print(
                        f'ERROR: Line {line_no+1}'
                        ' has only one path in json-paths/n - forgotten comma?'
                    )
                    raise ValueError(
                        f'Add comma or use json-path/1 instead of json-paths/n in "{complete_line}"'
                    )
                json_paths.extend(part.strip() for part in line.split(','))

    return json_paths


def extract_paths_and_snippets(lines: list[str]) -> tuple[SomeType, SomeType]:
    """Extract the json-path(s) and fenced YAML code blocks."""
    slot_snippets: SomeType = {}
    slot_paths: SomeType = {}
    in_yaml_fcb, my_start = False, None
    for start, complete_line in enumerate(lines):

        if in_yaml_fcb:
            if complete_line.rstrip() == YAML_FCB_OFF:
                in_yaml_fcb = False
                my_start = start
                continue
            slot_snippets[my_start].append(complete_line.rstrip(NL))

        if not in_yaml_fcb:
            if complete_line.startswith(YAML_FCB_ON):
                in_yaml_fcb = True
                my_start = start
                slot_snippets[my_start] = []
                slot_paths[start] = extract_paths(complete_line, my_start)

    return slot_paths, slot_snippets


def yaml_strip(yaml_lines: list[str]) -> list[str]:
    """Strip commented out lines."""
    stripped = []
    for line in yaml_lines:
        if line.lstrip().startswith(HASH):
            continue
        stripped.append(line)

    return stripped


def yaml_leaf_types(yaml_lines: list[str]) -> list[tuple[str, str]]:
    """Naive sequence of leaf-type pairs extractor."""
    indents = []
    for line in yaml_lines:
        indent = 0
        if COLON in line:
            indent = len(line) - len(line.lstrip())
        indents.append(indent)
    leaf_indent = max(indents)

    collected: list[tuple[str, str]] = []
    for indent, line in zip(indents, yaml_lines):
        if indent < leaf_indent:
            continue
        leaf, leaf_type = line.strip().split(COLON)
        collected.append((leaf, leaf_type.strip()))

    return collected


def find_type(mapping) -> str:
    """Types are expected in some places."""
    if isinstance(mapping, str):
        return mapping

    if isinstance(mapping, dict):
        try:
            main_type = mapping['type']
            if main_type == 'string':
                if sub_type := mapping.get('format', ''):
                    if sub_type == 'date-time':
                        return 'string.datetime'
                    if sub_type == 'uri':
                        return 'string.uri'
                if 'enum' in mapping:
                    return 'string.enum'
                if 'pattern' in mapping:
                    return 'string.pattern'
            return main_type
        except KeyError:
            pass
        try:
            _ = mapping['enum']
            return 'string.enum'
        except KeyError:
            pass
        try:
            return mapping['$ref'].replace('#/$defs/', '$defs.')
        except KeyError:
            pass
        try:
            alternatives = mapping['oneOf']
            return LS.join(alternative['$ref'] for alternative in alternatives)
        except KeyError:
            pass

    return 'UNKNOWN'


def level_warp(raw_finds: dict[str, str]) -> dict[str, str]:
    """Into and out of the fold ..."""
    if 'type' in raw_finds:
        return {jpath.split(DOT)[-1]: raw_finds['type']}
    if '$ref' in raw_finds:
        return {jpath.split(DOT)[-1]: raw_finds['$ref'].replace('#/$defs/', '$defs.')}
    return raw_finds


try:
    in_md = sys.argv[1]
except IndexError:
    try:
        some_path = pathlib.Path(__file__).absolute().relative_to(pathlib.Path().absolute())
    except:  # noqa
        some_path = __file__
    print(f'usage: {some_path} markdown-file-with-yaml-outline-fenced-code-block')
    sys.exit(2)


with open(CSAF_JSON_SCHEMA, 'rt', encoding=ENCODING, errors=ENC_ERRS) as handle:
    data = json.load(handle)

with open(in_md, 'rt', encoding=ENCODING, errors=ENC_ERRS) as handle:
    paths, snippets = extract_paths_and_snippets([line.rstrip(NL) for line in handle])

for slot, jpaths in paths.items():
    print(slot)
    stripped_yaml = yaml_strip(snippets[slot])
    print(DASH * 69)
    for y_line in stripped_yaml:
        print(y_line)
    print(DASH * 69)
    leaf_types = yaml_leaf_types(stripped_yaml)
    for x in leaf_types:
        if len(x) != 2:
            print('ERROR: Not a pair of leaf and type:', x)
        print(x[0], '<--', x[1])
    print(DASH * 69)
    for jslot, jpath in enumerate(jpaths):
        found = level_warp(jp.findall(jpath, data)[0])
        print(' ', jpath, '==>', LS.join(found.keys()))
        for k, v in found.items():
            vd = find_type(v)
            print('   ', k, '-->', vd)
        print('- ' * 34)
        for (ln, lt), (k, v) in zip(leaf_types, found.items()):
            vd = find_type(v)
            if len(jpaths) > 1 and jslot:
                if ln != k:
                    print(f'ERROR: leaf {ln} does not match expected field {k}')
                if vd == 'string':
                    if lt.lower() != vd and not lt.lower().startswith(vd):
                        print(
                            f'ERROR: leaf type {lt} of {ln}'
                            f' does not match expected string type {vd}'
                        )
                if vd == 'array':
                    if lt.lower() != 'sequence':
                        print(
                            f'ERROR: {jslot};{len(jpaths)}leaf type {lt} of {ln}'
                            f' does not match expected sequence type {vd}'
                        )
                if vd == 'object':
                    if lt.lower() != 'mapping':
                        print(
                            f'ERROR: leaf type {lt} of {ln}'
                            ' does not match expected mapping type {vd}'
                        )
            print('   ', lt, '<-->', vd)
    print(EQ * 69)
