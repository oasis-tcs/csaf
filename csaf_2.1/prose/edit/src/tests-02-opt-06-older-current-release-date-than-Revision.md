### Older Current Release Date than Revision History

It MUST be tested that the Current Release Date is not older than the `date` of the newest item in Revision History.
As the timestamps might use different timezones, the sorting and comparison MUST take timezones into account.

The relevant path for this test is:

```
    /document/tracking/current_release_date
```

*Example 1 (which fails the test):*

```
    "tracking": {
      "current_release_date": "2023-09-06T10:00:00.000Z",
      // ...
      "revision_history": [
        {
          "date": "2023-09-06T10:00:00.000Z",
          "number": "1",
          "summary": "Initial version."
        },
        {
          "date": "2024-01-21T11:00:00.000Z",
          "number": "2",
          "summary": "Second version."
        }
      ],
      // ...
    }
```

> The current release date `2023-09-06T10:00:00.000Z` is older than `2023-09-23T1100:00.000Z` which is the `date` of
> the newest item in Revision History.
