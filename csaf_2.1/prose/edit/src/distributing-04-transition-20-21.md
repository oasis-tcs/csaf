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

### Announcing the Transition

In the last scenario, a temporary parallel distribution of CSAF 2.0 and CSAF 2.1 documents and provider metadata is recommended.
The provider SHOULD announce a transition period containing three points in time:

- The begin of the transition period, where the provider is starting to serve CSAF 2.1 documents, while CSAF 2.0 being authoritative.
- The roll-over-date at which CSAF 2.1 becomes authoritative but CSAF 2.0 is still supported.
- The end of the transition period, after which CSAF 2.0 is not supported any more.

The announcement MAY contain also the following information:

- The first date, when CSAF 2.1 documents are available and automatically retrievable from the server through a CSAF 2.1 `provider-metadata.json`.
- The last date, when CSAF 2.0 documents are available and automatically retrievable from the server through a CSAF 2.0 `provider-metadata.json`.

### Transition Process for a CSAF provider

The following process SHOULD be followed within the transition period:

- A `provider-metadata.json` in conformance to CSAF 2.0 SHOULD be placed at `/.well-known/csaf/v2.0/provider-metadata.json`.
  - Its `canonical_url` MUST be set to an URL corresponding to the `/.well-known/csaf/v2.0/provider-metadata.json` path.
  > The property `maintained_until` was not defined in CSAF 2.0 and therefore cannot be used -
  > otherwise it would be set to the end of the transition period.
  - The URL SHALL also be added as an entry in the security.txt, if used.
- A `provider-metadata.json` in conformance to CSAF 2.1 SHOULD be placed at `/.well-known/csaf/v2.1/provider-metadata.json`.
  - Its `canonical_url` MUST be set to an URL corresponding to the `/.well-known/csaf/v2.1/provider-metadata.json` path.
  - Optionally the property `maintained_from` can be set to an appropriate date in the future, if the service is not considered stable yet.
  - The URL SHALL also be added to the security.txt, if used.
- At the begin of the transition period, a `provider-metadata.json` in conformance to CSAF 2.0 SHOULD be placed at `/.well-known/csaf/provider-metadata.json`.
  - The content of the resource SHALL be equal to the resource accessible at `/.well-known/csaf/v2.0/provider-metadata.json`.
  - For file-based distribution servers, this MAY be achieved by using a symlink.
    Redirects SHALL NOT be used (cf. to requirement [sec](requirement-9-well-known-url-for-provider-metadata-json))
- Sometime before the roll-over-date, all existing CSAF 2.0 documents SHOULD be converted to CSAF 2.1.
- A the roll-over-date, a `provider-metadata.json` in conformance to CSAF 2.1 SHOULD be placed at `/.well-known/csaf/provider-metadata.json`.
  - The content of the resource SHALL be equal to the resource accessible at `/.well-known/csaf/v2.1/provider-metadata.json`.
  - For file-based distribution servers, this MAY be achieved by using a symlink.
    Redirects SHALL NOT be used (cf. to requirement [sec](requirement-9-well-known-url-for-provider-metadata-json))
- At the end of the transition period, the URL of the CSAF 2.0 `provider-metadata.json` SHOULD be removed from the `security.txt`.
  - The unmaintained CSAF 2.0 directory structure and files SHOULD be removed or made inaccessible.
  - The CSAF 2.0 documents MAY be archived.

### Archive of CSAF document from previous version

The following rules apply for the archival of CSAF document from a previous version:

- This archive SHOULD be located in `/.well-known/csaf/archive/` and use the file name `v2.0.zst`, `v2.0.tar.bz2` or `v2.0.tar.xz`.
- The CSAF documents within the archive MUST be sorted into folders according to requirement 11 in section
  [sec](#requirement-11-one-folder-per-year) and be accompanied by a hash according to requirement 18 [sec](#requirement-18-integrity).
- The archive MUST be accompanied by a hash of the same algorithm.
- Existing signatures MAY also be included into the archive.
  It is NOT RECOMMENDED to renew the signatures in the archive unless the archive is not updated.

### Transition Process for a CSAF Aggregator

Similarly, to the process of transitioning `provider-metadata.json`, the same process SHOULD be used to transition `aggregator.json`.
It is RECOMMENDED to use the following URLs during the process:

- `/.well-known/csaf-aggregator/aggregator.json` for the currently valid aggregator metadata.  
- `/.well-known/csaf-aggregator/v2.0/aggregator.json` for a valid CSAF 2.0 `aggregator.json`
- `/.well-known/csaf-aggregator/v2.1/aggregator.json` for a valid CSAF 2.1 `aggregator.json`

A CSAF 2.1 aggregator MUST only sync and list CSAF 2.1 publishers and providers.
