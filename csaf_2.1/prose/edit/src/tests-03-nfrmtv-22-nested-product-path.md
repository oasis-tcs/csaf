### Nested Product Path

For each item in `/product_tree/product_paths[]` it MUST be tested that all referenced Product IDs are not defined under a
`full_product_name_t` element within items of `/product_tree/product_paths`.

> A product defined by a product path that contains another product path is usually harder to match.
> Nevertheless, there are scenarios that require such a nesting to correctly describe the reality
> or provide additional matching information.

The relevant paths for this test are:

```
  /product_tree/product_paths[]/beginning_product_reference
  /product_tree/product_paths[]/subpaths[]/next_product_reference
```

*Example 1 (which fails the test):*

```
  "product_tree": {
    "full_product_names": [
      {
        "name": "Product A",
        "product_id": "CSAFPID-908070601"
      },
      {
        "name": "Product B",
        "product_id": "CSAFPID-908070602"
      },
      {
        "name": "Product C",
        "product_id": "CSAFPID-908070603"
      }
    ],
    "product_paths": [
      {
        "beginning_product_reference": "CSAFPID-908070601",
        "full_product_name": {
          "name": "Product A installed on Product B",
          "product_id": "CSAFPID-908070604"
        },
        "subpaths": [
          {
            "category": "installed_on",
            "next_product_reference": "CSAFPID-908070602"
          }
        ]
      }
      {
        "beginning_product_reference": "CSAFPID-908070604",
        "full_product_name": {
          "name": "Product A installed on Product B installed on Product C",
          "product_id": "CSAFPID-908070605"
        },
        "subpaths": [
          {
            "category": "installed_on",
            "next_product_reference": "CSAFPID-908070603"
          }
        ]
      }
    ]
  }
```

> The Product with the ID `CSAFPID-908070605` is defined through a product reference which belongs to a product formed by a product path.
