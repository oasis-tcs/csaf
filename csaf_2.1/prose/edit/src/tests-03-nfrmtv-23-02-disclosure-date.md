### Disclosure Date

It SHALL be tested that `$.vulnerabilities[*].disclosure_date` exists.

The relevant value for `$.document.category` is:

```
  csaf_vulnerability_report
```

The relevant path for this test is:

```list-of-jsonpaths
  $.vulnerabilities[*].disclosure_date
```

*Example 1 (which fails the test):*

```
  "vulnerabilities": [
    {
      "cve": "CVE-1900-0001"
    }
  ]
```

> The vulnerability does not have a `disclosure_date` element.

Recommendation:

It is recommended that issuing parties use the disclosure date.
