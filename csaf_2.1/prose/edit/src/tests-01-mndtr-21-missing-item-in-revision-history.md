### Missing Item in Revision History

It MUST be tested that items of the revision history do not omit a version number when the items are sorted ascending by `date`.
In the case of semantic versioning, this applies only to the Major version.
It MUST also be tested that the first item in such a sorted list has either the version number 0 or 1 in the case of integer versioning or
a Major version of 0 or 1 in the case of semantic versioning.

The relevant path for this test is:

```
    /document/tracking/revision_history
```

*Example 1 (which fails the test):*

```
    "revision_history": [
      {
        "date": "2023-08-22T10:00:00.000Z",
        "number": "1",
        "summary": "Initial version."
      },
      {
        "date": "2024-01-21T10:00:00.000Z",
        "number": "3",
        "summary": "Some other changes."
      }
    ]
```

> The item for version `2` is missing.
