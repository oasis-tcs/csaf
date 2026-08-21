#### Reference to Superseding Document

If the document language is English or unspecified, it MUST be tested that at least one item in document references exists
that has a summary starting with `Superseding Document`.
The `category` of this item MUST be `external`.

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
        "category": "self",
        "summary": "Superseding Document",
        "url": "https://example.com/.well-known/csaf/clear/2024/esa-2024-1234.json"
      }
    ],
```

> The reference summary starts correctly with the string "Superseding Document". However, it uses the wrong category.
