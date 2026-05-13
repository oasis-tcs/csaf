#!/usr/bin/env python3
"""
Extract and check all JSONPaths
"""

import jsonpath
import re
import sys
from pathlib import Path

FENCE = "```"
LOJP = "list-of-jsonpaths"
INLINE = re.compile(r'`(\$|\$\..*?)\`')

def walk_through(text: str) -> str:
    olines = text.splitlines()
    jlines = []
    inside_fence = False
    last_lang = ""

    for index, line  in enumerate(olines):
        sline = line.strip()
        # Is this a code block marker?
        if sline.startswith(FENCE):
            inside_fence = not inside_fence
            last_lang = sline[3:]
            continue
        # Are we inside a LOJP code block?
        if inside_fence and last_lang == LOJP:
            jlines.append({"number": index, "path": sline})
        # Let's also check inline JSONPath...
        if not inside_fence:
            for instance in re.finditer(INLINE, sline):
                jlines.append({"number": index, "path": instance.group(1)})
    return jlines

def process_file(path: Path) -> int:
    result = 0
    try:
        text = path.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        return False
    jsonpaths = walk_through(text)
    for current in jsonpaths:
        try:
            jsonpath.compile(current["path"], strict=True)
        except Exception as e:
            print(path.name + ":" + str(current["number"]+1)+"\t" + e.message + "(" + current["path"]+")")
            result = 2
    return result

def main(argv):
    result = 0
    if len(argv) > 1:
        files = [Path(p) for p in argv[1:]]
    else:
        files = sorted(Path('.').glob('*.md'))
    if not files:
        print("No markdown files found.", file=sys.stderr)
        return 1
    for path in files:
        if not path.is_file():
            continue
        result += process_file(path)
    exit(result)

if __name__ == '__main__':
    main(sys.argv)
