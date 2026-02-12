#! /usr/bin/env python
"""Given a target date, bump the version in all relevant places for the next editor revision."""
import calendar as cal
import datetime as dti
import difflib
import pathlib
import os
import sys

ENCODING = 'utf-8'
ENC_ERRS = 'ignore'
NL = '\n'
CB_END = '}'
COLON = ':'
COMMA = ','
DASH = '-'
DOT = '.'
FULL_STOP = '.'
HASH = '#'
PARA = '§'
SEMI = ';'
SPACE = ' '
CSEP = COMMA + SPACE
TM = '™'

MONTHS_EN = (
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
)

here = pathlib.Path().absolute()
tool = pathlib.Path(__file__)
path = tool.relative_to(here)
usage = f'usage: {path} [--commit] "DD Month YYYY"'

args = sys.argv[1:]

if not args:
    print(usage)
    sys.exit(0)

commit = False
for slot, arg in enumerate(args):
    if arg.lower() == '--commit':
        commit = True
        del args[slot]

try:
    DD, Month, YYYY = args[0].split(SPACE)
except ValueError:
    print(usage)
    print(f'ERROR: Parsing date value ({args[0]})')
    sys.exit(2)
except IndexError:
    print(usage)
    print(f'ERROR: Not enough arguments')
    sys.exit(2)

PUB_DAY = DD
PUB_MONTH_EN = Month.title()
PUB_YEAR = YYYY

if len(PUB_DAY) != 2:
    print('ERROR: Day part must be two-digits (zero-padded)')
    sys.exit(2)

try:
    d = int(PUB_DAY)
    if not 1 <= d <= 31:
        raise ValueError
except ValueError:
    print('ERROR: Day part must be an integral number in [1, 31]')
    sys.exit(2)

if PUB_MONTH_EN not in MONTHS_EN:
    print(f'ERROR: English month part must be in ({CSEP.join(MONTHS_EN)})')
    sys.exit(2)

PUB_MONTH = '00'
for number, name in enumerate(MONTHS_EN, start=1):
    if PUB_MONTH_EN == name:
        PUB_MONTH = f'{number :02d}'

if PUB_MONTH == '00':
    print('ERROR: English month part to %m mapping failed')
    sys.exit(1)

if len(PUB_YEAR) != 4:
    print('ERROR: Year part must be four-digits')
    sys.exit(2)

now = dti.datetime.now(dti.UTC)
this_year = now.year

try:
    y = int(PUB_YEAR)
    if y < this_year - 1:
        raise ValueError
except ValueError:
    print(f'ERROR: Year part must be an integral number >= {this_year - 1}')
    sys.exit(2)

try:
    m = int(PUB_MONTH)
    if not 1 <= m <= 12:
        raise ValueError
except ValueError:
    print('ERROR: Month part must map to an integral number in [1, 12]')
    sys.exit(1)

_, max_days_of_month = cal.monthrange(y, m)
if d > max_days_of_month:
    print(f'ERROR: Day part must be inside days of month [1, {max_days_of_month}]')
    sys.exit(2)

if not commit:
    print('INFO: Dry-run only - only diffs are shown and no files changed.')
else:
    print('INFO: Commit mode - the magical four files will be bumped.')

PUB_DATE = f'{PUB_DAY} {PUB_MONTH_EN} {PUB_YEAR}'
DEBUG = bool(os.getenv('BUMP_DEBUG', ''))

# Configuration and runtime parameter candidates:
PDF_BOOKMATTER_IN = pathlib.Path('etc/liitos/bookmatter.tex.in')
PDF_META_YAML = pathlib.Path('etc/liitos/meta.yml')
SRC_FRONTMATTER = pathlib.Path('src/frontmatter.md')
SRC_HISTORY = pathlib.Path('src/revision-history.md')

with open(PDF_BOOKMATTER_IN, 'rt', encoding=ENCODING, errors=ENC_ERRS) as source:
    lines = [line.rstrip(NL) for line in source.readlines()]

bumped = []
for line in lines:
    prefix = r'\subsection*{'
    postfix = r'}\label{pub-date}'
    # \subsection*{28 January 2026}\label{pub-date}
    if line.startswith(prefix) and line.endswith(postfix):
        pub_date = line.replace(prefix, '').replace(postfix, '')
        DEBUG and print(f'DEBUG: Found prior pub-date ({pub_date})')
        bumped.append(prefix + PUB_DATE + postfix)
        DEBUG and print(f'DEBUG: Bumped to ({PUB_DATE})')
        continue

    prefix = 'Hagen, and Thomas Schmidt. '
    postfix = '. OASIS Committee Specification'
    # Hagen, and Thomas Schmidt. 28 January 2026. OASIS Committee Specification
    if line.startswith(prefix) and line.endswith('. OASIS Committee Specification'):
        pub_date = line.replace(prefix, '').replace('. OASIS Committee Specification', '')
        DEBUG and print(f'DEBUG: Found prior pub-date ({pub_date})')
        bumped.append(prefix + PUB_DATE + '. OASIS Committee Specification')
        DEBUG and print(f'DEBUG: Bumped to ({PUB_DATE})')
        continue

    bumped.append(line)

print(f'# - - - 8< - -(( {PDF_BOOKMATTER_IN} )) - - - - - - - - - - - - - - >')
print()
sys.stdout.writelines(difflib.unified_diff(
    tuple(line + NL for line in lines),
    tuple(line + NL for line in bumped),
    fromfile='bookmatter.tex.in',
    tofile='bookmatter-bumped.tex.in',
))

if commit:
    with open(PDF_BOOKMATTER_IN, 'wt', encoding=ENCODING, errors=ENC_ERRS) as target:
        target.write(NL.join(bumped) + NL)

with open(PDF_META_YAML, 'rt', encoding=ENCODING, errors=ENC_ERRS) as source:
    lines = [line.rstrip(NL) for line in source.readlines()]

bumped = []
for line in lines:
    #     footer_outer_field_normal_pages: 28 January 2026 - \theMetaPageNumPrefix { } \thepage { } of \pageref{LastPage}
    prefix = '    footer_outer_field_normal_pages: '
    postfix = r' - \theMetaPageNumPrefix { } \thepage { } of \pageref{LastPage}'
    if line.startswith(prefix) and line.endswith(postfix):
        pub_date = line.replace(prefix, '').replace(postfix, '')
        DEBUG and print(f'DEBUG: Found prior pub-date ({pub_date})')
        bumped.append(prefix + PUB_DATE + postfix)
        DEBUG and print(f'DEBUG: Bumped to ({PUB_DATE})')
        continue

    bumped.append(line)

print()
print(f'# - - - 8< - -(( {PDF_META_YAML} )) - - - - - - - - - - - - - - - - - - >')
print()
sys.stdout.writelines(difflib.unified_diff(
    tuple(line + NL for line in lines),
    tuple(line + NL for line in bumped),
    fromfile='meta.yml',
    tofile='meta-bumped.yml',
))

if commit:
    with open(PDF_META_YAML, 'wt', encoding=ENCODING, errors=ENC_ERRS) as target:
        target.write(NL.join(bumped) + NL)

with open(SRC_FRONTMATTER, 'rt', encoding=ENCODING, errors=ENC_ERRS) as source:
    lines = [line.rstrip(NL) for line in source.readlines()]

bumped = []
for line in lines:
    # ## 28 January 2026
    prefix = '## '
    postfix = ''
    if line.startswith(prefix):
        try:
            day = line.replace(prefix, '').replace(postfix, '').split(SPACE)[0]
            int(day)
            pub_date = line.replace(prefix, '').replace(postfix, '')
            DEBUG and print(f'DEBUG: Found prior pub-date ({pub_date})')
            bumped.append(prefix + PUB_DATE + postfix)
            DEBUG and print(f'DEBUG: Bumped to ({PUB_DATE})')
            continue
        except ValueError:
            pass

    # _Common Security Advisory Framework Version 2.1_. Edited by Stefan Hagen and Thomas Schmidt. \
    # 17 December 2025\
    #. OASIS Committee Specification Draft 02. https://docs.oasis-open.org/csaf/csaf/v2.1/csd02/csaf-v2.1-csd02.html. Latest stage: https://docs.oasis-open.org/csaf/csaf/v2.1/csaf-v2.1.html.
    prefix = '_Common Security Advisory Framework Version 2.1_. Edited by Stefan Hagen and Thomas Schmidt. '
    postfix = '. OASIS Committee Specification Draft 02. https://docs.oasis-open.org/csaf/csaf/v2.1/csd02/csaf-v2.1-csd02.html. Latest stage: https://docs.oasis-open.org/csaf/csaf/v2.1/csaf-v2.1.html.'
    if line.startswith(prefix) and line.endswith(postfix):
        pub_date = line.replace(prefix, '').replace(postfix, '')
        DEBUG and print(f'DEBUG: Found prior pub-date ({pub_date})')
        bumped.append(prefix + PUB_DATE + postfix)
        DEBUG and print(f'DEBUG: Bumped to ({PUB_DATE})')
        continue

    # Copyright © OASIS Open 2026. All Rights Reserved.
    prefix = 'Copyright © OASIS Open '
    postfix = '. All Rights Reserved.'
    if line.startswith(prefix) and line.endswith(postfix):
        pub_date = line.replace(prefix, '').replace(postfix, '')
        DEBUG and print(f'DEBUG: Found prior pub-date ({pub_date})')
        bumped.append(prefix + PUB_YEAR + postfix)
        DEBUG and print(f'DEBUG: Bumped to ({PUB_DATE})')
        continue

    bumped.append(line)

print()
print(f'# - - - 8< - -(( {SRC_FRONTMATTER} )) - - - - - - - - - - - - - - - - - - >')
print()
sys.stdout.writelines(difflib.unified_diff(
    tuple(line + NL for line in lines),
    tuple(line + NL for line in bumped),
    fromfile='frontmatter.md',
    tofile='frontmatter-bumped.md',
))

if commit:
    with open(SRC_FRONTMATTER, 'wt', encoding=ENCODING, errors=ENC_ERRS) as target:
        target.write(NL.join(bumped) + NL)

with open(SRC_HISTORY, 'rt', encoding=ENCODING, errors=ENC_ERRS) as source:
    lines = [line.rstrip(NL) for line in source.readlines()]

bumped = []
past_table = None  # State machine: None -> False -> True -> None
prefix = '| csaf-v2.1-wd'
in_between = f'{PUB_YEAR}{PUB_MONTH}{PUB_DAY}-dev | {PUB_YEAR}-{PUB_MONTH}-{PUB_DAY}'
postfix = ' | Stefan Hagen and Thomas Schmidt | Editor Revision for CSD02                   |'
for line in lines:
    # | csaf-v2.1-wd20260128-dev | 2025-01-28 | Stefan Hagen and Thomas Schmidt | Editor Revision for CSD02                   |
    # <-- append here when past_table is True
    prefix = '| csaf-v2.1-wd'
    if line.startswith(prefix) and past_table is None:
        past_table = False
        bumped.append(line)
        continue

    if line.startswith(prefix) and past_table is False:
        bumped.append(line)
        continue

    if not line.strip() and past_table is False:
        DEBUG and print('DEBUG: Found empty line following revision history table')
        bumped.append(prefix + in_between + postfix)
        DEBUG and print(f'DEBUG: Appended with in_between ({in_between})')
        bumped.append(line)
        continue

    bumped.append(line)

print()
print(f'# - - - 8< - -(( {SRC_HISTORY} )) - - - - - - - - - - - - - - - - - - >')
print()
sys.stdout.writelines(difflib.unified_diff(
    tuple(line + NL for line in lines),
    tuple(line + NL for line in bumped),
    fromfile='revision-history.md',
    tofile='revision-history-bumped.md',
))

if commit:
    with open(SRC_HISTORY, 'wt', encoding=ENCODING, errors=ENC_ERRS) as target:
        target.write(NL.join(bumped) + NL)
    print()
    print('Bumped - OK')
else:
    print()
    print('Dry-Bumped - OK')
