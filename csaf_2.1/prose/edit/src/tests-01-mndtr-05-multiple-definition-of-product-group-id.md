### Multiple Definition of Product Group ID

For each Product Group ID (type `/$defs/product_group_id_t`) Product Group elements (`/product_tree/product_groups[]`) it
MUST be tested that the `group_id` was not already defined within the same document.

The relevant path for this test is:

```
    /product_tree/product_groups[]/group_id
```

*Example 1 (which fails the test):*

```
  "product_tree": {
    "full_product_names": [
      {
        "product_id": "CSAFPID-9080700",
        "name": "Product A"
      },
      {
        "product_id": "CSAFPID-9080701",
        "name": "Product B"
      },
      {
        "product_id": "CSAFPID-9080702",
        "name": "Product C"
      }
    ],
    "product_groups": [
      {
        "group_id": "CSAFGID-1020300",
        "product_ids": [
          "CSAFPID-9080700",
          "CSAFPID-9080701"
        ]
      },
      {
        "group_id": "CSAFGID-1020300",
        "product_ids": [
          "CSAFPID-9080700",
          "CSAFPID-9080702"
        ]
      }
    ]
  }
```

> `CSAFGID-1020300` was defined twice.
