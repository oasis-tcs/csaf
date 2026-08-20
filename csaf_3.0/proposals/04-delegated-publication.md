# Proposal 4 — Delegated Publication (Proxy Trusted Provider + Provenance Chain)

**Status:** Sketch, no spec text yet. See [../README.md](../README.md) for motivation and how this
fits alongside the other three proposals.

**Dependencies:** Independent of P1–P3, can be developed in parallel.

## Goal

A formalized, publicly documented path for vendors without their own hosting/signature
infrastructure ("dumb file" vendors) to publish through a Trusted Provider — including a
cryptographic proof chain that the publication is authorized by the original vendor.

## Starting point in the existing spec

- The concept already exists as the **"CSAF Proxy Provider"** — currently only on the aggregator
  side and explicitly not publicly accessible (section 7.2.5). This proposal formalizes the pattern
  at the Trusted Provider level and turns it into a documented onboarding path.
- Identity anchor: `document.publisher.namespace` (already a mandatory field, a globally unique URL
  under the vendor's control).
- Signature infrastructure: Requirements 19/20 (OpenPGP signature + public key) already exist.
- Precedent for opt-in/delegation: `list_on_CSAF_aggregators` / `mirror_on_CSAF_aggregators`.

## Two variants

**A — Vendor has its own key:** the vendor signs the raw file itself, the Trusted Provider takes over
hosting and adds its own counter-signature as a relay attestation. The consumer verifies both
signatures independently.

**B — Vendor has no own key:** the Trusted Provider signs alone, after a one-time out-of-band
verification of the vendor's identity during onboarding — analogous to the existing aggregator rule
("If the issuing party does not provide those files, they SHALL be created by the CSAF aggregator").
Weaker non-repudiation, but a pragmatic fallback for the least-equipped vendors.

## Minimum field set for the delegation record

The one artifact this proposal genuinely adds (everything else reuses existing fields, see above):

| Field | Type | Purpose |
| --- | --- | --- |
| `vendor_namespace` | uri | must equal the delegating document's `$.document.publisher.namespace` |
| `trusted_provider_namespace` | uri | the delegate's own identity, same form as `publisher.namespace` |
| `vendor_key_fingerprint` | string, optional | OpenPGP fingerprint of the vendor's own key (Variant A only, see below) |
| `scope` | string or list | which products/namespaces the delegation covers — `*` for "all documents under this namespace" or a restricted list |
| `valid_from` / `valid_until` | date-time | delegation validity window, same freshness discipline as Requirement 19 signatures |
| `revoked_at` | date-time, optional | set on early revocation; absence means "not revoked" |
| `record_signature` | string | signs the record itself — see open question on who signs it |

## What needs to be newly specified

An explicit, time-limited and revocable **delegation record** ("Vendor X delegates publication rights
for namespace Z to Trusted Provider Y, valid from–to"). Governance model to follow: the already
successfully completed RVISC process (see meeting minutes 2026-04-29).

## Open questions

- Who signs `record_signature`? The vendor (Variant A, strongest — an active act of delegation),
  the Trusted Provider alone (Variant B, weaker — a self-declared claim), or both?
- Revocation/expiry mechanism for delegation records (reuse of the signature validity logic from
  Requirement 19?).
- Abuse protection: how is it prevented that someone falsely claims to be a vendor's delegate?
- Governance: who registers/vets delegations — the Trusted Provider, the TC, or a registry approach
  analogous to RVISC?

## TODO

Write concrete spec text as well as new mandatory tests for the signature chain (see README, "Open
items / do not forget" section).
