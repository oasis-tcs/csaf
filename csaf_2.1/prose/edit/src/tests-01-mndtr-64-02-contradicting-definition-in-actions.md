#### Contradicting Definition in Actions

It SHALL be tested that items of the list of actions do not contradict each other.

Ignoring the `action_id`, two items in the list of actions contradict each other, if:

1. all of the following fields contain the same value:
   - `category`
   - `date`
2. and all of the following sets contain the same values:
   - `acting_entity_refs`
   - `dl_vuln_ids`
   - `group_ids`
   - `product_ids`
   - `receiving_entity_refs`
   - `referenced_action_ids`
3. but have different values for `status`.

A `dl_vuln_ids` mentioning all vulnerabilities in the document is equivalent to the element missing.
All groups have to be expanded to their definitions for the test.
As the timestamps might use different timezones, the comparison SHALL take timezones into account.

> If the two dates are different, the test does not fail because status changes along the timeline are expected.

The relevant path for this test is:

```{.text sequence-of="jsonpath"}
  $.document.involvement.actions
```

*Example 1 (which fails the test):*

```
  "actions": [
    {
      "acting_entity_refs": [
        "EID-0001"
      ],
      "action_id": "ACN-1",
      "category": "notification",
      "date": "2024-01-10T09:00:00Z",
      "receiving_entity_refs": [
        "EID-0002"
      ],
      "status": "discontinued",
      "summary": "Did not report vulnerability to vendor."
    },
    {
      "acting_entity_refs": [
        "EID-0001"
      ],
      "action_id": "ACN-2",
      "category": "notification",
      "date": "2024-01-10T09:00:00Z",
      "receiving_entity_refs": [
        "EID-0002"
      ],
      "status": "completed",
      "summary": "Reported vulnerability to vendor."
    }
  ],
```

> The list of actions contains two items with contradicting content.
