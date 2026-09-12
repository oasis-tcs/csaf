### Involvements

It SHALL be tested that `$.document.involvement` exists.

> Recording involvement actions helps the participating parties understand the disclosure timeline and who has engaged in the process.

The relevant value for `$.document.category` is:

```
  csaf_vulnerability_report
```

The relevant path for this test is:

```list-of-jsonpaths
  $.document.involvement
```

*Example 1 (which fails the test):*

```
  document: {
    // ...
    "distribution": {
      "tlp": {
        "label": "AMBER"
      }
    },
    "publisher": {
      "category": "other",
      "name": "OASIS CSAF TC",
      "namespace": "https://csaf.io"
    },
    // ...
  }
```

> The vulnerability does not record any coordination activity in `$.document.involvement`.

Recommendation:

It is recommended that issuing parties use `$.document.involvement` to record coordination milestones during the CVD process.
