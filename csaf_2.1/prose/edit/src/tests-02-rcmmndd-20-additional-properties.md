### Additional Properties

It MUST be tested that there is no additional property in the CSAF document that was not defined in the CSAF JSON schema.

The relevant path for this test is:

```
  /
```

> To implement this test it is deemed sufficient to validate the CSAF document against a "strict" version schema that
> sets `additionalProperties` to `false` for every key of type `object`.

*Example 1 (which fails the test):*

```
  "document": {
    "category": "csaf_base",
    "csaf_version": "2.1",
    "custom_property": "any",
    // ...
  }
```

> The key `custom_property` is not defined in the JSON schema.

> A tool MAY remove such keys as a quick fix.
