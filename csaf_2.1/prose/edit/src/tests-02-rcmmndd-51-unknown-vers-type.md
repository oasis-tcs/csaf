### Unknown VERS Type

For each element of type `$['$defs'].branches_t` with `category` of `product_version_range` which indicates that it is using vers,
it SHALL be tested that the VERS type is officially registered and supported by the implementation.
The warning SHALL differentiate between officially registered VERS types and those that are not in this state.

> Different implementations might support different VERS types.
> Usually, unknown VERS types hinder the automated evaluation of VERS.
> However, it is expected that the test is able to recognize all officially registered VERS types.
> The differentiation will help users analyzing the result of the test and addressing the issue appropriately.  

The relevant paths for this test are:

```list-of-jsonpaths
  $.product_tree..branches[*].name
```

*Example 1 (which fails the test):*

```
    {
      "category": "product_version_range",
      "name": "vers:someweirdunknownverstype/<4.2.0|>3.91.1|!=3.2.0|<1.2",
      // ...
    }
```

> The VERS type `someweirdunknownverstype` is a not an officially registered one.
> Note: An implementation would also have to state whether it supports this VERS type.
