### Inconsistent Product Identification Helper

For each product identification helper which resides in `branches`, it SHALL be tested that the product identification helper contain at least
the same information as the categorized strings.
Information that cannot be represented in the specific product identification helper SHALL be omitted from the comparison.

> To implement this test it is deemed sufficient to follow the process below.
> It is based on a static mapping of branch categories to the corresponding part of the product identification helpers.
> The latter one are referred to as counterparts.
>
> 1. Determine the counterparts in the specific product identification helper for all categories used along the path up to the product.
> 2. Check whether the counterparts in the product identification helper are set.
> 3. Check whether each counterpart set does not contain a wildcard unless the value of the categorized string would indicate that.
>    Only exception is the version part in a CPE, which can be set to `*` for a product version range due to the matching exception
>    in section [sec](#full-product-name-type-product-identification-helper).
> 4. Check whether the version part algins between the categorized strings and the product identification helper.
>    Omit this check for a version part of `*` in a CPE.
> 5. For CPE only: Check whether extra information is included in the CPE that is not in the categorized string.
>    This might be a counterpart that is set but the corresponding categorized string is missing along th path.

The relevant paths for this test are:

```list-of-jsonpaths
  $.product_tree..branches[*].product.product_identification_helper.cpe
  $.product_tree..branches[*].product.product_identification_helper.purls[*]
```

*Example 1 (which fails the test):*

```
  "product_tree": {
    "branches": [
      {
        "category": "vendor",
        "name": "Example Company",
        "branches": [
          {
            "category": "product_name",
            "name": "Product A",
            "branches": [
              {
                "category": "product_version",
                "name": "2.2.0",
                "product": {
                  "product_id": "CSAFPID-9080700",
                  "name": "Example Company Product A 2.2.0",
                  "product_identification_helper": {
                    "cpe": "cpe:2.3:h:example:product_a:2.2.0:*:*:de:*:*:*:*"
                  }
                }
              },
              {
                "category": "product_version",
                "name": "2.3.0",
                "product": {
                  "product_id": "CSAFPID-9080701",
                  "name": "Example Company Product A 2.3.0",
                  "product_identification_helper": {
                    "cpe": "cpe:2.3:h:example:product_a:2.3.0:PL17:*:*:*:*:*:*"
                  }
                }
              }
            ]
          }
        ]
      }
    ]
  }
```

> The CPE of the first product contains a language part that is not given through the categorized strings.
> The CPE of the second product contains an update part that is not given through the categorized strings.
