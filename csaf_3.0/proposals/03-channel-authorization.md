# Proposal 3 — Channel Authorization (TLP/Sharing-Group Gate)

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

## Minimum field set

Kept deliberately minimal, since we scope out *how* authentication happens (see "Deliberate scoping"
below) — only the decision inputs and their source are specified:

| Field | Source | Role in the decision |
| --- | --- | --- |
| `document.distribution.tlp.label` | already exists, `$.document.distribution.tlp.label` | minimum clearance tier required |
| `document.distribution.sharing_group.id` | already exists, `$.document.distribution.sharing_group.id` | required only if the tier is scoped to a closed group (typically AMBER and above) |
| `subscriber.clearance_tiers` | new, provider-side subscriber record — format not mandated | which TLP tiers this subscriber may receive at all |
| `subscriber.sharing_groups` | new, provider-side subscriber record — format not mandated | which `sharing_group.id` values this subscriber is a member of |

The authorization decision on `hub.mode=subscribe` (P2) is then a pure comparison: reject the
subscription unless `document.distribution.tlp.label` is in `subscriber.clearance_tiers` **and**, if
present, `document.distribution.sharing_group.id` is in `subscriber.sharing_groups`. How a provider
establishes `subscriber.clearance_tiers`/`subscriber.sharing_groups` for a given subscriber (contract,
manual vetting, an existing IAM system) is explicitly out of scope — the spec only mandates that the
comparison itself must happen before a subscription is confirmed.

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
