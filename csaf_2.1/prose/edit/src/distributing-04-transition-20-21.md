## Transition between CSAF 2.0 and CSAF 2.1

This subsection details the process that SHOULD be followed when transitioning the distribution of documents from CSAF 2.0 to CSAF 2.1.
Different scenarios can be encountered:
- Providers will continue to use CSAF 2.0.
  This SHOULD be avoided, as the CSAF ecosystem greatly profits from adoption to the new standard version.
- Providers will immediately upgrade all documents as well as the `provider-metadata.json` to CSAF 2.1.
  While this benefits the adoption of CSAF 2.1, consumers that still rely on CSAF 2.0 are cut off.
- Providers will begin a transition period, in which they continue to serve existing documents in CSAF 2.0, gradually updating the existing
  document base (e.g. by using a CSAF 2.0 to CSAF 2.1 converter as described in [sec](#conformance-clause-18-csaf-2-0-to-csaf-2-1-converter))
  and publishing new documents using CSAF 2.1.

### Announcing the transition    

In the last scenario, a temporary parallel distribution of CSAF 2.0 and CSAF 2.1 documents and provider metadata is recommended.
The provider SHOULD announce a transition period containing three points in time:
  - The begin of the transition period, where the provider is starting to distribute serving CSAF 2.1 documents, while CSAF 2.0
    being authoritative.
  - The roll-over-date at which CSAF 2.1 comes authoritative but CSAF 2.0 is still supported.
  - The end of the transition period, after which CSAF 2.0 is not supported any more.

### Process of transition

The following process SHOULD be followed within the transition period:
- A `provider-metadata.json` in conformance to CSAF 2.0 SHOULD be placed at `/.well-known/csaf/v2.0/provider-metadata.json`.
  - Its `canonical_url` MUST be set to an URL corresponding to the `/.well-known/csaf/v2.0/provider-metadata.json` path.
  - The property `maintained_until` SHOULD be set to the end of the transition period.
  - The URL SHALL also be added as an entry in the security.txt, if used.
- A `provider-metadata.json` in conformance to CSAF 2.1 SHOULD be placed at `/.well-known/csaf/v2.1/provider-metadata.json`.
  - Its `canonical_url` MUST be set to an URL corresponding to the `/.well-known/csaf/v2.1/provider-metadata.json` path.
  - Optionally the property `maintained_from` can be set to an appropriate date in the future, if the service is not considered stable yet.
  - The URL SHALL also be added to the security.txt, if used.
- At the begin of the transition period, a `provider-metadata.json` in conformance to CSAF 2.0 SHOULD be placed at `/.well-known/csaf/provider-metadata.json`.
  - The content of the resource SHALL be equal to the resource accessible at `/.well-known/csaf/v2.0/provider-metadata.json`.
  - For file-based distribution servers, this MAY be achieved by using a symlink.
- Sometime before the roll-over-date, all existing CSAF 2.0 documents SHOULD be converted to CSAF 2.1.
- A the roll-over-date, a `provider-metadata.json` in conformance to CSAF 2.1 SHOULD be placed at `/.well-known/csaf/provider-metadata.json`.
  - The content of the resource SHALL be equal to the resource accessible at `/.well-known/csaf/v2.1/provider-metadata.json`.
  - For file-based distribution servers, this MAY be achieved by using a symlink.
- At the end of the transition period, it is RECOMMENDED to archive the remaining CSAF 2.0 documents, for example at
  `.well-known/csaf/archive/v2.0.tar.bz2`
