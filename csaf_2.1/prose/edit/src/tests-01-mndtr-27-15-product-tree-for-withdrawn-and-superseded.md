#### Product Tree{#product-tree-for-withdrawn-and-superseded}

It MUST be tested that the element `$.product_tree` does not exist.

The relevant values for `$.document.category` are:

```
  csaf_withdrawn
  csaf_superseded
```

The relevant path for this test is:

```list-of-jsonpaths
  $.product_tree
```

*Example 1 (which fails the test):*

```
    "product_tree": [
      // ...
    ]
```

> The element `$.product_tree` exists.
