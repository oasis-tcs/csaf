### Product Version Range without vers

For each element of type `/$defs/branches_t` with `category` of `product_version_range` it MUST be tested that
the value of `name` indicates that the product version range is using vers.

> Compliance with the vers specification itself is enforced via test [sec](#product-version-range-rules).
> Unknown version schemes are detected via test [sec](#unknown-version-scheme-in-vers).
>
> To implement this test it is deemed sufficient that the value of `name` matches the following regex:
>
> ```
>   ^vers:[a-z\\.\\-\\+][a-z0-9\\.\\-\\+]*/.+
> ```

The warning MUST clearly advise to carefully check whether vers can be used or the versions can be enumerated as
the use of vls is only a fallback option.
For more details, see sections [sec](#branches-type-category) and [sec](#branches-type-name-under-product-version-range).

> It is planned to deprecate and finally remove the support for vls in future versions of this standard.

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

> The version range `>4.2` is a valid vls but not valid according to the vers specification.
