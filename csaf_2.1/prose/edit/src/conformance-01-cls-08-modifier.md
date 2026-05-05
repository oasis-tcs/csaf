### Conformance Clause 8: CSAF Modifier

A program satisfies the "CSAF Modifier" conformance profile if the program fulfills the two following groups of requirements:

The program:

* satisfies the "CSAF Post-Processor" conformance profile.
* adds, deletes or modifies at least one property, array, object or value of a property or item of an array.
* does not emit any objects, properties, or values which, according to section [sec](#conformance),
  are intended to be produced only by CSAF Translators.
* satisfies the normative requirements given below.

The resulting modified document:

* does not have the same `/document/tracking/id` as the original document.
  The modified document can use a completely new `/document/tracking/id` or compute one by appending the original `/document/tracking/id` as
  a suffix after an ID from the naming scheme of the issuer of the modified version.
  It SHOULD NOT use the original `/document/tracking/id` as a prefix.
* includes a reference to the original advisory as first element of the array `/document/references[]`.
