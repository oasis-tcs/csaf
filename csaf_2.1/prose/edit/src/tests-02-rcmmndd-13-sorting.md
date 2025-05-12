### Sorting{#recommended-tests--sorting}

It MUST be tested that all keys in a CSAF document are sorted alphabetically.

The relevant path for this test is:

```
  /
```

*Example 1 (which fails the test):*

```
  "document": {
    "csaf_version": "2.1",
    "category": "csaf_base",
    // ...
  }
```

> The key `csaf_version` is not at the right place.

> A tool MAY sort the keys as a quick fix.
