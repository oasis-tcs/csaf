## Format Validation

The JSON schema 2020-12 dialect per default uses the `format` keyword just as annotation.
to be able to ensure that the format constraints are validated as intended, the following metaschema is defined.

```
  {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://docs.oasis-open.org/csaf/csaf/v2.1/meta_json_schema.json",
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
    "$schema": "https://docs.oasis-open.org/csaf/csaf/v2.1/meta_json_schema.json",
    // ...
  }
```
