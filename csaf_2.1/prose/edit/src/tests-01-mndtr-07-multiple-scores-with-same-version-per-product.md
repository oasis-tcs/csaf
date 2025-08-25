### Multiple Scores with Same Version per Product

For each item in `/vulnerabilities` it MUST be tested that the same Product ID is not member of more than one CVSS-Vectors with the same version and same source.

> Different source might assign different scores for the same product.

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
              "version": "3.1",
              "vectorString": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H",
              "baseScore": 10,
              "baseSeverity": "CRITICAL"
           }
          }
          "products": [
            "CSAFPID-9080700"
          ]          
        },
        {
          "content": {
            "cvss_v3": {
              "version": "3.1",
              "vectorString": "CVSS:3.1/AV:L/AC:L/PR:H/UI:R/S:U/C:H/I:H/A:H",
              "baseScore": 6.5,
              "baseSeverity": "MEDIUM"
            }
          }
          "products": [
            "CSAFPID-9080700"
          ]          
        }
      ]
    }
  ]
```

> Two CVSS v3.1 scores are given for `CSAFPID-9080700` by the document author.
