### CWE

It MUST be tested that given CWE exists and is valid.

The relevant path for this test is:

```
    /vulnerabilities[]/cwe
```

*Example 59 which fails the test:*

```
  "cwe": {
    "id": "CWE-79",
    "name": "Improper Input Validation"
  }
```

> The `CWE-79` exists. However, its name is `Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')`.
