### Use of Qualitative Severity Rating by Issuing Party

For each item in `metrics` provided by the issuing party it MUST be tested that it does not use the qualitative severity rating.

> This covers all items in `metrics` that do not have a `source` property and those where the `source` is equal to
> the canonical URL.
> It does not cover assessments made by third parties.

The relevant path for this test is:

```
    /vulnerabilities[]/metrics[]
```

*Example 1 (which fails the test):*

```
  "product_tree": {
    "full_product_names": [
      {
        "product_id": "CSAFPID-9080700",
        "name": "Product A"
      }
    ]
  },
  "vulnerabilities": [
    {
      "metrics": [
        {
          "content": {
            "qualitative_severity_rating": "low"
          },
          "products": [
            "CSAFPID-9080700"
          ]
        }
      ]
    }
  ]
```

> The document issuer provided metric for `CSAFPID-9080700` uses a `qualitative_severity_rating`.

> A tool MAY recommend other metrics or guide a CVSS assessment.
