### Use of Self Referencing URLs Failing to Resolve

For each item in an array of type `references_t` with the category `self` it MUST be tested that
the URL referenced resolves with a HTTP status code less than 400.

> This test will most likely fail if the CSAF document is in a status before the initial release.
> For details about the HTTP status code classes see [cite](#RFC7231).

The relevant paths for this test are:

```
  /document/references[]/url
  /vulnerabilities[]/references[]/url
```

*Example 1 (which fails the test):*

```
    "references": [
      {
        "category": "self",
        "summary": "A URL that does not resolve with HTTP status code in the interval between (including) 200 and (excluding) 400.",
        "url": "https://example.invalid"
      }
    ]
```

> The `category` is `self` and a request to that URL does not resolve with a status code from the 2xx (Successful) or 3xx (Redirection) class.
