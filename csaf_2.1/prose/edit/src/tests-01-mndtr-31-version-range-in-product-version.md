### Version Range in Product Version

For each element of type `/$defs/branches_t` with `category` of `product_version` it MUST be tested that
the value of `name` does not contain a version range.

> To implement this test it is deemed sufficient that, when converted to lower case,
> the value of `name` does not contain any of the following strings:
>
> ```
>   <
>   <=
>   >
>   >=
>   after
>   all
>   before
>   earlier
>   later
>   prior
>   versions
> ```

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/name
```

*Example 90 which fails the test:*

```
            "branches": [
              {
                "category": "product_version",
                "name": "prior to 4.2",
                // ...
              }
            ]
```

> The version range `prior to 4.2` is given for the branch category `product_version`.
