### Use of Non-self Referencing URLs Failing to Resolve

For each URL which is not in the category `self` it MUST be tested that it resolves with a HTTP status code from
the 2xx (Successful) or 3xx (Redirection) class.

> This test does not apply for any item in an array of type `references_t` with the category `self`.
> For details about the HTTP status code classes see [cite](#RFC7231).

The relevant paths for this test are:

```
  /document/acknowledgments[]/urls[]
  /document/aggregate_severity/namespace
  /document/distribution/tlp/url
  /document/references[]/url
  /document/publisher/namespace
  /product_tree/branches[]/product/product_identification_helper/sbom_urls[]
  /product_tree/branches[]/product/product_identification_helper/x_generic_uris[]/namespace
  /product_tree/branches[]/product/product_identification_helper/x_generic_uris[]/uri
  /product_tree/branches[](/branches[])*/product/product_identification_helper/sbom_urls[]
  /product_tree/branches[](/branches[])*/product/product_identification_helper/x_generic_uris[]/namespace
  /product_tree/branches[](/branches[])*/product/product_identification_helper/x_generic_uris[]/uri
  /product_tree/full_product_names[]/product_identification_helper/sbom_urls[]
  /product_tree/full_product_names[]/product_identification_helper/x_generic_uris[]/namespace
  /product_tree/full_product_names[]/product_identification_helper/x_generic_uris[]/uri
  /product_tree/relationships[]/full_product_name/product_identification_helper/sbom_urls[]
  /product_tree/relationships[]/full_product_name/product_identification_helper/x_generic_uris[]/namespace
  /product_tree/relationships[]/full_product_name/product_identification_helper/x_generic_uris[]/uri
  /vulnerabilities[]/acknowledgments[]/urls[]
  /vulnerabilities[]/references[]/url
  /vulnerabilities[]/remediations[]/url
```

*Example 1 (which fails the test):*

```
    "references": [
      {
        "summary": "A URL that does not resolve with HTTP status code in the interval between (including) 200 and (excluding) 400.",
        "url": "https://example.invalid"
      }
    ]
```

> The `category` is not set and therefore treated as its default value `external`.
> A request to that URL does not resolve with a status code from the 2xx (Successful) or 3xx (Redirection) class.
