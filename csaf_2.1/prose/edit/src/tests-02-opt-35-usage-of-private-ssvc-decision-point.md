### Usage of Private SSVC Decision Point Namespace in TLP:CLEAR Document

For each SSVC decision point given under `selections`, it MUST be tested the `namespace` is not a private one if the document is labeled `TLP:CLEAR`.

The relevant path for this test is:

```
   /vulnerabilities[]/metrics[]/content/ssvc_v1/selections[]/namespace
```

*Example 1 (which fails the test):*

```
  {
    "document": {
      // ...
      "distribution": {
        "tlp": {
          "label": "CLEAR"
        }
      },
      // ...
    }
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
                    "namespace": "x_custom",
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
  }
```

> The namespace `x_custom` is a private namespace.
> Its decision point definitions might therefore not be known to the reader of the document.
