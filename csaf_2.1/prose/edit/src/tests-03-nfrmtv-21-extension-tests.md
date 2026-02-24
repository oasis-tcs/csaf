### Extension Tests{#informative-tests--extension-tests}

This subsubsection structures the informative tests for extensions.
Each of the following tests SHOULD be treated as they where listed similar to the other tests.

> An application MAY group these tests when providing the additional function to only run one or more selected tests.

#### Extension Category Critical

For each item in an element of type `#/$defs/extensions_t` it MUST be tested that the extension `category` of the item
is not `critical`.

> It is sufficient to check whether the value of `category` is not `critical`.

The relevant paths for this test are:

```
  /document/x_extensions[]/category
  /product_tree/branches[](/branches[])*/product/x_extensions[]/category
  /product_tree/full_product_names[]/x_extensions[]/category
  /product_tree/relationships[]/full_product_name/x_extensions[]/category
  /vulnerabilities[]/metrics[]/content/x_extensions[]/category
  /vulnerabilities[]/x_extensions[]/category
  /x_extensions[]/category
```

*Example 1 (which fails the test):*

```
  "x_extensions": [
    {
      // ...
      "category": "critical",
      // ...
    }
  ]
```

> The extension category is `critical`.
> A reader that does not understand this extension might miss information that is critical to understand the content of the CSAF document.

#### Usage of Experimental Extension in Non TLP:CLEAR Document{#usage-of-experimental-extension-in-non-tlp-clear-document}

For each item in an element of type `#/$defs/extensions_t` it MUST be tested that no experimental extension is used
if the document is not labeled `TLP:CLEAR`.

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
  {
    // ...
    "document": {
      // ...
      "distribution": {
        "tlp": {
          "label": "GREEN"
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

#### Usage of Extension at Document Level

It MUST be tested that the element `/document/x_extensions` does not exist.

The relevant path for this test is:

```
  /document/x_extensions
```

*Example 1 (which fails the test):*

```
  {
    // ...
    "document": {
      // ...
      "x_extensions": [
        // ...
      ]
    }
  }
```

> The element `/document/x_extensions` exists.

#### Usage of Extension in Product Tree Branch Path

It MUST be tested that the element `x_extensions` does not exist in any path that starts with `/product_tree/branches`.

The relevant path for this test is:

```
  /product_tree/branches[](/branches[])*/product/x_extensions
```

*Example 1 (which fails the test):*

```
  "product_tree": {
    "branches": [
      {
        "branches": [
          {
            "branches": [
              {
                // ...
                "product": {
                  // ...
                  "x_extensions": [
                    // ...
                  ]
                }
              }
            ],
            // ...
          }
        ],
        // ...
      }
    ]
  }
```

> The element `x_extensions` exists in a path that starts with `/product_tree/branches`.

#### Usage of Extension in Product Tree Full Product Names Path

It MUST be tested that the element `x_extensions` does not exist in any path that starts with `/product_tree/full_product_names`.

The relevant path for this test is:

```
  /product_tree/full_product_names[]/x_extensions
```

*Example 1 (which fails the test):*

```
  "product_tree": {
    "full_product_names": [
      {
        // ...
        "x_extensions": [
          // ...
        ]
      }
    ]
  }
```

> The element `x_extensions` exists in a path that starts with `/product_tree/full_product_names`.

#### Usage of Extension in Product Tree Relationships Path

It MUST be tested that the element `x_extensions` does not exist in any path that starts with `/product_tree/relationships`.

The relevant path for this test is:

```
  /product_tree/relationships[]/full_product_name/x_extensions
```

*Example 1 (which fails the test):*

```
  "product_tree": {
    // ...
    "relationships": [
      {
        // ...
        "full_product_name": {
          // ...
          "x_extensions": [
            // ...
          ]
        },
        // ...
      }
    ]
  }
```

> The element `x_extensions` exists in a path that starts with `/product_tree/relationships`.

#### Usage of Extension in Vulnerabilities Metrics Path

It MUST be tested that the element `x_extensions` does not exist in any path that starts with `/vulnerabilities[]/metrics`.

The relevant path for this test is:

```
  /vulnerabilities[]/metrics[]/content/x_extensions
```

*Example 1 (which fails the test):*

```
  "vulnerabilities": [
    {
      "metrics": [
        {
          "content": {
            "x_extensions": [
              // ...
            ]
          },
          // ...
        }
      ]
    }
  ]
```

> The element `x_extensions` exists in a path that starts with `/vulnerabilities[]/metrics`.

#### Usage of Extension at Vulnerabilities Level

For each item `/vulnerabilities` it MUST be tested that the element `x_extensions` does not exist.

The relevant path for this test is:

```
  /vulnerabilities[]/x_extensions
```

*Example 1 (which fails the test):*

```
  {
    // ...
    "vulnerabilities": [
      {
        // ...
        "x_extensions": [
          // ...
        ]
      }
    ]
  }
```

> The element `x_extensions` exists inside a `vulnerabilities` item.
