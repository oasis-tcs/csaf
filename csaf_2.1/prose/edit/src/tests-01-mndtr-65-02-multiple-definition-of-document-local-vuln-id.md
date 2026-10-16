### Multiple Definition of Document-local Vuln ID

For each element of type `$['$defs'].dl_vuln_id_t` in vulnerabilities (`$.vulnerabilities[*].dl_vuln_id`)
it SHALL be tested that the `dl_vuln_id` was not already defined within the same document.

The relevant path for this test is:

```list-of-jsonpaths
  $.vulnerabilities[*].dl_vuln_id
```

*Example 1 (which fails the test):*

```
  "vulnerabilities": [
    {
      "dl_vuln_id": "VULN-1"
    },
    {
      "dl_vuln_id": "VULN-1"
    }
  ]
```

> `VULN-1` was defined twice.
