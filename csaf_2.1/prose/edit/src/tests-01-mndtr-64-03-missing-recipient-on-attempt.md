#### Missing Recipient on Attempt

For each item in `$.document.involvement.actions` with the `status` value of `attempted`
it SHALL be tested that the element `receiving_entity_refs` exists.

The relevant path for this test is:

```{.text sequence-of="jsonpath"}
  $.document.involvement.actions[*]
```

*Example 1 (which fails the test):*

```
  {
    "acting_entity_refs": [
      "EID-0001"
    ],
    "action_id": "ACN-1",
    "category": "notification",
    "date": "2024-01-10T09:00:00Z",
    "status": "attempted",
    "summary": "Tried to report vulnerability to vendor."
  }
```

> The action does not contain the element `receiving_entity_refs`.
