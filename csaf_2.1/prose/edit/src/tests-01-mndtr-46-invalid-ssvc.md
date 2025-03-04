### Invalid SSVC

It MUST be tested that the given SSVC object is valid according to the referenced schema.

The relevant path for this test is:

```
  /vulnerabilities[]/metrics[]/content/ssvc_v1
```

*Example 1 (which fails the test):*

```
  "ssvc_v1": {
    "id": "CVE-1900-0001",
    "schemaVersion": "1-0-1",
    "timestamp": "2024-01-24T10:00:00.000Z"
  }
```

> The required element `selections` is missing.

> A tool MAY add the missing property `id` based on the values given in `cve` respectively `ids[]/text` as quick fix.
