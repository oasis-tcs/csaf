### Use of CVSS v3.0

For each item in the list of metrics which contains the `cvss_v3` object under `content` it MUST be tested that CVSS v3.0 is not used.

The relevant paths for this test are:

```
  /vulnerabilities[]/metrics[]/content/cvss_v3/version
  /vulnerabilities[]/metrics[]/content/cvss_v3/vectorString
```

*Example 1 (which fails the test):*

```
  "cvss_v3": {
    "version": "3.0",
    "vectorString": "CVSS:3.0/AV:L/AC:L/PR:H/UI:R/S:U/C:H/I:H/A:H",
    "baseScore": 6.5,
    "baseSeverity": "MEDIUM"
  }
```

> The CVSS v3.0 is used.

Recommendation:

It is recommended to upgrade to CVSS v3.1.

> A tool MAY upgrade to CVSS v3.1 as quick fix.
> However, if such quick fix is supported the tool SHALL also recompute the `baseScore` and `baseSeverity`.
> The same applies for `temporalScore` and `temporalSeverity` respectively `environmentalScore` and `environmentalSeverity` if
> the necessary fields for computing their value are present and set.
