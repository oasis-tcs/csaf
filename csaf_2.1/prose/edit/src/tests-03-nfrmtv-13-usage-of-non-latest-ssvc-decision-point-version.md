### Usage of Non-Latest SSVC Decision Point Version

For each SSVC decision point given under `selections` with a registered `namespace`, it SHALL be tested the latest decision point
`version` available at the time of the test is performed.
The [SSVC registry](https://certcc.github.io/SSVC/data/json/ssvc_object_registry.json) will provide all the publicly available latest decision points.

The test SHALL fail if an earlier `version` was used.
Namespaces reserved for special purpose SHALL be treated as per their definition.

> A list of all valid decision points of registered namespaces including their values is available at the
> SSVC repository (see [cite](#SSVC-DP)).

The relevant path for this test is:

```list-of-jsonpaths
  $.vulnerabilities[*].metrics[*].content.ssvc_v2.selections[*]
```

*Example 1 (which fails the test):*

```
  "ssvc_v2": {
    // ...
    "selections": [
      {
        "key": "MI",
        "name": "Mission Impact",
        "namespace": "ssvc",
        // ...
        "version": "1.0.0"
      }
    ],
    "timestamp": "2024-01-24T10:00:00.000Z"
  }
```
> At the time of the test `2026-11-15T10:00:00.000Z` version `2.0.0` of the SSVC decision point `Mission Impact` was already available.
