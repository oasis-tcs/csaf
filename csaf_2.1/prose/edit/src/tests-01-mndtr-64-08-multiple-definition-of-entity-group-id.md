### Multiple Definition of Entity Group ID

For each Entity Group ID (type: `$['$defs'].entity_group_id_t`) in Entity Group elements (`$.document.involvement.entity_groups[*]`)
it SHALL be tested that the `entity_group_id` was not already defined within the same document.

The relevant path for this test is:

```list-of-jsonpaths
  $.document.involvement.entity_groups[*].entity_group_id
```

*Example 1 (which fails the test):*

```
  "entity_groups": [
    {
      "entity_group_id": "EGID-9001",
      "entity_ids": [
        "EID-0001",
        "EID-0003"
      ],
      "name": "JJ Research"
    },
    {
      "entity_group_id": "EGID-9001",
      "entity_ids": [
        "EID-0004",
        "EID-0005"
      ],
      "name": "J+J Research"
    }
  ]
```

> `EGID-9001` was defined twice.
