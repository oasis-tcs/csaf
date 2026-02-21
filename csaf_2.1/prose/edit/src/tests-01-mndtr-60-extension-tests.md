### Extension Tests{#mandatory-tests--extension-tests}

This subsubsection structures the mandatory tests for extensions.
Each of the following tests SHOULD be treated as they where listed similar to the other tests.

> An application MAY group these tests when providing the additional function to only run one or more selected tests.

#### Content Schema{#mandatory-tests--extension-tests-content-schema}

For each item in an element of type `#/$defs/extensions_t` it MUST be tested that the item is valid against the Extension Content Schema.

The relevant path for this test is:

```
  /document/x_extensions[]
  /product_tree/branches[](/branches[])*/product/x_extensions[]
  /product_tree/full_product_names[]/x_extensions[]
  /product_tree/relationships[]/full_product_name/x_extensions[]
  /vulnerabilities[]/x_extensions[]
  /x_extensions[]
```

*Example 1 (which fails the test):*

```
  "x_extensions": [
    {
      "$schema": "https://raw.githubusercontent.com/oasis-tcs/csaf/refs/heads/master/csaf_2.1/extension/data/invalid/documentation-01/documentation-01-content_1.0.0.json",
      "category": "high_value",
      "content": {
        "documentation": "This extension is for documentation and test purposed only. It is invalid as it misses the `critical` property. It is not allowed to be used in a production CSAF."
      }
    }
  ]
```

> The extension is missing the required property `critical`.
