### Inconsistent CVSS

It MUST be tested that the given CVSS properties do not contradict the CVSS vector.

The relevant paths for this test are:

```
  /vulnerabilities[]/metrics[]/content/cvss_v2
  /vulnerabilities[]/metrics[]/content/cvss_v3
  /vulnerabilities[]/metrics[]/content/cvss_v4
```

*Example 1 (which fails the test):*

```
  "cvss_v3": {
    "version": "3.1",
    "vectorString": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",
    "baseScore": 9.8,
    "baseSeverity": "CRITICAL",
    "attackVector": "LOCAL",
    "attackComplexity": "LOW",
    "privilegesRequired": "NONE",
    "userInteraction": "NONE",
    "scope": "CHANGED",
    "confidentialityImpact": "HIGH",
    "integrityImpact": "HIGH",
    "availabilityImpact": "LOW"
  }
```

> The values in CVSS vector differs from values of the properties `attackVector`, `scope` and `availabilityImpact`.

> A tool MAY overwrite contradicting values according to the `vectorString` as a quick fix.
