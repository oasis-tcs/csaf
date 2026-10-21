#### Missing Referenced Action IDs

For each item in `$.document.involvement.actions` which has one of the categories `confirmation` or `dispute`
it SHALL be tested that the element `referenced_action_ids` exists.

The relevant path for this test is:

```list-of-jsonpaths
  $.document.involvement.actions[*]
```

*Example 1 (which fails the test):*

```
  {
    "acting_entity_refs": [
      "EID-0002"
    ],
    "action_id": "ACN-2",
    "category": "confirmation",
    "date": "2024-01-10T15:00:00Z",
    "receiving_entity_refs": [
      "EID-0001"
    ],
    "status": "completed",
    "summary": "Confirmed receipt of the report."
  }
```

> The action does not contain the element `referenced_action_ids`.
