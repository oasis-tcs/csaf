### Additional Properties

It MUST be tested that there is no additional property in the CSAF document that was not defined in the CSAF JSON schema.
This also applies for referenced schemas.
For CSAF Extensions, the declared schemas MUST be checked additionally to the CSAF Extension Content Schema.
Additional and unevaluated properties allowed by the CSAF Extension Content Schema MUST not be reported.
CSAF Extensions not supported by the implementation SHALL result in a warning which MUST include the value of `$schema` of the extension.
Such warning SHALL differentiate between the different classes of extensions.

> Some of the errors could be reported by combining the JSON schema check with several mandatory tests,
> this test provides an one stop solution and can be used as quality gate in CSAF publication pipelines or contracts.
> Therefore, a potential double reporting is not consider an issue.

The relevant path for this test is:

```
  /
```

> To implement this test it is deemed sufficient to validate the CSAF document against a "strict" version schema that has all references integrated
> and sets `additionalProperties` respectively `unevaluatedProperties` to `false` at all appropriate places to detect additional properties.

*Example 1 (which fails the test):*

```
            "cvss_v3": {
              "baseScore": 6.4,
              "baseSeverity": "MEDIUM",
              "custom_property": "any",
              "vectorString": "CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:C/C:N/I:H/A:L",
              "version": "3.1"
            }
```

> The key `custom_property` is not defined in the JSON schema.

> A tool MAY remove such keys as a quick fix.
