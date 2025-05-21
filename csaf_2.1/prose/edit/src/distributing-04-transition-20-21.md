## Transition between CSAF 2.0 and CSAF 2.1

This subsection details the process that SHOULD be followed when transitioning the distribution of documents from CSAF 2.0 to CSAF 2.1.
Different scenarios can be encountered:
- Providers will continue to use CSAF 2.0.
  This SHOULD be avoided, as the CSAF ecosystem greatly profits from adoption to the new standard version.
- Providers will immediately upgrade all documents as well as the `provider-metadata.json` to CSAF 2.1.
  While this benefits the adoption of CSAF 2.1, consumers that still use CSAF 2.0
- Providers will begin a transition period, in which they continue to serve existing documents in CSAF 2.0, gradually updating the existing
  document base (using a CSAF 2.1/2.0 converter TODO conformance clause) and publishing new documents in CSAF 2.1.

In the last scenario, a temporary parallel distribution of CSAF 2.0 and CSAF 2.1 documents and provider metadata is recommended.
The following process SHOULD be followed:
- A `provider-metadata.json` in conformance to CSAF 2.0 SHOULD be placed at `/.well-known/csaf/v2.0/provider-metadata.json`.
  Its `canonical_url` must be set correctly and the property `maintained_until` SHOULD be set to an appropriate date in the future.
  The url MUST also be added as an entry to the security.txt, if used.
- A `provider-metadata.json` in conformance to CSAF 2.1 SHOULD be placed at `/.well-known/csaf/v2.1/provider-metadata.json`.
  Its `canonical_url` must be set correctly, optionally the property `maintained_from` can be set to an appropriate date in the future, 
  if the service is not considered stable yet.
  The url MUST also be added to the security.txt, if used.
- At the begin of the transition period, a `provider-metadata.json` in conformance to CSAF 2.0 SHOULD be placed at `/.well-known/csaf/provider-metadata.json`.
  The content of the resource MUST be equal to the resource accessible at `/.well-known/csaf/v2.0/provider-metadata.json`.
  For file-based distribution servers, this can for example be achieved by a symlink.
- After the transition period has ended, the contents of the `provider-metadata.json` at `/.well-known/csaf/provider-metadata.json` SHALL be replaced 
  with the contents of the resource available at `/.well-known/csaf/v2.1/provider-metadata.json`.
