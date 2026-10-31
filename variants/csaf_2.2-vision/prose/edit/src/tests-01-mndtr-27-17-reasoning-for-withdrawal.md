#### Reasoning for Withdrawal

If the document language is English or unspecified, it SHALL be tested that exactly one item in document notes exists
that has the title `Reasoning for Withdrawal`.
The `category` of this item SHALL be `description`.

The relevant value for `$.document.category` is:

```
  csaf_withdrawn
```

The relevant path for this test is:

```list-of-jsonpaths
  $.document.notes
```

*Example 1 (which fails the test):*

```
  "notes": [
    {
      "category": "summary",
      "text": "This CSAF document contained example data and was withdrawn to create test data.",
      "title": "Reasoning for Withdrawal"
    }
  ],
```

> The note has the correct title. However, it uses the wrong category.
