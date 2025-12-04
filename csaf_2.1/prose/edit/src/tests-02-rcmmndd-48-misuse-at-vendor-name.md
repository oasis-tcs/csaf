### Misuse at Vendor Name

For each item in `branches` with category `vendor` it MUST be tested that the `name` is not `Open Source`.
The comparison is case and white space insensitive.

> Some issuing parties use `Open Source` as a vendor name for all open source products.
> This usage hinders efficient matching and is most likely not true.
> However, if there is a vendor whose official name is exactly `Open Source` it would be expected and
> acceptable to fail this test.
> This does not apply, if the official name differs, e.g. `Open Source Ltd.`.

The relevant path for this test is:

```
    /product_tree/branches[](/branches[])*/name
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
