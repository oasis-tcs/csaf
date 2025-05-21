### Product Version Range without vers

For each element of type `/$defs/branches_t` with `category` of `product_version_range` it MUST be tested that
the value of `name` conforms the vers specification.

> To implement this test it is deemed sufficient that the value of `name` matches the following regex:
>
> ```
>   ^vers:[a-z\\.\\-\\+][a-z0-9\\.\\-\\+]*/.+
> ```

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/name
```

*Example 1 (which fails the test):*

```
            "branches": [
              {
                "category": "product_version_range",
                "name": ">4.2",
                // ...
              }
            ]
```

> The version range `>4.2` is a valid vsl but not valid according to the vers specification.
