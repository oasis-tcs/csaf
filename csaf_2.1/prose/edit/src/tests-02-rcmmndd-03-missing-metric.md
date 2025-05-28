### Missing Metric

For each Product ID (type `/$defs/product_id_t`) in the Product Status groups Affected it MUST be tested that
a metric object exists which covers this product.

The relevant paths for this test are:

```
  /vulnerabilities[]/product_status/first_affected[]  
  /vulnerabilities[]/product_status/known_affected[]
  /vulnerabilities[]/product_status/last_affected[]
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
        "first_affected": [
          "CSAFPID-9080700"
        ]
      }
    }
  ]
```

> `CSAFPID-9080700` has in Product Status `first_affected` but there is no metric object which covers this Product ID.
