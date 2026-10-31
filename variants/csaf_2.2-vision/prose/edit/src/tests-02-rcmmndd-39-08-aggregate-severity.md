#### Aggregate Severity

It SHALL be tested that the element `$.document.aggregate_severity` exists.

> An aggregate severity helps recipients quickly understand the overall urgency of the vulnerability report during coordination.

The relevant value for `$.document.category` is:

```
  csaf_vulnerability_report
```

The relevant path for this test is:

```list-of-jsonpaths
  $.document.aggregate_severity
```

*Example 1 (which fails the test):*

```
  "document": {
    "category": "csaf_vulnerability_report",
    // ...
  }
```

> The element `$.document.aggregate_severity` does not exist.

> A tool MAY add the highest value of all CVSS Severity values of all vulnerabilities as quick fix.
