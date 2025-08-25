### Use of MD5 As the Only Hash Algorithm

It MUST be tested that the hash algorithm `md5` is not the only one present.

> Since collision attacks exist for MD5 such value should be accompanied by a second cryptographically stronger hash.
> This will allow users to double check the results.

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/product/product_identification_helper/hashes[]/file_hashes
  /product_tree/full_product_names[]/product_identification_helper/hashes[]/file_hashes
  /product_tree/relationships[]/full_product_name/product_identification_helper/hashes[]/file_hashes
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
                  "algorithm": "md5",
                  "value": "6ae24620ea9656230f49234efd078935"
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

> The hash algorithm `md5` is used in one item of hashes without being accompanied by a second hash algorithm.
