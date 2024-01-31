# Schema Elements

The CSAF schema describes how to represent security advisory information as a JSON document.

The CSAF schema Version 2.1 builds on the JSON Schema draft 2020-12 rules.

```
    "$schema": "https://json-schema.org/draft/2020-12/schema"
```

The schema identifier is:

```
    "$id": "https://docs.oasis-open.org/csaf/csaf/v2.1/csaf_json_schema.json"
```

The further documentation of the schema is organized via Definitions and Properties.

* Definitions provide types that extend the JSON schema model
* Properties use these types to support assembling security advisories

Types and properties together provide the vocabulary for the domain specific language supporting security advisories.

The single mandatory property is `document`.
The optional two additional properties are `product_tree` and `vulnerabilities`.
