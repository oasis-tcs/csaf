### CWE

For each CWE it MUST be tested that the given CWE exists and is valid in the version provided.
Any `id` that refers to a CWE Category or View MUST fail the test.

The relevant path for this test is:

```
    /vulnerabilities[]/cwes[]
```

*Example 1 (which fails the test):*

```
  "cwes": [
    {
      "id": "CWE-79",
      "name": "Improper Input Validation",
      "version": "4.13"
    }
  ]
```

> The `CWE-79` exists. However, its name in version `4.13` is `Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')`.
