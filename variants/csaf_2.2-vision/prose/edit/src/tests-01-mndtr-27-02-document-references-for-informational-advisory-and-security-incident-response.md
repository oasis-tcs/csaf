#### Document References{#document-references-for-informational-advisory-and-security-incident-response}

It SHALL be tested that at least one item in `$.document.references` exists that contains a link to an `external` source.
The property `category` SHALL be present for this item.

> Other items MAY exist which do not contain the property `category`.
> Issuing parties are advised that tools MAY explicitly filter for or prioritize entries that have the contain
> the property `category` with the value of `external`.

The relevant values for `$.document.category` are:

```
  csaf_informational_advisory
  csaf_security_incident_response
  csaf_superseded
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
