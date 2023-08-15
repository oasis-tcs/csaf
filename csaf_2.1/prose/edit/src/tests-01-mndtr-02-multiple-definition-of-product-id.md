### Multiple Definition of Product ID

For each Product ID (type `/$defs/product_id_t`) in Full Product Name elements (type: `/$defs/full_product_name_t`) it
MUST be tested that the `product_id` was not already defined within the same document.

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/product/product_id
  /product_tree/full_product_names[]/product_id
  /product_tree/relationships[]/full_product_name/product_id
```

*Example 50 which fails the test:*

```
  "product_tree": {
    "full_product_names": [
      {
        "product_id": "CSAFPID-9080700",
        "name": "Product A"
      },
      {
        "product_id": "CSAFPID-9080700",
        "name": "Product B"
      }
    ]
  }
```

> `CSAFPID-9080700` was defined twice.
