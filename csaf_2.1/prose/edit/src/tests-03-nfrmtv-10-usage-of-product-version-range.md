### Usage of Product Version Range

For each element of type `/$defs/branches_t` it MUST be tested that the `category` is not `product_version_range`.

> It is usually hard decide for machines whether a product version matches a product version ranges.
> Therefore, it is recommended to avoid version ranges and enumerate versions wherever possible.

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/category
```

*Example 1 (which fails the test):*

```
                "category": "product_version_range",
```

> The category `product_version_range` was used.
