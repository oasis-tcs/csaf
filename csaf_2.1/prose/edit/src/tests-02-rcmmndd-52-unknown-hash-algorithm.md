### Unknown Hash Algorithm

For each element of type `/$defs/full_product_name_t/product_identification_helper/hashes[]/file_hashes[]/algorithm`,
it MUST be tested that the hash algorithm is supported by the implementation.
The warning MUST differentiate between the values mentioned in section [sec](#full-product-name-type-product-identification-helper-hashes)
and those not mentioned there.

> Different implementations might support different hash algorithms.
> Usually, unknown hash algorithms might hinder the automated matching of hashes.
> However, it is expected that the test is able to recognize all algorithms mentioned in the standard.
> The differentiation will help users analyzing the result of the test and addressing the issue appropriately.  

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/product/product_identification_helper/hashes[]/file_hashes[]/algorithm
  /product_tree/full_product_names[]/product_identification_helper/hashes[]/file_hashes[]/algorithm
  /product_tree/relationships[]/full_product_name/product_identification_helper/hashes[]/file_hashes[]/algorithm
```

*Example 1 (which fails the test):*

```
  {
    "algorithm": "unknown-algorithm",
    "value": "026a37919b182ef7c63791e82c9645e2f897a3f0b73c7a6028c7febf62e93838"
  }
```

> The hash algorithm `sunknown-algorithm` is not mentioned in section [sec](#full-product-name-type-product-identification-helper-hashes).
> Note: An implementation would also have to state whether it supports this algorithm.
