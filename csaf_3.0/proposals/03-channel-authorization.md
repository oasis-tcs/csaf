# Proposal 3 — Channel Authorization (TLP/Sharing-Group Gate)

*[Diese Seite auf Deutsch lesen](03-channel-authorization.de.md)* — the German version is a
faithful, complete translation of this document. In case of any discrepancy, this English version is
authoritative.

**Status:** Sketch, no spec text yet. See [../README.md](../README.md) for motivation and how this
fits alongside the other three proposals.

**Dependencies:** Requires P2 (or at least some push/access mechanism) to have anything to gate.
Uses only fields that already exist in the document schema.

## Goal

One channel per product instead of one channel per TLP tier. Delivery of an event/document only to
subscribers whose clearance matches the document's `distribution.tlp.label` or
`distribution.sharing_group.id`.

## Key points

- TLP:RED never leaves the distribution mechanism (internal preparatory work, not a channel concern).
- TLP:AMBER → bound to a sharing group, time-limited (the embargo grace period is a process/
  governance matter, not a new mandatory field — unless the TC wants to add a machine-readable
  "planned release date", see open questions).
- TLP:GREEN/CLEAR → open, no authorization needed.
- Staged release (RED → AMBER → GREEN) = a new revision of the same document at a higher TLP tier,
  not a separate document/channel-switch concept.

## Deliberate scoping

The spec mandates **that** an authorization decision must be based on `tlp`/`sharing_group` — **not
how** authentication is implemented (no requirement for a specific auth protocol/token format).
Analogous to Requirement 3 (TLS is mandated, the choice of certificate is left open).

## Open questions

- Machine-readable "planned release date" for AMBER documents — a genuinely new addition, not yet
  present. To be assessed separately from the pure channel question.
- Consistency requirement: the reconciliation source (P1/P2) for a given TLP tier must carry the same
  protection as the corresponding push channel.

## TODO

Write concrete spec text (likely an addition to section 7.1/7.2, plus possibly a clarification in
3.2.2.5).
