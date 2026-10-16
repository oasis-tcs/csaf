#### Missing Definition of Document-local Vuln ID

For each element of type `$['$defs'].dl_vuln_id_t` which is not inside a vulnerability (`$.vulnerabilities[*].dl_vuln_id`)
and therefore references a vulnerability
it SHALL be tested that the vulnerability element with the matching `dl_vuln_id` exists.

The relevant path for this test is:

```list-of-jsonpaths
  $.document.involvement.actions[*].dl_vuln_ids[*]
```

*Example 1 (which fails the test):*

```
  {
    // ...
    "document": {
      // ...
      "involvement": {
        "actions": [
          {
            // ...
            "dl_vuln_ids": [
              "VULN-1"
            ],
            // ...
          },
          // ...
        ],
        // ...
      },
      // ...
    },
    "vulnerabilities": [
      {
        "title": "A vulnerability without a document-local vuln ID."
      }
    ]
  }
```

> `VULN-1` is not defined in the list of vulnerabilities.
