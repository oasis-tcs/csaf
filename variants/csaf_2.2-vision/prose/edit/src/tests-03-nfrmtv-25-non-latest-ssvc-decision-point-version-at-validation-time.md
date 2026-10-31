### Non-Latest SSVC Decision Point Version at Validation Time

For each SSVC decision point given under `selections` with a registered `namespace`, it SHALL be tested the latest decision point
`version` available at the time the test is performed was used.
Namespaces reserved for special purpose SHALL be treated as per their definition.

> The result of the test is dependent upon the time of the execution of the test - it might change for a given CSAF document over time.
> This test is intended to be used during the editorial process of CSAF documents.
> The significance of the test result regarding released CSAF documents is limited.
> It is not expected to update a released CSAF document if this test fails and no other new information is available.
> Observatories and other reporting entities are requested to not include this test in their general score.
>
> Usage of a later version of a SSVC Decision Point will cause test [sec](#usage-of-non-latest-ssvc-decision-point-version) to fail.
> The reason for this is most likely an outdated data set of SSVC decision points.
> A list of all valid decision points of registered namespaces including their values is available at the
> SSVC registry (see [cite](#SSVC-OR)).

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

> > At the time of the test execution `2026-10-07T10:00:00.000Z` version `2.0.0` of the SSVC decision point `Mission Impact` was already available.
