#### Multiple Definition of Action ID

For each element of type `$['$defs'].action_id_t` which is defining an action (`$.document.involvement.actions[*].action_id`)
it SHALL be tested that the `action_id` was not already defined within the same document.

The relevant path for this test is:

```list-of-jsonpaths
  $.document.involvement.actions[*].action_id
```

*Example 1 (which fails the test):*

```
  "actions": [
    {
      // ...
      "action_id": "ACN-1",
      // ...
    },
    {
      // ...
      "action_id": "ACN-1",
      // ...
    },
    // ...
  ],
```

> `ACN-1` was defined twice.
