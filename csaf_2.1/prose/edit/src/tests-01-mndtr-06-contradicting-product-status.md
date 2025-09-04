### Contradicting Product Status

For each item in `/vulnerabilities` it MUST be tested that the same Product ID is not a member of contradicting
product status groups (see section [sec](#vulnerabilities-property-product-status)).
The sets formed by the contradicting groups within one vulnerability item MUST be pairwise disjoint.

The relevant path for this test is:

```
    /vulnerabilities[]/product_status
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
      "product_status": {
        "known_affected": [
          "CSAFPID-9080700"
        ],
        "known_not_affected": [
          "CSAFPID-9080700"
        ]
      }
    }
  ]
```

> `CSAFPID-9080700` is a member of the two contradicting groups "Affected" and "Not affected".
