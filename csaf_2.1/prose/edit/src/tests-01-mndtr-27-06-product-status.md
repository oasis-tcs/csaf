#### Product Status

For each item in `$.vulnerabilities` it MUST be tested that the element `product_status` exists.

The relevant values for `$.document.category` are:

```
  csaf_security_advisory
  csaf_deprecated_security_advisory
```

The relevant path for this test is:

```list-of-jsonpaths
  $.vulnerabilities[*].product_status
```

*Example 1 (which fails the test):*

```
  "vulnerabilities": [
    {
      "title": "A vulnerability item without a product status"
    }
  ]
```

> The vulnerability item has no `product_status` element.
