### Inconsistent SSVC Target IDs

For each `ssvc_v2` object it MUST be tested that each item in `target_ids` is either the CVE of the vulnerability given in `cve`
or the `text` of an item in the `ids` array of the vulnerability.
The test MUST fail, if the target ID equals the `/document/tracking/id` and the CSAF document contains more than one vulnerability.

The relevant path for this test is:

```
   /vulnerabilities[]/metrics[]/content/ssvc_v2/target_ids[]
```

*Example 1 (which fails the test):*

```
  "vulnerabilities": [
    {
      "cve": "CVE-1900-0001",
      "metrics": [
        {
          "content": {
            "ssvc_v2": {
              // ...
              "target_ids": [
                "CVE-1900-0002"
              ],
              // ...
            }
          },
          // ...
        }
      ]
    }
  ]
```

> The SSVC Target ID does not match the CVE ID.

> A tool MAY remove any inconsistent SSVC Target ID as a quick fix.

If the tool removes the last item of the array, it MUST remove the element `target_ids` as well.
