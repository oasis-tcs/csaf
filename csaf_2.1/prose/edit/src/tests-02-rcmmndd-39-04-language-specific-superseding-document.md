#### Language Specific Superseding Document

If the document language is specified but not English, it MUST be tested that at least one item in document references exists
that starts with the language specific translation of the term `Superseding Document` as `summary`.
The `category` of this item MUST be `external`.
If no language specific translation has been recorded, the test MUST be skipped and output an information to the user that no such translation is known.

> A list of the language specific translations is kept at the OASIS CSAF TC.

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
        "summary": "Ersetztes Dokument",
        "url": "https://example.com/.well-known/csaf/clear/2024/esa-2024-1234.json"
      }
    ],
```

> The note has the correct title. However, it uses the wrong category.
