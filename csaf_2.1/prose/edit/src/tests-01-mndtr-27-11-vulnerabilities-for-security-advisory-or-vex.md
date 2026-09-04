#### Vulnerabilities{#vulnerabilities-for-security-advisory-or-vex}

It SHALL be tested that the element `$.vulnerabilities` exists.

The relevant values for `$.document.category` are:

```
  csaf_security_advisory
  csaf_vex
  csaf_deprecated_security_advisory
  csaf_vulnerability_report
```

The relevant path for this test is:

```list-of-jsonpaths
  $.vulnerabilities
```

*Example 1 (which fails the test):*

```
  {
    "$schema": "https://docs.oasis-open.org/csaf/csaf/v2.1/schema/csaf.json",
    "document": {
      // ...
    },
    "product_tree": [
      // ...
    ]
  }
```

> The element `$.vulnerabilities` does not exist.
