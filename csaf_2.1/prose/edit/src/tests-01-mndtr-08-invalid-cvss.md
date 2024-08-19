### Invalid CVSS

It MUST be tested that the given CVSS object is valid according to the referenced schema.

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
    "vectorString": "CVSS:3.1/AV:L/AC:L/PR:H/UI:R/S:U/C:H/I:H/A:H",
    "baseScore": 6.5
  }
```

> The required element `baseSeverity` is missing.

> A tool MAY add one or more of the missing properties `version`, `baseScore` and `baseSeverity` based on
> the values given in `vectorString` as quick fix.
