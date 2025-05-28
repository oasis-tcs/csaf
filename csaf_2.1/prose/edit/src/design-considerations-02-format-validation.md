## Format Validation

The JSON schema 2020-12 dialect per default uses the `format` keyword just as annotation.
To be able to ensure that the format constraints are validated as intended, the following metaschema is defined.

```
  {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://docs.oasis-open.org/csaf/csaf/v2.1/schema/meta.json",
    "$dynamicAnchor": "meta",
    "$vocabulary": {
      "https://json-schema.org/draft/2020-12/vocab/core": true,
      "https://json-schema.org/draft/2020-12/vocab/format-assertion": true
    },
    "allOf": [
      { "$ref": "https://json-schema.org/draft/2020-12/meta/core" },
      { "$ref": "https://json-schema.org/draft/2020-12/meta/format-assertion" }
    ]
  }
```

It is then consequently used in all JSON schemas defined in this standard and replaces the reference to the JSON schema 2020-12.

```
  {
    "$schema": "https://docs.oasis-open.org/csaf/csaf/v2.1/schema/meta.json",
    // ...
  }
```

The format validation is enforced by setting the corresponding vocabulary as required.

> If a library used to parse, modify or create CSAF content is unable to deal with this meta schema, it could reach the objective by
> interpreting the schema as JSON schema 2020-12 dialect and enforcing the format validation via its implementation.
