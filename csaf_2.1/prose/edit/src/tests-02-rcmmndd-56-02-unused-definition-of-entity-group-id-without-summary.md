#### Unused Definition of Entity Group ID without Summary

For each Entity Group ID (type: `$['$defs'].entity_group_id_t`) in Entity Group elements (`$.document.involvement.entity_groups[*]`)
which does not contain a `summary` element
it SHALL be tested that the `entity_group_id` is referenced somewhere within the same document.

> Without being referenced or containing a `summary`, a reader has no clue how the group is related to the document and why it was added.

The relevant path for this test is:

```list-of-jsonpaths
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

> `EGID-9001` does not contain a `summary` and was not referenced elsewhere in the document.

> A tool MAY suggest to add a summary to such definition as a quick fix.
