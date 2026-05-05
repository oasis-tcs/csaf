### Conformance Clause 16: CSAF Full Validator

A CSAF Extended Validator satisfies the "CSAF Full Validator" conformance profile if the CSAF Extended Validator:

* satisfies the "CSAF Extended Validator" conformance profile.
* additionally performs all tests of the preset `informative` as given in section [sec](#presets-defined-through-test-subsections).
* provides an option to additionally use a custom dictionary for test [sec](#spell-check).
* additionally satisfies those normative requirements in section [sec](#informative-tests)
  that are designated as applying to CSAF Validators.

A CSAF Full Validator MAY provide an additional function to only run one or more selected informative tests.
