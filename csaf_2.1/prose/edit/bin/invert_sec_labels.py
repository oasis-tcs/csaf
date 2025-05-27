#! /usr/bin/env python 
"""Bread and butter inversion of section numbers to label mapping."""
import json
import pathlib

ETC_PATH = pathlib.Path('etc')
IN_PATH = ETC_PATH / 'section-display-to-label.json'
OUT_PATH = ETC_PATH / 'section-label-to-display.json'

if not ETC_PATH.is_dir():
    raise RuntimeError('Please execute me inside csaf_2.1/prose/edit/ because I am a simple tool')

with open(IN_PATH, 'rt', encoding='utf-8') as handle:
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
ordered = {k: inverted[k] for k in sorted(inverted)}

with open(OUT_PATH, 'wt', encoding='utf-8') as handle:
    json.dump(ordered, handle, indent=2)
