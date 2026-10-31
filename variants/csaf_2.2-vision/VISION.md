# CSAF 2.2 vision: author records, derive the views

This tree is a copy of `csaf_2.1` (CSD04) in which part of the specification is no longer written as prose
but as records, and the prose is derived from them. The copy starts lossless: `make check` proves that the
records reproduce today's files, so every later change shows up as a reviewable change of a record.

## What an editor authors

| You edit                         | Instead of                                       | Derived from it (never edit)                  |
|----------------------------------|--------------------------------------------------|-----------------------------------------------|
| `records/tests/<id>.yaml`        | `prose/edit/src/tests-0[123]-*-*.md`              | the same prose files, byte for byte           |
| the `fixtures:` of that record   | `test/validator/data/testcases.json`              | `testcases.json`                              |
| `records/roles.yaml`             | (nothing: today roles are 36 clauses + 5 roles)   | section 9.2 "Conformance Roles"; role views   |
| `records/conformance.yaml`       | (implicit in "satisfies the ... profile" bullets) | the role line under each actor clause         |
| `records/tables/<id>.yaml`       | a table and its lists inside a prose file         | that region of the prose file; one fixture    |
|                                  |                                                  | per cell (`test/validator/data/derived/`)     |
| `records/presets.yaml`, and the  | the three preset lists in `tests-04-presets.md`   | those lists; `views/presets.json` (each       |
| `topics:` of the test records    | (hand-kept lists of section links)               | preset resolved to test numbers)              |
| `applies-to:` of a test record,  | "The relevant value(s) for `$.document.category`" | those sentences and blocks;                   |
| `records/profiles.yaml`          | blocks and "SHALL be skipped for ..." sentences   | `views/applicability.md` (test x category)    |
| all other prose                  | (unchanged, still hand-written Markdown)          |                                               |

One record per test. Its file name is the stable `id` (a slug, not a number); the section number is kept
under `legacy:` only to map to today. A record holds what today is spread over several places:

- `title` (and `anchor` where the heading carries an explicit one), `statement` (the SHALL sentence),
  `paths` (the relevant JSON paths; "path ... is" / "paths ... are" follows their number)
- `applies-to`: the document categories, `only: [...]` or `except: [...]` (values from `records/profiles.yaml`);
  absent means every category. `only: [csaf_base]` is the open CSAF Base profile (6.1.26).
- `topics`: what the test is about; presets select by them
- `examples` (`verdict`, `json`, `explanation`): the caption "Example N (which fails the test)" is generated
- `notes` (e.g. quick fixes), `fixtures` (the official test files), `subtests` (only for sections made of
  sub-tests without sections of their own: 6.1.60, 6.2.50, 6.2.54, 6.3.19, 6.3.21)
- `kind: group` for the sections that only structure tests (6.1.27, 6.1.64, ...): `statement`, no paths
- `status: obsolete` with `reason` for withdrawn tests (6.2.7, 6.2.10): kept so numbers stay stable

A table record (today: `status-remediation`) holds the cells, the status groups with their member
properties, and one `ranking` of all non-prohibited combinations; the prose's two preference lists are that
ranking split by verdict. Derive refuses a table whose ranking does not list every allowed cell, then every
discouraged cell, each once. A test record links to a table with `uses:` and asks for fixtures with
`derive: {table, failures: [verdicts], valid: [verdicts]}`: 6.1.36 fails on the 11 prohibited cells and
passes the other 31, 6.2.27 fails on the 11 discouraged cells and passes the 20 allowed ones. Changing one
cell therefore changes the prose table, the preference lists (via the check), both tests' expectations and
the fixture in one edit.

A preset is a selection, not a list: by `level` (mandatory, ...), by `topics` (a test record says
`topics: [revision-history]`, and `consistent-revision-history` selects that topic), as a union (`basic` =
`schema` + `mandatory`) or as a difference (`external-request-free` = `full` without
`non-external-request-free`). A new test joins its presets by its own record; `presets.yaml` changes only
for a new preset. A section that consists of sub-tests (6.1.60, 6.3.21, ...) contributes its sub-tests.

Workflow: edit a record, run `make derive`, review the diff of the record and of the views, run `make check`
before committing. Editing a derived file directly makes `make check` fail.

## How the roles fit in

Today a requirement says "designated as applying to CSAF Consumers" at best, and the conformance clauses
bundle actors with capabilities (Basic / Extended / Full Validator, Library with ... Validation). The vision
separates the two:

- **Four roles** bind requirements: producer, intermediary, consumer, validator (`records/roles.yaml`),
  each also naming the distribution roles of section 7.2 it covers (Publisher; Provider, Lister, ...).
- **Which clause takes which role is derived, not listed.** `records/conformance.yaml` gives each of the 36
  clauses its `kind` (actor or artifact) and `builds-on`, exactly as the clause text says it ("satisfies the
  "CSAF Producer" conformance profile"); derive refuses when record and text disagree. Only 5 clauses
  state roles themselves (Producer, Consumer, Basic Validator, Library, Downloader); the other 20 actor
  clauses inherit theirs. Hence a Post-Processor (Consumer + Producer) and everything built on it
  (Modifier, Translator, Withdrawer, Superseder, RVISC ID Updater) is both producer and consumer.
- **Capabilities are presets.** Basic / Extended / Full Validator add `basic` / `extended` / `full`; the
  Libraries with Validation inherit them. A capability belongs to the role of the clause adding it.
- **The spec shows it**: a new section 9.2 "Conformance Roles" (`conformance-02-roles.md`, derived) gives
  per role its summary, what each test level means for it, its targets, distribution roles and capabilities;
  every actor clause gets one derived line under its heading, e.g. "This conformance target takes the
  roles Producer and Consumer (see section 9.2)". The 11 artifact clauses (Document, Additional Test,
  Extension*) take no role.
- **Each role has a duty per level**: a mandatory test is a MUST NOT for a producer, a MUST run for a
  validator, and a guarantee a consumer may rely on before automating. That is the gap the consumer side
  has today: nothing tells a consumer what it may conclude from a passed or failed test.
- A record may state `roles:` itself when its duties differ from the level default (none do yet).
- `views/roles/<role>.md` is what an implementer of that role reads: every requirement that binds it.

## State and next steps

Done (phase 1, mechanical, no normative change):

- the tree copy; 208 test records migrated by `bin/vision.py migrate` (one-off) and rendered back by
  `bin/vision.py derive`
- `testcases.json` generated from the records, including sub-tests
- the four roles with their duties and today's clauses, and the role views
- two normalisations against CSD04, both upstream formatting defects (to report):
  `tests-02-rcmmndd-39-07-...md` ends with an extra blank line; `testcases.json` has one mis-indented `{`
  before the entry `6.1.64.13`

Done (phase 2, step 1): every record is structured, none holds verbatim Markdown.

- 7 group sections and 2 obsolete tests got their own shapes (`kind: group`, `status: obsolete`)
- 13 tests failed the common shape only because the lead sentence's number disagrees with the paths
  (8x "paths ... are" before one path, 4x "path ... is" before several, 6.1.37 before 14); the derived
  sentence now follows the count: 12 corrected sentences, the 13th record (6.2.39.7) was only the blank line
- a phase 1 migration defect fixed: the group records had taken the fixtures of their tests (59 entries,
  e.g. 6.1.27.x) as sub-tests; they now sit in the test records (`testcases.json` unchanged)
- explicit anchors split from titles (34 records) so the views show plain titles

Done (phase 2, step 2): which document categories a test applies to is data.

- `applies-to` on 37 tests: the 35 profile tests' category blocks, 6.2.1 (`except` Informational Advisory),
  6.1.26 (`only` the open CSAF Base profile); the prose is derived and unchanged except for 6.1.26, whose
  closing sentence now precedes the applicability paragraphs and whose skip list is now sorted
  (`csaf_vulnerability_report` had been appended at the end)
- `views/applicability.md`: test x category
- compared with prototyyppi, where this knowledge is spread over the rule code: for 36 tests (all but
  6.1.26) every official failing fixture was re-run with each of the nine categories (783 runs); the test
  fails exactly in the categories `applies-to` names
- left as prose on purpose: conditions on content rather than document type ("skipped if the document
  language is not set", "... for official CSAF Extensions", "... algorithms with variable length output")

Done (phase 2, step 3):

- `records/tables/status-remediation.yaml`; the table and both preference lists in
  `schema-elements-02-props-04-vulnerabilities.md` are derived from it (byte for byte as in CSD04)
- 42 derived fixtures, listed in `testcases.json` under 6.1.36 and 6.2.27 next to the official ones; checked
  with prototyyppi: each fails exactly the test its verdict names and passes all other mandatory tests
- not yet: the remediation x remediation table (6.1.35) uses the same mechanism and is the next candidate

Done (phase 2, step 4):

- `records/presets.yaml` (14 official presets as selections); the topics of 53 tests and sub-tests seeded
  once from the CSD04 lists; the three lists of `tests-04-presets.md` derived, the prose around them kept
- `views/presets.json`: every preset resolved; compared with prototyyppi's independent hand copy, all 14
  agree except that prototyyppi runs 6.1.60 and 6.3.19 as one rule each where `testcases.json` has sub-tests
- two normalisations against CSD04: the stray blank line that made the additional presets list "loose"
  after `consistent-revision-history`, and 6.2.56.1 now sorted before 6.2.56.5 in `consistent-date-times`

Done (phase 2, step 5): conformance clauses as role + capabilities.

- `records/conformance.yaml` (36 clauses), `records/roles.yaml` without hand-kept clause lists; derived:
  section 9.2 (new, bound after clause 36 in `etc/bind.txt`), the role line in 25 actor clauses, the role
  views; `views/findings.md` collects what derive notices without refusing
- hand edits: `conformance-00.md` (it said the section has "only" one subsection), `etc/bind.txt`
- corrected against my phase 1 mapping: Additional Test (27) is an artifact, not a validator; the
  post-processors and the CMS are consumers too (inherited, no longer hand-assigned)
- built with nide (`make gfm-plus`, environment `csaf-2.1-dev-py-3-14-5`): every new reference resolves,
  9.2 to 9.2.4 are new and no existing section number moved; `prose/share/csaf-v2.1-draft.md` and `.ir.json`
  are the vision render now, while `.html`, `.pdf` and `.typ` there are still the CSD04 renders
- new normative text, for discussion: the duties per role and level (e.g. "A consumer ... MUST NOT
  derive an automated action from a part of a document that fails one of them")
- findings in CSD04 (to report):
  - clause 22's lead sentence says "CSAF Library with Extended Validation" instead of "... Full Validation"
  - `conformance-00.md` counts "all other 33 targets" besides the Document; there are 35
  - its note says there are "no capabilities organized in increasing quality levels", but Basic /
    Extended / Full Validator (and the Libraries with Validation) are exactly that

Done (phase 2, step 6): findings applied, each as one small edit.

- derive now checks the records and writes what it finds to `views/findings.md` (non-blocking):
  explanations naming an ID their example does not contain (whole tokens: `CSAFPID-908070` is a
  substring of `CSAFPID-9080700`), and normative sentences of a test restating hand-written prose
- record edits: 6.1.35, 6.1.36, 6.2.27 (`CSAFPID-908070` -> `CSAFPID-9080700`), 6.3.9 (the explanation
  named `CSAFPID-9080700`, the example uses `CSAFPID-0002`), 6.1.6 (dropped the restated "pairwise
  disjoint" SHALL; the requirement stays in the product status section, the test keeps its test sentence)
- prose edits: clause 22's lead sentence, the target count in `conformance-00.md`
- `views/findings.md` is empty now; `prose/share/csaf-v2.1-draft.md` re-rendered

## Corrections against CSD04 (to report upstream)

Each is visible as a diff between `csaf_2.1/` and this tree.

| Where | Correction | How found |
|-------|------------|-----------|
| 6.1.35, 6.1.36, 6.2.27 | explanation: `CSAFPID-908070` -> `CSAFPID-9080700` | findings check |
| 6.3.9 | explanation names `CSAFPID-9080700`, the example uses `CSAFPID-0002` | findings check |
| 6.1.6 | "pairwise disjoint" SHALL stated twice (here and in the product status section) | findings check |
| 12 tests (6.1.27.9, 6.1.28, 6.1.31, 6.1.37, 6.2.17, 6.2.18, 6.2.19, 6.2.51, 6.3.9, 6.3.10, 6.3.11, 6.3.20) | "path ... is" / "paths ... are" disagrees with the number of paths | derived sentence |
| 6.1.26 | skip list not sorted (`csaf_vulnerability_report` appended); closing sentence moved before it | derived from profiles |
| presets (6.4.3) | stray blank line makes the list loose; 6.2.56.5 listed before 6.2.56.1 | derived lists |
| clause 22 | lead sentence names "CSAF Library with Extended Validation" | builds-on check |
| `conformance-00.md` | "all other 33 targets": there are 35 | role derivation |
| `tests-02-rcmmndd-39-07-...md` | extra blank line at the end | round trip |
| `testcases.json` | one mis-indented `{` before `6.1.64.13` | round trip |

Open for discussion, not changed: the note in `conformance-00.md` says there are "no capabilities organized
in increasing quality levels", while Basic / Extended / Full Validator (and the Libraries with Validation) are
such levels; section 9.2 now names them as capabilities. The duties per role and level in 9.2 are new
normative text.

Next (phase 2, each a separate reviewable step):

1. Done (see above).
2. Done for document categories (see above); content conditions could follow as `skip-when`.
3. Done (see above); the remediation combinations table (6.1.35) follows the same way.
4. Done (see above).
5. Done (see above); the clause bodies themselves stay prose.
6. Done (see above).

Candidates after phase 2: the remediation combinations table (6.1.35) as a table record; content conditions
(`skip-when`); the conformance targets list (9.1) derived from `records/conformance.yaml`; a full build
(`make` in `prose/edit`) so that HTML and PDF in `prose/share/` show the vision too.
