#! /usr/bin/env python
"""Bread and butter inversion of section numbers to label mapping."""
import json
import pathlib

ETC_PATH = pathlib.Path('etc')
IN_PATH = ETC_PATH / 'section-display-to-label.json'
OUT_PATH = ETC_PATH / 'section-label-to-display.json'

ENCODING = 'utf-8'
ENC_ERRS = 'ignore'
NL = '\n'

if not ETC_PATH.is_dir():
    raise RuntimeError('Please execute me inside csaf_2.1/prose/edit/ because I am a simple tool')

with open(IN_PATH, 'rt', encoding=ENCODING, errors=ENC_ERRS) as handle:
    data = json.load(handle)

unique = {v for v in data.values()}
if sorted(unique) != sorted(data.values()):
    pairs = {}
    for k, v in data.items():
        if v not in pairs:
            pairs[v] = [k]
        else:
            pairs[v].append(k)
    for label, places in pairs.items():
        print(f'{label=} occurs in {places=}')
    raise RuntimeError('Please ensure the section labels are unique')

inverted = {v: k for k, v in data.items()}
ordered = {
    'Please do not edit manually!': (
        "Instead, call 'make invert-sections' inside the clone-root/csaf_2.1/prose/edit folder."
    )
}
for k in sorted(inverted):
    ordered[k] = inverted[k]

with open(OUT_PATH, 'wt', encoding=ENCODING, errors=ENC_ERRS) as handle:
    json.dump(ordered, handle, indent=2)
    handle.write(NL)  # For POSIX compliance
