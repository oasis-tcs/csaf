### Missing Definition of Action ID

For each element of type `$['$defs'].action_id_t` which is not defining an action (`$.document.involvement.actions[*].action_id`)
and therefore references an action
it SHALL be tested that the Action element with the matching `action_id` exists.

The relevant path for this test is:

```list-of-jsonpaths
  $.document.involvement.actions[*].referenced_action_ids[*]
```

*Example 1 (which fails the test):*

```
  "actions": [
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
      "referenced_action_ids": [
        "ACN-1"
      ],
      "status": "completed",
      "summary": "Confirmed receipt of the report."
    }
  ],
```

> The action `ACN-2` references action `ACN-1` which is not defined in the list of actions.
