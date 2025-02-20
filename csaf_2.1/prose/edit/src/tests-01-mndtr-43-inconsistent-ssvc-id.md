### Inconsistent SSVC ID

For each `ssvc_v1` object it MUST be tested that `id` is either the CVE of the vulnerability given in `cve` or the `text` of an item in the `ids` array.
The test MUST fail, if the `id` equals the `/document/tracking/id` and the CSAF document contains more than one vulnerability.

The relevant paths for this test are:

```
   /vulnerabilities[]/metrics[]/content/ssvc_v1/id
```

*Example 1 (which fails the test):*

```
  "vulnerabilities": [
    {
      "cve": "CVE-1900-0001",
      "metrics": [
        {
          "content": {
            "ssvc_v1": {
              "id": "CVE-1900-0002",
              "schemaVersion": "1-0-1",
              "selections": [
                {
                  "name": "Exploitation",
                  "namespace": "ssvc",
                  "values": [
                    "None"
                  ],
                  "version": "1.1.0"
                }
              ],
              "timestamp": "2024-01-24T10:00:00.000Z"
            }
          },
          // ...
        }
      ]
    }
  ]
```

> The SSVC ID does not match the CVE ID.
