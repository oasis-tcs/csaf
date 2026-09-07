### Involvements

It SHALL be tested that `$.vulnerabilities[*].involvements` exists.

> Recording involvement entries helps the participating parties understand the disclosure timeline and who has engaged in the process.

The relevant value for `$.document.category` is:

```
  csaf_vulnerability_report
```

The relevant path for this test is:

```list-of-jsonpaths
  $.vulnerabilities[*].involvements
```

*Example 1 (which fails the test):*

```
  "vulnerabilities": [
    {
      "cve": "CVE-1900-0001"
    }
  ]
```

> The vulnerability does not record any coordination activity in `$.vulnerabilities[*].involvements`.

Recommendation:

It is recommended that issuing parties use `$.vulnerabilities[*].involvements` to record coordination milestones during the CVD process.

