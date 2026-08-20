#### Revision History{#revision-history-for-withdrawn-and-superseded}

It MUST be tested that the revision history contains at least two entries.

The relevant values for `$.document.category` are:

```
  csaf_withdrawn
  csaf_superseded
```

The relevant path for this test is:

```list-of-jsonpaths
  $.document.tracking.revision_history
```

*Example 1 (which fails the test):*

```
  "revision_history": [
    {
      "date": "2024-01-24T10:00:00.000Z",
      "number": "1",
      "summary": "Initial version."
    }
  ],
```

> The revision history contains only one entry.
