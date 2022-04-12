#! /usr/bin/env python3
"""Verify or modify filenames of security advisories against CSAF 2.0 rules."""
import argparse
import json
import pathlib
import re
import sys

ENCODING = 'utf-8'
INVALID_ID = '_invalid'
VALID_NAME_PAT = r'([^+\-_a-z0-9]+)'
SUCC = 'TRUE'
FAIL = 'FALSE'


def load(csaf_path):
    """Load the CSAF data from the path to the JSON file or fail miserably."""
    with open(csaf_path, 'rt', encoding=ENCODING) as handle:
        return json.load(handle)


def dump(csaf_data, csaf_path):
    """Dump the CSAF data formated to 2 space indent to the JSON file given by the path."""
    with open(csaf_path, 'wt', encoding=ENCODING) as f:
        json.dump(csaf_data, f, indent=2)


def compute_filename(csaf_data):
    """Derive the filename from document/tracking/id if exists else return the conventional invalid json name."""
    document_tracking_id = INVALID_ID
    if (doc := csaf_data.get('document')) and (track := doc.get('tracking')) and (the_id := track.get('id')):  # noqa
        document_tracking_id = the_id

    return f'{re.sub(VALID_NAME_PAT, "_", document_tracking_id.lower())}.json'


def api():
    """Implementation of command line API returning parser."""
    parser = argparse.ArgumentParser(description='Verifies or modifies the name of a CSAF 2.0 advisory file')
    parser.add_argument('input_file', type=str, help='CSAF advisory file to verify or modify the filename of')
    parser.add_argument('-p', '--print', dest='echo', action='store_true', help='Prints the correct filename')
    parser.add_argument(
        '-v',
        '--verbose',
        dest='verbose',
        action='store_true',
        help=f'Prints the logic result as either {SUCC} or {FAIL}',
    )
    parser.add_argument(
        '-a',
        '--add',
        dest='add',
        action='store_true',
        help=(
            'Writes the CSAF advisory file to the correct filename if different'
            ' - will overrule -u/--update if given in addition'
        ),
    )
    parser.add_argument(
        '-u',
        '--update',
        dest='update',
        action='store_true',
        help=(
            'Renames the CSAF advisory file to the correct filename if necessary'
            ' - will be overruled by -a/--add if given in addition'
        ),
    )
    return parser


def main(argv=None):
    """Drive the verification or modification of advisory file(name)s per CSAF 2.0 rules."""
    argv = sys.argv[1:] if argv is None else argv
    job = api().parse_args(argv)
    data = load(job.input_file)
    current_path = pathlib.Path(job.input_file)
    correct_path = current_path.parent / compute_filename(data)
    ok = current_path == correct_path

    if job.echo:
        print(correct_path.name)
    if job.verbose:
        print(SUCC if ok else FAIL)

    if ok:
        return 0

    if job.add:
        dump(data, correct_path)
    elif job.update:
        _ = current_path.rename(correct_path)

    return 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))