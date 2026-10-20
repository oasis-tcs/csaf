#### Confirmation before Action

For each item in `$.document.involvement.actions` with category `confirmation`
it SHALL be tested that the `date` of the action is later than or equal to the newest item of actions
it refers to through `referenced_action_ids`.
As the timestamps might use different timezones, the sorting and comparison SHALL take timezones into account.

The relevant path for this test is:

```list-of-jsonpaths
  $.document.involvement.actions[*]
```

*Example 1 (which fails the test):*

```
  "actions": [
    {
      "acting_entity_refs": [
        "EID-0001"
      ],
      "action_id": "ACN-1",
      "category": "notification",
      "date": "2024-01-11T09:00:00Z",
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
```

> The `date` of `ACN-2` is older than the `date` of the newest item it refers to.
