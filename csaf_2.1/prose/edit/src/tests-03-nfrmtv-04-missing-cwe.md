### Missing CWE

It MUST be tested that at least one CWE is given.

The relevant path for this test is:

```
  /vulnerabilities[]/cwes
```

*Example 1 (which fails the test):*

```
  "vulnerabilities": [
    {
      "cve": "CVE-2019-0708",
      "title": "BlueKeep"
    }
  ]
```

> No CWE number is given.
