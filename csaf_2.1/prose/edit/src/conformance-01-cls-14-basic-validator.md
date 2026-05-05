### Conformance Clause 14: CSAF Basic Validator

A program satisfies the "CSAF Basic Validator" conformance profile if the program:

* reads documents and performs a check against the JSON schema,
  including also the format validation (cf. section [sec](#format-validation)).
* performs all tests of the preset `mandatory` as given in section [sec](#presets-defined-through-test-subsections).
* does not change the CSAF Documents.
* satisfies those normative requirements in sections [sec](#extensions), [sec](#schema-elements)  [sec](#mandatory-tests),
  [sec](#test-presets), and [sec](#safety-security-and-data-protection-considerations) that are designated as applying to
  CSAF Validators.
* issues a warning if an "not implemented warning" occurs as the validation status might not be correct.

A CSAF Basic Validator MAY provide one or more additional functions:

* Only run one or more selected mandatory tests.
* Apply quick fixes as specified in the standard.
* Apply additional quick fixes as implemented by the vendor.

A CSAF Basic Validator MAY implement CSAF Additional Tests.
In that case, it SHALL make through its documentation available which tests are implemented.
