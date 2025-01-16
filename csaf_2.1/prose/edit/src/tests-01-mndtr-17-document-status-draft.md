### Document Status Draft

It MUST be tested that document status is `draft` if the document version is `0` or `0.y.z` or contains the pre-release part.

The relevant path for this test is:

```
    /document/tracking/status
```

*Example 1 (which fails the test):*

```
    "tracking": {
      // ...
      "status": "final",
      "version": "0.9.5"
    }
```

> The `/document/tracking/version` is `0.9.5` but the document status is `final`.
