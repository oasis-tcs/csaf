### Language Specific License Text

If the document language is specified but not English,
and the `license_expression` contains license identifiers or exceptions that are not listed in the SPDX license list or AboutCode's "ScanCode LicenseDB",
it MUST be tested that exactly one item in document notes exists that has the language specific translation of the term `License` as title.
The category of this item MUST be `legal_disclaimer`.
If no language specific translation has been recorded, the test MUST be skipped and output an information to the user that no such translation is known.

The relevant path for this test is:

```
  /document/notes
```

*Example 1 (which fails the test):*

```
  "document": {
    // ...
    "lang": "de-DE",
    "license_expression": "LicenseRef-www.example.com-no-work",
    "notes": [
      {
        "category": "summary",
        "text": "Es handelt sich nicht um ein urheberrechtliches Werk, da die Schöpfungshöhe nicht erreicht ist.",
        "title": "Lizenz"
      }
    ],
    // ...
  }  
```

> The note has the correct title. However, it uses the wrong category.
