### License Expression

It MUST be tested that the license expression is valid.

> To implement this test, it it deemed sufficient to check for the ABNF defined in annex B of [cite](#SPDX301) and
> the restriction on the `DocumentRef` part given in [sec](#document-property-license-expression).

The relevant path for this test is:

```
  /document/license_expression
```

*Example 1 (which fails the test):*

```
    "license_expression": "This is a license text that should not be here.",
```

> The license expression contains a license text instead of a SPDX license expression.
