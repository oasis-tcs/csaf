### Unused Definition of Product ID

For each Product ID (type `/$defs/product_id_t`) in Full Product Name elements (type: `/$defs/full_product_name_t`) it MUST be tested that
the `product_id` is referenced somewhere within the same document.

This test SHALL be skipped for CSAF documents conforming the profile "Informational Advisory".

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/product/product_id
  /product_tree/full_product_names[]/product_id
  /product_tree/relationships[]/full_product_name/product_id
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
  }
```

> `CSAFPID-9080700` was defined but never used.

> A tool MAY remove the unused definition as quick fix. However, such quick fix shall not be applied if the test was skipped.
