#### Inconsistent Future Action Date

For each item in `$.document.involvement.actions` with one the `status` values `attempted`, `completed` or `discontinued`
it SHALL be tested that the `date` of the action is earlier than or equal to the newest item of the `revision_history`.
As the timestamps might use different timezones, the sorting and comparison SHALL take timezones into account.

> The aforementioned status indicate that the action occurred already which would have happened after the release of the document.

The relevant path for this test is:

```list-of-jsonpaths
  $.document.involvement.actions[*].date
```

*Example 1 (which fails the test):*

```
  "document": {
    // ...
    "involvement": {
      "actions": [
        // ...
        {
          "acting_entity_refs": [
            "EID-0002"
          ],
          "action_id": "ACN-3",
          "category": "coordination",
          "date": "2024-03-02T15:00:00Z",
          "receiving_entity_refs": [
            "EID-0001"
          ],
          "referenced_action_ids": [
            "ACN-1"
          ],
          "status": "completed",
          "summary": "Closed case after release of CSAF document."
        }
      ],
      // ...
    },
    // ...
    "tracking": {
      // ...
      "revision_history": [
        {
          "date": "2024-01-24T10:00:00.000Z",
          "number": "1",
          "summary": "Initial version."
        }
      ],
      // ...
    }
  }
```

> The `date` of `ACN-3` is newer than the `date` of the newest item in the `revision_history`.

> A tool MAY remove such element as a quick fix.
