### Missing Recipient on Attempt

For each item in `$.document.involvement.actions` with the `status` value of `attempted`
it SHALL be tested that the element `receiving_entity_refs` exists.

The relevant paths for this test are:

```list-of-jsonpaths
  $.document.involvement.actions[*]
```

*Example 1 (which fails the test):*

```
  {
    "action_id": "ACN-1",
    "acting_entity_refs": ["EID-0001"],
    "date": "2024-01-10T09:00:00Z",
    "category": "notification",
    "status": "attempted",
    "summary": "Tried to report vulnerability to vendor."
  }
```

> The action does not contain the element `receiving_entity_refs`.
