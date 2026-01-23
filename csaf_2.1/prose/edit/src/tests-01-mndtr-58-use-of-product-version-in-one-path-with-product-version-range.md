### Use of `product_version` in one Path with `product_version_range`

For each `full_product_name_t` element under `/product_tree/branches`, it MUST be tested that only one of the branch categories
`product_version` and `product_version_range` is used along the path leading to the `full_product_name_t` element.

The relevant path for this test is:

```
    /product_tree/branches[](/branches[])*/category
```

*Example 1 (which fails the test):*

```
    {
      "branches": [
        {
          "category": "product_version_range",
          "name": "vers:intdot/<1.1.1",
          "product": {
            // ...
          }
        }
      ],
      "category": "product_version",
      "name": "1.1"
    },       
```

> Both categories `product_version` and `product_version_range` were used along the path.

> A tool MAY convert the `product_version` into the `product_name` element which contains the value of the `product_version`
> appended to the original product name as a quick fix, if applicable.
> In such conversion, a tool MAY convert a previously existing `product_name` element into a `product_family`, if applicable.
