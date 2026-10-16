### Circular Reference of Action ID

For each action containing at least one referenced action id (type `$['$defs'].action_id_t`)
it SHALL be tested that the action does not end up in a circle.
This also includes actions containing their own `action_id` in the `referenced_action_ids`.

The relevant path for this test is:

```list-of-jsonpaths
  $.document.involvement.actions[*]
```

*Example 1 (which fails the test):*

```
  {
    // ...
    "action_id": "ACN-1",
    // ...
    "referenced_action_ids": [
      "ACN-1"
    ],
    // ...
  }
```

> `ACN-1` refers to itself - this is a circular reference.
