#! /usr/bin/env python
"""Derive section and example LUTs from source files ordered per bind.txt.

All spec-specific behaviour is driven by etc/sections-config.yaml.

Outputs (always):
  etc/section-display-to-label.json
  etc/section-label-to-display.json
  etc/section-display-to-text.json

Outputs (when track-examples: true):
  etc/example-local-to-global.json
  etc/example-global-to-local.json
"""

import json
import pathlib
import re
import sys
from typing import Union

import yaml

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
DASH = '-'
DOT = '.'
ENCODING = 'utf-8'
ENC_ERRS = 'ignore'
FULL_STOP = '.'
HASH = '#'
NL = '\n'
RS = chr(30)  # Record Separator — used in slugify
SPACE = ' '

PathLike = Union[str, pathlib.Path]

# Fixed paths (script must be invoked from prose/edit/)
ETC_AT = pathlib.Path('etc')
CONFIG_AT = ETC_AT / 'sections-config.yaml'
BINDER_AT = ETC_AT / 'bind.txt'
SOURCE_AT = pathlib.Path('src')
SECTION_DISPLAY_TO_LABEL_AT = ETC_AT / 'section-display-to-label.json'
SECTION_LABEL_TO_DISPLAY_AT = ETC_AT / 'section-label-to-display.json'
SECTION_DISPLAY_TO_TEXT_AT = ETC_AT / 'section-display-to-text.json'
EG_LOCAL_TO_GLOBAL_AT = ETC_AT / 'example-local-to-global.json'
EG_GLOBAL_TO_LOCAL_AT = ETC_AT / 'example-global-to-local.json'

GREMLINS = ' .,;?!_()[]{}<>\\/$:"\'`´'
TOK_LAB = '{#'
FENCED_BLOCK = '```'

# Matches inner annex/appendix sub-headings like "A.1. Document Status" or "B.2 Informative References"
APPENDIX_INNER_PATTERN = re.compile(r'(?P<display>[A-Z][.0-9]+) +(?P<rest>.+)')

EXAMPLE_DETECT = re.compile(r'^\*Examples?\ +(?P<number>\d+)\b')

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_config(path: PathLike) -> dict:  # type: ignore[type-arg]
    with open(path, 'rt', encoding=ENCODING, errors=ENC_ERRS) as handle:
        return yaml.safe_load(handle) or {}


def load_binder(path: PathLike) -> list[pathlib.Path]:
    with open(path, 'rt', encoding=ENCODING, errors=ENC_ERRS) as handle:
        return [pathlib.Path(line.strip()) for line in handle if line.strip()]


def slugify(text: str) -> str:
    """Derive a kebab-style slug from heading text."""
    ds, rs = DASH, RS
    sl = text.strip().replace(ds, rs)
    for gremlin in GREMLINS:
        sl = sl.replace(gremlin, ds)
    return ds.join(s.replace(rs, ds) for s in sl.split(ds) if s and s != ds).lower()


def normalize_enumerate(value: object) -> str:
    """Normalise a display prefix to a clean string (strips trailing dots)."""
    if value is False or value is None:
        return ''
    return str(value).rstrip(DOT)


def write_json(data: dict, path: PathLike) -> None:  # type: ignore[type-arg]
    with open(path, 'wt', encoding=ENCODING) as handle:
        json.dump(data, handle, indent=2)
        handle.write(NL)


def highlight(lines: list[str], pos: int, span: int = 10) -> None:
    """Print lines around pos with an arrow at pos, to help authors find errors."""
    for n in range(max(0, pos - span), min(pos + span, len(lines))):
        prefix = 'HERE>>>' if n == pos else '       '
        print(f'{prefix} {n:4} | {lines[n].rstrip(NL)}')
    print(DASH * 72)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main(argv: list[str]) -> int:  # noqa: C901
    if not CONFIG_AT.is_file():
        print(f'ERROR: config file not found at {CONFIG_AT}')
        print('INFO: Please run this script from inside the prose/edit/ directory.')
        return 1

    config = load_config(CONFIG_AT)
    clean_md_start: str = config.get('clean-md-start', '# Introduction')
    track_examples: bool = bool(config.get('track-examples', False))
    meta_eg_global: int = int(config.get('meta-example-global-number', 4321))

    print(f'INFO: clean-md-start   = {clean_md_start!r}')
    print(f'INFO: track-examples   = {track_examples}')
    if track_examples:
        print(f'INFO: meta-example-global-number = {meta_eg_global}')

    # ------------------------------------------------------------------
    # Phase 1: load sources
    # ------------------------------------------------------------------
    binder = load_binder(BINDER_AT)
    for resource in binder:
        if not (SOURCE_AT / resource).is_file():
            print(f'ERROR: source file not found: {resource}')
            return 1

    # documents: list of (body_lines, source_name)
    documents: list[tuple[list[str], str]] = []
    for resource in binder:
        with open(SOURCE_AT / resource, 'rt', encoding=ENCODING, errors=ENC_ERRS) as fh:
            raw = fh.readlines()
        if raw and raw[-1] != NL:
            raw.append(NL)
        documents.append((raw, str(resource)))

    # Flatten to a single line sequence with per-line source tracking
    all_lines: list[str] = []
    line_source: list[str] = []
    for body, source in documents:
        for line in body:
            all_lines.append(line)
            line_source.append(source)

    print(f'INFO: Loaded {len(binder)} source files → {len(all_lines)} lines total')

    # ------------------------------------------------------------------
    # Phase 2: scan headings
    # ------------------------------------------------------------------
    # Each section record: (level, text, slug, display, source)
    # display is None for auto-numbered sections, str for explicit display.
    SectionRecord = tuple[int, str, str, str | None, str]
    section_records: list[SectionRecord] = []

    # Per-line context: which section slug is "current" at that line
    section_of_line: list[str | None] = [None] * len(all_lines)

    in_fenced = False
    clean_headings = False
    current_section_slug: str | None = None
    is_appendix = False  # flips True permanently on first Annex/Appendix heading

    for idx, line in enumerate(all_lines):
        if line.startswith(clean_md_start):
            clean_headings = True

        if not clean_headings:
            continue

        if line.startswith(FENCED_BLOCK):
            in_fenced = not in_fenced

        section_of_line[idx] = current_section_slug

        if not line.startswith(HASH) or in_fenced:
            continue
        stripped = line.lstrip(HASH)
        if not stripped.startswith(SPACE):
            continue

        level = len(line) - len(stripped)
        text_plus = stripped.strip()

        # Strip ephemeral region marks
        if '<mark title="Ephemeral region marking">' in text_plus:
            text_plus = (
                text_plus
                .replace('<mark title="Ephemeral region marking">', '')
                .replace('</mark>', '')
                .strip()
            )

        # Extract explicit slug override if present
        if TOK_LAB in text_plus:
            text, slug = text_plus.rstrip('}').split(TOK_LAB, 1)
            text = text.strip()
            slug = slug.strip()
        else:
            text = text_plus
            slug = slugify(text)

        # Determine display value from heading text
        # For appendix headings the slug is re-derived from the text AFTER the display
        # prefix is stripped, so that labels match what volatile.py produces.
        display: str | None
        if text.startswith('Appendix '):
            is_appendix = True
            parts = text.split(SPACE, 2)
            display = f'Appendix {parts[1]}'
            text = parts[2] if len(parts) > 2 else parts[1]
            if TOK_LAB not in text_plus:
                slug = slugify(text)
        elif text.startswith('Annex '):
            is_appendix = True
            parts = text.split(SPACE, 2)
            display = f'Annex {parts[1]}'
            text = parts[2] if len(parts) > 2 else parts[1]
            if TOK_LAB not in text_plus:
                slug = slugify(text)
        elif is_appendix:
            m = APPENDIX_INNER_PATTERN.match(text)
            if m:
                display = normalize_enumerate(m.group('display'))
                text = m.group('rest')
                if TOK_LAB not in text_plus:
                    slug = slugify(text)
            else:
                # Unnumbered OASIS-mandated sub-heading (e.g. Leadership, Revision History)
                display = text
        else:
            display = None  # will be auto-numbered in Phase 3

        section_records.append((level, text, slug, display, line_source[idx]))
        current_section_slug = slug
        section_of_line[idx] = current_section_slug

    print(f'INFO: Identified {len(section_records)} relevant section headings')

    # ------------------------------------------------------------------
    # Phase 3: validate section nesting
    # ------------------------------------------------------------------
    level_counts: dict[int, int] = {n: 0 for n in range(1, 7)}
    previous_level = 0
    nesting_defects = 0
    for level, text, slug, display, src in section_records:
        level_counts[level] += 1
        if level > previous_level and level - previous_level > 1:
            nesting_defects += 1
            print(
                f'ERROR: Section nesting jump from level {previous_level}'
                f' to level {level} in {src!r}:'
            )
            print(f'  >>> {HASH * level} {text}')
        previous_level = level

    for lvl, cnt in level_counts.items():
        if cnt:
            print(f'INFO: - {cnt} level-{lvl} section heading(s)')

    if nesting_defects:
        print(f'ERROR: Found {nesting_defects} section nesting defect(s) — aborting.')
        return 1
    print('INFO: Section level nesting is valid.')

    # ------------------------------------------------------------------
    # Phase 4: assign display values to auto-numbered sections, build LUTs
    # ------------------------------------------------------------------
    lvl_cnt: dict[int, int] = {n: 0 for n in range(1, 7)}

    display_to_label: dict[str, str] = {}
    display_to_text: dict[str, str] = {}

    for level, text, slug, display, _src in section_records:
        if display is None:
            # Auto-number
            lvl_cnt[level] += 1
            for sub in range(level + 1, 7):
                lvl_cnt[sub] = 0
            display = DOT.join(str(lvl_cnt[n]) for n in range(1, level + 1))

        if display in display_to_label and display_to_label[display] != slug:
            print(
                f'ERROR: Duplicate display key {display!r} for slugs'
                f' {display_to_label[display]!r} and {slug!r}'
            )
            return 1

        display_to_label[display] = slug
        display_to_text[display] = text

    label_to_display: dict[str, str] = {
        'Please do not edit manually!': 'Cf. sections-config.yaml and bin/sections.py',
        **{slug: disp for disp, slug in sorted(display_to_label.items(), key=lambda kv: kv[1])},
    }

    write_json(display_to_label, SECTION_DISPLAY_TO_LABEL_AT)
    write_json(label_to_display, SECTION_LABEL_TO_DISPLAY_AT)
    write_json(display_to_text, SECTION_DISPLAY_TO_TEXT_AT)

    print(f'INFO: Wrote {len(display_to_label)} entries to section LUT files.')

    # ------------------------------------------------------------------
    # Phase 5: example scanning
    # ------------------------------------------------------------------
    # Even when track-examples is false, warn about detected example lines.
    example_lines_found: list[tuple[int, str, int]] = []  # (line_idx, section_slug, local_num)

    for idx, line in enumerate(all_lines):
        m = EXAMPLE_DETECT.match(line.lstrip())
        if m:
            num = int(m.group('number'))
            sec = section_of_line[idx]
            if sec is None:
                print(
                    f'WARN: Example {num} at line {idx} has no enclosing section context.'
                )
                continue
            example_lines_found.append((idx, sec, num))

    if example_lines_found and not track_examples:
        print(
            f'WARN: Detected {len(example_lines_found)} example line(s) but track-examples is false.'
        )
        print('WARN: Set track-examples: true in etc/sections-config.yaml to validate and generate LUTs.')
        return 0

    if not track_examples:
        return 0

    if not example_lines_found:
        print('INFO: No example lines detected — skipping example LUT generation.')
        write_json({'Please do not edit manually!': 'Cf. sections-config.yaml and bin/sections.py'}, EG_LOCAL_TO_GLOBAL_AT)
        write_json({'Please do not edit manually!': 'Cf. sections-config.yaml and bin/sections.py'}, EG_GLOBAL_TO_LOCAL_AT)
        return 0

    # ------------------------------------------------------------------
    # Phase 6: validate example continuity per section and assign globals
    # ------------------------------------------------------------------
    # Build per-section example list in document order
    examples_per_section: dict[str, list[tuple[int, int]]] = {}  # slug → [(line_idx, local_num)]
    for line_idx, sec_slug, local_num in example_lines_found:
        examples_per_section.setdefault(sec_slug, []).append((line_idx, local_num))

    example_defects = 0
    for sec_slug, entries in examples_per_section.items():
        nums = [n for _, n in entries]
        # Must start at 1
        if nums[0] != 1:
            example_defects += 1
            first_idx = entries[0][0]
            print(
                f'ERROR: First example in section {sec_slug!r} is number {nums[0]}'
                f' (expected 1) — line {first_idx}:'
            )
            highlight(all_lines, first_idx)
        # Must be gap-free and duplicate-free
        for pos in range(1, len(nums)):
            if nums[pos] == nums[pos - 1]:
                example_defects += 1
                dup_idx = entries[pos][0]
                print(
                    f'ERROR: Duplicate example number {nums[pos]}'
                    f' in section {sec_slug!r} — line {dup_idx}:'
                )
                highlight(all_lines, dup_idx)
            elif nums[pos] != nums[pos - 1] + 1:
                example_defects += 1
                gap_idx = entries[pos][0]
                print(
                    f'ERROR: Example number gap in section {sec_slug!r}:'
                    f' {nums[pos - 1]} → {nums[pos]} — line {gap_idx}:'
                )
                highlight(all_lines, gap_idx)

    if example_defects:
        print(f'ERROR: Found {example_defects} example continuity defect(s) — aborting.')
        return 1
    print(f'INFO: Example continuity valid across {len(examples_per_section)} section(s).')

    # ------------------------------------------------------------------
    # Phase 7: assign global example numbers and write LUTs
    # ------------------------------------------------------------------
    local_to_global: dict[str, str] = {
        'Please do not edit manually!': 'Cf. sections-config.yaml and bin/sections.py',
    }
    global_to_local: dict[str, str] = {
        'Please do not edit manually!': 'Cf. sections-config.yaml and bin/sections.py',
    }

    first_example = True
    global_counter = 0

    for line_idx, sec_slug, local_num in example_lines_found:
        local_label = f'{sec_slug}-eg-{local_num}'
        if first_example:
            global_num_str = str(meta_eg_global)
            first_example = False
        else:
            global_counter += 1
            global_num_str = str(global_counter)
        local_to_global[local_label] = global_num_str
        global_to_local[global_num_str] = local_label

    write_json(local_to_global, EG_LOCAL_TO_GLOBAL_AT)
    write_json(global_to_local, EG_GLOBAL_TO_LOCAL_AT)

    total = len(example_lines_found)
    print(f'INFO: Wrote {total} example LUT entries ({total - 1} real + 1 meta at {meta_eg_global}).')

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
