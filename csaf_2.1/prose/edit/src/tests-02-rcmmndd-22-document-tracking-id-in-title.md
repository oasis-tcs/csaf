### Document Tracking ID in Title

It MUST be tested that the `/document/title` does not contain the `/document/tracking/id`.

The relevant path for this test is:

```
  /document/title
```

*Example 1 (which fails the test):*

```
    "title": "OASIS_CSAF_TC-CSAF_2.1-2024-6-2-22-01: Recommended test: Document Tracking ID in Title (failing example 1)",
    "tracking": {
      // ...
      "id": "OASIS_CSAF_TC-CSAF_2.1-2024-6-2-22-01",
      // ...
    }
```

> The document title contains the document tracking id.

> A tool MAY remove the document tracking id from the document title.
> It SHOULD also remove any separating characters including white space, colon, dash and brackets.
