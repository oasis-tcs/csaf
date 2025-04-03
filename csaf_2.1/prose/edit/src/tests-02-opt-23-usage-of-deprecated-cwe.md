### Usage of Deprecated CWE

For each item in the CWE array it MUST be tested that the CWE is not deprecated in the given version.

The relevant path for this test is:

```
  /vulnerabilities[]/cwes[]
```

*Example 1 (which fails the test):*

```
     "cwes": [
        {
          "id": "CWE-596",
          "name": "DEPRECATED: Incorrect Semantic Object Comparison",
          "version": "4.13"
        }
      ]
```

> The `CWE-596` is deprecated in version `4.13`.

> A tool MAY suggest to replace the deprecated CWE with its replacement or closest equivalent.
