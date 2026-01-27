#! /usr/bin/env python
"""Validate YAML partial information models against their underlying JSON schema."""
import glob
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

OK = 'OK'
FAIL = 'FAIL'

PathLike = str | pathlib.Path
SomeType = dict[int, list[str]]

VALERY_JSON_SCHEMA = os.getenv('VALERY_JSON_SCHEMA', '../../json_schema/csaf.json')

if not pathlib.Path(VALERY_JSON_SCHEMA).is_file():
    print('Please set environment variable VALERY_JSON_SCHEMA to location of targeted JSON schema file')
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


def level_warp(raw_finds: dict[str, str], jpath: str) -> None:
    """Inplace into and out of the fold ..."""
    if 'type' in raw_finds:
        return {jpath.split(DOT)[-1]: raw_finds['type']}
    if '$ref' in raw_finds:
        return {jpath.split(DOT)[-1]: raw_finds['$ref'].replace('#/$defs/', '$defs.')}
    return raw_finds


def rel_path_or(to_loc: PathLike, from_loc: PathLike = None, fallback: PathLike | None = None) -> str:
    """Derive the relative path from src to tgt or on failure the fallback."""
    if from_loc is None:
        from_loc = pathlib.Path()  # Default is the current working dir
    if fallback is None:
        fallback = to_loc  # Default is the "to" location
    try:
        return str(pathlib.Path(to_loc).absolute().relative_to(pathlib.Path(from_loc).absolute()))
    except:  # noqa
        return fallback


def extract_verbosity_if(args: list[str]) -> bool:
    """Extract any verbosity arguments and return the result."""
    verbosity = False
    for pos, arg in enumerate(list(args)):
        if arg in ('-v', '--verbose'):
            verbosity = True
            del args[pos]
    return verbosity


def extract_quietness_if(args: list[str]) -> bool:
    """Extract any quietness arguments and return the result."""
    quietness = False
    for pos, arg in enumerate(list(args)):
        if arg in ('-q', '--quiet'):
            quietness = True
            del args[pos]
    return quietness


def do_that(ln, lt, k, vd, vadet) -> str:
    """Later."""
    jp_status = OK
    if ln != k:
        vadet.append(f'ERROR: leaf {ln} does not match expected field {k}')
        jp_status = FAIL
    if vd == 'string':
        if lt.lower() != vd and not lt.lower().startswith(vd):
            vadet.append(
                f'ERROR: leaf type {lt} of {ln}'
                f' does not match expected string type {vd}'
            )
            jp_status = FAIL
    elif vd == 'array':
        if lt.lower() != 'sequence':
            vadet.append(
                f'ERROR: leaf type {lt} of {ln}'
                f' does not match expected sequence type {vd}'
            )
            jp_status = FAIL
    elif vd == 'object':
        if lt.lower() != 'mapping':
            vadet.append(
                f'ERROR: leaf type {lt} of {ln}'
                ' does not match expected mapping type {vd}'
            )
            jp_status = FAIL
    elif lt.startswith('$defs.'):
        if lt != vd:
            vadet.append(
                f'ERROR: leaf type {lt} of {ln}'
                ' does not match expected mapping type reference {vd}'
            )
            jp_status = FAIL
    return jp_status


def leaf_types_shape_ok(leaf_types: list[tuple[str, str]], vadet: list[str]) -> bool:
    """Iterate over leaf name-type pairs and return false if any is not a pair."""
    valid = True
    for x in leaf_types:
        if len(x) != 2:
            vadet.append(f'ERROR: Not a pair of leaf and type: {x}')
            valid = False
    return valid


def main(args: list[str]) -> int:
    """Drive the validation."""
    quiet = extract_quietness_if(args)
    verbose = extract_verbosity_if(args)
    if quiet:
        verbose = False
    if not args:
        some_path = rel_path_or(__file__)
        print(f'usage: {some_path} markdown-file(s)-or-glob-with-yaml-outline-fenced-code-block')
        return 2


    with open(VALERY_JSON_SCHEMA, 'rt', encoding=ENCODING, errors=ENC_ERRS) as handle:
        data = json.load(handle)

    file_paths = sorted(set(file_path for arg in args for file_path in glob.glob(arg)))
    passes = True
    varep = []
    file_count = len(file_paths)
    for file_no, file_path in enumerate(file_paths):
        record = []
        with open(file_path, 'rt', encoding=ENCODING, errors=ENC_ERRS) as handle:
            paths, snippets = extract_paths_and_snippets([line.rstrip(NL) for line in handle])
        valog = f'file({rel_path_or(file_path)}): $file_status$'
        file_status = OK
        snip_count = len(paths)
        snap = 0
        for slot, jpaths in paths.items():
            snap += 1
            fence_length = len(snippets[slot])
            vasnip = f'snip({rel_path_or(file_path)})[{slot + 1},{slot + 1 + fence_length + 1}]: $snip_status$'
            snip_status = OK
            snip_rep = []
            stripped_yaml = yaml_strip(snippets[slot])
            vadet = [EQ * 69]
            vadet.extend(stripped_yaml)
            leaf_types = yaml_leaf_types(stripped_yaml)
            if not leaf_types_shape_ok(leaf_types, vadet):
                snip_status = FAIL
                file_status = FAIL
                passes = False
            jp_count = len(jpaths)
            for jslot, jpath in enumerate(jpaths):
                vadet.append(DASH * 69)
                vapath = f'path({rel_path_or(file_path)})[{slot + 1},{slot + 1 + fence_length + 1}]{{{jpath}}}: $jp_status$'
                jp_status = OK
                jp_rep = []
                found = jp.findall(jpath, data)[0]
                level_warp(found, jpath)
                vadet.append(f'  json-path({jslot+1}/{jp_count}): {jpath} ==> {LS.join(found.keys())}')
                for k, v in found.items():
                    vd = find_type(v)
                    vadet.append(f'    {k} --> {vd}')
                vadet.append('- ' * 35)
                for (ln, lt), (k, v) in zip(leaf_types, found.items()):
                    vd = find_type(v)
                    if not jslot:
                        pass  # Later alligator - lots of expansions needed for many use cases
                    else:
                        jp_status = do_that(ln, lt, k, vd, vadet)
                    vadet.append(f'    {lt} ~ {vd}')
                    if jp_status == FAIL:
                        snip_status = FAIL
                        file_status = FAIL
                        passes = False

                    if jp_status == FAIL:
                        jp_rep.append(vapath.replace('$jp_status$', jp_status))

                if snip_status == FAIL or not quiet:
                    snip_rep.extend(jp_rep)
                    if jslot == len(jpaths) - 1:
                        if snip_status == FAIL:
                            snip_rep.append('= ' * 35)
                        snip_rep.append(vasnip.replace('$snip_status$', snip_status))

                if snip_status == FAIL:
                    snip_rep.extend(vadet)

            if snip_status == FAIL or not quiet:
                varep.extend(snip_rep)
            record.append('.' if snip_status == OK else 'x')

        if snap == snip_count:
            record_disp =  SP + ''.join(record) if not quiet else ''
            varep.append(valog.replace('$file_status$', f'{file_status}{record_disp}'))
            if verbose:
                varep.append('* ' * 35)

    print(NL.join(varep))

    return 0 if passes else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
