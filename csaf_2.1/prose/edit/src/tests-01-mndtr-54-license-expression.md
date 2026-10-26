### License Expression

It SHALL be tested that the license expression is valid.

> To implement this test, it is deemed sufficient to check for the ABNF defined in annex B of [cite](#SPDX31) and
> the restriction on the `DocumentRef` part and case sensitivity given in [sec](#document-property---license-expression).
> Although a match against the SPDX License List (`license-id`) or a specific `LicenseRef` or `AdditionalRef` list
> is not in scope for this test, it checks all other constraints given in the ABNF.

The relevant path for this test is:

```{.text sequence-of="jsonpath"}
  $.document.license_expression
```

*Example 1 (which fails the test):*

```
    "license_expression": "This is a license text that should not be here.",
```

> The license expression contains a license text instead of a SPDX license expression.

> A tool MAY provide a function to fix case errors as a quick fix, if applicable.
