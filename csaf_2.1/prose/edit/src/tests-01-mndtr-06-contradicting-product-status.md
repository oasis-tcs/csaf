### Contradicting Product Status

For each item in `/vulnerabilities` it MUST be tested that the same Product ID is not member of contradicting product status groups.
The sets formed by the contradicting groups within one vulnerability item MUST be pairwise disjoint.

Contradiction groups are:

* Affected:

   ```
   /vulnerabilities[]/product_status/first_affected[]  
   /vulnerabilities[]/product_status/known_affected[]
   /vulnerabilities[]/product_status/last_affected[]
   ```

* Not affected:

  ```
  /vulnerabilities[]/product_status/known_not_affected[]
  ```

* Fixed:

  ```
  /vulnerabilities[]/product_status/first_fixed[]
  /vulnerabilities[]/product_status/fixed[]
  ```

* Under investigation:

  ```
  /vulnerabilities[]/product_status/under_investigation[]
  ```

> Note: An issuer might recommend (`/vulnerabilities[]/product_status/recommended`) a product version from any group - also from the affected group,
> i.e. if it was discovered that fixed versions introduce a more severe vulnerability.

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
        "known_affected": [
          "CSAFPID-9080700"
        ],
        "known_not_affected": [
          "CSAFPID-9080700"
        ]
      }
    }
  ]
```

> `CSAFPID-9080700` is a member of the two contradicting groups "Affected" and "Not affected".
