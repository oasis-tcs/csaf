### Usage of Unknown SSVC Decision Point Namespace without Resource

For each SSVC object containing a decision point with a full `namespace` that is not registered,
it MUST be tested that a Decision Point Resource exists for each one that provides additional context about the
decision points from this namespace.
Namespaces reserved for special purpose MUST be treated as per their definition.

> A full namespace includes any extension.
> To implement this test it is deemed sufficient to check whether the `summary` contains the full `namespace`.

Namespaces reserved for special purpose MUST be treated as per their definition.

The relevant path for this test is:

```
   /vulnerabilities[]/metrics[]/content/ssvc_v2/decision_point_resources
```

*Example 1 (which fails the test):*

```
  "content": {
    "ssvc_v2": {
      "decision_point_resources": [
        {
          "summary": "Specification for Decision Points within 'x_example.test#some-other-collection'",
          "uri": "https://test.example/ssvc-collection/test-some-other-collection"
        }
      ],
      // ...
      "selections": [
        {
          // ...
          "namespace": "x_example.test#without-resource/de-DE",
          // ...
        }
      ],
      // ...
    }
  },
```

> The namespace `x_example.test#without-resource/de-DE` is not a registered one,
> however no `decision_point_resources` mentions the `namespace` in its `summary`.
