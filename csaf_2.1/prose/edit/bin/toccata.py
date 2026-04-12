#! /usr/bin/env python
import json
import pathlib
import sys
from typing import Union

ENCODING = 'utf-8'
NL = '\n'
SP = ' '
COLON = ':'
DASH = '-'
DOT = '.'

LANG_PATCH = '<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">'
LOGO_TARGET = 'https://docs.oasis-open.org/templates/OASISLogo-v3.0.png'

TOC_STARTSWITH_TRIGGER = '<h1 id="table-of-contents'
INTRO_STARTSWITH_TRIGGER = '<h1 id="1-introduction'

# Configuration and runtime parameter candidates:
BUILD_AT = pathlib.Path('build')
HTML_IN_AT = BUILD_AT / 'tmp.html'
TOC_AT = BUILD_AT / 'toc-mint.json'
LOGO_AT = pathlib.Path('..') / 'media' / 'logo-data-url.txt'
BASE_CSS_AT = pathlib.Path('..') / 'share' / 'style' / 'base.css'
SKIN_CSS_AT = pathlib.Path('..') / 'share' / 'style' / 'skin.css'

# Type declarations:
META_TOC_TYPE = dict[str, dict[str, Union[bool, str, list[dict[str, str]]]]]
SEC_LVL_CNT_TYPE = tuple[int, int, int, int, int, int]
APX_LVL_UNION_TYPE = Union[bool, int]
SEC_NUM_DISP_TYPE = str
SEC_TOC_TEXT = str
SEC_TOC_TARGET_SLUG = str
TOC_ENTRY_TYPE = tuple[SEC_LVL_CNT_TYPE, APX_LVL_UNION_TYPE, SEC_NUM_DISP_TYPE, SEC_TOC_TEXT, SEC_TOC_TARGET_SLUG]


def load_toc(toc_at: Union[str, pathlib.Path]) -> list[TOC_ENTRY_TYPE]:
    """Load the TOC JSON file into a list of toc entries."""
    with open(toc_at, 'rt', encoding=ENCODING) as resource:
        return [(tuple(e[0]), *e[1:]) for e in json.load(resource) if e]  # type: ignore # noqa


def generate_toc(toc_db: list[TOC_ENTRY_TYPE]) -> str:
    """Generate the table of contents from the database."""
    entries_prefix = ['<div id="toc_container">', '<ul class="toc_list">']
    entries_postfix = ['</ul>', '</div>']
    entries = []
    past = 0
    in_appendix = False
    for slot, toc_entry in enumerate(toc_db):
        levels, is_appendix_level, num_disp, text, slug = toc_entry
        pres = num_disp.rstrip('.').count(DOT) + 1 if not is_appendix_level else is_appendix_level
        if is_appendix_level and not in_appendix:
            in_appendix = True
            # past = 3
        if past == 0:
            if pres != 1:
                raise RuntimeError(f'error in first toc db entry: ({toc_entry})')
            hack_a_did_ack = '<ul>' if slot else ''
            entries.append(f'{hack_a_did_ack}<li>{num_disp} <a href="#{slug}">{text}</a></li>')
            past = pres
            continue
        if pres == past:
            entries.append(f'<li>{num_disp} <a href="#{slug}">{text}</a></li>')
            past = pres
            continue
        if pres > past:
            patch_me = entries[slot - 1]
            there = len('</li>')
            entries[slot - 1] = patch_me[:-there] + '<ul>'
            entries.append(f'<li>{num_disp} <a href="#{slug}">{text}</a></li>')
            past = pres
            continue
        if pres < past:
            stack = past
            closing = ''
            while stack > pres:
                closing += '</ul></li>'
                stack -= 1
            entries.append(f'{closing}<li>{num_disp} <a href="#{slug}">{text}</a></li>')
            past = pres
            continue

    return NL.join(entries_prefix + entries + entries_postfix)


def main(argv: list[str]) -> int:
    """Drive the injections."""

    toc_db = load_toc(TOC_AT)
    # print(toc_db[0])
    # print(toc_db[1])
    # print("...")
    # print(toc_db[-1])
    the_toc = generate_toc(toc_db)
    # print(the_toc)

    with open('../share/style/base.css', 'rt', encoding=ENCODING) as handle:
        base_css = handle.read()
    with open('../share/style/skin.css', 'rt', encoding=ENCODING) as handle:
        skin_css = handle.read()
    with open(LOGO_AT, 'rt', encoding=ENCODING) as handle:
        logo_data = handle.read().strip()

    with open('build/tmp.html', 'rt', encoding=ENCODING) as handle:
        incoming = handle.readlines()

    outgoing = []
    in_toc = False
    for line in incoming:
        if in_toc:
            if line.startswith(INTRO_STARTSWITH_TRIGGER):
                in_toc = False
                outgoing.append(line)
            else:
                pass
            continue
        if not in_toc and line.startswith(TOC_STARTSWITH_TRIGGER):
            in_toc = True
            outgoing.append(line)
            outgoing.append(the_toc)
            continue
        if line.startswith('<html xmlns'):
            line = LANG_PATCH
        elif '</style>' in line:
            line = NL + base_css + NL + skin_css + NL + line
        elif 'style/base.css' in line:
            continue
        elif 'style/skin.css' in line:
            continue
        elif LOGO_TARGET in line:
            line = line.replace(LOGO_TARGET, logo_data)

        outgoing.append(line)

    with open('build/injected.html', 'wt', encoding=ENCODING) as handle:
        handle.write(''.join(outgoing))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
