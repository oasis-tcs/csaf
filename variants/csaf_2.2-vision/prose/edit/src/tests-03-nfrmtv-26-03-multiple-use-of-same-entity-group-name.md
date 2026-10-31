#### Multiple Use of Same Entity Group Name

For each `name` in `$.document.involvement.entity_groups[*]`
it SHALL be tested that the `name` was not already used for another entity group within the same document.

> For the justified scenarios, the test should be ignored.

The relevant path for this test is:

```list-of-jsonpaths
  $.document.involvement.entity_groups[*].name
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
      "entity_group_id": "EGID-9002",
      "entity_ids": [
        "EID-0001",
        "EID-0003"
      ],
      "name": "JJ Research"
    }
  ]
```

> `JJ Research` was used twice.
