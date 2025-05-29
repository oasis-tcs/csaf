#! /usr/bin/env python
"""Bread and butter inversion of global example number to example sug mapping."""
import json
import pathlib

ETC_PATH = pathlib.Path('etc')
G2L_PATH = ETC_PATH / 'example-global-to-local.json'
L2G_PATH = ETC_PATH / 'example-local-to-global.json'

ENCODING = 'utf-8'
ENC_ERRS = 'ignore'
NL = '\n'

if not ETC_PATH.is_dir():
    raise RuntimeError('Please execute me inside csaf_2.1/prose/edit/ because I am a simple tool')

with open(G2L_PATH, 'rt', encoding=ENCODING, errors=ENC_ERRS) as handle:
    data = json.load(handle)

marker_value = "4321"
marker_seen = False
auto_serial = 1
cleansed = {}
for k, v in data.items():
    if not marker_seen:
        if k == marker_value:
            marker_seen = True
            cleansed[marker_value] = v
            continue
    cleansed[str(auto_serial)] = v
    auto_serial += 1

with open(G2L_PATH, 'wt', encoding=ENCODING, errors=ENC_ERRS) as handle:
    json.dump(cleansed, handle, indent=2)
    handle.write(NL)  # For POSIX compliance

inverted = {v: k for k, v in cleansed.items()}
ordered = {
    'Please do not edit manually!': (
        "Instead, call 'make invert-examples' inside the clone-root/csaf_2.1/prose/edit folder."
    )
}
for k in sorted(inverted):
    ordered[k] = inverted[k]

with open(L2G_PATH, 'wt', encoding=ENCODING, errors=ENC_ERRS) as handle:
    json.dump(ordered, handle, indent=2)
    handle.write(NL)  # For POSIX compliance
