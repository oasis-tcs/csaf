### Invalid CVSS Computation

It MUST be tested that the given CVSS object has the values computed correctly according to the definition.

> The `vectorString` SHOULD take precedence.

The relevant paths for this test are:

```
  /vulnerabilities[]/metrics[]/content/cvss_v2/baseScore
  /vulnerabilities[]/metrics[]/content/cvss_v2/temporalScore
  /vulnerabilities[]/metrics[]/content/cvss_v2/environmentalScore
  /vulnerabilities[]/metrics[]/content/cvss_v3/baseScore
  /vulnerabilities[]/metrics[]/content/cvss_v3/baseSeverity
  /vulnerabilities[]/metrics[]/content/cvss_v3/temporalScore
  /vulnerabilities[]/metrics[]/content/cvss_v3/temporalSeverity
  /vulnerabilities[]/metrics[]/content/cvss_v3/environmentalScore
  /vulnerabilities[]/metrics[]/content/cvss_v3/environmentalSeverity
  /vulnerabilities[]/metrics[]/content/cvss_v4/baseScore
  /vulnerabilities[]/metrics[]/content/cvss_v4/baseSeverity
```

> Note: CVSS v4 does not define `threatScore`, `threatSeverity`, `environmentalScore` and `environmentalSeverity`.
> The existence of these JSON keys in an older version of the schema was fixed with version `4.0.1`.

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
