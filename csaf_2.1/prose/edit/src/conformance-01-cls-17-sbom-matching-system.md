### Conformance Clause 17: CSAF SBOM Matching System

A CSAF SBOM Matching System satisfies the "CSAF SBOM Matching System" conformance profile if the SBOM matching system:

* satisfies the "CSAF Management System" conformance profile.
* is an SBOM database or connects to one.

  > A repository or any other location that can be queried for SBOMs and their content is also considered an SBOM database.
* matches the CSAF Documents within the system to the respective SBOM components.
  This might be done with a probability which gives the user the chance to broaden or narrow the results.
  The process of matching is also referred to as "run of the SBOM matching module".
* provides for each SBOM of the SBOM database a list of matched advisories.
* provides for each SBOM component of the SBOM database a list of matched advisories.
* provides for each CSAF Document a list of matched SBOMs of the SBOM database.
* provides for each CSAF Document a list of matched SBOM components of the SBOM database.
* provides for each vulnerability within a CSAF Document the option to mark a matched SBOM component in the SBOM database as "not remediated",
  "remediation in progress", or "remediation done".
  A switch to mark all SBOM component at once MAY be implemented.
* does not bring up a newer revision of a CSAF Document as a new match if the remediation for the matched SBOM or SBOM component has not changed.
* detects the usage semantic version (as described in section [sec](#version-type---semantic-versioning)).
* is able to trigger a run of the SBOM matching module:
  * manually:
    * per CSAF Document
    * per list of CSAF Documents
    * per SBOM component
    * per list of SBOM components
  * automatically:
    * when a new CSAF Document is inserted (for this CSAF Document)
    * when a new SBOM component is inserted (for this SBOM component)
    * when the Major version in a CSAF Document with semantic versioning changes (for this CSAF Document)

    > These also apply if more than one CSAF Document or SBOM component was added.
    > To reduce the computational efforts the runs can be pooled into one run which fulfills all the tasks at once (batch mode).

  > Manually and automatically triggered runs should not be pooled.

* provides at least the following statistics for the count of SBOM component:
  * matching that CSAF Document at all
  * marked with a given status
