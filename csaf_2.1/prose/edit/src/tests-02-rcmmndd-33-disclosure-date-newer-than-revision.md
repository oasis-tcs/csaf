### Disclosure Date Newer than Revision History

For each vulnerability, it MUST be tested that the `disclosure_date` is earlier or equal to the `date` of the newest item of the `revision_history`
if the `disclosure_date` is in the past at the time of the test execution.
As the timestamps might use different timezones, the sorting MUST take timezones into account.

> The result of the test is dependent upon the time of the execution of the test - it might change for a given CSAF document over time.
> However, the latest version of a CSAF document should always pass the test.

The relevant path for this test is:

```
    /vulnerabilities[]/disclosure_date
```

*Example 1 (which fails the test):*

```
  "document": {
    // ...
    "distribution": {
      "tlp": {
        "label": "GREEN"
      }
    },
    // ...
    "tracking": {
      "current_release_date": "2024-01-24T10:00:00.000Z",
      // ...
      "initial_release_date": "2024-01-24T10:00:00.000Z",
      "revision_history": [
        {
          "date": "2024-01-24T10:00:00.000Z",
          "number": "1",
          "summary": "Initial version."
        }
      ],
      "status": "final",
      "version": "1"
    }
  },
  "vulnerabilities": [
    {
      "disclosure_date": "2024-02-24T10:00:00.000Z"
    }
  ]
```

> The `disclosure_date` is in the past but newer than the date of newest item in the `revision_history`.
