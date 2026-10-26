#### Missing Definition of Entity Group ID

For each element of type `$['$defs'].entity_group_id_t` which is not inside the list of entity groups (`$.document.involvement.entity_groups`)
and therefore references an item within the list of entity groups
it SHALL be tested that the Entity Group element with the matching `entity_group_id` exists.
This test SHALL ignore elements of type `$['$defs'].entity_id_t` in items of elements of type `$['$defs'].entity_refs_id_t`.

The relevant paths for this test are:

```{.text sequence-of="jsonpath"}
  $.document.involvement.actions[*].acting_entity_refs[*]
  $.document.involvement.actions[*].receiving_entity_refs[*]
```

*Example 1 (which fails the test):*

```
  "involvement": {
    "actions": [
      {
        "acting_entity_refs": [
          "EGID-9011"
        ],
        "action_id": "ACN-1",
        "category": "notification",
        "date": "2024-01-10T09:00:00Z",
        "receiving_entity_refs": [
          "EID-0002"
        ],
        "status": "completed",
        "summary": "Reported vulnerability to vendor."
      },
      // ...
    ],
    // ...
    "entity_groups": [
      {
        "entity_group_id": "EGID-9001",
        "entity_ids": [
          "EID-0001",
          "EID-0003"
        ],
        "name": "JJ Research"
      }
    ]
  },
```

> The action `ACN-1` contains `EGID-9011` as acting entity which is not defined in the list of entity groups.
