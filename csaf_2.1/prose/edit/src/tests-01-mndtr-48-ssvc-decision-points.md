### SSVC Decision Points

For each SSVC decision point given under `selections` within a registered `namespace`, it MUST be tested that given decision point exists,
is valid and the items in `values` are ordered correctly.

The test SHALL pass, if a unregistered `namespace` is used.

This test also covers decision points which have use a registered namespace with any number of extensions.
The rules for namespace extensions as specified by SSVC MUST be applied in such case.

> Extensions can limit the number of available values, but not add new ones or change the order.
> Extensions can translate or refine the `name` and `description` but not change the `key`.

Namespaces reserved for special purpose MUST be treated as per their definition.

> According to the SSVC project, the following values are currently registered:
>
> ```
>   cisa
>   cvss
>   ssvc
> ```
>
> A list of all valid decision points including their values is available at the [SSVC repository](https://github.com/CERTCC/SSVC/tree/main/data/json/decision_points).
> The items in `values` need to have the same order as in their definition.

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
