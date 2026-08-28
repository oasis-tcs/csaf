#### Missing Fixed Product

For each product listed in the product status group affected in any vulnerability,
it SHALL be tested that a corresponding version of the product is listed as fixed in the same vulnerability.
The test SHALL be skipped if there is a clear indication, that such a version of the product does not exist.
Indicators include a remediation item with one of the categories `fix_planned`, `no_fix_planned` or `none_available` referring to the affected product.
The test SHALL NOT be skipped, if there is an indication, that such a version of the product might exist.
Indicators include an affected product version range with the comparator `<` in the last version constraint and
a remediation item with the categories `vendor_fix` referring to the affected product.

The relevant value for `$.document.category` is:

```
  csaf_security_advisory
```

The relevant path for this test is:

```list-of-jsonpaths
  $.vulnerabilities[*].product_status
```

*Example 1 (which fails the test):*

```
  "vulnerabilities": [
    {
      // ...
      "product_status": {
        "known_affected": [
          "CSAFPID-9080700"
        ]
      },
      "remediations": [
        {
          "category": "vendor_fix",
          "details": "Update to the latest version, at least version 4.2.",
          "product_ids": [
            "CSAFPID-9080700"
          ]
        }
      ]
    }
  ]
```

> The fixed product is not listed in the advisory but there is a clear indication that such product exists as there is a remediation
> with category `vendor_fix`.

> A tool MAY create the missing fixed product based on the data available in the advisory as a quick fix.
