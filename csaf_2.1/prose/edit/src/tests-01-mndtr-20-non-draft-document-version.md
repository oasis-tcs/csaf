### Non-draft Document Version

It MUST be tested that document version does not contain a pre-release part if the document status is `final` or `interim`.

The relevant path for this test is:

```
    /document/tracking/version
```

*Example 68 which fails the test:*

```
    "tracking": {
      // ...
      "status": "interim",
      "version": "1.0.0-alpha"
    }
```

> The document status is `interim` but the document version contains the pre-release part `-alpha`.
