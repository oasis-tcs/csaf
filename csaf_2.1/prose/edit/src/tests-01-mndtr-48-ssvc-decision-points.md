### SSVC Decision Points

For each SSVC decision point given under `selections` within a registered base `namespace`, it MUST be tested that given decision point exists,
is valid and the items in `values` are ordered correctly.
The test SHALL pass, if a unregistered `namespace` is used.
Namespaces reserved for special purpose MUST be treated as per their definition.

> A list of all currently registered namespaces is a available in the SSVC documentation at [cite](#SSVC-RNS).
>
> A list of all valid decision points of registered namespaces including their values is available at the
> SSVC repository (see [cite](#SSVC-DP)).
> The items in `values` need to have the same order as in their definition.
>
> This test also covers decision points which use a registered base namespace with any number of extensions.
> The rules for namespace extensions as specified by SSVC must be applied in such case.
> Note that:
>
> - Extensions can limit the number of available values, but not add new ones or change the order.
> - Extensions can translate or refine the `name` and `definition`, but not change the `key`.

The relevant path for this test is:

```
   /vulnerabilities[]/metrics[]/content/ssvc_v2/selections[]
```

*Example 1 (which fails the test):*

```
  "ssvc_v2": {
    // ...
    "selections": [
      {
        "key": "MI",
        "namespace": "ssvc",
        "values": [
          {
            "key": "N",
            "name": "None"
          },
          {
            "key": "D",
            "name": "Degraded"
          }
        ],
        "version": "1.0.0"
      }
    ],
    // ...
  }
```

> The SSVC decision point `Mission Impact` doesn't have the value `Degraded` in version `1.0.0`.

> If applicable, a tool MAY sort the items in `values` according to the order of their definition as a quick fix.
