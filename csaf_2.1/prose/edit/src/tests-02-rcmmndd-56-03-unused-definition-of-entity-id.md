#### Unused Definition of Entity ID

For each Entity ID (type: `$['$defs'].entity_id_t`) in Entity elements (`$.document.involvement.entities[*]`)
it SHALL be tested that the `entity_id` is referenced somewhere within the same document.

The relevant path for this test is:

```{.text sequence-of="jsonpath"}
  $.document.involvement.entities[*].entity_id
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
    "entities": [
      // ...
      {
        "category": "discoverer",
        "entity_id": "EID-0003",
        "name": "Joe Researcher"
      }
    ]
  },
```

> `EID-0003` was defined but never used.

> A tool MAY remove the unused definition as a quick fix.
