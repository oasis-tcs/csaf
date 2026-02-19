### Branch Categories

For each element of type `/$defs/full_product_name_t` in `/product_tree/branches` it MUST be tested that
ancestor nodes along the path exist which use the following branch categories `vendor` -> `product_name` -> `product_version` in that
order starting with the Product tree node.

> Other branch categories can be used before, after or between the aforementioned branch categories without making the test invalid.

The relevant paths for this test are:

```
  /product_tree/branches
```

*Example 1 (which fails the test):*

```
    "branches": [
      {
        "category": "vendor",
        "name": "Example Company",
        "branches": [
          {
            "category": "product_name",
            "name": "Product A",
            "branches": [
              {
                "category": "patch_level",
                "name": "91",
                "product": {
                  "product_id": "CSAFPID-0002",
                  "name": "Example Company Product A Update 91"
                }
              }
            ]
          }
        ]
      }
    ]
```

> The product `CSAFPID-9080700` does not have any ancestor with the branch category `product_version`.
