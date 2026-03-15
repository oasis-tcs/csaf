#! /usr/bin/env python
"""Extract sections from source files concat per binder and write display to label(slug) mapping."""
import pathlib
import os
import re
import sys

from inverso.implementation import process as process_inversion, nonjective  # type: ignore
from muuntuu.implementation import json_dump  # type: ignore

# "Un-lit(t)er-al" the code
DASH = '-'
DOT = '.'
ENCODING = 'utf-8'
ENC_ERRS = 'ignore'
FULL_STOP = '.'
HASH = '#'
NL = '\n'
RS = chr(30)  # Record Separator
SPACE = ' '

PathLike = str | pathlib.Path

DEBUG = bool(os.getenv('SECTIONS_DEBUG', ''))

# Configuration and runtime parameter candidates:
GREMLINS = ' .,;?!_()[]{}<>\\/$:"\'`´'
BINDER_AT = pathlib.Path('etc') / 'bind.txt'
SOURCE_AT = pathlib.Path('src')
SECTION_DISPLAY_TO_LABEL_AT = pathlib.Path('etc') / 'section-display-to-label.json'
SECTION_LABEL_TO_DISPLAY_AT = pathlib.Path('etc') / 'section-label-to-display.json'
SECTION_DISPLAY_TO_TEXT_AT = pathlib.Path('etc') / 'section-display-to-text.json'
TOK_LAB = '{#'
CLEAN_MD_START = '# Introduction'
FENCED_BLOCK_FLIP_FLOP = '```'
APPENDIX_INNER_PATTERN = re.compile(r'(?P<display>[A-Z][\.0-9]+)\ +(?P<rest>.+)')


def load_binder(binder_at: PathLike) -> list[pathlib.Path]:
    """Load the linear binder text file into a list of file paths."""
    with open(binder_at, 'rt', encoding=ENCODING, errors=ENC_ERRS) as resource:
        return [pathlib.Path(entry.strip()) for entry in resource.readlines() if entry.strip()]


def load_document(path: PathLike) -> list[str]:
    """Load the text file into a list of strings."""
    with open(path, 'rt', encoding=ENCODING, errors=ENC_ERRS) as resource:
        return resource.readlines()


def slugify(
    text: str,
    connector: str = DASH,
    marker: str = RS,
    gremlins: str = GREMLINS,
    policy: str = 'lower',
) -> str:
    """Derive kebab style slug from text.

    Implementer notes:

    - Every character not in gremlins is kept.
    - Incoming connector chars (default dashes) are preserved by
      sandwich transform to and from marker char (default ASCII RS).
      If the marker char occurs in the text, it will be replaced
      with the connector char during the back transform.
    """
    ds = connector
    rs = marker

    sl = text.strip().replace(ds, rs)
    for gremlin in gremlins:
        sl = sl.replace(gremlin, ds)

    return getattr(
        ds.join(s.replace(rs, ds) for s in sl.split(ds) if s and s != ds),
        policy
    )()


def invert(
    source: dict[str, str],
    options: dict[str, bool | int | str] | None = None
) -> dict[str, str]:
    """Invert between and within the known formats (inverso API has a gap)."""
    if options is None:
        options = {}
    auto_serial: bool = options.get('auto_serial', False)
    auto_serial_step: int = options.get('auto_serial_step', 1)
    generator_caveat: bool = options.get('generator_caveat', True)
    marker_token: str = options.get('marker_token', '')
    marker_is_value: bool = options.get('marker_is_value', False)

    cleansed: dict[str, str] = {}
    for k, v in source.items():
        key, value, seen = process_inversion(k, v, auto_serial, marker_token, marker_is_value)
        cleansed[key] = value
        if auto_serial:
            if not marker_token or not seen:
                auto_serial += auto_serial_step

    if findings := nonjective(cleansed):
        print('Error: source has ambiguous values.', file=sys.stderr)
        for finding in findings:
            print(f'- {finding}', file=sys.stderr)
        return {}

    inverted = {v: k for k, v in cleansed.items()}
    ordered = {'Please do not edit manually!': 'Cf. documentation'} if generator_caveat else {}
    for k in sorted(inverted):
        ordered[k] = inverted[k]

    return ordered


def main(argv: list[str]) -> int:
    """Drive the extraction."""

    bind_seq_path = pathlib.Path(argv[0]) if argv else BINDER_AT
    binder = load_binder(bind_seq_path)
    for resource in binder:
        if not (SOURCE_AT / resource).is_file():
            print(f'Problem reading {resource}')
            return 1

    lines: list[str] = []
    for resource in binder:
        part_lines = load_document(SOURCE_AT / resource)
        if part_lines[-1] != NL:
            part_lines.append(NL)
        lines.extend(part_lines)

    in_fenced_block = False
    clean_headings = False
    sections = []
    for line in lines:
        if line.startswith(CLEAN_MD_START):
            clean_headings = True

        if not clean_headings:
            continue

        if line.startswith(FENCED_BLOCK_FLIP_FLOP):
            in_fenced_block = not in_fenced_block

        if line.startswith(HASH) and not in_fenced_block:
            if line.lstrip(HASH).startswith(SPACE):
                sections.append(line.rstrip(NL))

    print(f'Identified {len(sections)} relevant sections ...')

    level_counts = {n: 0 for n in range(1, 7)}
    previous_level = 0
    defects = 0
    for section in sections:
        level = len(section.split(SPACE, 1)[0])
        level_counts[level] += 1
        if level > previous_level:
            if level - previous_level > 1:
                defects += 1
                print(
                    f'! LEVEL_NEST_ERROR jumping from level {previous_level}'
                    f' directly to {level}'
                )
                print(f'>>> {section}')
        previous_level = level

    for level, count in level_counts.items():
        print(f'- {count} level {level} sections')

    if defects:
        print(f'Found {defects} defects in section nesting!')
    else:
        print('Section level nesting is valid')

    db = []
    is_appendix = False
    root: int = 0
    appr = ''
    for section in sections:
        display = ''
        level = len(section.split(SPACE, 1)[0])
        if level == 1:
            root += 1
        text_plus = section[level + 1:]
        if '<mark title="Ephemeral region marking">' in text_plus:
            text_plus = (
                text_plus
                .replace('<mark title="Ephemeral region marking">', '')
                .replace('</mark>', '')
            )
        if text_plus.startswith('Appendix '):
            appr = text_plus.replace('Appendix ', '')[0]
            display = f'Appendix {appr}.'
            text_plus = text_plus.replace(f'{display} ', '')
            is_appendix = True
        else:
            match = APPENDIX_INNER_PATTERN.match(text_plus)
            if match:
                found = match.groupdict()
                display = found['display']
                text_plus = text_plus.replace(f'{display} ', '')

        if TOK_LAB in text_plus:
            text, slug = text_plus.rstrip(SPACE).rstrip('}').split(TOK_LAB, 1)
        else:
            text = text_plus.rstrip(SPACE)
            slug = slugify(text)
        if not is_appendix:
            a_root = str(root)
        else:
            a_root = appr
        db.append([is_appendix, a_root, level, display, text, slug])

    if DEBUG:
        for is_appendix, a_root, level, display, text, slug in db:
            print(
                f'{"        " if not is_appendix else "APPENDIX"} | {a_root} |'
                f' {(HASH * level).rjust(7)} "{text}" <-- {slug}'
            )

    display_to_label = {}
    display_to_text = {}
    lvl_min, lvl_sup = 1, 7
    level_domain: tuple[int, ...] = tuple(range(lvl_min, lvl_sup))
    sec_cnt: dict[str, int] = {f'{HASH * level} ': 0 for level in level_domain}
    sec_lvl: dict[str, int] = {f'{HASH * level} ': level for level in level_domain}
    lvl_sec: dict[int, str] = {level: f'{HASH * level} ' for level in level_domain}
    cur_lvl: int = sec_lvl[f'{HASH * 1} ']
    for is_appendix, a_root, level, display, text, slug in db:
        if not is_appendix:
            tag = f'{HASH * level} '
            nxt_lvl = sec_lvl[tag]
            sec_cnt[tag] += 1
            if nxt_lvl < cur_lvl:
                for lvl in range(nxt_lvl + 1, lvl_sup):
                    sec_cnt[lvl_sec[lvl]] = 0
            sec_cnt_disp_vec = []
            for s_tag, cnt in sec_cnt.items():
                if cnt == 0:
                    raise RuntimeError(f'ERROR: Counting is hard: {sec_cnt} at {tag} for {text}')
                sec_cnt_disp_vec.append(str(cnt))
                if s_tag == tag:
                    break
            sec_cnt_disp = FULL_STOP.join(sec_cnt_disp_vec)
            cur_lvl = nxt_lvl

            display = sec_cnt_disp.rstrip(DOT)
        else:
            pass  # display, text = text.split(SPACE, 1)
        display_to_label[display] = slug
        display_to_text[display] = text
        if DEBUG:
            print(f' {display} "{display_to_text[display]}" <-- {slug}')

    json_dump(display_to_label, SECTION_DISPLAY_TO_LABEL_AT, options={'debug': DEBUG})
    json_dump(invert(display_to_label), SECTION_LABEL_TO_DISPLAY_AT, options={'debug': DEBUG})
    json_dump(display_to_text, SECTION_DISPLAY_TO_TEXT_AT, options={'debug': DEBUG})

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
