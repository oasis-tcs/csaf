### Additional Properties

It MUST be tested that there is no additional property in the CSAF document that was not defined in the CSAF JSON schema.
This also applies for referenced schemas.

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
