### Conformance Clause 28: CSAF Extension

A JSON object satisfies the "CSAF Extension" conformance profile if it:

* conforms to the syntax and semantics defined in section [sec](#extensions).
* validates against the [CSAF Extension Content Schema](https://docs.oasis-open.org/csaf/csaf/v2.1/schema/extension-content.json)
  and the schema given through its `$schema` property.
* uses the value of `$id` of its CSAF Extension Schema as the value of its `$schema` property.
* conveys additional information that cannot be conveyed with the CSAF Core elements.
* does not convey any content that can be conveyed with the CSAF Core elements.
* does not contradict the content or purpose of this specification.
