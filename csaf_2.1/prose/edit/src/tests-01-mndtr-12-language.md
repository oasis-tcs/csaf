### Language

For each element of type `/$defs/language_t` it MUST be tested that the language code is valid and exists.

The relevant paths for this test are:

```
  /document/lang
  /document/source_lang
```

*Example 60 which fails the test:*

```
  "lang": "EZ"
```

> `EZ` is not a valid language. It is the subtag for the region "Eurozone".

> For any deprecated subtag, a tool MAY replace it with its preferred value as a quick fix.
