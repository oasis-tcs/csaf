#! /usr/bin/env python
"""check labels script file for prototyping that may take on different behaviors in time.

This one-off script checks whether the labels assigned to examples match the names and orders of the sections.
It may report any failures for the editors to fix.
It does not check against the files in the sources.
"""

import json
import pathlib
import sys
import os
from typing import Union


ENCODING = 'utf-8'
ENC_ERRS = 'ignore'
NL = '\n'
TAB = '\t'

SECTION_DISPLAY_TO_LABEL_AT = pathlib.Path('etc') / 'section-display-to-label.json'
SECTION_LABEL_TO_DISPLAY_AT = pathlib.Path('etc') / 'section-label-to-display.json'
EG_GLOBAL_TO_LABEL_AT = pathlib.Path('etc') / 'example-global-to-local.json'
EG_LABEL_TO_GLOBAL_AT = pathlib.Path('etc') / 'example-local-to-global.json'

DEBUG = bool(os.getenv('LABELS_DEBUG', ''))


def load(path: Union[str, pathlib.Path]) -> dict[str, str]:
    """Load mapping from a JSON file."""
    with pathlib.Path(path).open('rt', encoding=ENCODING, errors=ENC_ERRS) as handle:
        return json.load(handle)

def load_display_to_label_lut(path: Union[str, pathlib.Path] = SECTION_DISPLAY_TO_LABEL_AT) -> dict[str, str]:
    """Load the LUT for section display -> labels."""
    return load(path)


def load_eg_global_to_label_lut(path: Union[str, pathlib.Path] = EG_GLOBAL_TO_LABEL_AT) -> dict[str, str]:
    """Load the LUT for example global -> labels."""
    return load(path)


def compare_luts(sec_display_to: dict[str, str], eg_global_to: dict[str, str]) -> int:
    """Compare LUTs: each entry in examples must match an entry in global"""
    eg_global_list = list(eg_global_to.items())
    counter= 0

    for s_key, s_value in sec_display_to.items():
        DEBUG and print(s_key, s_value)
        repeat=True
        while (repeat and counter < len(eg_global_list)):
            current_eg = eg_global_list[counter]
            current_eg_label = current_eg[1]
            DEBUG and print(current_eg_label)
            if current_eg_label[:-5] == s_value:
                print(f'{TAB}- Found Example: {current_eg[0]} {current_eg_label}')
                counter += 1
                repeat=True
            else:
                DEBUG and print(f'{TAB}- No example in this section')
                repeat=False

    if counter >= len(eg_global_list):
        print('All examples found - OK')
        return 0

    print('Following examples missing:')
    for i in range(counter, len(eg_global_list)):
        print("-", eg_global_list[i])

    return 1


def main() -> int:
    """Drive the check."""

    display_to = load_display_to_label_lut()
    eg_global_to = load_eg_global_to_label_lut()

    result = compare_luts(display_to, eg_global_to)

    return result


if __name__ == '__main__':
    sys.exit(main())
