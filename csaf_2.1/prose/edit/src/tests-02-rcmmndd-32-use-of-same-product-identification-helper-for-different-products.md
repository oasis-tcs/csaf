### Use of same Product Identification Helper for different Products

For each Product Identification Helper category it MUST be tested that the same value is not used for multiple products in this category.

> This test detects a potentially incorrect constructed product tree.
> Note: This test will fail if the CSAF document contains in its `product_tree` the old and new name of a product that was renamed.
> However, this is expected and considered a good reason for the test to fail.
> This does not make the CSAF document invalid.
>
> For the comparison, arrays need to be treated as unordered sets which need to be pairwise disjoint.
> When comparing two helper-objects' array properties whose items are themselves JSON objects (e.g. `hashes` or `file_hashes`),
> the array needs to be treated as an unordered set, and each object is compared by deep-equality of its key/value pairs (ignoring key‐order).

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/product/product_identification_helper
  /product_tree/full_product_names[]/product_id/product_identification_helper
  /product_tree/relationships[]/full_product_name/product_id/product_identification_helper
```

*Example 1 (which fails the test):*

```
  "product_tree": {
    "branches": [
      {
        "branches": [
          {
            "branches": [
              {
                "category": "product_version",
                "name": "1.0",
                "product": {
                  "name": "Example Company Product A 1.0",
                  "product_id": "CSAFPID-908070601",
                  "product_identification_helper": {
                    "serial_numbers": [
                      "143-D-354"
                    ]
                  }
                }
              },
              {
                "category": "product_version",
                "name": "2.0",
                "product": {
                  "name": "Example Company Product A 2.0",
                  "product_id": "CSAFPID-908070602",
                  "product_identification_helper": {
                    "serial_numbers": [
                      "143-D-354"
                    ]
                  }
                }
              }
            ],
            "category": "product_name",
            "name": "Product A"
          }
        ],
        "category": "vendor",
        "name": "Example Company"
      }
    ]
  }
```

> Both products are identified by the same serial number `143-D-354`.
