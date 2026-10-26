#### Multiple Use of Same Entity Name

For each `name` in `$.document.involvement.entities[*]`
it SHALL be tested that the `name` was not already used for another entity within the same document.

> Such a construct is expected to happen, e.g. if a entity is reached out to under multiple addresses or
> the entity has different roles.
> For the justified scenarios, the test should be ignored.

The relevant path for this test is:

```{.text sequence-of="jsonpath"}
  $.document.involvement.entities[*].name
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
      "entity_id": "EID-0003",
      "name": "Jane Researcher"
    }
  ]
```

> `Jane Researcher` was used twice.
