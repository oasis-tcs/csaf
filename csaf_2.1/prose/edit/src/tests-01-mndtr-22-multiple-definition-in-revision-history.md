### Multiple Definition in Revision History

It MUST be tested that items of the revision history do not contain the same version number.

The relevant path for this test is:

```
    /document/tracking/revision_history
```

*Example 1 (which fails the test):*

```
   "revision_history": [
      {
        "date": "2021-07-20T10:00:00.000Z",
        "number": "1",
        "summary": "Initial version."
      },
      {
        "date": "2021-07-21T10:00:00.000Z",
        "number": "1",
        "summary": "Some other changes."
      }
    ]
```

> The revision history contains two items with the version number `1`.
