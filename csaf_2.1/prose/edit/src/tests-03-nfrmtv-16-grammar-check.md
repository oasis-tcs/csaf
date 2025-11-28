### Grammar Check

If the document language is given it MUST be tested that a grammar check for the given language does not find any mistakes.
The test SHALL be skipped if the document language is not set.
It SHALL fail if the given language is not supported.

The relevant paths for this test are:

```
  /document/acknowledgments[]/summary
  /document/aggregate_severity/text
  /document/distribution/text
  /document/notes[]/audience
  /document/notes[]/text
  /document/notes[]/title
  /document/publisher/issuing_authority
  /document/references[]/summary
  /document/title
  /document/tracking/revision_history[]/summary
  /product_tree/product_groups[]/summary
  /vulnerabilities[]/acknowledgments[]/summary
  /vulnerabilities[]/involvements[]/summary
  /vulnerabilities[]/notes[]/audience
  /vulnerabilities[]/notes[]/text
  /vulnerabilities[]/notes[]/title
  /vulnerabilities[]/references[]/summary
  /vulnerabilities[]/remediations[]/details
  /vulnerabilities[]/remediations[]/entitlements[]
  /vulnerabilities[]/remediations[]/restart_required/details
  /vulnerabilities[]/threats[]/details
  /vulnerabilities[]/title
```

*Example 1 (which fails the test):*

```
  "document": {
    // ...
    "lang": "en",
    "notes": [
      {
        "category": "summary",
        "text": "The security hardening guide must followed for ensure secure operations of a products."
      }
    ],
    // ...
  }
```

> Multiple grammar mistakes exist:
>
> - a `be` is missing between `must` and `followed`
> - the `for` needs to be a `to`
> - `a products` is also incorrect as `a` indicates singular.
