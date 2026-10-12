### Inconsistent Hash Value Length

For each file hash object, it SHALL be tested that the `value` length aligns with the `algorithm`.
The test SHALL be skipped for algorithms with variable length output.
Algorithms not supported by the implementation SHALL result in a warning which SHALL include the value of `algorithm`.
The warning SHALL differentiate between the values mentioned in section [sec](#full-product-name-type---product-identification-helper---hashes)
and those not mentioned there.

The relevant paths for this test are:

```list-of-jsonpaths
  $.product_tree..branches[*].product.product_identification_helper.hashes[*].file_hashes[*]
  $.product_tree.full_product_names[*].product_identification_helper.hashes[*].file_hashes[*]
  $.product_tree.product_paths[*].full_product_name.product_identification_helper.hashes[*].file_hashes[*]
```

*Example 1 (which fails the test):*

```
  "product_tree": {
    "full_product_names": [
      {
        "name": "Product A",
        "product_id": "CSAFPID-9080700",
        "product_identification_helper": {
          "hashes": [
            {
              "file_hashes": [
                {
                  "algorithm": "sha256",
                  "value": "026a37919b182ef7c63791e82c9645e2f897a3f0b73c7a6028c7febf62e93838d0143"
                }
              ],
              "filename": "product_a.so"
            }
          ]
        }
      }
    ]
  }
```

> The hash claims to be an MD4 but its length (69 characters) is longer than the expected length (64 characters).
