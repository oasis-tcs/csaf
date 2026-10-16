### Missing Definition of Entity ID

For each element of type `$['$defs'].entity_id_t` which is not inside the list of entities (`$.document.involvement.entities`)
and therefore references an item within the list of entities
it SHALL be tested that the Entity element with the matching `entity_id` exists.
This test SHALL ignore elements of type `$['$defs'].entity_group_id_t` in items of elements of type `$['$defs'].entity_refs_id_t`.

The relevant paths for this test are:

```list-of-jsonpaths
  $.document.involvement.actions[*].acting_entity_refs[*]
  $.document.involvement.actions[*].receiving_entity_refs[*]
  $.document.involvement.entity_groups[*].entity_ids[*]
```

*Example 1 (which fails the test):*

```
    "involvement": {
      "actions": [
        {
          "acting_entity_refs": [
            "EID-0001"
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
      "entities": [
        {
          "category": "discoverer",
          "entity_id": "EID-0001",
          "name": "Jane Researcher"
        }
      ]
    },
```

> The action `ACN-1` contains `EID-0002` as receiving entity which is not defined in the list of entities.

