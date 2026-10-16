### Multiple Definition of Entity ID

For each Entity ID (type: `$['$defs'].entity_id_t`) in Entity elements (`$.document.involvement.entities[*]`)
it SHALL be tested that the `entity_id` was not already defined within the same document.

The relevant path for this test is:

```list-of-jsonpaths
  $.document.involvement.entities[*].entity_id
```

*Example 1 (which fails the test):*

```
  "entities": [
    {
      "category": "discoverer",
      "entity_id": "EID-0001",
      "name": "Jane Researcher"
    },
    // ...
    {
      "category": "discoverer",
      "entity_id": "EID-0001",
      "name": "Joe Researcher"
    }
  ]
```

> `EID-0001` was defined twice.
