### Missing Canonical URL

It MUST be tested that the CSAF document has a canonical URL.

> To implement this test it is deemed sufficient that one item in `/document/references` fulfills all of the following:
>
> * It has the category `self`.
> * The `url` starts with `https://`.
> * The `url` ends with the valid filename for the CSAF document according to the rules in section [sec](#filename).

The relevant path for this test is:

```
  /document/references
```

*Example 1 (which fails the test):*

```
  "document": {
    // ...
    "references": [
      {
        "category": "self",
        "summary": "A non-canonical URL.",
        "url": "https://example.com/security/data/csaf/2024/oasis_csaf_tc-csaf_2.1-2024-6-2-11-01_1.json"
      }
    ],
    // ...
    "tracking": {
      // ...
      "id": "OASIS_CSAF_TC-CSAF_2.1-2024-6-2-11-01",
      // ...
      "version": "1"
    },
    // ...
  }
```

> The only element where the `category` is `self` has a URL that does not fulfill the requirement of a valid filename for a CSAF document.
