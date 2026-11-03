# The CSAF 2.1 Prose Folder

This folder holds the editorial sources and versioned delivery items for the CSAF v2.1 specification.

| Subfolder | Purpose                                                                               |
|:----------|:--------------------------------------------------------------------------------------|
| `edit/`   | Authoring workspace — sources, configuration, and build tooling; see `edit/README.md` |
| `share/`  | Versioned delivery items built from `edit/`; see `share/README.md`                    |

## How editing works in this tree

Part of the specification (tests, the status/remediation table, presets, applicability, conformance roles) is
kept as records in `../records/`, and the matching prose in `edit/src/` is derived from them; the rest of the
prose is hand-written as before. A fact is therefore entered once, in its record, and `make derive` writes it
into every place that shows it. `edit/README.md` walks through the workflow with two real examples and a FAQ;
`../VISION.md` lists what is a record and the corrections the records found in CSD04.

Quick answers:

- **Where do I change a test?** In its record, `../records/tests/<slug>.yaml` (its number is under `legacy:`),
  then `make derive` in `..`. Editing the derived `.md` makes `make check` fail.
- **How do I know nothing broke?** `make check` in `..` (records and prose agree), then `make release` in `edit/`
  (everything from scratch, with every gate).
- **Is this decided?** No: a proposal on the branch `csaf-2.2-refactor` for the editors and the TC to discuss.

## Delivery formats

We build four delivery channels from the same source:

- **GFM+** (`csaf-v2.1-draft.md`) — optimised for reading on version-control web interfaces
  (Codeberg, GitHub, GitLab, SourceHut, …)
- **HTML** (`csaf-v2.1-draft.html`) — standalone file for any browser
- **PDF** (`csaf-v2.1-draft.pdf`) — compiled via typst
- **IR** (`csaf-v2.1-draft.ir.json`) — nide's channel-neutral internal representation;
  useful for tooling and diffing

To build what you hand over (a PR or a release) from scratch, with every gate, run from `edit/`:

    make release

To build incrementally:

    make gfm-plus   # GFM+ and IR
    make html       # HTML (implies gfm-plus)
    make pdf        # PDF + typst source + checksums
    make render     # HTML and PDF together, no cleaning, no gates

To check document completeness against the editorial rules:

    make quality    # per-rule PASS/FAIL/NA report (reads etc/rules/spec.rules.yaml)

Execution of any target that uses non-standard tools will verify the tools are available.
If an essential tool is missing, make aborts with a message describing what is needed and how to install it.
