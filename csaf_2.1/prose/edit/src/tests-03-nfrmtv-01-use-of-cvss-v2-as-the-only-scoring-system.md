### Use of CVSS v2 As the Only Scoring System

For each item in the list of metrics which contains the `cvss_v2` object under `content` it MUST be tested that is not the only scoring item present.
The test SHALL pass if a second scoring object is available regarding the specific product.

> One source might just provide CVSS v2.
> As long as at least one different source provides a different scoring system for the same products, the test passes.

The relevant path for this test is:

```
    /vulnerabilities[]/metrics
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
            "cvss_v2": {
              "version": "2.0",
              "vectorString": "AV:N/AC:L/Au:N/C:C/I:C/A:C",
              "baseScore": 10
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

> There is only a CVSS v2 score given for `CSAFPID-9080700`.

Recommendation:

It is recommended to (also) use the CVSS v4.0.
