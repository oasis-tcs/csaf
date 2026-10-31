### Misuse at Vendor Name

For each item in `branches` with category `vendor` it SHALL be tested that the `name` is not `Open Source`.
Any occurrences of dash, hyphen, minus, underscore, white space and invisible characters are removed from the value on both sides
before the case insensitive match.

> Some issuing parties use `Open Source` as a vendor name for all open source products.
> This usage hinders efficient matching and is most likely not true.
> However, if there is a vendor whose official name is exactly `Open Source` it would be expected and
> acceptable to fail this test.
> The same applies for any other name that results in `opensource` after the removal step from sentence two.
> This does not apply, if the official name differs, e.g. `Open Source Ltd.`.
> Users are advised to carefully review the results of this test.

The relevant path for this test is:

```list-of-jsonpaths
  $.product_tree..branches[*].name
```

*Example 1 (which fails the test):*

```
  "product_tree": {
    "branches": [
      {
        "branches": [
          {
            // ...
            "category": "product_name",
            "name": "ISDuBA"
          }
        ],
        "category": "vendor",
        "name": "Open Source"
      }
    ]
  }
```

> The issuing party used `Open Source` as vendor name for the open source product `ISDuBA`.

> A tool MAY replace the vendor name with the correct one as a quick fix.
