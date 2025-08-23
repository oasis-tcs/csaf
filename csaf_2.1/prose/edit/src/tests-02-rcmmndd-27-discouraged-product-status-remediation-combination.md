### Discouraged Product Status Remediation Combination

For each item in `/vulnerabilities[]/remediations`, it MUST be tested that a Product is not member of a discouraged product status group
remediation category combination (see table [tab](#vulnerabilities-property-remediations-category-tab-2)).
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
          "category": "fix_planned",
          "details": "The fix should be available in Q4 2024.",
          "product_ids": [
            "CSAFPID-9080700"
          ]
        }
      ]
```

> For the product with product ID `CSAFPID-908070` a fix is planned but the product was not affected at all.
