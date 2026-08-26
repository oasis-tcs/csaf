#### Extension in Superseded or Withdrawn Document

It SHALL be tested that the document does not contain an extension.

The relevant values for `$.document.category` are:

```
  csaf_withdrawn
  csaf_superseded
```

The relevant paths for this test are:

```list-of-jsonpaths
  $.document.x_extensions
  $.x_extensions
```

*Example 1 (which fails the test):*

```
  {
    // ...
    "x_extensions": [
      {
        "$schema": "https://raw.githubusercontent.com/oasis-tcs/csaf/refs/heads/master/csaf_2.1/extension/data/valid/documentation-11/documentation-11-content_1.0.0.json",
        // ...
      }
    ]
  }
```

> The document contains a CSAF Extension.
