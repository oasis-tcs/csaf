### Conformance Clause 14: CSAF Basic Validator

A program satisfies the "CSAF Basic Validator" conformance profile if the program:

- reads documents and performs a check against the JSON schema,
  including also the format validation (cf. section [sec](#format-validation)).
- performs all tests of the preset `mandatory` as given in section [sec](#presets-defined-through-test-subsections).
- does not change the CSAF Documents unless explicitly invoked to do so (e.g. for applying quick fixes).
- satisfies those normative requirements in sections [sec](#extensions), [sec](#schema-elements), [sec](#mandatory-tests),
  [sec](#test-presets), and [sec](#safety-security-and-data-protection-considerations) that are designated as applying to
  CSAF Validators.
- satisfies those normative requirements in section [sec](#extensions) that are designated as applying to CSAF Tools.
- issues a warning if an "not implemented warning" occurs as the validation status might not be correct.

A CSAF Basic Validator MAY provide one or more additional functions:

- Only run one or more selected mandatory tests.
- Apply quick fixes as specified in the standard.
- Apply additional quick fixes as implemented by the vendor.
- Provide an option to fail after the first error.
- Provide an option to generate all error messages.
  Such option SHOULD NOT be the default as it could lead into a DoS situation.

A CSAF Basic Validator MAY implement CSAF Additional Tests.
In that case, it SHALL make through its documentation available which tests are implemented.
