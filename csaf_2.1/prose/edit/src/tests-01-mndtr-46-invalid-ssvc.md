### Invalid SSVC

It SHALL be tested that the given SSVC object is valid according to the referenced schema.
If the object contains a language code, for example as a part of a `namespace`,
it SHALL also be tested that the language code is valid and exists.
CSAF Validators SHALL differentiate in the error message between the language code that contain subtags not in the registry
and those that contain only subtags from the registry but the compiled language code is invalid.

The relevant path for this test is:

```list-of-jsonpaths
  $.vulnerabilities[*].metrics[*].content.ssvc_v2
```

*Example 1 (which fails the test):*

```
  "ssvc_v2": {
    "schemaVersion": "2.0.0",
    "timestamp": "2024-01-24T10:00:00.000Z"
  }
```

> The required element `selections` is missing.
