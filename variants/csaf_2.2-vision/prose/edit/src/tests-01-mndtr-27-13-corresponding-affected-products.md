#### Corresponding Affected Products

For each product listed in the product status group fixed in any vulnerability,
it SHALL be tested that a corresponding version of the product is listed as affected in the same vulnerability.

> For a product path including the `installed_with` relationship the product path leading to but not including the relationship
> is a corresponding product.
> Such product path could also be just the product identified by `beginning_product_reference` if the first subpath element
> has the category `installed_with`.

The relevant value for `$.document.category` is:

```
  csaf_security_advisory
```

The relevant path for this test is:

```list-of-jsonpaths
  $.vulnerabilities[*].product_status.known_affected
```

*Example 1 (which fails the test):*

```
  {
    // ...
    "product_tree": {
      "branches": [
        {
          "branches": [
            {
              "branches": [
                {
                  "category": "product_version",
                  "name": "4.2",
                  "product": {
                    "name": "Example Company Product A 4.2",
                    "product_id": "CSAFPID-9080700"
                  }
                }
              ],
              "category": "product_name",
              "name": "Product A"
            }
          ],
          "category": "vendor",
          "name": "Example Company"
        }
      ]
    },
    "vulnerabilities": [
      {
        // ...
        "product_status": {
          "fixed": [
            "CSAFPID-9080700"
          ]
        }
      }
    ]
  }
```

> The vulnerability just contains the fixed product but does not list corresponding affected products.
