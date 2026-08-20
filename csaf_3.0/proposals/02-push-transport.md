# Proposal 2 — Push Transport (WebSub Extension)

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

## Minimum field set

The subscription handshake reuses WebSub's own parameters as-is — nothing new to specify there:

| Field | Source | Value in our mapping |
| --- | --- | --- |
| `hub.mode` | WebSub standard | `subscribe` / `unsubscribe` |
| `hub.topic` | WebSub standard | the ROLIE category feed URL for one product (Requirement 17) |
| `hub.callback` | WebSub standard | subscriber-supplied |
| `hub.secret` | WebSub standard | used to HMAC-sign notification payloads |
| `hub.lease_seconds` | WebSub standard | subscription expiry; renewal handling still open, see below |

The one thing that *is* new: what the hub sends on notification. We propose the notification body be
one or more [P1 events](01-event-schema.md) (JSON array, one entry per change since the last
notification), HMAC-signed with `hub.secret`, rather than the bare "topic changed, go re-fetch" ping
that vanilla WebSub defaults to. This is what makes P1 and P2 combine into an actual push
notification instead of just a push-triggered poll.

## Example (illustrative, non-normative)

The subscribe request is plain WebSub, form-encoded per the standard:

```
POST /websub/hub HTTP/1.1
Host: psirt.acme.example
Content-Type: application/x-www-form-urlencoded

hub.mode=subscribe
&hub.topic=https%3A%2F%2Fpsirt.acme.example%2Fcsaf%2Ffeed-set-top-box.json
&hub.callback=https%3A%2F%2Ftrustsource.io%2Fwebhook%2Facme-set-top-box
&hub.secret=8f3e...
&hub.lease_seconds=2592000
```

The notification the hub sends once a matching document is published — body is a JSON array of
[P1 events](01-event-schema.md), signature over the raw body carried in a header per the WebSub
authenticated-content-distribution mechanism:

```
POST /webhook/acme-set-top-box HTTP/1.1
Host: trustsource.io
Content-Type: application/json
X-Hub-Signature: <HMAC of the body below, keyed with hub.secret>
Link: <https://psirt.acme.example/csaf/feed-set-top-box.json>; rel="self",
      <https://psirt.acme.example/websub/hub>; rel="hub"

[
  {
    "document_id": "acme-vex-2026-0512",
    "document_version": "1.0.0",
    "publisher_namespace": "https://psirt.acme.example",
    "document_category": "csaf_vex",
    "product": {
      "vendor": "Acme Corp",
      "product_name": "Acme Streamline Set-Top Box",
      "product_version": "4.2.1"
    },
    "vulnerability_ids": [{ "system_name": "CVE", "text": "CVE-2026-12345" }],
    "status": "not_affected",
    "justification": "vulnerable_code_not_present",
    "release_date": "2026-08-20T09:00:00Z",
    "signature": "<detached event signature>"
  }
]
```

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
