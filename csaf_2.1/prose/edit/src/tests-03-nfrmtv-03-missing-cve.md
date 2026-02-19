### Missing CVE

It MUST be tested that the CVE number is given.

The relevant path for this test is:

```
  /vulnerabilities[]/cve
```

*Example 1 (which fails the test):*

```
  "vulnerabilities": [
    {
      "title": "BlueKeep"
    }
  ]
```

> The CVE number is not given.

Recommendation:

It is recommended to provide a CVE number to support the users efforts to find more details about a vulnerability and
potentially track it through multiple advisories.
If no CVE exists for that vulnerability, it is recommended to get one assigned.
