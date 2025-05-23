### Missing Remediation

For each Product ID (type `/$defs/product_id_t`) in the Product Status groups Affected and Under investigation it MUST be tested that
a remediation exists.

> The remediation might be of the category `none_available` or `no_fix_planned`.

The relevant paths for this test are:

```
  /vulnerabilities[]/product_status/first_affected[]  
  /vulnerabilities[]/product_status/known_affected[]
  /vulnerabilities[]/product_status/last_affected[]
  /vulnerabilities[]/product_status/under_investigation[]
```

*Example 1 (which fails the test):*

```
  "product_tree": {
    "full_product_names": [
      {
        "product_id": "CSAFPID-9080700",
        "name": "Product A"
      }
    ]
  },
  "vulnerabilities": [
    {
      "product_status": {
        "last_affected": [
          "CSAFPID-9080700"
        ]
      }
    }
  ]
```

> `CSAFPID-9080700` has in Product Status `last_affected` but there is no remediation object for this Product ID.
