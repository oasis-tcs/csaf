### Unknown Version Scheme in vers

For each element of type `/$defs/branches_t` with `category` of `product_version_range` which indicates that it is using vers,
it MUST be tested that the version scheme is supported by the implementation.
The warning MUST differentiate between officially registered version schemes and those that are not in this state.

> Different implementations might support different version schemes.
> Usually, unknown version schemes hinder the automated evaluation of vers.
> However, it is expected that the test is able to recognize all officially registered version schemes.
> The differentiation will help users analyzing the result of the test and addressing the issue appropriately.  

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/name
```

*Example 1 (which fails the test):*

```
    {
      "category": "product_version_range",
      "name": "vers:someweirdunknownversionscheme/<4.2.0|>3.91.1|!=3.2.0|<1.2",
      // ...
    }
```

> The version scheme `someweirdunknownversionscheme` is a not an officially registered vers version scheme.
> Note: An implementation would also have to state whether it supports this version scheme.
