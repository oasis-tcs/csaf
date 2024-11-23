### Multiple Use of Same Hash Algorithm

It MUST be tested that the same hash algorithm is not used multiple times in one item of hashes.

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/product/product_identification_helper/←
  hashes[]/file_hashes
  /product_tree/full_product_names[]/product_identification_helper/hashes[]/←
  file_hashes
  /product_tree/relationships[]/full_product_name/product_identification_helper/←
  hashes[]/file_hashes
```

  > For the significance of the left pointing arrow character (`←`) at the end of lines in the preceding
  > paths listing and following example 1 please cf. the guidance in section [sec](#typographical-conventions).

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
                  "value": "026a37919b182ef7c63791e82c9645e2f897a3f0b73c7←
                  a6028c7febf62e93838"
                },
                {
                  "algorithm": "sha256",
                  "value": "0a853ce2337f0608489ac596a308dc5b7b19d35a52b10←
                  bf31261586ac368b175"
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

> The hash algorithm `sha256` is used two times in one item of hashes.
