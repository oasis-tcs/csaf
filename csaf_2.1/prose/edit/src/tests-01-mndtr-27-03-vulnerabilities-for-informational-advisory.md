#### Vulnerabilities{#vulnerabilities-for-informational-advisory}

It SHALL be tested that the element `$.vulnerabilities` does not exist.

The relevant values for `$.document.category` are:

```
  csaf_informational_advisory
  csaf_withdrawn
  csaf_superseded
```

The relevant path for this test is:

```list-of-jsonpaths
  $.vulnerabilities
```

*Example 1 (which fails the test):*

```
  "vulnerabilities": [
    {
      "title": "A vulnerability item that SHALL NOT exist"
    }
  ]
```

> The element `$.vulnerabilities` exists.

> A tool MAY change the `$.document.category` to `csaf_base` as a quick fix.
