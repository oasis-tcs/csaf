### PURL Qualifiers

For each `product_identification_helper` object containing multiple purls it MUST be tested that the purls only differ in their qualifiers.

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/product/product_identification_helper/purls[]
  /product_tree/full_product_names[]/product_identification_helper/purls[]
  /product_tree/relationships[]/full_product_name/product_identification_helper/purls[]
```

*Example 1 (which fails the test):*

```
  "product_tree": {
    "full_product_names": [
      {
        "name": "Product A",
        "product_id": "CSAFPID-9080700",
        "product_identification_helper": {
          "purls": [
            "pkg:maven/com.example/logging@1.3.4",
            "pkg:maven/com.example/audit@1.3.4"
          ]
        }
      }
    ]
  }
```

> The two purls differ in the name component.
