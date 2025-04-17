### Usage of Unregistered SSVC Decision Point Namespace

For each SSVC decision point given under `selections`, it MUST be tested the `namespace` is one of the case-sensitive registered namespaces.

The relevant path for this test is:

```
   /vulnerabilities[]/metrics[]/content/ssvc_v1/selections[]/namespace
```

*Example 1 (which fails the test):*

```
  "vulnerabilities": [
    {
      "cve": "CVE-1900-0001",
      "metrics": [
        {
          "content": {
            "ssvc_v1": {
              "id": "CVE-1900-0001",
              "schemaVersion": "1-0-1",
              "selections": [
                {
                  "name": "Technical Impact",
                  "namespace": "some-yet-unknown-or-maybe-private-namespace",
                  "values": [
                    "Total"
                  ],
                  "version": "1.0.0"
                }
              ],
              "timestamp": "2024-01-24T10:00:00.000Z"
            }
          },
          // ...
        }
      ]
    }
  ]
```

> The namespace `some-yet-unknown-or-maybe-private-namespace` is not a registered namespace.
> Its decision point definitions might therefore not be known to the reader of the document.
