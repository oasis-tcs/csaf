### CVSS for Fixed Products

For each item the fixed products group (`first_fixed` and `fixed`) it MUST be tested that
a CVSS applying to this product has an environmental score of `0`.
The test SHALL pass if none of the Product IDs listed within product status `fixed` or
`first_fixed` is found in `products` of any item of the `metrics` element.

The relevant path for this test is:

```
  /vulnerabilities[]/product_status/first_fixed[]
  /vulnerabilities[]/product_status/fixed[]
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
        "fixed": [
          "CSAFPID-9080700"
        ]
      },
      "metrics": [
        {
          "content": {
            "cvss_v3": {
              "baseScore": 6.5,
              "baseSeverity": "MEDIUM",
              "vectorString": "CVSS:3.1/AV:L/AC:L/PR:H/UI:R/S:U/C:H/I:H/A:H",
              "version": "3.1"
            }
          }          ,
          "products": [
            "CSAFPID-9080700"
          ]
        }
      ]
    }
  ]
```

> Neither the `environmentalScore` nor the properties `modifiedAvailabilityImpact`, `modifiedConfidentialityImpact`, `modifiedIntegrityImpact` nor
> the corresponding attributes in the `vectorString` have been set.

> A tool MAY remove any Product IDs listed within product status `fixed` or `first_fixed` from `products` of all items of the `metrics` element.
>
> Alternatively, a tool MAY set those environmental properties according to the CVSS version used that reduce score to `0`
> and compute the `environmentalScore` as quick fix.
> The following environmental properties have been identified:
>
> - CVSS v2: `targetDistribution` to `NONE`
> - CVSS v3: all of `modifiedAvailabilityImpact`, `modifiedConfidentialityImpact`, and `modifiedIntegrityImpact` to `NONE`
> - CVSS v4: all of
>   - `modifiedVulnAvailabilityImpact`, `modifiedVulnConfidentialityImpact`, and `modifiedVulnIntegrityImpact` to `NONE` and
>   - `modifiedSubAvailabilityImpact`, `modifiedSubConfidentialityImpact`, and `modifiedSubIntegrityImpact` to `NEGLIGIBLE`
