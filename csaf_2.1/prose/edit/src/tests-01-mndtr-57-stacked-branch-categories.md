### Stacked Branch Categories

For each `full_product_name_t` element under `/product_tree/branches`, it MUST be tested that branch categories used along the path
leading to the `full_product_name_t` element appear only once in the path.
The sole exception is `product_family` which can occur multiple times.
Therefore, `product_family` MUST be ignored in the test.

The relevant path for this test is:

```
    /product_tree/branches[](/branches[])*/category
```

*Example 1 (which fails the test):*

```
  "product_tree": {
    "branches": [
      {
        "branches": [
          {
            // ...
            "category": "vendor",
            "name": "ISDuBA"
          }
        ],
        "category": "vendor",
        "name": "Open Source"
      }
    ]
  }
```

> The category `vendor` was used twice along the path.

> A tool MAY collapse the stacked branch categories as a quick fix, if applicable.
