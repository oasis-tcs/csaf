### Same Timestamps in Revision History

It MUST be tested that the timestamps of all items in the revision history are pairwise disjoint.
As the timestamps might use different timezones, the comparison MUST take timezones into account.

The relevant path for this test is:

```
  /document/tracking/revision_history[]/date
```

*Example 1 (which fails the test):*

```
  "revision_history": [
    {
      "date": "2024-01-21T10:00:00.000Z",
      "number": "2.0.0",
      "summary": "Second version."
    },
    {
      "date": "2024-01-21T10:00:00.000Z",
      "number": "1.0.0",
      "summary": "Initial version."
    }
  ]
```

> The first and second revision have the same timestamp.
