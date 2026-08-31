#### Document References{#document-references-for-informational-advisory-and-security-incident-response}

It SHALL be tested that at least one item in `$.document.references` exists that has links to an `external` source.

The relevant values for `$.document.category` are:

```
  csaf_informational_advisory
  csaf_security_incident_response
```

The relevant path for this test is:

```list-of-jsonpaths
  $.document.references
```

*Example 1 (which fails the test):*

```
  "references": [
    {
      "category": "self",
      "summary": "The canonical URL.",
      "url": "https://example.com/security/data/csaf/2024/oasis_csaf_tc-csaf_2_1-2024-6-1-27-02-01.json"
    }
  ]
```

> The document references do not contain any item which has the category `external`.
