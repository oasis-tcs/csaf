### Missing Definition of Product Group ID

For each element of type `/$defs/product_group_id_t` which is not inside a Product Group (`/product_tree/product_groups[]`) and
therefore reference an element within the `product_tree` it MUST be tested that the Product Group element with the matching `group_id` exists.
The same applies for all items of elements of type `/$defs/product_groups_t`.

The relevant paths for this test are:

```
  /document/notes[]/group_ids[]
  /vulnerabilities[]/flags[]/group_ids[]
  /vulnerabilities[]/notes[]/group_ids[]
  /vulnerabilities[]/remediations[]/group_ids[]
  /vulnerabilities[]/threats[]/group_ids[]
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
      "threats": [
        {
          "category": "exploit_status",
          "details": "Reliable exploits integrated in Metasploit.",
          "group_ids": [
            "CSAFGID-1020301"
          ]
        }
      ]
    }
  ]
```

> `CSAFGID-1020301` was not defined in the Product Tree.
