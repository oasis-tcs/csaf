### Invalid SSVC

It MUST be tested that the given SSVC object is valid according to the referenced schema.

The relevant path for this test is:

```
  /vulnerabilities[]/metrics[]/content/ssvc_v2
```

*Example 1 (which fails the test):*

```
  "ssvc_v2": {
    "schemaVersion": "2.0.0",
    "timestamp": "2024-01-24T10:00:00.000Z"
  }
```

> The required element `selections` is missing.
