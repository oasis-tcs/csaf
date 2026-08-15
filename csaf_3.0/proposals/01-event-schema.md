# Proposal 1 — Event/Digest Schema

*[Diese Seite auf Deutsch lesen](01-event-schema.de.md)* — the German version is a faithful,
complete translation of this document. In case of any discrepancy, this English version is
authoritative.

**Status:** Sketch, no spec text yet. See [../README.md](../README.md) for motivation and how this
fits alongside the other three proposals.

**Dependencies:** None. Usable on its own, independent of whether push (P2) is ever adopted — could
also land as an additional field on ROLIE feed entries or in `changes.csv`.

## Goal

A compact, machine-readable object per document publication or change that enables a relevance check
without loading the actual CSAF document.

## Proposed fields

- Product / product version (reference to product-tree concepts, likely `product_id` or a comparably
  compact identifier)
- Vulnerability ID (CVE, GHSA, gCVE, vendor-specific ID — check alignment with RVISC)
- Document type (SA / SI / IA / VEX — relates to the existing profiles, section 4 of the spec)
- Status (e.g. `investigating`, `won't fix`, `fixed`, … — check reuse of existing
  flags/remediation vocabulary rather than inventing new enums)
- Document ID (to fetch details, `tracking.id`)
- Date
- Signature

## Open questions

- Precedence rule when event and document drift apart: the document is always authoritative — how is
  this phrased normatively?
- Reuse of existing vocabularies (status/flags) instead of new enums.
- Where does the schema structurally live — its own JSON schema, or an extension of the ROLIE
  entry/`changes.csv`?

## TODO

Write concrete spec text once P1 has been presented to the TC and received generally positive
feedback.
