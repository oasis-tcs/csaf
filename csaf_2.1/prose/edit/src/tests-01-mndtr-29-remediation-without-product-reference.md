### Remediation without Product Reference

For each item in `/vulnerabilities[]/remediations` it MUST be tested that it includes at least one of the elements `group_ids` or `product_ids`.

The relevant path for this test is:

```
  /vulnerabilities[]/remediations[]
```

*Example 88 which fails the test:*

```
      "remediations": [
        {
          "category": "no_fix_planned",
          "details": "These products are end-of-life. Therefore, no fix will be provided."
        }
      ]
```

> The given remediation does not specify to which products it should be applied.

> A tool MAY add all products of the affected group of this vulnerability to the remediation as quick fix.
