### Extension Tests{#mandatory-tests--extension-tests}

This subsubsection structures the mandatory tests for extensions.
Each of the following tests SHOULD be treated as they where listed similar to the other tests.

> An application MAY group these tests when providing the additional function to only run one or more selected tests.

#### Content Schema{#mandatory-tests--extension-tests-content-schema}

For each item in an element of type `#/$defs/extensions_t` it MUST be tested that the item is valid against the Extension Content Schema.

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
      "$schema": "https://raw.githubusercontent.com/oasis-tcs/csaf/refs/heads/master/csaf_2.1/extension/data/invalid/documentation-01/documentation-01-content_1.0.0.json",
      "category": "high_value",
      "content": {
        "documentation": "This extension is for documentation and test purposed only. It is invalid as it misses the `critical` property. It is not allowed to be used in a production CSAF."
      }
    }
  ]
```

> The extension is missing the required property `critical`.

#### Extension Schema{#mandatory-tests--extension-tests-extension-schema}

For each item in an element of type `#/$defs/extensions_t` it MUST be tested that the item is valid against the declared CSAF Extension Schema.
CSAF Extensions not supported by the implementation SHALL result in a warning which MUST include the value of `$schema` of the extension.
Such warning SHALL differentiate between the different classes of extensions.

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
      "$schema": "https://raw.githubusercontent.com/oasis-tcs/csaf/refs/heads/master/csaf_2.1/extension/data/valid/documentation-12/documentation-12-content_1.0.0.json",
      // ...
      "content": {
        
      }
    }
  ]
```

> The extension is missing the property `documentation` which is required by the declared CSAF Extension Schema.

#### Extension Metadata{#mandatory-tests--extension-tests-metadata}

For each element of type `#/$defs/extensions_t` it MUST be tested that the requirements provided through its metadata are fulfilled
for each CSAF Extension used.
CSAF Extensions not supported by the implementation SHALL result in a warning which MUST include the value of `$schema` of the extension.
Such warning SHALL differentiate between the different classes of extensions.

> This includes, but is not limited to:
>
> * The extension is allowed at this path at all.
> * The extension is not used more often than allowed.
> * The extension is not used with other incompatible extensions.

The relevant paths for this test are:

```
  /document/x_extensions
  /product_tree/branches[](/branches[])*/product/x_extensions
  /product_tree/full_product_names[]/x_extensions
  /product_tree/relationships[]/full_product_name/x_extensions
  /vulnerabilities[]/metrics[]/content/x_extensions
  /vulnerabilities[]/x_extensions
  /x_extensions
```

*Example 1 (which fails the test):*

```
  {
    // ...
    "x_extensions": [
      {
        "$schema": "https://raw.githubusercontent.com/oasis-tcs/csaf/refs/heads/master/csaf_2.1/extension/data/valid/documentation-11/documentation-11-content_1.0.0.json",
        "category": "high_value",
        "critical": false,
        "content": {
          "documentation": "This extension is for documentation and test purposed only. It is valid. It is not allowed to be used in a production CSAF."
        }
      },
      {
        "$schema": "https://raw.githubusercontent.com/oasis-tcs/csaf/refs/heads/master/csaf_2.1/extension/data/valid/documentation-11/documentation-11-content_1.0.0.json",
        "category": "informational",
        "critical": false,
        "content": {
          "documentation": "This extension is for documentation and test purposed only. It is valid. It is not allowed to be used in a production CSAF."
        }
      }
    ]
  }
```

> The extension is only allowed once in the path `/x_extensions`.
