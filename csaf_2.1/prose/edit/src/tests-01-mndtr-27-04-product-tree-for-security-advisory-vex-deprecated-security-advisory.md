#### Product Tree{#product-tree-for-security-advisory-vex-deprecated-security-advisory}

It SHALL be tested that the element `$.product_tree` exists.

The relevant values for `$.document.category` are:

```
  csaf_security_advisory
  csaf_vex
  csaf_deprecated_security_advisory
  csaf_vulnerability_report
```

The relevant path for this test is:

```list-of-jsonpaths
  $.product_tree
```

*Example 1 (which fails the test):*

```
  {
    "document": {
      // ...
    },
    "vulnerabilities": [
      // ...
    ]
  }
```

> The element `$.product_tree` does not exist.
