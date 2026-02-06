### Use of Qualitative Severity Rating

For each item in `metrics` it MUST be tested that it does not use the qualitative severity rating.

> This covers all items in `metrics` regardless of their origin.
> Even though the Qualitative Severity Rating is a specified property, it's usage is discouraged as it provides
> no information about the assessment inputs.
> Nevertheless, it can be useful to provide the such limited assessment result, especially for supply chain vulnerabilities
> where the upstream product just provides a qualitative severity rating.

The relevant path for this test is:

```
    /vulnerabilities[]/metrics[]
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
      "metrics": [
        {
          "content": {
            "qualitative_severity_rating": "low"
          },
          "products": [
            "CSAFPID-9080700"
          ],
          "source": "https://upstream.example/advisories/42/an-advisory-with-just-a-severity-without-other-metrics"
        }
      ]
    }
  ]
```

> The upstream provided metric for `CSAFPID-9080700` uses a `qualitative_severity_rating`.

-------
