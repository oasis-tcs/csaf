### Mixed Integer and Semantic Versioning

It MUST be tested that all elements of type `/$defs/version_t` follow either integer versioning or
semantic versioning homogeneously within the same document.

The relevant paths for this test are:

```
  /document/tracking/revision_history[]/number
  /document/tracking/version
```

*Example 1 (which fails the test):*

```
    "tracking": {
      // ...
      "revision_history": [
        {
          "date": "2024-01-21T09:00:00.000Z",
          "number": "1.0.0",
          "summary": "Initial version."
        },
        {
          "date": "2024-01-21T10:00:00.000Z",
          "number": "2",
          "summary": "Second version."
        }
      ],
      // ...
      "version": "2"
    }
```

> The document started with semantic versioning (`1.0.0`) and switched to integer versioning (`2`).

> A tool MAY assign all items their corresponding value according to integer versioning as a quick fix.
> In such case, the old `number` SHOULD be stored in `legacy_version`.
