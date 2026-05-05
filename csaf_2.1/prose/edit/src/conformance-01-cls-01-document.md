### Conformance Clause 1: CSAF Document

A text file or data stream satisfies the "CSAF Document" conformance profile if it:

* conforms to the syntax and semantics defined in section [sec](#format-validation).
* conforms to the syntax and semantics defined in section [sec](#date-and-time).
* conforms to the syntax and semantics defined in section [sec](#extensions).
* conforms to the syntax and semantics defined in section [sec](#schema-elements).
* satisfies at least one profile defined in section [sec](#profiles).
* conforms to the syntax and semantics defined in section [sec](#additional-conventions).
* does not fail any mandatory test defined in section [sec](#mandatory-tests) respectively its corresponding CSAF Extension Test.
* contains no extension that does not fulfill the conformance profile "CSAF Extension".
* contains no extension at any other path than the specified ones in sections [sec](#full-product-name-type---extensions),
  [sec](#document-property---extensions), [sec](#vulnerabilities-property---metrics---content),
  [sec](#vulnerabilities-property---extensions) and [sec](#extensions-property).
