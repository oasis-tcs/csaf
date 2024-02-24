### purl

It MUST be tested that given purl is valid.

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/product/product_identification_helper/purl
  /product_tree/full_product_names[]/product_identification_helper/purl
  /product_tree/relationships[]/full_product_name/product_identification_helper/purl
```

*Example 1 (which fails the test):*

```
  "product_tree": {
    "full_product_names": [
      {
        "name": "Product A",
        "product_id": "CSAFPID-9080700",
        "product_identification_helper": {
          "purl": "pkg:maven/@1.3.4"
        }
      }
    ]
  }
```

> Any valid purl has a name component.
