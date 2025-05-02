### Missing Product Identification Helper

For each element of type `/$defs/full_product_name_t` it MUST be tested that it includes the property `product_identification_helper`.

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/product
  /product_tree/full_product_names[]
  /product_tree/relationships[]/full_product_name
```

*Example 1 (which fails the test):*

```
    "full_product_names": [
      {
        "product_id": "CSAFPID-9080700",
        "name": "Product A"
      }
    ]
```

> The product `CSAFPID-9080700` does not provide any Product Identification Helper at all.
