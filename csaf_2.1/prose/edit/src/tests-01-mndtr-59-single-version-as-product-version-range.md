### Single Version as Product Version Range

For each element of type `/$defs/branches_t` with `category` of `product_version_range`, it MUST be tested that the value of `name` does not
identify only a single version.

The relevant path for this test is:

```
    /product_tree/branches[](/branches[])*/name
```

*Example 1 (which fails the test):*

```
        {
          "category": "product_version_range",
          "name": "vers:intdot/4.2.0",
          // ...
        }
```

> The version range given identifies just a single version.

> A tool MAY change the branch category to `product_version` and replace the value for `name` with the version as quick fix.
