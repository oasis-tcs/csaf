#! /usr/bin/env python 
"""Bread and butter inversion of global example number to example sug mapping."""
import json
import pathlib

ETC_PATH = pathlib.Path('etc')
IN_PATH = ETC_PATH / 'example-global-to-local.json'
OUT_PATH = ETC_PATH / 'example-local-to-global.json'

if not ETC_PATH.is_dir():
    raise RuntimeError('Please execute me inside csaf_2.1/prose/edit/ because I am a simple tool')

with open(IN_PATH, 'rt', encoding='utf-8') as handle:
    data = json.load(handle)

inverted = {v: k for k, v in data.items()}
ordered = {k: inverted[k] for k in sorted(inverted)}

with open(OUT_PATH, 'wt', encoding='utf-8') as handle:
    json.dump(ordered, handle, indent=2)
