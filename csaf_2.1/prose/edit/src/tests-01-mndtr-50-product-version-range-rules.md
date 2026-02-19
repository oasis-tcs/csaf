### Product Version Range Rules

For each element of type `/$defs/branches_t` with `category` of `product_version_range`, it MUST be tested that the value of `name` complies with
the rules given in section [sec](#branches-type-name-under-product-version-range).
Version schemes of vers not supported by the implementation SHALL result in a warning which MUST include the version scheme name use.
Nevertheless, all other rules MUST be checked to the extend possible.

The relevant path for this test is:

```
    /product_tree/branches[](/branches[])*/name
```

*Example 1 (which fails the test):*

```
        {
          "category": "product_version_range",
          "name": "all versions < 4.2.0",
          // ...
        }
```

> The version range given does not comply with the rules given in section [sec](#branches-type-name-under-product-version-range).
