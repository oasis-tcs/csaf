### License Expression

It MUST be tested that the license expression is valid.

> To implement this test, it is deemed sufficient to check for the ABNF defined in annex B of [cite](#SPDX301) and
> the restriction on the `DocumentRef` part given in [sec](#document-property---license-expression).
> Although a match against the SPDX License List (`license-id`) or a specific `LicenseRef` or `AdditionalRef` list
> is not in scope for this test, it checks all other constraints given in the ABNF.

The relevant path for this test is:

```list-of-jsonpaths
  $.document.license_expression
```

*Example 1 (which fails the test):*

```
    "license_expression": "This is a license text that should not be here.",
```

> The license expression contains a license text instead of a SPDX license expression.
