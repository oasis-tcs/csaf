### Missing CVSS v4.0

For each item in the list of metrics that contains any CVSS object it MUST be tested that a `cvss_v4` object is present.
The test MUST fail, if any Product ID (type `/$defs/product_id_t`) in the product status group Affected (see section [sec](#vulnerabilities-property-product-status)) is not covered by
any CVSS object.

The relevant path for this test is:

```
    /vulnerabilities[]/metrics[]/content
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
          },
          "products": [
            "CSAFPID-9080700"
          ]
        }
      ]
    }
  ]
```

> There is no CVSS v4.0 score given for `CSAFPID-9080700`.
