### Use of Default Language

For each element of type `/$defs/lang_t` it MUST be tested that the language code is not `i-default`.

The relevant paths for this test are:

```
  /document/lang
  /document/source_lang
```

*Example 1 (which fails the test):*

```
  "lang": "i-default"
```

> The language code `i-default` is used.

> A tool MAY remove such element as a quick fix.
