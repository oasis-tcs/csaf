### Conformance Clause 31: CSAF Extension Additional Test

A test satisfies the "CSAF Extension Additional Test" conformance profile if it:

* is executed only if the specifying CSAF Extension is present.

  > To reuse a test from a different CSAF Extension, it is sufficient to assign it a name according to the rules below
  > and point to the specification of the test it reuses.
  > The referenced specification in such case must be accessible to anyone that can retrieve the referencing CSAF Extension.

* provides additional checks in the context of the CSAF Extension or the CSAF Document the extension is embedded in.
* has a name starting with `Extension_Additional_Test_` followed by a name of the specifying entity conforming to the
  rules for prefixes of test presets (cf. section [sec](#test-presets)) and an unique number for the test within that entity.
* has its definition specified in the same structure as in section [sec](#tests).
