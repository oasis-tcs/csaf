#! /usr/bin/env python
"""Derive a Table of Contents (TOC) in HTML ordered list format from a toc-mint.json database.

The database is expected to provide a list of lists with the latter representing TOC entries.
Any such TOC entry provides five items with the following meaning (in the order they appear):

1. ordered list of number per one of the six usual nesting levels from 1 to 6
2. union field for special appendix nesting with boolean value of false or numeric nesting level if appendix
3. string value of the section "number" code as to be shown to the left of any TOC
4. string value of the section title for display in the TOC
5. string value of the section slug for use as link target into the document (to the section itself)

For now, we do include some additional processing to inject style classes and remove noise from the
pandoc derived HTML document as final processing step in our pipeline for publication ready HTML format.
"""
import json
import pathlib
import sys
from typing import Union

ENCODING = 'utf-8'
NL = '\n'
COLON = ':'
DASH = '-'
DOT = '.'

# Configuration and runtime parameter candidates:
BUILD_AT = pathlib.Path('build')
HTML_IN_AT = BUILD_AT / 'tmp.html'
TOC_AT = BUILD_AT / 'toc-mint.json'
LOGO_AT = pathlib.Path('..') / 'media' / 'logo-data-url.txt'
BASE_CSS_AT = pathlib.Path('..') / 'share' / 'style' / 'base.css'
SKIN_CSS_AT = pathlib.Path('..') / 'share' / 'style' / 'skin.css'

# Specific tokens:
LOCAL_LOGO = '<img src="media/OASISLogo-v3.0.png" style="width:3.01036in;height:0.61978in" />'
OASIS_LOGO = '![OASIS Logo](https://docs.oasis-open.org/templates/OASISLogo-v3.0.png)'

# Trigger for the injections (on as well as off)
STYLE_BASE_REPLACE_LINE = '<link rel="stylesheet" href="style/base.css" />'
STYLE_SKIN_REPLACE_LINE = '<link rel="stylesheet" href="style/skin.css" />'

HTML_BODY_HEADER_START_REMOVE_EXCL = '<header id="title-block-header">'
HTML_BODY_HEADER_END_REMOVE_INCL = '</header>'

POST_HEADER_END_REMOVE_LOGO_LINE = (
    '<p><img src="https://docs.oasis-open.org/templates/OASISLogo-v3.0.png" alt="OASIS Logo" /></p>'
)

HTML_BODY_HEADER_END_INSERT_AFTER = '<hr />'
POST_HEADER_TITLE_CLASS_TITLE_LINE = (
    '<h1 id="common-security-advisory-framework-version-20">Common Security Advisory Framework Version 2.0</h1>'  # TODO: Make more robust
)
POST_TITLE_SUBTITLE_CLASS_TYPE_LINE = '<h2 id="oasis-standard">OASIS Standard</h2>'  # TODO: Make more robust
POST_TYPE_SUBTITLE_CLASS_DATE_LINE = '<h2 id="18-november-2022">18 November 2022</h2>'  # TODO: Make more robust
POST_DATE_TITLEPAGE_INFO_CLASS_THIS_STAGE_LINE = '<h4 id="this-stage">This stage:</h4>'
IN_THIS_STAGE_ANY_P_HREF_CLASS_DENSE = '<p><a href="https://docs.oasis-open.org/'
POST_THIS_STAGE_TITLEPAGE_INFO_CLASS_PREVIOUS_STAGE_LINE = '<h4 id="previous-stage">Previous stage:</h4>'
IN_PREVIOUS_STAGE_ANY_P_HREF_CLASS_DENSE = '<p><a href="https://docs.oasis-open.org/'
POST_PREVIOUS_STAGE_TITLEPAGE_INFO_CLASS_LATEST_STAGE_LINE = '<h4 id="latest-stage">Latest stage:</h4>'
IN_LATEST_STAGE_ANY_P_HREF_CLASS_DENSE = '<p><a href="https://docs.oasis-open.org/'
POST_LATEST_STAGE_TITLEPAGE_INFO_CLASS_TECHNICAL_COMMITTEE_LINE = '<h4 id="technical-committee">Technical Committee:</h4>'
POST_TECHNICAL_COMMITTEE_TITLEPAGE_INFO_CLASS_CHAIRS_LINE = '<h4 id="chair">Chair:</h4>'  # TODO: Make more robust
IN_CHAIRS_P_CLASS_DENSE = '<p>'
POST_CHAIRS_TITLEPAGE_INFO_CLASS_EDITORS_LINE = '<h4 id="editors">Editors:</h4>'  # TODO: Make more robust
IN_EDITORS_P_CLASS_DENSE = '<p>'
POST_EDITORS_TITLEPAGE_INFO_CLASS_ADDITIONAL_ARTIFACTS_LINE = '<h4 id="additional-artifacts">Additional artifacts:</h4>'

# <h4 id="related-work">Related work:</h4>
# <h4 id="declared-json-namespaces">Declared JSON namespaces:</h4>

POST_ADDITIONAL_ARTIFACTS_TITLEPAGE_INFO_CLASS_ABSTRACT_LINE = '<h4 id="abstract">Abstract:</h4>'
POST_ABSTRACT_TITLEPAGE_INFO_CLASS_STATUS_LINE = '<h4 id="status">Status:</h4>'
POST_STATUS_TITLEPAGE_INFO_CLASS_CITATION_FORMAT_LINE = '<h4 id="citation-format">Citation format:</h4>'
POST_CITATION_FORMAT_TITLEPAGE_INFO_CLASS_NOTICES_LINE = '<h2 id="notices">Notices</h2>'

TOC_START_INCL = '<h1 id="table-of-contents">Table of Contents</h1>'
TOC_END_EXCL = '<h1 id="1-introduction-">1. Introduction <a id=\'introduction\'></a></h1>'

# Data for injections
LOGO_DATA_URL = open(LOGO_AT, 'rt', encoding=ENCODING).read().strip()
LOGO_REPLACEMENT_LINE = f'<p><img src="{LOGO_DATA_URL}" alt="OASIS Logo" /></p>'
BASE_CSS = open(BASE_CSS_AT, 'rt', encoding=ENCODING).read()
SKIN_CSS = open(SKIN_CSS_AT, 'rt', encoding=ENCODING).read()

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
    entries = []
    past = 0
    for slot, toc_entry in enumerate(toc_db):
        levels, _, num_disp, text, slug = toc_entry  # Ignoring appendix_level / is appendix info
        pres = num_disp.rstrip('.').count(DOT) + 1
        if past == 0:
            if pres != 1:
                raise RuntimeError(f'error in first toc db entry: ({toc_entry})')
            entries.append(f'<ol class="toc-{pres}"><li>{num_disp} <a href="#{slug}">{text}</a></li>')
            past = pres
            continue
        if pres == past:
            entries.append(f'<li>{num_disp} <a href="#{slug}">{text}</a></li>')
            past = pres
            continue
        if pres > past:
            patch_me = entries[slot - 1]
            there = len('</li>')
            entries[slot - 1] = patch_me[:-there] + f'<ol class="toc-{pres}">'
            entries.append(f'<li>{num_disp} <a href="#{slug}">{text}</a></li>')
            past = pres
            continue
        if pres < past:
            stack = past
            closing = ''
            while stack > pres:
                closing += '</ol></li>'
                stack -= 1
            entries.append(f'{closing}<li>{num_disp} <a href="#{slug}">{text}</a></li>')
            past = pres
            continue

    return NL.join(entries)


def cleansed_startswith(text: str, token: str) -> bool:
    """Helper anchor the token matcher."""
    return text.strip().startswith(token)


def is_base_style_rel_line(text: str) -> bool:
    """Detect the base style rel line."""
    return cleansed_startswith(text, STYLE_BASE_REPLACE_LINE)


def is_skin_style_rel_line(text: str) -> bool:
    """Detect the skin style rel line."""
    return cleansed_startswith(text, STYLE_SKIN_REPLACE_LINE)


def is_header_start_line(text: str) -> bool:
    """Detect the header start line."""
    return cleansed_startswith(text, HTML_BODY_HEADER_START_REMOVE_EXCL)


def is_header_end_line(text: str) -> bool:
    """Detect the header end line."""
    return cleansed_startswith(text, HTML_BODY_HEADER_END_REMOVE_INCL)


def is_logo_line(text: str) -> bool:
    """Detect the logo line."""
    return cleansed_startswith(text, POST_HEADER_END_REMOVE_LOGO_LINE)


def replace_logo_line(text: str) -> str:
    """Replace the logo line."""
    return text.replace(POST_HEADER_END_REMOVE_LOGO_LINE, LOGO_REPLACEMENT_LINE)


def is_document_title_line(text: str) -> bool:
    """Detect the funny paragraph that is the document title (on page)."""
    return cleansed_startswith(text, POST_HEADER_TITLE_CLASS_TITLE_LINE)


def is_document_type_line(text: str) -> bool:
    """Detect the funny paragraph that is the document type (on page)."""
    return cleansed_startswith(text, POST_TITLE_SUBTITLE_CLASS_TYPE_LINE)


def is_document_date_line(text: str) -> bool:
    """Detect the funny paragraph that is the document date (on page)."""
    return cleansed_startswith(text, POST_TYPE_SUBTITLE_CLASS_DATE_LINE)


def is_document_this_stage_line(text: str) -> bool:
    """Detect the funny paragraph that is the document this stage section (on page)."""
    return cleansed_startswith(text, POST_DATE_TITLEPAGE_INFO_CLASS_THIS_STAGE_LINE)


def is_document_previous_stage_line(text: str) -> bool:
    """Detect the funny paragraph that is the document previous stage section (on page)."""
    return cleansed_startswith(text, POST_THIS_STAGE_TITLEPAGE_INFO_CLASS_PREVIOUS_STAGE_LINE)


def is_document_latest_stage_line(text: str) -> bool:
    """Detect the funny paragraph that is the document latest stage section (on page)."""
    return cleansed_startswith(text, POST_PREVIOUS_STAGE_TITLEPAGE_INFO_CLASS_LATEST_STAGE_LINE)


def is_document_technical_committee_line(text: str) -> bool:
    """Detect the funny paragraph that is the document technical committee section (on page)."""
    return cleansed_startswith(text, POST_LATEST_STAGE_TITLEPAGE_INFO_CLASS_TECHNICAL_COMMITTEE_LINE)


def is_document_chairs_line(text: str) -> bool:
    """Detect the funny paragraph that is the document chairs section (on page)."""
    return cleansed_startswith(text, POST_TECHNICAL_COMMITTEE_TITLEPAGE_INFO_CLASS_CHAIRS_LINE)


def is_document_editors_line(text: str) -> bool:
    """Detect the funny paragraph that is the document editors section (on page)."""
    return cleansed_startswith(text, POST_CHAIRS_TITLEPAGE_INFO_CLASS_EDITORS_LINE)


def is_document_additional_artifacts_line(text: str) -> bool:
    """Detect the funny paragraph that is the document additional artifacts section (on page)."""
    return cleansed_startswith(text, POST_EDITORS_TITLEPAGE_INFO_CLASS_ADDITIONAL_ARTIFACTS_LINE)


def is_document_abstract_line(text: str) -> bool:
    """Detect the funny paragraph that is the document abstract section (on page)."""
    return cleansed_startswith(text, POST_ADDITIONAL_ARTIFACTS_TITLEPAGE_INFO_CLASS_ABSTRACT_LINE)


def is_document_status_line(text: str) -> bool:
    """Detect the funny paragraph that is the document status section (on page)."""
    return cleansed_startswith(text, POST_ABSTRACT_TITLEPAGE_INFO_CLASS_STATUS_LINE)


def is_document_citation_format_line(text: str) -> bool:
    """Detect the funny paragraph that is the document citation format section (on page)."""
    return cleansed_startswith(text, POST_STATUS_TITLEPAGE_INFO_CLASS_CITATION_FORMAT_LINE)


def is_document_notices_line(text: str) -> bool:
    """Detect the funny paragraph that is the document notices section (on page)."""
    return cleansed_startswith(text, POST_CITATION_FORMAT_TITLEPAGE_INFO_CLASS_NOTICES_LINE)


def start_of_toc_in(text: str) -> bool:
    """Detect the start of the table of contents."""
    return cleansed_startswith(text, TOC_START_INCL)


def end_of_toc_in(text: str) -> bool:
    """Detect the end of the table of contents."""
    return cleansed_startswith(text, TOC_END_EXCL)


def load_html_document(path: Union[str, pathlib.Path]) -> list[str]:
    """Load the html file into a list of strings."""
    with open(path, 'rt', encoding=ENCODING) as resource:
        return resource.readlines()


def dump_html_assembly(text_lines: list[str], to_path: Union[str, pathlib.Path]) -> None:
    """Dump the lines of text into the (html) text file at path."""
    with open(to_path, 'wt', encoding=ENCODING) as resource:
        resource.write(''.join(text_lines))


def main(argv: list[str]) -> int:
    """Drive the injections."""

    html_in_path = pathlib.Path(argv[0]) if argv else HTML_IN_AT
    html_in = load_html_document(html_in_path)

    toc_db = load_toc(TOC_AT)

    lines = []
    inline_style_start_seen = False
    inline_style_end_seen = False
    base_style_seen = False
    skin_style_seen = False
    header_start_seen = False
    header_end_seen = False
    logo_replaced = False
    title_seen = False
    type_seen = False
    date_seen = False
    this_stage_seen = False
    previous_stage_seen = False
    latest_stage_seen = False
    technical_committee_seen = False
    chairs_seen = False
    editors_seen = False
    additional_artifacts_seen = False
    abstract_seen = False
    status_seen = False
    citation_format_seen = False
    notices_seen = False
    toc_start_seen = False
    toc_end_seen = False
    for slot, line in enumerate(html_in):
        cand = line.replace('<component>', '&lt;component>').replace('lang=""', 'lang="en"')  # TODO: Remove the hacks
        if not inline_style_start_seen and cand.strip() == '<style>':
            inline_style_start_seen = True
            continue  # ignore all automatic inline styles from generator (pandoc)

        if inline_style_start_seen and not inline_style_end_seen:
            if cand.strip() == '</style>':
                inline_style_end_seen = True
            continue  # ignore all automatic inline styles from generator (pandoc)

        if inline_style_end_seen and not base_style_seen:
            if is_base_style_rel_line(cand):
                cand = '<style>' + NL + BASE_CSS + NL
                base_style_seen = True
                lines.append(cand)
            else:
                print(f'diff-{STYLE_BASE_REPLACE_LINE}-')
                print(f'diff+{cand.strip()}+')
                raise RuntimeError(f'error in parser at base style detect[slot {slot}]: ({cand.strip()})')
            continue

        if base_style_seen and not skin_style_seen:
            if is_skin_style_rel_line(cand):
                cand = SKIN_CSS + NL + '</style>' + NL
                skin_style_seen = True
                lines.append(cand)
            else:
                print(f'diff-{STYLE_SKIN_REPLACE_LINE}-')
                print(f'diff+{cand.strip()}+')
                raise RuntimeError(f'error in parser at skin style detect[slot {slot}]: ({cand.strip()})')
            continue

        if skin_style_seen and not header_start_seen:
            if is_header_start_line(cand):
                header_start_seen = True
            lines.append(cand)
            continue

        if header_start_seen and not header_end_seen:
            if is_header_end_line(cand):
                header_end_seen = True
            continue  # omit all found html/body/header entries besides start

        if header_start_seen and not logo_replaced:
            if is_logo_line(cand):
                cand = replace_logo_line(cand) + NL + '</header>' + NL  # TODO: horizontal rule should go in header
                logo_replaced = True
                lines.append(cand)
            continue

        if logo_replaced and not title_seen:
            if is_document_title_line(cand):
                # cand = cand.replace('<p>', '<p class="title">')
                title_seen = True
                lines.append(cand)
                continue

        if title_seen and not type_seen:
            if is_document_type_line(cand):
                # cand = cand.replace('<p>', '<p class="sub-title">')
                type_seen = True
                lines.append(cand)
                continue

        if type_seen and not date_seen:
            if is_document_date_line(cand):
                # cand = cand.replace('<p>', '<p class="sub-title">')
                date_seen = True
                lines.append(cand)
                continue

        if date_seen and not this_stage_seen:
            if is_document_this_stage_line(cand):
                this_stage_seen = True
                # cand = cand.replace('<p>', '<p class="titlepage-info">')
                lines.append(cand)
                continue

        if this_stage_seen and not previous_stage_seen:
            if is_document_previous_stage_line(cand):
                previous_stage_seen = True
                # cand = cand.replace('<p>', '<p class="titlepage-info">')
                lines.append(cand)
                continue
            cand = cand.replace('<p>', '<p class="dense">')

        if previous_stage_seen and not latest_stage_seen:
            if is_document_latest_stage_line(cand):
                latest_stage_seen = True
                # cand = cand.replace('<p>', '<p class="titlepage-info">')
                lines.append(cand)
                continue
            cand = cand.replace('<p>', '<p class="dense">')

        if latest_stage_seen and not technical_committee_seen:
            if is_document_technical_committee_line(cand):
                technical_committee_seen = True
                # cand = cand.replace('<p>', '<p class="titlepage-info">')
                lines.append(cand)
                continue
            cand = cand.replace('<p>', '<p class="dense">')

        if technical_committee_seen and not chairs_seen:
            if is_document_chairs_line(cand):
                chairs_seen = True
                # cand = cand.replace('<p>', '<p class="titlepage-info">')
                lines.append(cand)
                continue

        if chairs_seen and not editors_seen:
            if is_document_editors_line(cand):
                editors_seen = True
                # cand = cand.replace('<p>', '<p class="titlepage-info">')
                lines.append(cand)
                continue
            cand = cand.replace('<p>', '<p class="dense">')

        if editors_seen and not additional_artifacts_seen:
            if is_document_additional_artifacts_line(cand):
                print('additional_artifacts_seen')
                additional_artifacts_seen = True
                # cand = cand.replace('<p>', '<p class="titlepage-info">')
                lines.append(cand)
                continue
            cand = cand.replace('<p>', '<p class="dense">')

        if additional_artifacts_seen and not abstract_seen:
            if is_document_abstract_line(cand):
                print('abstract_seen')
                abstract_seen = True
                # cand = cand.replace('<p>', '<p class="titlepage-info">')
                lines.append(cand)
                continue

        if abstract_seen and not status_seen:
            if is_document_status_line(cand):
                print('status_seen')
                status_seen = True
                # cand = cand.replace('<p>', '<p class="titlepage-info">')
                lines.append(cand)
                continue

        if status_seen and not citation_format_seen:
            if is_document_citation_format_line(cand):
                print('citation_format_seen')
                citation_format_seen = True
                # cand = cand.replace('<p>', '<p class="titlepage-info">')
                lines.append(cand)
                continue

        if citation_format_seen and not notices_seen:
            if is_document_notices_line(cand):
                print('notices_seen')
                notices_seen = True
                # cand = cand.replace('<p>', '<p class="notices">')
                lines.append(cand)
                continue

        if notices_seen and not toc_start_seen:
            if start_of_toc_in(cand):
                print('toc_start_seen')
                toc_start_seen = True
                lines.append(cand)
                continue

        if toc_start_seen and not toc_end_seen:
            if end_of_toc_in(cand):
                print('toc_end_seen')
                toc_end_seen = True
                cand = generate_toc(toc_db) + NL + cand
                lines.append(cand)
            continue

        lines.append(cand)

    # remove any trailing blank line
    while lines[-1] == NL:
        del lines[-1]

    BUILD_AT.mkdir(parents=True, exist_ok=True)
    dump_html_assembly(lines, BUILD_AT / 'injected.html')

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
