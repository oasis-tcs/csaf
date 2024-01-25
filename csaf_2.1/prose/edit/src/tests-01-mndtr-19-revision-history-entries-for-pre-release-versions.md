### Revision History Entries for Pre-release Versions

It MUST be tested that no item of the revision history has a `number` which includes pre-release information.

The relevant path for this test is:

```
    /document/tracking/revision_history[]/number
```

*Example 1 (which fails the test):*

```
    "revision_history": [
      {
        "date": "2023-08-22T10:00:00.000Z",
        "number": "1.0.0-rc",
        "summary": "Release Candidate for initial version."
      },
      {
        "date": "2023-08-23T10:00:00.000Z",
        "number": "1.0.0",
        "summary": "Initial version."
      }
    ]
```

> The revision history contains an item which has a `number` that indicates that this is pre-release.
