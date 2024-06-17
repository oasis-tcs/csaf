### Sorted Revision History

It MUST be tested that the value of `number` of items of the revision history are sorted ascending when the items are sorted
ascending by `date` and as a second level criteria `number`.
As the timestamps might use different timezones, the sorting MUST take timezones into account.

The relevant path for this test is:

```
    /document/tracking/revision_history
```

*Example 1 (which fails the test):*

```
  "revision_history": [
    {
      "date": "2024-01-22T10:00:00.000Z",
      "number": "2",
      "summary": "Second version."
    },
    {
      "date": "2024-01-23T10:00:00.000Z",
      "number": "1",
      "summary": "Initial version."
    }
  ]
```

> The first item has a higher version number than the second.
