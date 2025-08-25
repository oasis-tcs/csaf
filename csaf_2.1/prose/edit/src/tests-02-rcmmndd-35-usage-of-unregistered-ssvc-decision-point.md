### Usage of Unregistered SSVC Decision Point Base Namespace in TLP:CLEAR Document

For each SSVC decision point given under `selections`, it MUST be tested the base `namespace` is not an unregistered one
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
                    "namespace": "x_example.unregistered#namespace",
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

> The namespace `x_example.unregistered#namespace` is an unregistered base namespace.
> Its decision point definitions might therefore not be known to the reader of the document.
