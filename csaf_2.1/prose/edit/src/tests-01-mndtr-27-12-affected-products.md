#### Affected Products

For each item in `$.vulnerabilities` it SHALL be tested that the element `product_status/known_affected` exists.

The relevant value for `$.document.category` is:

```
  csaf_security_advisory
```

The relevant path for this test is:

```{.text sequence-of="jsonpath"}
  $.vulnerabilities[*].product_status.known_affected
```

*Example 1 (which fails the test):*

```
      "product_status": {
        "under_investigation": [
          "CSAFPID-9080700"
        ]
      }
```

> The product status does not contain the `known_affected` element.
