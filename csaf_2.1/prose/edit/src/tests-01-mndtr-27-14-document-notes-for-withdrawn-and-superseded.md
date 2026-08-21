#### Document Notes{#document-notes-for-withdrawn-and-superseded}

It MUST be tested that at least one item in `$.document.notes` exists which has a `category` of `description`.

The relevant values for `$.document.category` are:

```
  csaf_withdrawn
  csaf_superseded
```

The relevant path for this test is:

```list-of-jsonpaths
  $.document.notes
```

*Example 1 (which fails the test):*

```
  "notes": [
    {
      "category": "legal_disclaimer",
      "text": "The CSAF document is provided to You \"AS IS\" and \"AS AVAILABLE\" and with all faults and defects without warranty of any kind.",
      "title": "Terms of Use"
    }
  ]
```

> The document notes do not contain an item which has a `category` of `description`.
