### Usage of Unknown SSVC Role

For each SSVC object, it MUST be tested the `role` is one of the case-sensitive registered roles.

The relevant path for this test is:

```
   /vulnerabilities[]/metrics[]/content/ssvc_v1/role
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
              "role": "An unregistered role",
              "schemaVersion": "1-0-1",
              "selections": [
                {
                  "name": "Technical Impact",
                  "namespace": "ssvc",
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

> The role `An unregistered role` is not a registered role.
> Its structure might therefore not be known to the reader of the document.
