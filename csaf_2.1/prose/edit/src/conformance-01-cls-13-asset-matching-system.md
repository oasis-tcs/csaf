### Conformance Clause 13: CSAF Asset Matching System

A CSAF Asset Matching System satisfies the "CSAF Asset Matching System" conformance profile if the asset matching system:

* satisfies the "CSAF Management System" conformance profile.
* is an asset database or connects to one.
* matches the CSAF Documents within the system to the respective assets.
  This might be done with a probability which gives the end user the chance to broaden or narrow the results.
  The process of matching is also referred to as "run of the asset matching module".
* provides for each product of the asset database a list of matched advisories.
* provides for each asset of the asset database a list of matched advisories.
* provides for each CSAF Document a list of matched product of the asset database.
* provides for each CSAF Document a list of matched asset of the asset database.
* provides for each vulnerability within a CSAF Document the option to mark a matched asset in the asset database as "not remediated",
  "remediation in progress", or "remediation done". A switch to mark all assets at once MAY be implemented.
* does not bring up a newer revision of a CSAF Document as a new match if the remediation for the matched product or asset has not changed.
* detects the usage semantic version (as described in section [sec](#version-type---semantic-versioning)).
* is able to trigger a run of the asset matching module:
  * manually:
    * per CSAF Document
    * per list of CSAF Documents
    * per asset
    * per list of assets
  * automatically:
    * when a new CSAF Document is inserted (for this CSAF Document)
    * when a new asset is inserted (for this asset)
    * when the Major version in a CSAF Document with semantic versioning changes (for this CSAF Document)

    > These also apply if more than one CSAF Document or asset was added.
    > To reduce the computational efforts the runs can be pooled into one run which fulfills all the tasks at once (batch mode).

  * Manually and automatically triggered runs SHOULD NOT be pooled.
* provides at least the following statistics for the count of assets:
  * matching that CSAF Document at all
  * marked with a given status
