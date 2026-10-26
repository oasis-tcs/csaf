### Language

For each element of type `$['$defs'].lang_t` it SHALL be tested that the language code is valid and exists.
A CSAF validator SHALL differentiate in the error message between the language code that contain subtags not in the registry
and those that contain only subtags from the registry but the compiled language code is invalid.

> For example, this happens if a subtag for a region is used as primary language subtag.

The relevant paths for this test are:

```{.text sequence-of="jsonpath"}
  $.document.lang
  $.document.source_lang
```

*Example 1 (which fails the test):*

```
  "lang": "EZ"
```

> `EZ` is not a valid language. It is the subtag for the region "Eurozone".

> For any deprecated subtag, a tool MAY replace it with its preferred value as a quick fix.
