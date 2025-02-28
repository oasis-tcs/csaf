### Inconsistent Disclosure Date

For each vulnerability, it MUST be tested that the `disclosure_date` is not newer than the `date` of the newest item of the `revision_history`
if the document is labeled `TLP:CLEAR` and the document status is `final` or `interim`.
As the timestamps might use different timezones, the sorting MUST take timezones into account.

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
        "label": "CLEAR"
      }
    },
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
      "disclosure_date": "2024-02-24T10:00:00.000Z"
    }
  ]
```

> The document is labeled `TLP:CLEAR` and in status `final` but the `disclosure_date` is newer than the date of newest item in the `revision_history`.
