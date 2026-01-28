### Use of CVSS and Qualitative Severity Rating

For each item in `/vulnerabilities` it MUST be tested that no Qualitative Severity Rating and CVSS values are listed for the tuple of Product ID
and source.

> Different source might assign different metrics for the same product.

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
            "cvss_v3": {
              // ...
            }
          },
          "products": [
            "CSAFPID-9080700"
          ]
        },
        {
          "content": {
            "qualitative_severity_rating": "critical"
          },
          "products": [
            "CSAFPID-9080700"
          ]
        }
      ]
    }
  ]
```

> A CVSS v3.1 score and a Qualitative Severity Rating is given for `CSAFPID-9080700` by the document author.

> A tool MAY remove the `qualitative_severity_rating` as a quick fix.
