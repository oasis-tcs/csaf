### Missing CVE

It SHALL be tested that the element `cve` is present and set.
A CSAF Validator SHALL differentiate in the error message between the key being present but having no or an empty value
and not being present at all.

The relevant path for this test is:

```list-of-jsonpaths
  $.vulnerabilities[*].cve
```

*Example 1 (which fails the test):*

```
  "vulnerabilities": [
    {
      "title": "BlueKeep"
    }
  ]
```

> The element `cve` is not present.

Recommendation:

It is recommended to provide a CVE number to support the users efforts to find more details about a vulnerability and
potentially track it through multiple advisories.
If no CVE exists for that vulnerability, it is recommended to get one assigned.
