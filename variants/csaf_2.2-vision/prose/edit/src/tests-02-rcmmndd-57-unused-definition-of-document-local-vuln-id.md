### Unused Definition of Document-local Vuln ID

For each element of type `$['$defs'].dl_vuln_id_t` in vulnerabilities (`$.vulnerabilities[*].dl_vuln_id`)
it SHALL be tested that the `dl_vuln_id` is referenced somewhere within the same document.

The relevant path for this test is:

```list-of-jsonpaths
  $.vulnerabilities[*].dl_vuln_id
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
          "acting_entity_refs": [
            "EID-0001"
          ],
          "action_id": "ACN-1",
          "category": "notification",
          "date": "2024-01-01T09:00:00Z",
          "receiving_entity_refs": [
            "EID-0002"
          ],
          "status": "completed",
          "summary": "Reported vulnerability to vendor."
        },
        {
          "acting_entity_refs": [
            "EID-0002"
          ],
          "action_id": "ACN-2",
          "category": "confirmation",
          "date": "2024-01-02T15:00:00Z",
          "receiving_entity_refs": [
            "EID-0001"
          ],
          "referenced_action_ids": [
            "ACN-1"
          ],
          "status": "completed",
          "summary": "Confirmed receipt of the report."
        }
      ],
      // ...
    },
    // ...
  },
  "vulnerabilities": [
    {
      "dl_vuln_id": "VULN-1",
      "title": "A vulnerability with an unreferenced Document-local Vuln ID."
    }
  ]
}
```

> `VULN-1` was defined but never used.

> A tool MAY remove the unused definition as a quick fix.
> However, such quick fix shall not be applied if the test was skipped.
