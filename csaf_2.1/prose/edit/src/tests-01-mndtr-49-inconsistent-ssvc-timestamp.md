### Inconsistent SSVC Timestamp

For each vulnerability, it MUST be tested that the each SSVC `timestamp` is earlier than or equal to the `date` of the newest item of the
`revision_history` if the document status is `final` or `interim`.
As the timestamps might use different timezones, the sorting MUST take timezones into account.

The relevant path for this test is:

```
    /vulnerabilities[]/metrics[]/content/ssvc_v1/timestamp
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
  // ...
  "vulnerabilities": [
    {
      "cve": "CVE-1900-0001",
      "metrics": [
        {
          "content": {
            "ssvc_v1": {
              "id": "CVE-1900-0001",
              "schemaVersion": "1-0-1",
              "selections": [
                {
                  "name": "Exploitation",
                  "namespace": "ssvc",
                  "values": [
                    "Active"
                  ],
                  "version": "1.1.0"
                }
              ],
              "timestamp": "2024-07-13T10:00:00.000Z"
            }
          },
          // ...
        }
      ]
    }
  ]
```

> The document is in status `final` but the SSVC `timestamp` is newer than the `date` of newest item in the `revision_history`.
