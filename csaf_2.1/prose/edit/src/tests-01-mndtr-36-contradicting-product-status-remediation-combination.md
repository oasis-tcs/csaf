### Contradicting Product Status Remediation Combination

For each item in `/vulnerabilities[]/remediations` it MUST be tested that a Product is not member of a contradicting product status group.
This takes indirect relations through Product Groups into account.

The relevant path for this test is:

```
  /vulnerabilities[]/remediations[]
```

*Example 1 (which fails the test):*

```
      "product_status": {
        "known_not_affected": [
          "CSAFPID-9080700"
        ]
      },
      "remediations": [
        {
          "category": "vendor_fix",
          "details": "Update to version >=14.3 to fix the vulnerability.",
          "product_ids": [
            "CSAFPID-9080700"
          ]
        }
      ]
```

> For the product with product ID `CSAFPID-908070` a `vendor_fix` is given but the product was not affected at all.
