### Use of Short Hash

It MUST be tested that the length of the hash value is not shorter than 64 characters.

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/product/product_identification_helper/hashes[]/file_hashes[]/value
  /product_tree/full_product_names[]/product_identification_helper/hashes[]/file_hashes[]/value
  /product_tree/relationships[]/full_product_name/product_identification_helper/hashes[]/file_hashes[]/value
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
                  "algorithm": "md4",
                  "value": "3202b50e2e5b2fcd75e284c3d9d5f8d6"
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

> The length of the hash value is only 32 characters long.
