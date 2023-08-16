### Flag without Product Reference

For each item in `/vulnerabilities[]/flags` it MUST be tested that it includes at least one of the elements `group_ids` or `product_ids`.

The relevant path for this test is:

```
  /vulnerabilities[]/flags[]
```

*Example 1 (which fails the test):*

```
      "flags": [
        {
          "label": "component_not_present"
        }
      ]
```

> The given flag does not specify to which products it should be applied.
