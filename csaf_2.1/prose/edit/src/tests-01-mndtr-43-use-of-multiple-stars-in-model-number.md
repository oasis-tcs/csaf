### Use of Multiple Stars in Model Number

For each model number it MUST be tested that the it does not contain multiple unescaped stars.

> Multiple `*` that match zero or multiple characters within a model number introduce ambiguity and is therefore prohibited.

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/product/product_identification_helper/model_numbers[]
  /product_tree/full_product_names[]/product_id/product_identification_helper/model_numbers[]
  /product_tree/relationships[]/full_product_name/product_id/product_identification_helper/model_numbers[]
```

*Example 1 (which fails the test):*

```
          "model_numbers": [
            "P*A*"
          ]
```

> The model number contains two unescaped stars.
