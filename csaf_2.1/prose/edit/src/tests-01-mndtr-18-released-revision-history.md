### Released Revision History

It MUST be tested that no item of the revision history has a `number` of `0` or `0.y.z` when the document status is `final` or `interim`.

The relevant path for this test is:

```
    /document/tracking/revision_history[]/number
```

*Example 1 (which fails the test):*

```
    "tracking": {
      // ...
      "revision_history": [
        {
          "date": "2023-09-17T10:00:00.000Z",
          "number": "0",
          "summary": "First draft"
        },
        {
          "date": "2024-01-21T10:00:00.000Z",
          "number": "1",
          "summary": "Initial version."
        }
      ],
      "status": "final",
      "version": "1"
    }
```

> The document status is `final` but the revision history includes an item which has `0` as value for `number`.
