### Circular Definition of Product ID

For each new defined Product ID (type `/$defs/product_id_t`) in items of relationships (`/product_tree/relationships`) it
MUST be tested that the `product_id` does not end up in a circle.

The relevant path for this test is:

```
  /product_tree/relationships[]/full_product_name/product_id
```

> As this can be quite complex a program for large CSAF documents, a program could check first whether
> a Product ID defined in a relationship item is used as `product_reference` or `relates_to_product_reference`.
> Only for those which fulfill this condition it is necessary to run the full check following the references.

*Example 51 which fails the test:*

```
  "product_tree": {
    "full_product_names": [
      {
        "product_id": "CSAFPID-9080700",
        "name": "Product A"
      }
    ],
    "relationships": [
      {
        "category": "installed_on",
        "full_product_name": {
          "name": "Product B",
          "product_id": "CSAFPID-9080701"
        },
        "product_reference": "CSAFPID-9080700",
        "relates_to_product_reference": "CSAFPID-9080701"
      }
    ]
  }
```

> `CSAFPID-9080701` refers to itself - this is a circular definition.
