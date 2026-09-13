### Inconsistent Discovery Date

For each vulnerability, it SHALL be tested that the `discovery_date` is earlier than or equal to the `date` of the newest item
of the `revision_history` if the document status is `final` or `interim`.
Also, the `discovery_date` SHALL be earlier than or equal to the `disclosure_date` of the same vulnerability.

As the timestamps might use different timezones, the sorting SHALL take timezones into account.

The relevant path for this test is:

```list-of-jsonpaths
  $.vulnerabilities[*].discovery_date
```

*Example 1 (which fails the test):*

```
  "document": {
    // ...
    "tracking": {
      // ...
      "revision_history": [
        {
          "date": "2024-01-24T10:00:00.000Z",
          "number": "1",
          "summary": "Initial version."
        }
      ],
      "status": "final",
      // ...
    }
  },
  "vulnerabilities": [
    {
      "discovery_date": "2024-02-24T10:00:00.000Z"
    }
  ]
```

> The document is in status `final` but the `discovery_date` is newer than the `date` of newest item in the `revision_history`.
