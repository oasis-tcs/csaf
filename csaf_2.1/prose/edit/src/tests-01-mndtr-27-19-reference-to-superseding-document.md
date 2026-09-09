#### Reference to Superseding Document

If the document language is English or unspecified, it SHALL be tested that at least one item in document references exists
that has a summary starting with `Superseding Document`.
For each of these items, the `category` SHALL be present and have the value `external`.

The relevant value for `$.document.category` is:

```
  csaf_superseded
```

The relevant path for this test is:

```list-of-jsonpaths
  $.document.references
```

*Example 1 (which fails the test):*

```
    "references": [
      {
        "category": "external",
        "summary": "Superseded Document",
        "url": "https://example.com/.well-known/csaf/clear/2024/esa-2024-1234.json"
      }
    ],
```

> There is no reference where the `summary` starts with the correct term `Superseding Document`.
