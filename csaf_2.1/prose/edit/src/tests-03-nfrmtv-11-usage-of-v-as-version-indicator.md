### Usage of V as Version Indicator

For each element of type `/$defs/branches_t` with `category` of `product_version` it MUST be tested that
the value of `name` does not start with `v` or `V` before the version.

> To implement this test it is deemed sufficient that the value of `name` does not match the following regex:
>
> ```
>   ^[vV][0-9].*$
> ```

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/name
```

*Example 1 (which fails the test):*

```
            "branches": [
              {
                "category": "product_version",
                "name": "v4.2",
                // ...
              }
            ]
```

> The product version starts with a `v`.
