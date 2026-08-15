# Proposal 2 — Push Transport (WebSub Extension)

*[Diese Seite auf Deutsch lesen](02-push-transport.de.md)* — the German version is a faithful,
complete translation of this document. In case of any discrepancy, this English version is
authoritative.

**Status:** Sketch, no spec text yet. See [../README.md](../README.md) for motivation and how this
fits alongside the other three proposals.

**Dependencies:** Does not strictly require any of the other proposals, but is only meaningfully
usable for public (TLP:CLEAR/GREEN) channels without P3. Ideally delivers the P1 event as its
payload.

## Goal

Optional, additional push capability for Trusted Providers, without replacing the existing pull
mechanism (ROLIE feed, Requirements 15–17).

## Mechanism (short version)

Based on [WebSub](https://www.w3.org/TR/websub/) (W3C Recommendation, 2018):

1. **Topic** = existing ROLIE category feed per product (Requirement 17).
2. **Hub** = new, optional capability of the Trusted Provider (or a third-party hub it designates).
3. Subscriber subscribes via the standard WebSub handshake (including `hub.challenge` verification
   against abuse).
4. On new/changed publication: hub notifies subscribers — payload = P1 event instead of just "go
   check again".

## Mandatory safety-net requirement

The pull mechanism remains authoritative in all cases. Subscribers MUST be able to reconcile after
detecting a gap (own timestamp vs. feed/`changes.csv`) without depending on the hub (see discussion
in the README, "Open items" section).

## Open questions

- Retention window for feed/`changes.csv` as a reconciliation basis (currently unspecified).
- Lease/renewal handling for long-lived customer subscriptions.
- Third-party hub operation (analogous to Superfeedr) — what requirements would apply then?

## TODO

Write concrete spec text (new requirement in section 7.1, new role or addition to "CSAF Trusted
Provider" in 7.2).
