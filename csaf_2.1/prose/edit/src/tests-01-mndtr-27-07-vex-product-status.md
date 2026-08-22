#### VEX Product Status

For each item in `$.vulnerabilities` it MUST be tested that at least one of the elements `fixed`, `known_affected`, `known_not_affected`,
or `under_investigation` is present in `product_status`.

The relevant values for `$.document.category` are:

```
  csaf_vex
  csaf_vulnerability_report
```

The relevant paths for this test are:

```list-of-jsonpaths
  $.vulnerabilities[*].product_status.fixed
  $.vulnerabilities[*].product_status.known_affected
  $.vulnerabilities[*].product_status.known_not_affected
  $.vulnerabilities[*].product_status.under_investigation
```

*Example 1 (which fails the test):*

```
  "product_status": {
    "first_fixed": [
      // ...
    ],
    "recommended": [
      // ...
    ]
  }
```

> None of the elements `fixed`, `known_affected`, `known_not_affected`, or `under_investigation` is present in `product_status`.
