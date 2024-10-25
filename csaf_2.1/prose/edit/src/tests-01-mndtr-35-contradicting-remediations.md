### Contradicting Remediations

For each item in `/vulnerabilities[]/remediations` it MUST be tested that a product is not member of contradicting remediation categories.
This takes indirect relations through product groups into account.

The relevant path for this test is:

```
  /vulnerabilities[]/remediations[]
```

*Example 1 (which fails the test):*

```
      "remediations": [
        {
          "category": "no_fix_planned",
          "details": "The product is end-of-life. Therefore, no fix will be provided.",
          "product_ids": [
            "CSAFPID-9080700"
          ]
        },
        {
          "category": "vendor_fix",
          "details": "Update to version >=14.3 to fix the vulnerability.",
          "product_ids": [
            "CSAFPID-9080700"
          ]
        }
      ]
```

> The two remediations given for the product with product ID `CSAFPID-908070` contradict each other.

> A tool MAY apply the conversion rules from the conformance target CSAF 2.0 to CSAF 2.1 converter if applicable or
> remove the product from the remediation with the lower priority.
> The priority MAY be defined as follows:
> `vendor_fix` > `mitigation` > `workaround` > `fix_planned` > `no_fix_planned` > `optional_patch` > `none_available`
