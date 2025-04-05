### Missing Document Language

It MUST be tested that the document language is present and set.

The relevant path for this test is:

```
  /document/lang
```

*Example 1 (which fails the test):*

```
  "document": {
    "category": "csaf_base",
    "csaf_version": "2.1",
    "distribution": {
      "tlp": {
        "label": "CLEAR"
      }
    },
    "publisher": {
      // ...
    },
    // ...
  }
```

> The document language is not defined.
