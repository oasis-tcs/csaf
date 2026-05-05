### Conformance Clause 29: CSAF Extension Schema

A JSON schema satisfies the "CSAF Extension Schema" conformance profile if fulfills the following two groups of requirements:

Firstly, it:

* describes a JSON object satisfying the "CSAF Extension" conformance profile.
* validates against the [CSAF Extension Metaschema](https://docs.oasis-open.org/csaf/csaf/v2.1/schema/extension-metaschema.json).
* uses the [CSAF Extension Metaschema](https://docs.oasis-open.org/csaf/csaf/v2.1/schema/extension-metaschema.json)
  as the value of its `$schema` property.
* is versioned according to [cite](#SemVer).
* has an `$id` that conforms to the `pattern` given for the property `$schema` in section [sec](#content-schema-property---schema).
* does not allow unevaluated properties.
  It MAY include `patternProperties` if they are typed.

  > `patternProperties` are typed if they can't have more than one `type` and that `type` is given through the schema.

Secondly, it:

* SHOULD avoid unpredictable JSON key names.

  > Implementations usually ignore any additional properties as they are hard to access, process and may imply security risks.
