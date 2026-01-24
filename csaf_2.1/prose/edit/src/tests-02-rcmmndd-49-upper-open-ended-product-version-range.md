### Upper Open Ended Product Version Range

For each element of type `/$defs/branches_t` with `category` of `product_version_range`, it MUST be tested that the value of `name` is not an
upper open ended product version range.

> Usually, the last including version constraint of an upper open ended product version range contains as comparator either `>` or `>=`.

The relevant path for this test is:

```
    /product_tree/branches[](/branches[])*/name
```

*Example 1 (which fails the test):*

```
        {
          "category": "product_version_range",
          "name": "vers:intdot/>=4.2.0",
          // ...
        }
```

> The version range has no specific upper end point and states a right-open interval.

> If the upper open ended product version range consists only of one version constraint, a tool MAY convert it into the product version
> it starts with as a quick fix, if applicable.
> If the upper open ended product version range consists of more than one version constraint and the upper open range is the last version
> constraint, a tool MAY convert it into the product version range ending with the version the upper open ended product version as a quick
> fix, if applicable.
