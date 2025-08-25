### Usage of Unknown SSVC Decision Point Namespace without Resource

For each SSVC object containing a decision point with a full `namespace` that is not registered,
it MUST be tested that a Decision Point Resource exists that provides additional context about the
decision points from this namespace.
Namespaces reserved for special purpose MUST be treated as per their definition.

>
> To implement this test it is deemed sufficient to check whether the `summary` contains the full `namespace`.

Namespaces reserved for special purpose MUST be treated as per their definition.

The relevant path for this test is:

```
   /vulnerabilities[]/metrics[]/content/ssvc_v2/decision_point_resources
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
