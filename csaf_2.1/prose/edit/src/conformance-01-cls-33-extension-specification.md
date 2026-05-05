### Conformance Clause 33: CSAF Extension Specification

A specification satisfies the "CSAF Extension Specification" conformance profile if:

* it defines exactly one extension satisfying the "CSAF Extension" conformance profile.
* it defines exactly one JSON schema satisfying the "CSAF Extension Schema" conformance profile.
* all tests defined in it satisfy the "CSAF Extension Test" conformance profile.
* it contains all tests needed for the validation of the extension.

  > This includes tests that check for prerequisites in the CSAF document, if applicable.
  > Referencing an existing test is considered to fulfill the "contains" requirement,
  > if the referenced test is accessible to anyone that can access the referencing specification.

* all requirements above are fulfilled for the same extension.
