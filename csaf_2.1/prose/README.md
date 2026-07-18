# The CSAF 2.1 Prose Folder

This folder holds the editorial sources and versioned delivery items for the CSAF v2.1 specification.

| Subfolder | Purpose                                                                               |
|:----------|:--------------------------------------------------------------------------------------|
| `edit/`   | Authoring workspace — sources, configuration, and build tooling; see `edit/README.md` |
| `share/`  | Versioned delivery items built from `edit/`; see `share/README.md`                    |

## Delivery formats

We build four delivery channels from the same source:

- **GFM+** (`csaf-v2.1-draft.md`) — optimised for reading on version-control web interfaces
  (Codeberg, GitHub, GitLab, SourceHut, …)
- **HTML** (`csaf-v2.1-draft.html`) — standalone file for any browser
- **PDF** (`csaf-v2.1-draft.pdf`) — compiled via typst
- **IR** (`csaf-v2.1-draft.ir.json`) — nide's channel-neutral internal representation;
  useful for tooling and diffing

To build all channels and verify the manifest, run from `edit/`:

    make release

To build incrementally:

    make gfm-plus   # GFM+ and IR
    make html       # HTML (implies gfm-plus)
    make pdf        # PDF + typst source + checksums

To check document completeness against the editorial rules:

    make quality    # per-rule PASS/FAIL/NA report (reads etc/rules/spec.rules.yaml)

Execution of any target that uses non-standard tools will verify the tools are available.
If an essential tool is missing, make aborts with a message describing what is needed and how to install it.
