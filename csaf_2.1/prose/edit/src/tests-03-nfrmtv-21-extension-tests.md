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
