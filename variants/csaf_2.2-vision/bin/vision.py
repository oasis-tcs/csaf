#!/usr/bin/env python3
"""Records -> views for the CSAF vision variant: tests are authored as records, the prose and the test suite are derived.

  vision.py migrate   one-off: read today's tests-*.md and testcases.json into records/tests/*.yaml (refuses to overwrite)
  vision.py derive    write the views: the test sections of the prose, testcases.json, views/roles/*.md
  vision.py check     derive in memory and report every view that differs from the tree (exit 1 if any)

Requires PyYAML. Paths are relative to the variant root (the parent of bin/).
"""

from __future__ import annotations

import argparse
import functools
import json
import pathlib
import re
import sys
from typing import Any

import yaml

ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC = ROOT / 'prose' / 'edit' / 'src'
TESTCASES = ROOT / 'test' / 'validator' / 'data' / 'testcases.json'
RECORDS = ROOT / 'records'
TESTS = RECORDS / 'tests'
VIEWS = ROOT / 'views'

LEVELS = {'01': 'mandatory', '02': 'recommended', '03': 'informative'}
TEST_FILE = re.compile(r'tests-(0[123])-[a-z]+-(\d\d)(?:-(\d\d))?-(.+)\.md')
CAPTION = re.compile(r'\*Example (\d+) \(which (fails|passes) the test\):\*')
PATHS_LEAD = {1: 'The relevant path for this test is:', 2: 'The relevant paths for this test are:'}


# -- Markdown blocks ----------------------------------------------------------------------------------


def blocks_of(text: str) -> list[str]:
    """Split on blank lines outside code fences; joining with a blank line restores the text when it is regular."""
    out: list[str] = []
    cur: list[str] = []
    fenced = False
    for line in text.split('\n'):
        if line.lstrip().startswith('```'):
            fenced = not fenced
        if line == '' and not fenced:
            if cur:
                out.append('\n'.join(cur))
            cur = []
            continue
        cur.append(line)
    if cur:
        out.append('\n'.join(cur))
    return out


def fence_body(block: str) -> tuple[str, str]:
    """`(info string, body)` of a fenced block."""
    lines = block.split('\n')
    return lines[0].strip()[3:], '\n'.join(lines[1:-1])


# -- Records from today's prose (migrate) -------------------------------------------------------------


def parse_test(text: str) -> dict[str, Any]:
    """Structured fields of one test section; `blocks` (verbatim) when the section does not follow the common shape."""
    blocks = blocks_of(text)
    head = re.fullmatch(r'(#+) (.+)', blocks[0])
    assert head, blocks[0]
    rec: dict[str, Any] = {'heading': len(head[1]), 'title': head[2]}
    rest = blocks[1:]
    lead = next((i for i, b in enumerate(rest) if b in PATHS_LEAD.values()), None)
    if lead is None or not rest[lead + 1].startswith('```list-of-jsonpaths'):
        rec['blocks'] = rest
        return rec
    rec['statement'] = '\n\n'.join(rest[:lead])
    rec['paths'] = [p.strip() for p in fence_body(rest[lead + 1])[1].split('\n')]
    tail = rest[lead + 2 :]
    examples: list[dict[str, Any]] = []
    while len(tail) >= 2 and (cap := CAPTION.fullmatch(tail[0])) and int(cap[1]) == len(examples) + 1 and tail[1].startswith('```'):
        info, body = fence_body(tail[1])
        example: dict[str, Any] = {'verdict': cap[2], 'json': body}
        if info:
            example['fence'] = info
        tail = tail[2:]
        explain: list[str] = []
        while tail and tail[0].startswith('> ') and not tail[0].startswith('> A tool MAY'):
            explain.append(tail.pop(0))
        if explain:
            example['explanation'] = [unquote(b) for b in explain]
        examples.append(example)
    if examples:
        rec['examples'] = examples
    if tail:
        rec['notes'] = tail
    return rec


def unquote(block: str) -> str:
    return '\n'.join(line[2:] if line.startswith('> ') else line[1:] for line in block.split('\n'))


def quote(text: str) -> str:
    return '\n'.join('> ' + line if line else '>' for line in text.split('\n'))


def slug(stem: str) -> str:
    return re.sub(r'^\d\d-', '', stem)


def legacy_number(tier: str, num: str, sub: str | None) -> str:
    base = f'6.{int(tier)}.{int(num)}'
    return base if sub is None or sub == '00' else f'{base}.{int(sub)}'


def migrate() -> int:
    if TESTS.exists() and any(TESTS.iterdir()):
        sys.exit('records/tests/ is not empty; migrate runs once')
    TESTS.mkdir(parents=True, exist_ok=True)
    suite = json.loads(TESTCASES.read_text(encoding='utf-8'))
    by_id = {t['id']: t for t in suite['tests']}
    paths = sorted(SRC.glob('tests-0[123]-*-*.md'))
    stems = [slug(TEST_FILE.fullmatch(p.name)[4]) for p in paths]  # type: ignore[index]
    for path in paths:
        m = TEST_FILE.fullmatch(path.name)
        assert m, path.name
        tier, num, sub, stem = m.groups()
        text = path.read_text(encoding='utf-8')
        number = legacy_number(tier, num, sub)
        unique = slug(stem) if stems.count(slug(stem)) == 1 else f'{slug(stem)}-{LEVELS[tier]}'
        rec: dict[str, Any] = {'id': unique, 'kind': 'group' if sub == '00' else 'test', 'level': LEVELS[tier]}
        rec['legacy'] = {'number': number, 'file': path.name}
        rec |= parse_test(text)
        if rec['kind'] == 'test' and number in by_id:
            entry = by_id.pop(number)
            rec['fixtures'] = {k: v for k, v in entry.items() if k not in ('id', 'group')}
        # Sub-tests without a section of their own (6.1.60.1, ...) are defined inside their parent's section
        subs = sorted((k for k in by_id if k.startswith(number + '.')), key=lambda k: int(k.rsplit('.', 1)[1]))
        if subs:
            rec['subtests'] = [{'number': k} | {f: v for f, v in by_id.pop(k).items() if f not in ('id', 'group')} for k in subs]
        if render_test(rec) != text:
            rec = {k: v for k, v in rec.items() if k not in ('statement', 'paths', 'examples', 'notes')}
            rec['blocks'] = blocks_of(text)[1:]
        dump(TESTS / f'{rec["id"]}.yaml', rec)
    for orphan in by_id:
        print(f'testcases.json entry without a prose section: {orphan}', file=sys.stderr)
    return 0


# -- Views from records (derive / check) --------------------------------------------------------------


def render_test(rec: dict[str, Any]) -> str:
    out = ['#' * rec['heading'] + ' ' + rec['title'] + (f'{{#{rec["anchor"]}}}' if 'anchor' in rec else '')]
    if 'blocks' in rec:  # migration fallback only; no record uses it any more
        out += rec['blocks']
    elif rec.get('status') == 'obsolete':
        out.append(quote(rec['reason']))
    else:
        if rec.get('statement'):
            out.append(rec['statement'])
        if 'applies-to' in rec:
            out += render_applies_to(rec['applies-to'])
        if 'paths' in rec:  # groups have none
            out.append(PATHS_LEAD[min(len(rec['paths']), 2)])
            out.append('```list-of-jsonpaths\n' + '\n'.join('  ' + p for p in rec['paths']) + '\n```')
        for n, ex in enumerate(rec.get('examples', []), 1):
            out.append(f'*Example {n} (which {ex["verdict"]} the test):*')
            out.append('```' + ex.get('fence', '') + '\n' + ex['json'] + '\n```')
            out += [quote(e) for e in ex.get('explanation', [])]
        out += rec.get('notes', [])
    return '\n\n'.join(out) + '\n'


@functools.cache
def profiles() -> dict[str, dict[str, Any]]:
    data = yaml.safe_load((RECORDS / 'profiles.yaml').read_text(encoding='utf-8'))
    return {p['id']: p for p in data['profiles']}


def render_applies_to(applies: dict[str, list[str]]) -> list[str]:
    """The prose for a test's document categories: `only` (a list, or the open CSAF Base profile) or `except`."""
    known = profiles()
    unknown = [c for c in applies.get('only', []) + applies.get('except', []) if c not in known]
    if unknown or len(applies) != 1:
        sys.exit(f'applies-to: unknown categories {unknown} or not exactly one of only / except: {applies}')
    if 'except' in applies:
        names = ' or '.join(f'"{known[c]["title"]}"' for c in applies['except'])
        return [f'This test SHALL be skipped for CSAF documents conforming the profile {names}.']
    only = applies['only']
    if [known[c].get('open') for c in only] == [True]:
        title = known[only[0]]['title']
        values = '\n'.join(f'>  {c}' for c in sorted(known))
        return [
            f'This test does only apply for CSAF documents with the profile "{title}".\n'
            f'Therefore, it SHALL be skipped if the document category matches one of the values defined for the profile other than "{title}".',
            f'> For CSAF 2.1, the test must be skipped for the following values in `$.document.category`:\n>\n> ```\n{values}\n> ```',
        ]
    lead = 'The relevant value for `$.document.category` is:' if len(only) == 1 else 'The relevant values for `$.document.category` are:'
    return [lead, '```\n' + '\n'.join('  ' + c for c in only) + '\n```']


def render_applicability(tests: list[dict[str, Any]]) -> str:
    """Test x document category for every test with `applies-to`; all other tests apply to every category."""
    known = profiles()
    lines = [
        '# Applicability by document category',
        '',
        'Tests not listed apply to every document category. `x`: the test applies to documents of that category.',
        'CSAF Base also covers every category value that belongs to no other profile.',
        '',
        '| test | ' + ' | '.join(p['title'] for p in known.values()) + ' |',
        '|:-----|' + '|'.join(':---:' for _ in known) + '|',
    ]
    for r in sorted((r for r in tests if 'applies-to' in r), key=number_key):
        a = r['applies-to']
        marks = ['x' if (c in a['only'] if 'only' in a else c not in a['except']) else '' for c in known]
        lines.append(f'| `{r["legacy"]["number"]}` {r["title"]} | ' + ' | '.join(marks) + ' |')
    return '\n'.join(lines) + '\n'


def load_tests() -> list[dict[str, Any]]:
    return [yaml.safe_load(p.read_text(encoding='utf-8')) for p in sorted(TESTS.glob('*.yaml'))]


def number_key(rec: dict[str, Any]) -> tuple[int, ...]:
    return tuple(int(part) for part in rec['legacy']['number'].split('.'))


def render_testcases(tests: list[dict[str, Any]], tables: dict[str, dict[str, Any]]) -> str:
    head = json.loads(TESTCASES.read_text(encoding='utf-8'))
    entries = []
    for r in sorted(tests, key=number_key):
        if 'fixtures' in r:
            fixtures = {k: list(v) for k, v in r['fixtures'].items()}
            if 'derive' in r:
                table = tables[r['derive']['table']]
                for kind in ('failures', 'valid'):
                    fixtures[kind] += [{'name': name, 'valid': kind == 'valid'} for name in derived_names(table, r['derive'][kind])]
            entries.append({'id': r['legacy']['number'], 'group': r['level']} | fixtures)
        entries += [{'id': s['number'], 'group': r['level']} | {k: v for k, v in s.items() if k not in ('number', 'topics')} for s in r.get('subtests', [])]
    suite = {k: v for k, v in head.items() if k != 'tests'} | {'tests': entries}
    return json.dumps(suite, indent=2, ensure_ascii=False) + '\n'


def render_roles(tests: list[dict[str, Any]]) -> dict[str, str]:
    """One view per role: its conformance targets and every requirement binding it, with the duty its level gives that role."""
    clauses = load_clauses()
    views: dict[str, str] = {}
    for role in load_roles():
        targets = [f'{c["number"]}: {c["title"]}' for c in clauses if role['id'] in c['roles_']] + role.get('distribution-roles', [])
        lines = [f'# {role["title"]}', '', role['summary'].strip(), '', f'Conformance targets: {", ".join(targets)}.', '']
        for level in ('mandatory', 'recommended', 'informative'):
            duty = role.get('duties', {}).get(level)
            picked = [r for r in sorted(tests, key=number_key) if r['kind'] == 'test' and r['level'] == level]
            picked = [r for r in picked if role['id'] in r.get('roles', {role['id']: None} if duty else {})]
            if not picked:
                continue
            lines += [f'## {level.capitalize()} ({len(picked)})', '', duty.strip(), '']
            lines += [f'- `{r["legacy"]["number"]}` {r["title"]} (`{r["id"]}`)' for r in picked]
            lines.append('')
        views[f'{role["id"]}.md'] = '\n'.join(lines)
    return views


# -- Tables -------------------------------------------------------------------------------------------


def load_tables() -> dict[str, dict[str, Any]]:
    tables = {}
    for path in sorted((RECORDS / 'tables').glob('*.yaml')):
        table = yaml.safe_load(path.read_text(encoding='utf-8'))
        check_table(table)
        tables[table['id']] = table
    return tables


def table_cells(table: dict[str, Any]) -> list[tuple[str, str, str]]:
    """`(category, column id, verdict)` for every cell, row by row."""
    return [(cat, col['id'], v) for cat, row in table['cells'].items() for col, v in zip(table['columns'], row, strict=True)]


def check_table(table: dict[str, Any]) -> None:
    cells = table_cells(table)
    bad = [c for c in cells if c[2] not in table['verdicts']]
    verdict = {(cat, col): v for cat, col, v in cells}
    ranked = [verdict.get(tuple(pair), 'missing') for pair in table['ranking']]  # type: ignore[arg-type]
    expected = sorted((v for v in verdict.values() if v != 'prohibited'), key=table['verdicts'].index)
    if bad or ranked != expected or len({tuple(p) for p in table['ranking']}) != len(ranked):
        sys.exit(f'{table["id"]}: unknown verdicts {bad} or ranking is not allowed-then-discouraged, each cell once: {ranked}')


def _center(text: str, width: int) -> str:
    left = (width - len(text)) // 2
    return ' ' * left + text + ' ' * (width - len(text) - left)


def render_table_region(table: dict[str, Any]) -> str:
    """The prose between the region anchors: typesetting hints, the table, its caption, the ranked lists."""
    esc = {cat: cat.replace('_', '\\_') for cat in table['cells']}
    first = max(len('category value'), *map(len, esc.values())) + 2
    widths = [max(len(col['title']), *(len(row[i]) for row in table['cells'].values())) + 2 for i, col in enumerate(table['columns'])]
    rows = [
        '| ' + 'category value'.ljust(first - 1) + '|' + '|'.join(_center(c['title'], w) for c, w in zip(table['columns'], widths)) + '|',
        '|:' + '-' * (first - 1) + '|' + '|'.join(':' + '-' * (w - 2) + ':' for w in widths) + '|',
    ]
    rows += [
        '| ' + esc[cat].ljust(first - 1) + '|' + '|'.join(_center(v, w) for v, w in zip(row, widths)) + '|' for cat, row in table['cells'].items()
    ]
    title = {col['id']: col['title'] for col in table['columns']}
    verdict = {(cat, col): v for cat, col, v in table_cells(table)}
    out = ['\n'.join(table['legacy']['typesetting']), '\n'.join(rows), f'Table: {table["title"]}{{#{table["legacy"]["label"]}}}']
    for kind, lead in table['lead'].items():
        ranked = [(cat, col) for cat, col in table['ranking'] if verdict[(cat, col)] == kind]
        out += [lead, '\n'.join(f'{n}. `{cat}` and {title[col]}' for n, (cat, col) in enumerate(ranked, 1))]
    return '\n\n'.join(out)


def splice_region(text: str, region: dict[str, str], body: str) -> str:
    """Replace the lines strictly between the anchor lines `after` and `before` (`before: null`: to the end of the file)."""
    lines = text.split('\n')
    start = lines.index(region['after'])
    end = len(lines) - 1 if region['before'] is None else lines.index(region['before'])
    assert lines.count(region['after']) == 1 and (region['before'] is None or lines.count(region['before']) == 1) and start < end, region
    gap = [] if region['before'] is None else ['']
    return '\n'.join(lines[: start + 1] + [''] + body.split('\n') + gap + lines[end:])


def derived_name(table: dict[str, Any], cat: str, col: str) -> str:
    return 'derived/oasis_csaf_tc-csaf_2_1-2024-' + f'tab-{table["id"]}-{cat}-{col}'.replace('_', '-') + '.json'


def derived_names(table: dict[str, Any], verdicts: list[str]) -> list[str]:
    return [derived_name(table, cat, col) for cat, col, v in table_cells(table) if v in verdicts]


def derived_fixtures(table: dict[str, Any]) -> dict[pathlib.Path, str]:
    """One document per cell: the base fixture with one product in that status group and one remediation of that category."""
    data = TESTCASES.parent
    base = json.loads((data / table['fixture-base']).read_text(encoding='utf-8'))
    member = {col['id']: col for col in table['columns']}
    out = {}
    for cat, col, verdict in table_cells(table):
        doc = json.loads(json.dumps(base))
        name = derived_name(table, cat, col)
        stem = pathlib.Path(name).stem.removeprefix('oasis_csaf_tc-csaf_2_1-2024-')
        doc['document']['title'] = f'Derived Test: {table["title"]} ({cat} and {member[col]["title"]}: {verdict})'
        doc['document']['tracking']['id'] = f'OASIS_CSAF_TC-CSAF_2.1-2024-{stem.upper()}'
        vuln = doc['vulnerabilities'][0]
        pid = base['product_tree']['full_product_names'][0]['product_id']
        vuln['product_status'] = {member[col]['fixture']: [pid]}
        vuln['remediations'] = [{'category': cat, 'details': f'Derived from table {table["id"]}, cell ({cat}, {col}).', 'product_ids': [pid]}]
        out[data / name] = json.dumps(doc, indent=2, ensure_ascii=False) + '\n'
    return out


# -- Presets ------------------------------------------------------------------------------------------

LEVEL_SECTION = {'mandatory': '6.1', 'recommended': '6.2', 'informative': '6.3'}


def _labels() -> dict[str, str]:
    """Section number -> anchor, as nide assigns them (prose/edit/etc)."""
    return json.loads((ROOT / 'prose' / 'edit' / 'etc' / 'section-display-to-label.json').read_text(encoding='utf-8'))


def testables(tests: list[dict[str, Any]]) -> list[tuple[str, str, list[str]]]:
    """`(number, level, topics)` of every test; a section with sub-tests contributes its sub-tests, not itself."""
    out = []
    for r in tests:
        if r['kind'] == 'test' and not r.get('subtests'):
            out.append((r['legacy']['number'], r['level'], r.get('topics', [])))
        out += [(s['number'], r['level'], s.get('topics', [])) for s in r.get('subtests', [])]
    return out


def resolve_presets(presets: list[dict[str, Any]], tests: list[dict[str, Any]]) -> dict[str, list[str] | None]:
    """Preset id -> sorted test numbers (`schema` for the schema check); None when implementation-defined."""
    by_id = {p['id']: p for p in presets}
    pool = testables(tests)

    def resolve(pid: str) -> set[str] | None:
        p = by_id[pid]
        if p.get('implementation-defined'):
            return None
        if p.get('schema'):
            return {'schema'}
        if 'union' in p:
            return set().union(*(resolve(u) or set() for u in p['union']))
        if 'minus' in p:
            return (resolve(p['minus']['from']) or set()) - (resolve(p['minus']['without']) or set())
        sel = p['select']
        return {n for n, level, topics in pool if level == sel.get('level') or set(topics) & set(sel.get('topics', []))}

    def order(n: str) -> tuple[int, ...]:
        return (0,) if n == 'schema' else tuple(int(x) for x in n.split('.'))

    out: dict[str, list[str] | None] = {}
    for pid in by_id:
        got = resolve(pid)
        if got is not None and not got:
            sys.exit(f'preset {pid} selects no test')
        out[pid] = None if got is None else sorted(got, key=order)
    return out


def render_preset_item(p: dict[str, Any], numbers: list[str] | None, labels: dict[str, str]) -> str:
    def note(text: str, indent: str) -> str:
        return '\n\n' + '\n'.join(indent + '> ' + line for line in text.split('\n')) + '\n'

    if p['group'] == 'subsections':
        return f'- `{p["id"]}`: all tests given in section [sec](#{labels[LEVEL_SECTION[p["select"]["level"]]]})'
    if p['group'] == 'conformance':
        body = p['text'] if 'text' in p else ' + '.join(f'`{u}`' for u in p['union']) + f' (see section [sec](#{p["see"]}))'
        return f'- `{p["id"]}`: {body}' + (note(p['note'], '  ') if 'note' in p else '')
    item = f'- `{p["id"]}`:\n  - Description: {p["description"]}' + (note(p['note'], '    ') if 'note' in p else '')
    if 'minus' in p:
        return item + f'\n  - Set: `{p["minus"]["from"]}` excluding tests from preset `{p["minus"]["without"]}`'
    return item + '\n  - Set:\n' + '\n'.join(f'    - [sec](#{labels[n]})' for n in numbers or [])


def presets_views(tests: list[dict[str, Any]], text: str) -> tuple[str, str]:
    """(tests-04-presets.md with its three lists derived, views/presets.json)."""
    spec = yaml.safe_load((RECORDS / 'presets.yaml').read_text(encoding='utf-8'))
    resolved, labels = resolve_presets(spec['presets'], tests), _labels()
    for group, region in spec['regions'].items():
        items = [render_preset_item(p, resolved[p['id']], labels) for p in spec['presets'] if p['group'] == group]
        text = splice_region(text, region, '\n'.join(items).replace('\n\n\n', '\n\n').rstrip('\n'))
    return text, json.dumps(resolved, indent=2) + '\n'


# -- Conformance: clauses, roles by inheritance, section 9.2 ------------------------------------------

ROLE_LINE = 'This conformance target takes the role'


def load_roles() -> list[dict[str, Any]]:
    roles: list[dict[str, Any]] = yaml.safe_load((RECORDS / 'roles.yaml').read_text(encoding='utf-8'))['roles']
    return roles


def load_clauses() -> list[dict[str, Any]]:
    """The clauses with `roles_` and `presets_` resolved through `builds-on`; refuses unknown references."""
    clauses: list[dict[str, Any]] = yaml.safe_load((RECORDS / 'conformance.yaml').read_text(encoding='utf-8'))['clauses']
    by_id, role_ids = {c['id']: c for c in clauses}, [r['id'] for r in load_roles()]
    bad = [(c['id'], b) for c in clauses for b in c.get('builds-on', []) if b not in by_id]
    bad += [(c['id'], r) for c in clauses for r in c.get('roles', []) if r not in role_ids]
    if bad or len(by_id) != len(clauses):
        sys.exit(f'conformance.yaml: unknown references {bad} or duplicate ids')

    def roles(c: dict[str, Any]) -> set[str]:
        return set(c.get('roles', [])).union(*(roles(by_id[b]) for b in c.get('builds-on', [])))

    def presets(c: dict[str, Any]) -> tuple[list[str], set[str]]:
        """(presets, roles of the clause adding them): a capability belongs to the role of the clause that adds it."""
        if c.get('presets'):
            return c['presets'], roles(c)
        inherited = [presets(by_id[b]) for b in c.get('builds-on', [])]
        return sorted({p for ps, _ in inherited for p in ps}), set().union(*(rs for ps, rs in inherited if ps))

    for c in clauses:
        c['roles_'] = [r for r in role_ids if r in roles(c)]
        c['presets_'], c['capability_roles_'] = presets(c)
        if (c['kind'] == 'actor') != bool(c['roles_']):
            sys.exit(f'conformance.yaml: {c["id"]} is {c["kind"]} but has roles {c["roles_"]}')
    return clauses


def clause_file(c: dict[str, Any]) -> pathlib.Path:
    (path,) = SRC.glob(f'conformance-01-cls-{c["number"]:02d}-*.md')
    return path


def clause_label(c: dict[str, Any], labels: dict[str, str]) -> str:
    (label,) = [v for v in labels.values() if v.startswith(f'conformance-clause-{c["number"]}-')]
    return label


def _names(items: list[str]) -> str:
    return items[0] if len(items) == 1 else ', '.join(items[:-1]) + ' and ' + items[-1]


def render_clause(c: dict[str, Any], text: str, title: dict[str, str], findings: list[str]) -> str:
    """The clause with its role line under the heading; checks `builds-on` against the clause text."""
    lines = text.split('\n')
    assert lines[0].startswith('### Conformance Clause ') and lines[1] == '', c['id']
    if lines[2].startswith(ROLE_LINE):
        del lines[2:4]
    body = '\n'.join(lines[3:])
    missing = [b for b in c.get('builds-on', []) if f'"{title[b]}" conformance profile' not in body]
    if missing:
        sys.exit(f'clause {c["number"]} builds on {missing} in conformance.yaml, but its text does not say so')
    if f'"{c["title"]}" conformance profile' not in lines[2]:
        findings.append(f'Clause {c["number"]} ({c["title"]}): the lead sentence names another profile: {lines[2]}')
    if c['kind'] == 'actor':
        role_title = {r['id']: r['title'] for r in load_roles()}
        names = [role_title[r] for r in c['roles_']]
        plural = 's' if len(names) > 1 else ''
        lines[2:2] = [f'{ROLE_LINE}{plural} {_names(names)} (see section [sec](#conformance-roles)).', '']
    return '\n'.join(lines)


def render_conformance_roles(clauses: list[dict[str, Any]], labels: dict[str, str]) -> str:
    spec = yaml.safe_load((RECORDS / 'roles.yaml').read_text(encoding='utf-8'))
    out = ['## Conformance Roles{#conformance-roles}', spec['intro'].strip()]
    for role in spec['roles']:
        out += [f'### Conformance Role: {role["title"]}{{#conformance-role-{role["id"]}}}', role['summary'].strip()]
        out += [
            'The tests mean for a target in this role:',
            '\n'.join(f'- {level} tests: {duty.strip()}' for level, duty in role['duties'].items()),
        ]
        targets = [c for c in clauses if role['id'] in c['roles_']]
        out += ['Conformance targets taking this role:', '\n'.join(f'- [sec](#{clause_label(c, labels)})' for c in targets)]
        if role.get('distribution-roles'):
            dist = [f'- [sec](#{labels_by_value(labels, "role-" + name.lower().replace(" ", "-"))})' for name in role['distribution-roles']]
            out += ['Roles in the distribution of CSAF Documents covered by this role:', '\n'.join(dist)]
        capable = [c for c in targets if role['id'] in c['capability_roles_']]
        if capable:
            out += [
                'Capabilities, as the presets of tests the target runs:',
                '\n'.join(f'- [sec](#{clause_label(c, labels)}): ' + ', '.join(f'`{p}`' for p in c['presets_']) for c in capable),
            ]
    return '\n\n'.join(out) + '\n'


def labels_by_value(labels: dict[str, str], label: str) -> str:
    if label not in labels.values():
        sys.exit(f'no section with the anchor {label}')
    return label


def conformance_views() -> tuple[dict[pathlib.Path, str], list[str]]:
    clauses, labels, findings = load_clauses(), _labels(), []
    title = {c['id']: c['title'] for c in clauses}
    out = {clause_file(c): render_clause(c, clause_file(c).read_text(encoding='utf-8'), title, findings) for c in clauses}
    out[SRC / 'conformance-02-roles.md'] = render_conformance_roles(clauses, labels)
    return out, findings


def render_findings(findings: list[str]) -> str:
    lines = ['# Findings', '', 'What derive noticed in the records and the prose without refusing to derive (to report or correct).', '']
    return '\n'.join(lines + [f'- {f}' for f in findings] + ([] if findings else ['- none'])) + '\n'


def lint_records(tests: list[dict[str, Any]]) -> list[str]:
    """Findings in the records: explanations naming IDs their example lacks; normative sentences restated from hand-written prose."""
    ident = re.compile(r'\b(?:CSAFPID|CSAFGID|EID|ACN|VULN|CVE)-[0-9A-Za-z]+(?:-[0-9A-Za-z]+)*')
    findings = []
    for r in sorted(tests, key=number_key):
        for n, ex in enumerate(r.get('examples', []), 1):
            used = set(ident.findall(ex['json']))
            missing = sorted({tok for e in ex.get('explanation', []) for tok in ident.findall(e)} - used)
            if missing:
                findings.append(f'`{r["legacy"]["number"]}` example {n}: the explanation names {missing}, the example has {sorted(used)}')

    def norm(text: str) -> str:
        return ' '.join(text.split()).lower()

    from_records = {SRC / r['legacy']['file'] for r in tests}  # other files are hand-written, at least in part
    prose = norm(' '.join(p.read_text(encoding='utf-8') for p in sorted(SRC.glob('*.md')) if p not in from_records))
    for r in sorted(tests, key=number_key):
        for sentence in re.split(r'(?<=\.)\s+', ' '.join((r.get('statement') or '').split())):
            if re.search(r'\b(?:SHALL|MUST|SHOULD)\b', sentence) and len(sentence) > 40 and norm(sentence) in prose:
                findings.append(f'`{r["legacy"]["number"]}` restates hand-written prose: "{sentence}"')
    return findings


def views() -> dict[pathlib.Path, str]:
    tests, tables = load_tests(), load_tables()
    out = {SRC / r['legacy']['file']: render_test(r) for r in tests}
    for table in tables.values():
        path = SRC / table['legacy']['file']
        out[path] = splice_region(out.get(path, path.read_text(encoding='utf-8')), table['legacy']['region'], render_table_region(table))
        if any(r.get('derive', {}).get('table') == table['id'] for r in tests):
            out |= derived_fixtures(table)
    out[TESTCASES] = render_testcases(tests, tables)
    presets_md = SRC / 'tests-04-presets.md'
    out[presets_md], out[VIEWS / 'presets.json'] = presets_views(tests, presets_md.read_text(encoding='utf-8'))
    out |= {VIEWS / 'roles' / name: text for name, text in render_roles(tests).items()}
    out[VIEWS / 'applicability.md'] = render_applicability(tests)
    conformance, findings = conformance_views()
    out |= conformance
    out[VIEWS / 'findings.md'] = render_findings(findings + lint_records(tests))
    return out


def derive() -> int:
    for path, text in views().items():
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists() or path.read_text(encoding='utf-8') != text:
            path.write_text(text, encoding='utf-8')
            print(f'wrote {path.relative_to(ROOT)}')
    return 0


def check() -> int:
    stale = [p for p, text in views().items() if not p.exists() or p.read_text(encoding='utf-8') != text]
    for path in stale:
        print(f'stale view: {path.relative_to(ROOT)} (run: bin/vision.py derive)')
    return 1 if stale else 0


# -- YAML with literal blocks -------------------------------------------------------------------------


class _Dumper(yaml.SafeDumper):
    pass


def _str(dumper: yaml.SafeDumper, value: str) -> yaml.ScalarNode:
    style = '|' if '\n' in value else None
    return dumper.represent_scalar('tag:yaml.org,2002:str', value, style=style)


_Dumper.add_representer(str, _str)


def dump(path: pathlib.Path, rec: dict[str, Any]) -> None:
    text = yaml.dump(rec, Dumper=_Dumper, sort_keys=False, allow_unicode=True, width=1000)
    assert yaml.safe_load(text) == rec, path
    path.write_text(text, encoding='utf-8')


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('command', choices=['migrate', 'derive', 'check'])
    return {'migrate': migrate, 'derive': derive, 'check': check}[parser.parse_args().command]()


if __name__ == '__main__':
    sys.exit(main())
