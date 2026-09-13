### Multiple Definition in Actions

It SHALL be tested that items of the list of actions do differ in more values than just the `action_id`.

Ignoring the `action_id`, two items in the list of actions are the same, if:

1. all of the following fields contain the same value:
   - `category`
   - `date`
   - `status`
   - `summary`
2. and all of the following sets contain the same values:
   - `acting_entity_refs`
   - `dl_vuln_ids`
   - `group_ids`
   - `product_ids`
   - `receiving_entity_refs`
   - `referenced_action_ids`

The relevant path for this test is:

```list-of-jsonpaths
  $.document.involvement.actions
```

*Example 1 (which fails the test):*

```
  "actions": [
    {
      "action_id": "ACN-1",
      "acting_entity_refs": ["EID-0001"],
      "date": "2024-01-10T09:00:00Z",
      "category": "notification",
      "receiving_entity_refs": ["EID-0002"],
      "status": "completed",
      "summary": "Reported vulnerability to vendor."
    },
    {
      "action_id": "ACN-2",
      "acting_entity_refs": ["EID-0001"],
      "date": "2024-01-10T09:00:00Z",
      "category": "notification",
      "receiving_entity_refs": ["EID-0002"],
      "status": "completed",
      "summary": "Reported vulnerability to vendor."
    }
  ]
```

> The list of actions contains two items with the same content when ignoring their `action_id`.
