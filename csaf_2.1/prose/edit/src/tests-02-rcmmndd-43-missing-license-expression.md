### Missing License Expression

It MUST be tested that the license expression is present and set.
A CSAF Validator SHALL differentiate in the error message between the key being present but having no or an empty value and
not being present at all.

The relevant path for this test is:

```
  /document/license_expression
```

*Example 1 (which fails the test):*

```
  "document": {
    // ...
    "lang": "en-US",
    "publisher": {
      // ...
    },
    // ...
  }
```

> The license expression is not defined.

> A tool MAY add the key as a quick fix.
> In such case, the value still needs to be set - either manually or by other means from the tool, e.g. through a given configuration.
