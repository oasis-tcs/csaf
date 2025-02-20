### SSVC Decision Points

For each SSVC decision point given under `selections` with the `namespace` of `ssvc`, it MUST be tested that given decision point exists, is valid and the items in `values` are ordered correctly.

> A list of all valid decision points including their values is available at the [SSVC repository](https://github.com/CERTCC/SSVC/tree/main/data/json/decision_points).
> The items in `values` need to have the same order as in their definition.

The relevant paths for this test are:

```
   /vulnerabilities[]/metrics[]/content/ssvc_v1/selections[]
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
                  "name": "Mission Impact",
                  "namespace": "ssvc",
                  "values": [
                    "None",
                    "Degraded"
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

> The SSVC decision point `Mission Impact` doesn't have the value `Degraded` in version `1.0.0`.

> If applicable, a tool MAY sort the items in `values` according to the order of their definition as a quick fix.
