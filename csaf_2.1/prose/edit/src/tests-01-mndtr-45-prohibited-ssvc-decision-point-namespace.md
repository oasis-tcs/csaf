### Prohibited SSVC Decision Point Namespace

For each SSVC decision point given under `selections` with a `namespace` other than case-sensitive reserved values, it MUST be tested that the
`namespace` it not equal to the case-insensitive reserved values.

> The following values are reserved:
>
> ```
>   cvssv4
>   ssvc
> ```

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
                  "name": "Mission Impact",
                  "namespace": "SSVC",
                  "values": [
                    "None"
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

> The SSVC decision point namespace uses the capitalized version of the reserved namespace `ssvc`.

> A tool MAY convert the reserved namespace to lowercase as a quick fix.
