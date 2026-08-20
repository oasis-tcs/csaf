# Proposal 1 — Event/Digest Schema

**Status:** Sketch, no spec text yet. See [../README.md](../README.md) for motivation and how this
fits alongside the other three proposals.

**Dependencies:** None. Usable on its own, independent of whether push (P2) is ever adopted — could
also land as an additional field on ROLIE feed entries or in `changes.csv`.

## Goal

A compact, machine-readable object per document publication or change that enables a relevance check
without loading the actual CSAF document.

## Proposed fields

Every field below is a **projection of an already-normative CSAF field** — nothing here introduces
new vocabulary. That is a deliberate design constraint: the event is a repackaging of facts the
document already states, not a second source of truth with its own semantics. It will automatically 
generated from the dcoument.

| Event field | Type | Source in the CSAF document | Notes |
| --- | --- | --- | --- |
| `document_id` | string | `$.document.tracking.id` | to fetch the full document |
| `document_version` | string | `$.document.tracking.version` | current revision at event time |
| `publisher_namespace` | uri | `$.document.publisher.namespace` | identity anchor, also used by P4 |
| `document_category` | enum | `$.document.category` | ties to the profile (Base/SI/IA/SA/VEX/…, section 4) |
| `product` | object: `{vendor, product_name, product_version, helpers?}` | `vendor`/`product_name`/`product_version` from the branch ancestry (3.1.2.2) of the matched `full_product_name`; `helpers` from `product_identification_helper` (cpe/purl/model_numbers) if present | see "Design note" below — **not** the raw `product_id` |
| `vulnerability_ids` | array of `{system_name, text}` | `$.vulnerabilities[*].cve` and/or `$.vulnerabilities[*].ids[*]` | reuses the existing ID Type structure verbatim, including RVISC-registered `system_name` values |
| `status` | enum: `affected` / `not_affected` / `fixed` / `under_investigation` / `unknown` | derived from which `product_status` bucket (3.2.4.12) the product appears in — see mapping below | the field the VEX use case hinges on |
| `justification` | enum, present only if `status = not_affected` | `$.vulnerabilities[*].flags[*].label` | the 5 VEX-Justification codes (3.2.4.7) — lets the consumer see *why*, not just *that* |
| `release_date` | date-time | `$.document.tracking.current_release_date` | |
| `signature` | string | new, event-level | signs the event payload itself; separate from the document's own signature (Requirement 19) |

**`status` mapping** (mirrors the product status groups already defined in 3.2.4.12, no new
vocabulary invented):

| Event `status` | Sourced from CSAF bucket(s) |
| --- | --- |
| `affected` | `product_status.first_affected`, `.known_affected`, `.last_affected` |
| `not_affected` | `product_status.known_not_affected` |
| `fixed` | `product_status.first_fixed`, `.fixed` |
| `under_investigation` | `product_status.under_investigation` |
| `unknown` | `product_status.unknown` |

### Why `status` + `justification` together solve the motivating example

Profile 5 (VEX, section 4.5) already *requires* that every product listed under
`known_not_affected` carries either a machine-readable flag (`flags[*].label`, one of the five
VEX-Justification codes) or an equivalent human-readable threat/impact statement. That means the
`not_affected` + `justification` pair is not something we have to invent — it is already mandatory
content in every conformant VEX document today, just not exposed outside the document. Once it rides
in the event, a consumer who receives `status: not_affected, justification:
vulnerable_code_not_present` for their product/CVE combination can close the item immediately, with
no further download — exactly the "I am not affected, full stop" message from the motivating example.

### Design note: product identification (important correction, revised)

`product_id` (e.g. `CSAFPID-0001`) is **scoped to a single document's `product_tree`** — it carries
no meaning to a consumer who has not already downloaded that document, which defeats the entire
purpose of the event. An earlier draft of this proposal suggested resolving to CPE/PURL instead. That
does not hold up for all product categories and needed correcting:

**CPE and PURL do not cover hardware well.** PURL is a package-manager-ecosystem identifier (npm,
Maven, deb, …) and has no meaningful notion of a set-top box or a TV. CPE dictionary coverage for
consumer electronics/embedded hardware is thin and inconsistent in practice. Neither is a safe primary
key to build matching on across product categories.

**The actual universal fallback already exists in the product tree: the vendor/product-name/
product-version triple.** The `branches` category enum (3.1.2.2) explicitly defines `vendor`,
`product_name`, and `product_version` as branch categories — every `full_product_name` is reached by
walking an ancestry of such categorized branches, and their `name` values are plain, human-meaningful
strings ("Siemens" / "SIMATIC PCS 7" / "10"), not document-scoped IDs. Crucially, the spec itself
already acknowledges this is the real matching mechanism where identification helpers are absent:
section 3.1.2.2 notes that without a helper, "product identification and also therefore matching...
solely relies on the categorized strings." We are not inventing a new fallback, just exposing the one
the spec already leans on.

Revised design: the `product` field carries the **vendor/product-name/product-version triple**
(derived by walking the branch ancestry of the matched `full_product_name`) as the mandatory baseline
— present for every product in every product tree, hardware included. Any available
`product_identification_helper` values (`cpe`, `purl`, and — worth calling out specifically for the
hardware case — `model_numbers`, which section 3.1.4.3.3 explicitly states "can also be used to
identify hardware") ride along as optional, higher-precision fields *in addition to* the triple, used
when present for tighter automated matching, but never as the only carrier of identity.

## Example (illustrative, non-normative)

These examples show the shape the fields above would produce — not proposed spec wording, no
normative language, just here to make the table concrete.

**Example 1 — the motivating case: a VEX "not affected" for a set-top box.** A consumer holding
CVE-2026-12345 open for "Acme Streamline Set-Top Box" can close it on receipt of this event alone,
no document download:

```json
{
  "document_id": "acme-vex-2026-0512",
  "document_version": "1.0.0",
  "publisher_namespace": "https://psirt.acme.example",
  "document_category": "csaf_vex",
  "product": {
    "vendor": "Acme Corp",
    "product_name": "Acme Streamline Set-Top Box",
    "product_version": "4.2.1",
    "helpers": {
      "model_numbers": ["STB-4200-*"]
    }
  },
  "vulnerability_ids": [
    { "system_name": "CVE", "text": "CVE-2026-12345" }
  ],
  "status": "not_affected",
  "justification": "vulnerable_code_not_present",
  "release_date": "2026-08-20T09:00:00Z",
  "signature": "<detached event signature>"
}
```

**Example 2 — an affected product, tying back to the Keycloak example from the original motivation.**
Here `helpers` carries CPE/PURL because the product is software and both are actually available —
`product` still carries the triple as the baseline:

```json
{
  "document_id": "rhsa-2026-0431",
  "document_version": "2",
  "publisher_namespace": "https://access.redhat.com/security/data/csaf/v2",
  "document_category": "csaf_security_advisory",
  "product": {
    "vendor": "Red Hat",
    "product_name": "Red Hat build of Keycloak",
    "product_version": "26.0",
    "helpers": {
      "cpe": "cpe:/a:redhat:build_keycloak:26.0",
      "purl": "pkg:maven/org.keycloak/keycloak-core@26.0"
    }
  },
  "vulnerability_ids": [
    { "system_name": "CVE", "text": "CVE-2026-0431" }
  ],
  "status": "affected",
  "release_date": "2026-08-14T14:32:00Z",
  "signature": "<detached event signature>"
}
```

## Open questions

- Precedence rule when event and document drift apart: the document is always authoritative — how is
  this phrased normatively?
- Not every product tree uses `vendor`/`product_name`/`product_version` branches consistently (some
  vendors nest differently, e.g. `product_family` in between, or skip a level) — does the event
  require a normalized triple, and if the source tree doesn't cleanly provide one, what happens?
- Should `helpers` be capped to a shortlist (cpe, purl, model_numbers) or pass through all
  `product_identification_helper` sub-fields as-is?
- Should `vulnerability_ids` be capped (e.g. CVE + one RVISC-registered ID) or unbounded, matching
  `$.vulnerabilities[*].ids` as-is?
- Where does the schema structurally live — its own JSON schema, or an extension of the ROLIE
  entry/`changes.csv`?

## TODO

Write concrete spec text once P1 has been presented to the TC and received generally positive
feedback.
