### Missing Definition of Product ID

For each element of type `/$defs/product_id_t` which is not inside a Full Product Name (type: `full_product_name_t`) and
therefore reference an element within the `product_tree` it MUST be tested that the Full Product Name element with the matching `product_id` exists.
The same applies for all items of elements of type `/$defs/products_t`.

The relevant paths for this test are:

```
  /document/notes[]/product_ids[]
  /product_tree/product_groups[]/product_ids[]
  /product_tree/relationships[]/product_reference
  /product_tree/relationships[]/relates_to_product_reference
  /vulnerabilities[]/flags[]/product_ids[]
  /vulnerabilities[]/metrics[]/products[]
  /vulnerabilities[]/notes[]/product_ids[]
  /vulnerabilities[]/product_status/first_affected[]
  /vulnerabilities[]/product_status/first_fixed[]
  /vulnerabilities[]/product_status/fixed[]
  /vulnerabilities[]/product_status/known_affected[]
  /vulnerabilities[]/product_status/known_not_affected[]
  /vulnerabilities[]/product_status/last_affected[]
  /vulnerabilities[]/product_status/recommended[]
  /vulnerabilities[]/product_status/under_investigation[]
  /vulnerabilities[]/remediations[]/product_ids[]
  /vulnerabilities[]/threats[]/product_ids[]
```

*Example 1 (which fails the test):*

```
  "product_tree": {
    "product_groups": [
      {
        "group_id": "CSAFGID-1020300",
        "product_ids": [
          "CSAFPID-9080700",
          "CSAFPID-9080701"
        ]
      }
    ]
  }
```

> Neither `CSAFPID-9080700` nor `CSAFPID-9080701` were defined in the `product_tree`.
