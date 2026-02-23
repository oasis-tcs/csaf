### Extension Tests{#recommended-tests--extension-tests}

This subsubsection structures the recommended tests for extensions.
Each of the following tests SHOULD be treated as they where listed similar to the other tests.

> An application MAY group these tests when providing the additional function to only run one or more selected tests.

#### Registered Extension

For each item in an element of type `#/$defs/extensions_t` it MUST be tested that the item is a registered CSAF Extension.
The test MUST be skipped for official CSAF Extensions.

The relevant path for this test is:

```
  /document/x_extensions[]
  /product_tree/branches[](/branches[])*/product/x_extensions[]
  /product_tree/full_product_names[]/x_extensions[]
  /product_tree/relationships[]/full_product_name/x_extensions[]
  /vulnerabilities[]/metrics[]/content/x_extensions[]
  /vulnerabilities[]/x_extensions[]
  /x_extensions[]
```

*Example 1 (which fails the test):*

```
  "x_extensions": [
    {
      "$schema": "https://raw.githubusercontent.com/oasis-tcs/csaf/refs/heads/master/csaf_2.1/extension/data/valid/documentation-11/documentation-11-content_1.0.0.json",
      // ...
    }
  ]
```

> The extension is neither an official nor a registered CSAF Extension.

#### Official Extension

For each item in an element of type `#/$defs/extensions_t` it MUST be tested that the item is an official CSAF Extension.

The relevant path for this test is:

```
  /document/x_extensions[]
  /product_tree/branches[](/branches[])*/product/x_extensions[]
  /product_tree/full_product_names[]/x_extensions[]
  /product_tree/relationships[]/full_product_name/x_extensions[]
  /vulnerabilities[]/metrics[]/content/x_extensions[]
  /vulnerabilities[]/x_extensions[]
  /x_extensions[]
```

*Example 1 (which fails the test):*

```
  "x_extensions": [
    {
      "$schema": "https://raw.githubusercontent.com/oasis-tcs/csaf/refs/heads/master/csaf_2.1/extension/data/valid/documentation-11/documentation-11-content_1.0.0.json",
      // ...
    }
  ]
```

> The extension is not an official CSAF Extension.
