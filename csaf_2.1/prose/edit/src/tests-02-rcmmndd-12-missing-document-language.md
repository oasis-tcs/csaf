### Missing Document Language

It MUST be tested that the document language member is present and set.
A CSAF Validator SHALL differentiate in the error message between the key being present but having no or an empty value and
not being present at all.

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

> A tool MAY add the key as a quick fix.
> In such case, the value still needs to be set - either manually or by other means from the tool, e.g. through a given configuration.
