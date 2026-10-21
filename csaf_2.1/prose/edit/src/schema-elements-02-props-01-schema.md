### Schema Property

JSON schema (`$schema`) of value type `string` and `const` with format `uri` contains the URL of the CSAF JSON schema which the document promises to be valid for.
The value for this `const` is:

```
  https://docs.oasis-open.org/csaf/csaf/v2.1/schema/csaf.json
```

> This value allows for tools to identify that a JSON document is meant to be valid against this schema.
> Tools can use that to support users by automatically checking whether the CSAF adheres to the JSON schema identified by this URL.
