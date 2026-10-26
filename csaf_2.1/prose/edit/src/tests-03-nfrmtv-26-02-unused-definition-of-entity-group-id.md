#### Unused Definition of Entity Group ID

For each Entity Group ID (type: `$['$defs'].entity_group_id_t`) in Entity Group elements (`$.document.involvement.entity_groups[*]`)
it SHALL be tested that the `entity_group_id` is referenced somewhere within the same document.

The relevant path for this test is:

```{.text sequence-of="jsonpath"}
  $.document.involvement.entity_groups[*].entity_group_id
```

*Example 1 (which fails the test):*

```
  "involvement": {
    "actions": [
      {
        "acting_entity_refs": [
          "EID-0001"
        ],
        // ...
        "receiving_entity_refs": [
          "EID-0002"
        ],
        // ...
      },
      {
        "acting_entity_refs": [
          "EID-0002"
        ],
        // ...
        "receiving_entity_refs": [
          "EID-0001"
        ],
        // ...
      }
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

> `EGID-9001` was not referenced elsewhere in the document.

> A tool MAY remove the unused definition as a quick fix.
