### Invalid CVSS computation

It MUST be tested that the given CVSS object has the values computed correctly according to the definition.

> The `vectorString` SHOULD take precedence.

The relevant paths for this test are:

```
  /vulnerabilities[]/scores[]/cvss_v2/baseScore
  /vulnerabilities[]/scores[]/cvss_v2/temporalScore
  /vulnerabilities[]/scores[]/cvss_v2/environmentalScore
  /vulnerabilities[]/scores[]/cvss_v3/baseScore
  /vulnerabilities[]/scores[]/cvss_v3/baseSeverity
  /vulnerabilities[]/scores[]/cvss_v3/temporalScore
  /vulnerabilities[]/scores[]/cvss_v3/temporalSeverity
  /vulnerabilities[]/scores[]/cvss_v3/environmentalScore
  /vulnerabilities[]/scores[]/cvss_v3/environmentalSeverity
```

*Example 1 (which fails the test):*

```
  "cvss_v3": {
    "version": "3.1",
    "vectorString": "CVSS:3.1/AV:L/AC:L/PR:H/UI:R/S:U/C:H/I:H/A:H",
    "baseScore": 10.0,
    "baseSeverity": "LOW"
  }
```

> Neither `baseScore` nor `baseSeverity` has the correct value according to the specification.

> A tool MAY set the correct values as computed according to the specification as quick fix.
