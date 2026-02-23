### PURL

It MUST be tested that all given PURLs are valid.

> It is not sufficient to just test against the `pattern` provided in section [sec](#full-product-name-type-product-identification-helper-purls).
> The PURL must be validated against the requirements in the [cite](#ECMA-427) specification and the additional constraints given in
> section [sec](#full-product-name-type-product-identification-helper-purls).

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/product/product_identification_helper/purls[]
  /product_tree/full_product_names[]/product_identification_helper/purls[]
  /product_tree/relationships[]/full_product_name/product_identification_helper/purls[]
```

*Example 1 (which fails the test):*

```
  "product_tree": {
    "full_product_names": [
      {
        "name": "Product A",
        "product_id": "CSAFPID-9080700",
        "product_identification_helper": {
          "purls": [
            "pkg:maven/@1.3.4"
          ]
        }
      }
    ]
  }
```

> Any valid PURL has a name component.
