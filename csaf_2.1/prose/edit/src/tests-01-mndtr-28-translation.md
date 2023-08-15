### Translation

It MUST be tested that the given source language and document language are not the same.

The relevant path for this test is:

```
  /document/lang
  /document/source_lang
```

*Example 87 which fails the test:*

```
  "document": {
    // ...
    "lang": "en-US",
    // ...
    "source_lang": "en-US",
    // ...
  }
```

> The document language and the source language have the same value `en-US`.
>
> Note: A translation from `en-US` to `en-GB` would pass the test.

> A tool MAY remove the source language as quick fix.
