#! /usr/bin/env python
"""Given a testcases instance list, check all mentioned result files for consistency."""

import sys
import json
import pathlib

# Types
Job = dict[str, bool | str | int]
Messages = list[str]
PathLike = str | pathlib.Path

# General constants
ENCODING = 'utf-8'
ENC_ERRS = 'ignore'
SPACE = ' '

# Harden the key based job user data interface
TESTCASES_PATH = 'testcases-path'

# Nicer usage info
here = pathlib.Path().absolute()
tool = pathlib.Path(__file__)
path = tool.relative_to(here)
USAGE = f'usage: {path}  "path/to/testcases.json"'

# Mapping
MAPPING = {'1': 'errors', '2': 'warnings', '3': 'infos'}

def parse_args(args: list[str]) -> tuple[int, Job, Messages]:
    """Parse the given arguments returning an error code, the expected job structure, and messages."""
    job: Job = {}
    messages: Messages = []
    if not args:
        return 0, job, messages

    job[TESTCASES_PATH] = ''
    try:
        slot = 0
        job[TESTCASES_PATH] = args[slot].strip(SPACE)
        del args[slot]
    except IndexError:
        messages.append('ERROR: Not enough arguments')
        return 2, job, messages

    if args:
        messages.append('ERROR: Too many arguments')
        return 2, job, messages

    return 0, job, messages

def calculate_path_offset(testcase_path: PathLike) -> PathLike:
    return pathlib.Path(testcase_path).parent

def load_json(file_path: PathLike) -> dict:
    """Load the JSON from file path and return as dict."""
    with open(file_path, 'rt', encoding=ENCODING, errors=ENC_ERRS) as source:
        return json.loads(source.read())

def check_result_consistency(result: dict) -> tuple[int, list[str]]:
    """Check a result object for consistency"""
    error_count = 0
    messages = []
    passed = result['passed']
    id = result['id']
    group = id.split('.')[1]
    expected_value = MAPPING[group]

    # if the test fails, there must be an appropriate message
    if not passed:
        actual = result.get(expected_value, [])
        if len(actual) == 0:
            error_count += 1
            messages.append('\t- inconsistent result (expected len of ' + expected_value + ' > 0 , actual length: is 0)')
    # also there can't be a higher message
    for i in range(int(group)-1):
        current = result.get(MAPPING[str(i+1)])
        if current is not None:
            error_count += 1
            messages.append('\t- inconsistent result (expected ' + MAPPING[str(i+1)] + ' to be empty, actual: ' + str(current) + ' )')
    return error_count, messages

def check_testcase_consistency(testcase: dict, path_offset: PathLike, result_path: PathLike, expected_state: bool) -> int:
    """Check testcase consistency"""
    error_count = 0
    result = load_json(path_offset / result_path)
    print(result_path, end='\t')
    overall_valid = result['overall_valid']
    primary_result = result['primary_result']
    secondary_results = result.get("secondary_results", [])
    passed = primary_result.get('passed', False)
    messages = []

    # overall_valid matches valid in testcase
    if overall_valid != testcase['valid']:
        error_count += 1
        messages.append('\t- has inconsistent overall_valid state (expected: ' + str(testcase['valid']) + ', actual: ' + str(overall_valid) + ')')

    # overall_valid needs at least one error message
    pr_error_list_len = len(primary_result.get("errors", []))
    sr_error_list_len = 0
    for i in secondary_results:
        sr_error_list_len += len(i.get("errors", []))

    if (overall_valid != ((pr_error_list_len + sr_error_list_len) == 0)):
        error_count += 1
        messages.append('\t- overall_valid state is ' + str(overall_valid) + ' but length of primary_result errors is ' + str(pr_error_list_len)
                + ' and length of secondary errors is ' + str(sr_error_list_len))

    # testcase expected_state (valid / failure) needs to be consistent with result state
    if passed is None or passed != expected_state:
        error_count += 1
        messages.append('\t- passed state is ' + str(passed) + ' but expected state is ' + str(expected_state))

    # Todo: Check primary result consistency
    pr_err_count, pr_messages = check_result_consistency(primary_result)
    error_count += pr_err_count
    messages += pr_messages
    # Todo: Check secondary results consistency
    for sr in secondary_results:
        sr_err_count, sr_messages = check_result_consistency(sr)
        error_count += sr_err_count
        messages += sr_messages

    if error_count == 0:
        print("... SUCCESS")
    else:
        print("... FAILED")
        print(*messages, sep='\n')

    return error_count

def walk_testcases(testcases: dict, path_offset: PathLike) -> int:
    """Walk over testcases and check consistency"""
    error_count = 0
    tests = testcases['tests']
    for current in tests:
        # Check result of testcases expected to fail
        failures = current.get('failures', [])
        for cfailing in failures:
            result_path = cfailing.get('result', None)

            if result_path is not None:
                error_count += check_testcase_consistency(cfailing, path_offset, result_path, False)

        # Check result of testcases expected to be valid
        valid = current.get('valid', [])
        for cvalid in valid:
            result_path = cvalid.get('result', None)
            if result_path is not None:
                error_count += check_testcase_consistency(cvalid, path_offset, result_path, True)
    return error_count


def main(args: list[str]) -> int:
    """Drive the consistency checks based on the given argument."""
    err, job, messages = parse_args(args)

    if not err and not job:
        print(USAGE)
        return err

    if err:
        print(USAGE)
        for message in messages:
            print(message)
        return err

    testcases = load_json(job[TESTCASES_PATH])
    path_offset = calculate_path_offset(job[TESTCASES_PATH])
    error_count = walk_testcases(testcases, path_offset)
    return error_count

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
