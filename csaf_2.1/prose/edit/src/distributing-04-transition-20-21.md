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

In the last scenario, a temporary parallel distribution of CSAF 2.0 and CSAF 2.1 documents and provider metadata is recommended.
The following process SHOULD be followed:
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
  - For file-based distribution servers, this MAY for example be achieved by a symlink.
- After the transition period has ended, the contents of the `provider-metadata.json` at `/.well-known/csaf/provider-metadata.json` SHALL be
  replaced with the contents of the resource available at `/.well-known/csaf/v2.1/provider-metadata.json`.
  - The canonical URL SHALL be set to the URL corresponding to `/.well-known/csaf/provider-metadata.json`.
