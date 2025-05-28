### Missing License Expression

It MUST be tested that the license expression is present and set.

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
