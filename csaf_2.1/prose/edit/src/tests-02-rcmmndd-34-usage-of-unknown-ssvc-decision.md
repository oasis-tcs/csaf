### Usage of Unknown SSVC Decision Point Base Namespace

For each SSVC decision point given under `selections`, it MUST be tested that the base `namespace` is a registered one.
Namespaces reserved for special purpose MUST be treated as per their definition.

> This test fails on unregistered namespaces as well as registered ones not yet supported by the implementation.

The relevant path for this test is:

```
   /vulnerabilities[]/metrics[]/content/ssvc_v2/selections[]/namespace
```

*Example 1 (which fails the test):*

```
  "ssvc_v2": {
    "schemaVersion": "2.0.0",
    "selections": [
      {
        // ...
        "namespace": "x_example.unregistered#some-yet-unknown-or-maybe-private-namespace",
        // ...
      }
    ],
    // ...
  }
```

> The namespace `x_example.unregistered#some-yet-unknown-or-maybe-private-namespace` is not a registered namespace.
> Its decision point definitions might therefore not be known to the reader of the document.
