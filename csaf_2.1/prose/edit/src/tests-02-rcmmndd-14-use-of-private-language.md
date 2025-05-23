### Use of Private Language

For each element of type `/$defs/lang_t` it MUST be tested that the language code does not contain subtags reserved for private use.

The relevant paths for this test are:

```
  /document/lang
  /document/source_lang
```

*Example 1 (which fails the test):*

```
  "lang": "qtx"
```

> The language code `qtx` is reserved for private use.

> A tool MAY remove such subtag as a quick fix.
