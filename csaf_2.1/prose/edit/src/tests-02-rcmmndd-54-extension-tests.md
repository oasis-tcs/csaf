### Extension Tests{#recommended-tests--extension-tests}

This subsubsection structures the recommended tests for extensions.
Each of the following tests SHOULD be treated as they where listed similar to the other tests.

> An application MAY group these tests when providing the additional function to only run one or more selected tests.

#### Registered Extension

For each item in an element of type `#/$defs/extensions_t` it MUST be tested that the item is a registered CSAF Extension.
The test MUST be skipped for official CSAF Extensions.

The relevant paths for this test are:

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

The relevant paths for this test are:

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

#### Critical Extension

For each item in an element of type `#/$defs/extensions_t` it MUST be tested that the item is not a critical extension.

> It is sufficient to check whether the value of `critical` is `false`.

The relevant paths for this test are:

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
      // ...
      "critical": true,
      // ...
    }
  ]
```

> The extension is critical.

#### Usage of Experimental Extension in TLP:CLEAR Document{#usage-of-experimental-extension-in-tlp-clear-document}

For each item in an element of type `#/$defs/extensions_t` it MUST be tested that no experimental extension is used
if the document is labeled `TLP:CLEAR`.

The relevant path for this test is:

```
  /document/x_extensions[]/critical
  /product_tree/branches[](/branches[])*/product/x_extensions[]/critical
  /product_tree/full_product_names[]/x_extensions[]/critical
  /product_tree/relationships[]/full_product_name/x_extensions[]/critical
  /vulnerabilities[]/metrics[]/content/x_extensions[]/critical
  /vulnerabilities[]/x_extensions[]/critical
  /x_extensions[]/critical
```

*Example 1 (which fails the test):*

```
  {
    // ...
    "document": {
      // ...
      "distribution": {
        "tlp": {
          "label": "CLEAR"
        }
      },
      // ...
    }
    "x_extensions": [
      {
        "$schema": "https://raw.githubusercontent.com/oasis-tcs/csaf/refs/heads/master/csaf_2.1/extension/data/valid/documentation-11/documentation-11-content_1.0.0.json",
        // ...
      }
    ]
  }
```

> The extension is an experimental CSAF Extension.
> Its properties and meaning might therefore not be known to the reader of the document.
