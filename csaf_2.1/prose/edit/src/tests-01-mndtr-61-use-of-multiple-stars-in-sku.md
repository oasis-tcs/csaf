### Use of Multiple Stars in SKU

For each stock keeping unit it MUST be tested that the it does not contain multiple unescaped stars.

> Multiple `*` that match zero or multiple characters within a model number introduce ambiguity and are therefore prohibited.

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/product/product_identification_helper/skus[]
  /product_tree/full_product_names[]/product_identification_helper/skus[]
  /product_tree/product_paths[]/full_product_name/product_identification_helper/skus[]
```

*Example 1 (which fails the test):*

```
          "skus": [
            "NL*12*"
          ]
```

> The stock keeping unit contains two unescaped stars.
