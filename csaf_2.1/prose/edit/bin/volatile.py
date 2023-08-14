#! /usr/bin/env python
"""Volatile script file for prototyping that may take on different behaviors in time.

This one off script is a constant place to document the early stages of tools for processing the editable
sources and build the delivery items.

Currently impersonating phase zero concatenate and map from the initial sources to the GFM+gh_cosmetics file.
"""
import json
import pathlib
import re
import os
import sys
from typing import Union

import yaml

ENCODING = 'utf-8'
NL = '\n'
CB_END = '}'
COLON = ':'
FULL_STOP = '.'
HASH = '#'
PARA = '§'
SEMI = ';'
SPACE = ' '
TM = '™'

# Optionally dump the look-up tables (LUT)s for section display and label:
DUMP_LUT = bool(os.getenv('DUMP_LUT', ''))

# Configuration and runtime parameter candidates:
BINDER_AT = pathlib.Path('etc') / 'bind.txt'
SOURCE_AT = pathlib.Path('src')
BUILD_AT = pathlib.Path('build')
SECTION_DISPLAY_TO_LABEL_AT = pathlib.Path('etc') / 'section-display-to-label.json'
SECTION_LABEL_TO_DISPLAY_AT = pathlib.Path('etc') / 'section-label-to-display.json'

# Parsers and magical literals:
IS_CITE_REF = 'cite'
CITE_REF_DETECT = re.compile(r'\\\[\[(?P<text>cite)\]\(#(?P<label>[^)]+)\)\\\]')  # \[[ref](#label)\] pattern
IS_SEC_REF = 'sec'
SEC_REF_DETECT = re.compile(r'\[(?P<text>sec)\]\(#(?P<label>[^)1-9]+)\)')  # [ref](#label) pattern
MD_REF_DETECT = re.compile(r'\[(?P<text>[^]]+)\]\(#(?P<target>[^)]+)\)')  # [ref](#anylabel) pattern

# Detecting code block references with label values
# e.g. ' #  ((#run-object)).'
SEC_LABEL_BRACKET_CB_DETECT = re.compile(r'\ +#\ +[^(]+\((?P<label>\(#(?P<value>[0-9a-z-]+)\))\)\.')
# e.g. ' #  (#run-object).'
SEC_LABEL_FREE_CB_DETECT = re.compile(r'\ +#\ +[^(]+(?P<label>\(#(?P<value>[0-9a-z-]+)\))\.')

# Reverse detection patterns for documentation purposes
# e.g. ' # A run object (§3.14).' or ' #  (§3.1.2).'
SEC_DISP_BRACKET_CB_DETECT = re.compile(r'\ +#\ +[^(]+\((?P<disp>§[0-9.]+)\)\.')
SEC_DISP_FREE_CB_DETECT = re.compile(r'\ +#\ +[^(]+(?P<disp>§[0-9.]+)\.')  # e.g. ' # See §3.14.14.'

# Specific tokens:
HC_BEG = '<!--'
HC_END = '-->'
YAML_SEP = '---'
TOK_TOC = '(#$thing$)'  # Transform phase ToC label string template replacing $thing$ with the old value
TOK_SEC = "<a id='$thing$'></a>"  # Transform phase section title label string template ($thing$ -> old value)
TOK_LAB = '{#'
H = '#'
TOC_HEADER = """Table of Contents
"""
CLEAN_MD_START = '# Introduction'

SECTION_DISPLAY_TO_LABEL = {}
SEC_LABEL_TEXT = {}  # Mapping section labels to the display text

TOC_TEMPLATE = {
    1: '$sec_cnt_disp$ [$text$](#$label$)  ',
    2: '\t$sec_cnt_disp$ [$text$](#$label$)  ',
    3: '\t\t$sec_cnt_disp$ [$text$](#$label$)  ',
    4: '\t\t\t$sec_cnt_disp$ [$text$](#$label$)  ',
    5: '\t\t\t\t$sec_cnt_disp$ [$text$](#$label$)  ',
}

# This value leads to empty line needed on GitHub to respect the new line for non-numerically starting lines
TOC_VERTICAL_SPACER = ''

# Data interface robustness hacks:
CHILDREN = 'children'
ENUMERATE = 'enumerate'
LABEL = 'label'
TOC = 'toc'

CITE_COSMETICS_TEMPLATE = '**\\[**<span id="$label$" class="anchor"></span>**$code$\\]** $text$'
CITATION_SOURCES = ('introduction-03-normative-references.md', 'introduction-04-informative-references.md')
GLOSSARY_SOURCES = ('introduction-02-terminology-glossary.md',)

# Type declarations:
META_TOC_TYPE = dict[str, dict[str, Union[bool, str, list[dict[str, str]]]]]


def load_binder(binder_at: Union[str, pathlib.Path]) -> list[pathlib.Path]:
    """Load the linear binder text file into a list of file paths."""
    with open(binder_at, 'rt', encoding=ENCODING) as resource:
        return [pathlib.Path(entry.strip()) for entry in resource.readlines() if entry.strip()]


def end_of_toc_in(text: str) -> bool:
    """Detect the end of the table of contents."""
    return text.startswith('#') and ' Introduction' in text


def detect_meta(text_lines: list[str]) -> tuple[META_TOC_TYPE, list[str]]:
    """Extract any YAML data from top, remove used lines from text lines, and yield meta as well as remaining lines."""
    meta_lines = []
    if text_lines[0].startswith(HC_BEG) and text_lines[1].startswith(YAML_SEP):
        for line in text_lines[2:]:
            if line.startswith(YAML_SEP):
                break
            meta_lines.append(line)

    from_here = len(meta_lines) + 4
    if from_here > 4:
        text_lines = text_lines[from_here:]

    return yaml.safe_load(''.join(meta_lines)) if meta_lines else {}, text_lines


def load_document(path: Union[str, pathlib.Path]) -> tuple[META_TOC_TYPE, list[str]]:
    """Load the text file into a list of strings and harvest any YAML meta info (if present remove the lines)."""
    with open(path, 'rt', encoding=ENCODING) as resource:
        return detect_meta(resource.readlines())


def dump_assembly(text_lines: list[str], to_path: Union[str, pathlib.Path]) -> None:
    """Dump the lines of text into the text file at path."""
    with open(to_path, 'wt', encoding=ENCODING) as resource:
        resource.write(''.join(text_lines))


def label_derive_from(text: str) -> str:
    """Transform text to kebab style conventional label assuming no newlines present."""
    good_nuff = (' ', '.', ',', ';', '?', '!', '_', '(', ')', '[', ']', '{', '}', '<', '>', '\\', '/', '$', ':')
    slug = text.strip()
    for bad in good_nuff:
        slug = slug.replace(bad, '-')
    parts = slug.split('-')
    slug = '-'.join(s for s in parts if s and s != '-')
    return slug.lower()


def label_in(text: str) -> bool:
    """Detect if the text line contains a label."""
    return '](#' in text


def code_block_label_in(text: str) -> bool:
    """Detect if the text line contains a code block section label."""
    return '(#' in text and ' # ' in text


def load_label_to_display_lut(path: Union[str, pathlib.Path] = SECTION_LABEL_TO_DISPLAY_AT) -> dict[str, str]:
    """Load the LUT for section labels -> display."""
    with pathlib.Path(path).open('rt', encoding=ENCODING) as handle:
        return json.load(handle)


def main(argv: list[str]) -> int:
    """Drive the assembly."""

    bind_seq_path = pathlib.Path(argv[0]) if argv else BINDER_AT
    binder = load_binder(bind_seq_path)
    for resource in binder:
        if not (SOURCE_AT / resource).is_file():
            print(f'Problem reading {resource}')
            return 1

    display_from = load_label_to_display_lut()

    lines: list[str] = []
    meta_hooks = {}
    first_meta_slot = None
    for resource in binder:
        meta, part_lines = load_document(SOURCE_AT / resource)
        if part_lines[-1] != NL:
            part_lines.append(NL)
        if meta:
            meta_hooks[len(lines)] = meta
            meta_hooks[len(lines) + len(part_lines) - 1] = {}
            if first_meta_slot is None:
                first_meta_slot = len(lines) + len(part_lines) - 1

        if resource.name in CITATION_SOURCES:  # TODO: citation management -> class
            patched = []
            in_citation = False
            for line in part_lines:
                if line.startswith(HASH):
                    patched.append(line)
                    continue
                if line.strip() and not line.startswith(COLON):
                    # the term -> citation code, the visible text in the square brackets
                    in_citation = True
                    # prepare the data triplet
                    code = line.strip()
                    label = code.replace(COLON, SEMI).rstrip(TM)
                    text = ''
                    continue
                if in_citation:
                    if line.startswith(COLON):
                        text += line.lstrip(COLON).strip()
                        continue
                    if line.strip():
                        text += SPACE + line.strip()
                        continue
                    if not line.strip():
                        citation = (
                            CITE_COSMETICS_TEMPLATE.replace('$label$', label)
                            .replace('$code$', code)
                            .replace('$text$', text)
                            + NL
                        )
                        in_citation = False
                        patched.append(citation)
                        patched.append(line)
                        continue
                else:
                    patched.append(line)
            part_lines = [a for a in patched]

        if resource.name in GLOSSARY_SOURCES:  # TODO: glossary management -> class
            patched = ['<dl>' + NL]
            in_definition = False
            for line in part_lines:
                if not in_definition and line.strip() and not line.startswith(COLON):
                    # the term -> glossary term, the visible text in the square brackets for refs
                    in_definition = True
                    # prepare the data triplet
                    term = line.strip()
                    label = 'def;' + label_derive_from(term)
                    definition = ''
                    continue
                if in_definition:
                    if line.startswith(COLON):
                        definition += line.lstrip(COLON).strip()
                        continue
                    if line.strip():
                        definition += '<br><br>' + NL + ' ' * 6 + line.strip()
                        continue
                    if not line.strip():
                        for ref in MD_REF_DETECT.finditer(definition):
                            if ref:
                                # Found ref in markdown format
                                found = ref.groupdict()
                                text = found['text']
                                target = found['target']
                                md_ref = f'[{text}](#{target})'
                                html_ref = f'<a href="#{target}">{text}</a>'
                                definition = definition.replace(md_ref, html_ref)

                        item = f'{" " * 2}<dt id="{label}">{term}</dt>\n{" " * 2}<dd>{definition}</dd>\n'
                        in_definition = False
                        patched.append(item)
                        continue
                else:
                    patched.append(line)
            patched.append('</dl>' + NL + NL)
            part_lines = [a for a in patched]

        lines.extend(part_lines)

    # TODO: counter management -> class
    lvl_min, lvl_sup = 1, 7
    sec_cnt = {f'{H * level} ': 0 for level in range(lvl_min, lvl_sup)}
    sec_lvl = {f'{H * level} ': level for level in range(lvl_min, lvl_sup)}
    lvl_sec = {level: f'{H * level} ' for level in range(lvl_min, lvl_sup)}
    H1 = f'{H} '
    cur_lvl = sec_lvl[H1]
    meta_hook = {}
    # TODO: ToC builder -> class
    tic_toc = [TOC_HEADER]
    did_appendix_sep = False
    clean_headings = False
    for slot, line in enumerate(lines):
        if meta_hooks.get(slot) is not None:
            meta_hook = meta_hooks[slot]
        is_plain = True  # No special meta data needed
        if line.startswith(CLEAN_MD_START):
            clean_headings = True
        for tag in sec_cnt:
            if line.startswith(tag) and clean_headings:
                # manage counter
                if not meta_hook:
                    # auto counters
                    is_plain = True
                    nxt_lvl = sec_lvl[tag]
                    sec_cnt[tag] += 1
                    if nxt_lvl < cur_lvl:
                        for level in range(nxt_lvl + 1, lvl_sup):
                            sec_cnt[lvl_sec[level]] = 0
                    sec_cnt_disp_vec = []
                    for s_tag, cnt in sec_cnt.items():
                        if cnt == 0:
                            raise RuntimeError(f'counting is hard: {sec_cnt} at {tag} for {slot}:{line.rstrip(NL)}')
                        sec_cnt_disp_vec.append(str(cnt))
                        if s_tag == tag:
                            break
                    sec_cnt_disp = FULL_STOP.join(sec_cnt_disp_vec)
                    # Hack to amend first level numeric section counter displays with a full stop - do not ask ...
                    if FULL_STOP not in sec_cnt_disp:
                        sec_cnt_disp += FULL_STOP
                else:
                    # pull in counters from meta
                    is_plain = False
                    app_lvl = 1  # belt and braces ...
                    text = line.split(tag, 1)[1].rstrip()
                    if TOK_LAB in text:
                        # special label
                        label = text.split(TOK_LAB, 1)[1].rstrip(CB_END)
                        text = text.split(TOK_LAB, 1)[0]
                    if text == meta_hook[TOC][LABEL]:
                        sec_cnt_disp = meta_hook[TOC][ENUMERATE]  # type: ignore
                        app_lvl = 1
                    elif meta_hook[TOC].get(CHILDREN):
                        for cand in meta_hook[TOC][CHILDREN]:  # type: ignore
                            if text == cand[LABEL]:  # type: ignore
                                sec_cnt_disp = cand[ENUMERATE]  # type: ignore
                                app_lvl = 2

                # manage label
                text = line.split(tag, 1)[1].rstrip()
                if TOK_LAB in text:
                    # special label
                    label = text.split(TOK_LAB, 1)[1].rstrip(CB_END)
                    text = text.split(TOK_LAB, 1)[0]
                else:
                    label = label_derive_from(text)
                clean_sec_cnt_disp = (f'{sec_cnt_disp}' if is_plain else sec_cnt_disp).rstrip(FULL_STOP)
                SEC_LABEL_TEXT[label] = clean_sec_cnt_disp
                SECTION_DISPLAY_TO_LABEL[clean_sec_cnt_disp] = label
                line = tag + text + ' ' + TOK_SEC.replace('$thing$', label)

                line = line.replace(tag, f'{tag}{sec_cnt_disp} ', 1) + NL
                lines[slot] = line
                cur_lvl = nxt_lvl
                if not did_appendix_sep and meta_hook and slot < first_meta_slot:  # type: ignore
                    tic_toc.append(TOC_VERTICAL_SPACER)
                    did_appendix_sep = True
                toc_template = TOC_TEMPLATE[cur_lvl if not meta_hook else app_lvl]
                tic_toc.append(
                    toc_template.replace('$sec_cnt_disp$', sec_cnt_disp)
                    .replace('$text$', text)
                    .replace('$label$', label)
                )

    # Process the text display of citation refs
    for slot, line in enumerate(lines):
        if label_in(line):
            for ref in CITE_REF_DETECT.finditer(line):
                if ref:
                    # Found citation label in markdown format
                    found = ref.groupdict()
                    trigger_text = found['text']
                    if trigger_text != IS_CITE_REF:
                        raise RuntimeError(f'false positive cite ref in ({line.rstrip(NL)})')
                    label = found['label']
                    text = label.replace(';', ':')
                    sem_ref = f'\\[[cite](#{label})\\]'
                    evil_ref = f'\\[[{text}](#{label})\\]'  # \[[GFMCMARK](#GFMCMARK)\]
                    line = line.replace(sem_ref, evil_ref)
                    lines[slot] = line
            if '[CWE](#CWE)' in line:
                lines[slot] = line.replace('[CWE](#CWE)', f'[CWE{TM}](#CWE)')  # Do not ask. Thanks.
            if '[F.2](#' in line:
                lines[slot] = line.replace('[F.2](#', '[Appendix F.2](#')  # Do not ask. Thanks.
            if '[F.4](#' in line:
                lines[slot] = line.replace('[F.4](#', '[Appendix F.4](#')  # Do not ask. Thanks.

    # Process the text display of section refs TODO
    for slot, line in enumerate(lines):
        if label_in(line):
            for ref in SEC_REF_DETECT.finditer(line):
                if ref:
                    # Found section label in markdown format
                    found = ref.groupdict()
                    trigger_text = found['text']
                    if trigger_text != IS_SEC_REF:
                        raise RuntimeError(f'false positive sec ref in ({line.rstrip(NL)})')
                    label = found['label']
                    if label not in SEC_LABEL_TEXT:
                        raise RuntimeError(f'missing register label for sec ref in ({line.rstrip(NL)})')
                    text = SEC_LABEL_TEXT[label]
                    sem_ref = f'[sec](#{label})'
                    evil_ref = f'[{text}](#{label})'  # [GFMCMARK](#GFMCMARK)
                    line = line.replace(sem_ref, evil_ref)
                    lines[slot] = line

    # Process the code blocks for references to map from label to display value
    for slot, line in enumerate(lines):
        if code_block_label_in(line):
            for ref in SEC_LABEL_BRACKET_CB_DETECT.finditer(line):
                if ref:
                    # Found bracketed label ref to section in code block
                    found = ref.groupdict()
                    value = found['value']
                    if not value or value not in display_from:
                        continue
                    label = found['label']
                    display = display_from[value]
                    sem_ref = label
                    disp_ref = display
                    line = line.replace(sem_ref, disp_ref)
                    lines[slot] = line
            for ref in SEC_LABEL_FREE_CB_DETECT.finditer(line):
                if ref:
                    # Found free label ref to section in code block
                    found = ref.groupdict()
                    value = found['value']
                    if not value or value not in display_from:
                        continue
                    label = found['label']
                    display = display_from[value]
                    sem_ref = label
                    disp_ref = display
                    line = line.replace(sem_ref, disp_ref)
                    lines[slot] = line

    tic_toc.append(NL)
    # Inject the table of contents:
    for slot, line in enumerate(lines):
        if end_of_toc_in(line):
            lines[slot] = NL.join(tic_toc) + line
            break

    # remove any trailing blank line
    while lines[-1] == NL:
        del lines[-1]

    BUILD_AT.mkdir(parents=True, exist_ok=True)
    dump_assembly(lines, BUILD_AT / 'tmp.md')

    if DUMP_LUT:
        with SECTION_DISPLAY_TO_LABEL_AT.open('wt', encoding=ENCODING) as handle:
            json.dump(SECTION_DISPLAY_TO_LABEL, handle, indent=2)
        SECTION_LABEL_TO_DISPLAY = {
            label: disp for label, disp in sorted((label, disp) for disp, label in SECTION_DISPLAY_TO_LABEL.items())
        }
        with SECTION_LABEL_TO_DISPLAY_AT.open('wt', encoding=ENCODING) as handle:
            json.dump(SECTION_LABEL_TO_DISPLAY, handle, indent=2)

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
