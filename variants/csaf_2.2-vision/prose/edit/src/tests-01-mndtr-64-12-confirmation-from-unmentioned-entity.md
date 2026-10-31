#### Confirmation from Unmentioned Entity

For each item in `$.document.involvement.actions` with the `category` value of `confirmation`
it SHALL be tested that all acting entities are mentioned as receiving entities in each action referenced through `referenced_action_ids`.
This takes indirect relations through entity groups into account.

The relevant path for this test is:

```list-of-jsonpaths
  $.document.involvement.actions[*]
```

*Example 1 (which fails the test):*

```
  "actions": [
    {
      // ...
      "action_id": "ACN-1",
      // ...
      "receiving_entity_refs": [
        "EID-0002"
      ],
      // ...
    },
    // ...
    {
      "acting_entity_refs": [
        "EID-0003"
      ],
      "action_id": "ACN-3",
      "category": "confirmation",
      // ...
      "referenced_action_ids": [
        "ACN-1"
      ],
      // ...
    }
  ],
```

> `EID-0003` confirms in `ACN-3` receiving action `ACN-1`.
> However, `ACN-1` does not list `EID-0003` as receiving entity of this action.

If an entity receives an unsolicited confirmation,
it is likely that the acting entity has received the corresponding information through a third party, e.g. a notification was forwarded.
However, such a representation could also result from mistake while authoring the CSAF document.
To maintain consistency, a confirmation from unmentioned entity is not allowed to be denoted as confirmation
but SHALL be represented as notification.
