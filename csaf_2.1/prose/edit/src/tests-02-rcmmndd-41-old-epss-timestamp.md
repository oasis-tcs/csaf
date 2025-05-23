### Old EPSS Timestamp

For each vulnerability, it MUST be tested that the youngest EPSS `timestamp` is not more than 15 days older than to the `date` of the newest item of the
`revision_history` if the document status is `final` or `interim`.
As the timestamps might use different timezones, the sorting MUST take timezones into account.

The relevant path for this test is:

```
    /vulnerabilities[]/metrics[]/content/epss/timestamp
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
      "cve": "CVE-1900-0001",
      "metrics": [
        {
          "content": {
            "epss": {
              "percentile": "0.999990000",
              "probability": "0.975570000",
              "timestamp": "2024-07-13T10:00:00.000Z"
            }
          },
          "products": [
            "CSAFPID-9080700"
          ]
        }
      ]
    }
  ]
```

> The document is in status `final` but the EPSS `timestamp` is more than 15 days older than the `date` of newest item in the `revision_history`.
