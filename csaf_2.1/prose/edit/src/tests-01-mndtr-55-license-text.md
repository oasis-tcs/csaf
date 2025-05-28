### License Text

If the document language is English or unspecified,
and the `license_expression` contains license identifiers or exceptions that are not listed in the SPDX license list or Aboutcode's "ScanCode LicenseDB",
it MUST be tested that exactly one item in document notes exists that has the title `License`.
The category of this item MUST be `legal_disclaimer`.

The relevant path for this test is:

```
  /document/notes
```

*Example 1 (which fails the test):*

```
  "document": {
    // ...
    "license_expression": "LicenseRef-www.example.com-no-work-pd",
    "notes": [
      {
        "category": "other",
        "text": "This is not a work and therefore it can't be licensed. Use it as public domain.",
        "title": "License"
      }
    ],
    // ...
  }  
```

> The note has the correct title. However, it uses the wrong category.
