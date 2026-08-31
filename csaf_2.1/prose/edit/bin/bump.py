#! /usr/bin/env python
"""Given a target date, bump the version in all relevant places for the next editor revision."""
import calendar as cal
import datetime as dti
import difflib
import json
import locale
import pathlib
import os
import sys

# Types
Job = dict[str, bool | str | int]
Messages = list[str]
PathLike = str | pathlib.Path
Replacements = list[str]
Transforms = list[dict[str, dict[str]]]

# General constants
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
LANG_CODE = 'C'

# Generate tuple with English month names in title case
locale.setlocale(locale.LC_ALL, LANG_CODE)
MONTHS_EN = tuple(name for name in cal.month_name[1:])

# Harden the key based job user data interface
COMMIT = 'commit'
DEBUG = 'debug'
DATE_SPEC = 'date-spec'

# Harden the key based job derived data interface
PUB_DAY_STR = 'pub-day-str'
PUB_MONTH_NAME_EN = 'pub-month-name-en'
PUB_YEAR_STR = 'pub-year-str'

PUB_DAY_INT = 'pub-day-int'
PUB_MONTH_STR = 'pub-month-en-str'
PUB_MONTH_INT = 'pub-month-int'
PUB_YEAR_INT = 'pub-year-int'

PUB_DATE = 'pub-date'
PUB_ISO_COMPACT = 'pub-iso-compact'
PUB_ISO_DASH = 'pub-iso-dash'

# Transform keys
PREFIX = 'prefix'
POSTFIX = 'postfix'
OPERATOR = 'operator'
TOKEN = 'token'
REPLACEMENT_CODE = 'replacement-code'

# Nicer usage info
here = pathlib.Path().absolute()
tool = pathlib.Path(__file__)
path = tool.relative_to(here)
USAGE = f'usage: {path} [--{COMMIT}] [--{DEBUG}] "DD Month YYYY"'

# Configuration and runtime parameter candidates:
PDF_CSAF_TYP = pathlib.Path('etc/csaf.typ')
SRC_FRONTMATTER = pathlib.Path('src/frontmatter.md')

SIMPLE_TRANSFORMS = {
    PDF_CSAF_TYP: [
        {
            PREFIX: {
                TOKEN: '    text(size: 8pt)[Copyright © OASIS Open ',
                OPERATOR: 'startswith',
            },
            REPLACEMENT_CODE: PUB_YEAR_STR,
            POSTFIX: {
                TOKEN: '. All Rights Reserved.],',
                OPERATOR: 'endswith',
            },
        },
        {
            PREFIX: {
                TOKEN: '    text(size: 8pt)[',
                OPERATOR: 'startswith',
            },
            REPLACEMENT_CODE: PUB_DATE,
            POSTFIX: {
                TOKEN: ' — Page #counter(page).display()',
                OPERATOR: 'endswith',
            },
        },
    ],
}


def parse_date_spec(job: Job, month_names: tuple[str, ...] = MONTHS_EN) -> tuple[int, Job, Messages]:
    """Parse (and validate) the given date-spec in the job into a multi format structure.

    Note: Expected is format DD B YYYY, where B is the format-code for a title cased
          English month name like January.
    """
    messages: Messages = []
    try:
        day_str, month_name_en, year_str = job[DATE_SPEC].split(SPACE)
        job[PUB_DAY_STR] = day_str
        month_name_en = month_name_en.title()
        job[PUB_MONTH_NAME_EN] = month_name_en
        job[PUB_YEAR_STR] = year_str
    except ValueError:
        messages.append(f'ERROR: Parsing date value ({job[DATE_SPEC]})')
        return 2, messages
    except IndexError:
        messages.append(f'ERROR: Not enough arguments for date-spec in ({job[DATE_SPEC]})')
        return 2, messages

    if len(job[PUB_DAY_STR]) != 2:
        messages.append('ERROR: Day part must be two-digits (zero-padded)')
        return 2, messages

    try:
        job[PUB_DAY_INT] = int(job[PUB_DAY_STR])
        if not 1 <= job[PUB_DAY_INT] <= 31:
            raise ValueError
    except ValueError:
        messages.append('ERROR: Day part must be an integral number in [1, 31]')
        return 2, messages

    if job[PUB_MONTH_NAME_EN] not in month_names:
        messages.append(f'ERROR: English month part must be in ({CSEP.join(month_names)})')
        return 2, messages

    job[PUB_MONTH_STR] = '00'
    for number, name in enumerate(month_names, start=1):
        if month_name_en == name:
            job[PUB_MONTH_STR] = f'{number :02d}'

    if job[PUB_MONTH_STR] == '00':
        messages.append('ERROR: English month part to %m mapping failed')
        return 1, messages

    if len(year_str) != 4:
        messages.append('ERROR: Year part must be four-digits')
        return 2, messages

    now = dti.datetime.now(dti.UTC)
    this_year = now.year
    try:
        job[PUB_YEAR_INT] = int(job[PUB_YEAR_STR])
        if job[PUB_YEAR_INT] < this_year - 1:
            raise ValueError
    except ValueError:
        messages.append(f'ERROR: Year part must be an integral number >= {this_year - 1}')
        return 2, messages

    try:
        job[PUB_MONTH_INT] = int(job[PUB_MONTH_STR])
        if not 1 <= job[PUB_MONTH_INT] <= 12:
            raise ValueError
    except ValueError:
        messages.append('ERROR: Month part must map to an integral number in [1, 12]')
        return 1, messages

    _, max_days_of_month = cal.monthrange(job[PUB_YEAR_INT], job[PUB_MONTH_INT])
    if job[PUB_DAY_INT] > max_days_of_month:
        messages.append(f'ERROR: Day part must be inside days of month [1, {max_days_of_month}]')
        return 2, messages

    job[PUB_DATE] = f'{job[PUB_DAY_STR]}{SPACE}{job[PUB_MONTH_NAME_EN]}{SPACE}{job[PUB_YEAR_STR]}'
    job[PUB_ISO_DASH] = f'{job[PUB_YEAR_STR]}{DASH}{job[PUB_MONTH_STR]}{DASH}{job[PUB_DAY_STR]}'
    job[PUB_ISO_COMPACT] = job[PUB_ISO_DASH].replace(DASH, '')

    return 0, messages


def parse_args(args: list[str]) -> tuple[int, Job, Messages]:
    """Parse the given arguments returning an error code, the expected job structure, and messages."""
    job: Job = {}
    messages: Messages = []
    if not args:
        return 0, job, messages

    job[DEBUG] = bool(os.getenv('BUMP_DEBUG', ''))
    for slot, arg in enumerate(args):
        if arg.lower() == f'--{DEBUG}':
            job[DEBUG] = True
            del args[slot]

    job[COMMIT] = False
    for slot, arg in enumerate(args):
        if arg.lower() == f'--{COMMIT}':
            job[COMMIT] = True
            del args[slot]

    job[DATE_SPEC] = ''
    try:
        slot = 0
        job[DATE_SPEC] = args[slot].strip(SPACE)
        del args[slot]
    except IndexError:
        messages.append('ERROR: Not enough arguments')
        return 2, job, messages

    if args:
        messages.append('ERROR: Too many arguments')
        return 2, job, messages

    return 0, job, messages


def dump_target(file_path: PathLike, lines: list[str]) -> None:
    """Dump the newline joined lines to the target text file path.

    Note: a trailing newline is appended for POSIX conformance.
    """
    with open(file_path, 'wt', encoding=ENCODING, errors=ENC_ERRS) as target:
        target.write(NL.join(lines) + NL)


def output(file_path: PathLike, old: list[str], new: list[str], changes_detected: bool, do_commit: bool) -> bool:
    """Show change state, diff if applicable, dump to path if do-commit, and return chained change state."""
    if old != new:
        if not changes_detected:
            changes_detected = True
        print()
        print(f'# - - - 8< - -(( {file_path} )) - - - - - - - - - - - - - - - - - - >')
        print()
        sys.stdout.writelines(difflib.unified_diff(
            tuple(line + NL for line in old),
            tuple(line + NL for line in new),
            fromfile=f'{file_path}(old)',
            tofile=f'{file_path}(new)',
        ))
        if do_commit:
            dump_target(file_path, new)
    else:
        print(f'INFO: No changes to {file_path}')

    return changes_detected


def load_target(file_path: PathLike) -> list[str]:
    """Load the target text from file path and return the list of newline stripped lines."""
    with open(file_path, 'rt', encoding=ENCODING, errors=ENC_ERRS) as source:
        return [line.rstrip(NL) for line in source.readlines()]


def apply_simple_changes(
    file_path: PathLike,
    old: list[str],
    transforms: Transforms,
    job: Job,
) -> tuple[int, list[str]]:
    """Apply the transforms and replacements to old in simple cases and return error code and new.

    Note: when error code not zero, than new contains not the transformed data but a list of messages"""
    if file_path not in transforms:
        msg = f'ERROR: [{file_path}] not in keys ({COMMA.join(transforms)}) of transforms map'
        return 2, [msg]
    we_debug = job.get(DEBUG, False)
    if we_debug:
        print('#  -  -  -  -  -  -  -  -  - ')
        print(f'DEBUG: [{file_path}] Applying transforms:')
        print(json.dumps(transforms[file_path], indent=2))
    new = []
    for line in old:
        applied = False
        for transform in transforms[file_path]:

            pre_tok = transform[PREFIX][TOKEN]
            op_str = transform[PREFIX][OPERATOR]
            pre_op = getattr(line, op_str, None)
            if pre_op is None:
                msg = f'ERROR: [{file_path}] unexpected prefix matching operator {op_str}'
                return 2, [msg]

            replacement = job.get(transform[REPLACEMENT_CODE], None)
            if replacement is None:
                msg = f'ERROR: [{file_path}] replacement code ({transform[REPLACEMENT_CODE]}) not known'
                return 2, [msg]

            post_tok = transform[POSTFIX][TOKEN]
            op_str = transform[POSTFIX][OPERATOR]
            post_op = getattr(line, op_str, None)
            if post_op is None:
                msg = f'ERROR: [{file_path}] unexpected postfix matching operator {op_str}'
                return 2, [msg]

            if pre_op(pre_tok) and post_op(post_tok):
                value = line.replace(pre_tok, '').replace(post_tok, '')
                we_debug and print(f'DEBUG: Found prior value ({value})')
                new.append(pre_tok + replacement + post_tok)
                we_debug and print(f'DEBUG: Replaced with ({replacement})')
                applied = True

        if not applied:
            new.append(line)

    return 0, new


def main(args: list[str]) -> int:
    """Drive the transform to bump the dates based on the given argument."""
    err, job, messages = parse_args(args)

    if not err and not job:
        print(USAGE)
        return err

    if err:
        print(USAGE)
        for message in messages:
            print(message)
        return err

    err, messages = parse_date_spec(job)

    if err:
        print(USAGE)
        for message in messages:
            print(message)
        return err

    do_commit = job[COMMIT]
    debug = job[DEBUG]
    if debug:
        print('DEBUG: The job was parsed as follows:')
        print(json.dumps(job, indent=2))

    if not do_commit:
        print('INFO: Dry-run only - only diffs are shown and no files changed.')
        print()
    else:
        print('INFO: Commit mode - the magical five files will be bumped.')
        print()

    any_changes = False

    lines = load_target(PDF_CSAF_TYP)
    err, bumped = apply_simple_changes(PDF_CSAF_TYP, lines, SIMPLE_TRANSFORMS, job)
    if err:
        for message in messages:
            print(message)
        return err
    any_changes = output(PDF_CSAF_TYP, lines, bumped, any_changes, do_commit)

    lines = load_target(SRC_FRONTMATTER)
    bumped = []
    debug and print('#  -  -  -  -  -  -  -  -  - ')
    for line in lines:
        prefix = '## '
        postfix = ''
        if line.startswith(prefix):
            try:
                day = line.replace(prefix, '').replace(postfix, '').split(SPACE)[0]
                int(day)
                pub_date = line.replace(prefix, '').replace(postfix, '')
                debug and print(f'DEBUG: Found prior pub-date ({pub_date})')
                bumped.append(prefix + job[PUB_DATE] + postfix)
                debug and print(f'DEBUG: Replaced with ({job[PUB_DATE]})')
                continue
            except ValueError:
                pass

        prefix = '_Common Security Advisory Framework Version 2.1_. Edited by Stefan Hagen and Thomas Schmidt. '
        postfix = '. OASIS Committee Specification Draft 03. https://docs.oasis-open.org/csaf/csaf/v2.1/csd03/csaf-v2.1-csd03.html. Latest stage: https://docs.oasis-open.org/csaf/csaf/v2.1/csaf-v2.1.html.'
        if line.startswith(prefix) and line.endswith(postfix):
            pub_date = line.replace(prefix, '').replace(postfix, '')
            debug and print(f'DEBUG: Found prior pub-date ({pub_date})')
            bumped.append(prefix + job[PUB_DATE] + postfix)
            debug and print(f'DEBUG: Replaced with ({job[PUB_DATE]})')
            continue

        if 11 < len(line) < 19 and line.endswith(postfix):
            pub_date = line.replace(prefix, '').replace(postfix, '')
            try:
                a_day, a_month_name, a_year = pub_date.split(SPACE)  # noqa
            except (ValueError, IndexError):
                bumped.append(line)
                continue
            debug and print(f'DEBUG: Found prior pub-date ({pub_date})')
            bumped.append(prefix + job[PUB_DATE] + postfix)
            debug and print(f'DEBUG: Replaced with ({job[PUB_DATE]})')
            continue

        prefix = 'Copyright © OASIS Open '
        postfix = '. All Rights Reserved.'
        if line.startswith(prefix) and line.endswith(postfix):
            pub_date = line.replace(prefix, '').replace(postfix, '')
            debug and print(f'DEBUG: Found prior pub-date ({pub_date})')
            bumped.append(prefix + job[PUB_YEAR_STR] + postfix)
            debug and print(f'DEBUG: Replaced with ({job[PUB_DATE]})')
            continue

        bumped.append(line)

    any_changes = output(SRC_FRONTMATTER, lines, bumped, any_changes, do_commit)

    print()
    if any_changes:
        print('INFO: Bumped - OK') if do_commit else print('INFO: Dry-Bumped - OK')
    else:
        print('INFO: No changes - no commit - OK') if do_commit else print('INFO: No dry-changes - nothing would be committed - OK')

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
