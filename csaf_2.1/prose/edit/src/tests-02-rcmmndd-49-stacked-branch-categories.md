### Stacked Branch Categories

For each path to a `full_product_name_t`element starting at `/product_tree/branches` it MUST be tested that categories used
appear only once along the path.
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
