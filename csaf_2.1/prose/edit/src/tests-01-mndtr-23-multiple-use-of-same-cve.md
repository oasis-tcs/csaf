### Multiple Use of Same CVE

It MUST be tested that a CVE is not used in multiple vulnerability items.

The relevant path for this test is:

```
    /vulnerabilities[]/cve
```

*Example 71 which fails the test:*

```
  "vulnerabilities": [
    {
      "cve": "CVE-2017-0145"
    },
    {
      "cve": "CVE-2017-0145"
    }
  ]
```

> The vulnerabilities array contains two items with the same CVE identifier `CVE-2017-0145`.
