### Conformance Clause 30: CSAF Extension Overlay Test

A test satisfies the "CSAF Extension Overlay Test" conformance profile if it:

* is executed only if the specifying CSAF Extension is present.

  > To reuse a test from a different CSAF Extension, it is sufficient to assign it a name according to the rules below
  > and point to the specification of the test it reuses.
  > The referenced specification in such case must be accessible to anyone that can retrieve the referencing CSAF Extension.

* extends or replaces a test specified in this standard in section [sec](#tests) or a CSAF Additional Test.
* does not adversely affect the purpose of the test in question.
* has a name starting with `Extension_Overlay_Test_` followed by a name of the specifying entity conforming to the
  rules for prefixes of test presets (cf. section [sec](#test-presets)) and the name of the tests that it replaces.
* has its definition specified in the same structure as in section [sec](#tests).

The CSAF Extension Overlay Test SHOULD only differ in the paths or the document categories it is applied to.

> This ensures maximum compatibility with other extensions as multiple CSAF Extension can define
> CSAF Extension Overlay Tests for the same test which are then executed as a union set.
