### Usage of Non-Latest SSVC Decision Point Version

For each SSVC decision point given under `selections` with a registered `namespace`, it MUST be tested the latest decision point
`version` available at the time of the `timestamp` was used.
The test SHALL fail if a later `version` was used.
Namespaces reserved for special purpose MUST be treated as per their definition.

> A list of all valid decision points of registered namespaces including their values is available at the
> SSVC repository (see [cite](#SSVC-DP)).

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
        "name": "Mission Impact",
        "namespace": "ssvc",
        // ...
        "version": "1.0.0"
      }
    ],
    "timestamp": "2024-01-24T10:00:00.000Z"
  }
```

> At the timestamp `2024-01-24T10:00:00.000Z` version `2.0.0` of the SSVC decision point `Mission Impact` was already available.
