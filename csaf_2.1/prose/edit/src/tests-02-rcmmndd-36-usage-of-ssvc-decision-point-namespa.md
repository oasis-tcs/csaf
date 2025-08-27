### Usage of SSVC Decision Point Namespace with Extension in TLP:CLEAR Document

For each SSVC decision point given under `selections`, it MUST be tested that the `namespace` does not use an extension
if the document is labeled `TLP:CLEAR`.
Namespaces reserved for special purpose MUST be treated as per their definition.

The relevant path for this test is:

```
   /vulnerabilities[]/metrics[]/content/ssvc_v2/selections[]/namespace
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
        "metrics": [
          {
            "content": {
            "ssvc_v2": {
              // ...
              "selections": [
                {
                  // ...
                  "namespace": "ssvc//.example.test#refined-technical-impacts",
                  // ...
                }
                ],
                // ...
              }
            },
            // ...
          }
        ]
      }
    ]
  }
```

> The namespace contains the extension `.example.test#refined-technical-impacts`.
> Its decision point definitions might therefore not be known to the reader of the document.
> However, as per SSVC specification, extensions cannot extend an existing decision point with new values.
> Thus, they can be treated as decision points from the base namespace, if the extension is unknown.
