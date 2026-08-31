#### Language Specific Reasoning for Supersession

If the document language is specified but not English, it SHALL be tested that exactly one item in document notes exists
that has the language specific translation of the term `Reasoning for Supersession` as `title`.
The `category` of this item SHALL be `description`.
If no language specific translation has been recorded, the test SHALL be skipped and output an information to the user that no such translation is known.

> A list of the language specific translations is kept at the OASIS CSAF TC.

The relevant value for `$.document.category` is:

```
  csaf_superseded
```

The relevant path for this test is:

```list-of-jsonpaths
  $.document.notes
```

*Example 1 (which fails the test):*

```
    "notes": [
      {
        "category": "summary",
        "text": "Das CSAF Dokument enthielt Beispieldaten und wurde ersetzt, um Testdaten zu erzeugen.",
        "title": "Begründung für die Ersetzung"
      }
    ],
```

> The note has the correct title. However, it uses the wrong category.
