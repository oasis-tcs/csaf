#### Completed Notification without any Confirmation

For each item in `$.document.involvement.actions` with the `category` value of `notification` and `status` value of `completed`
it SHALL be tested that at least one of the receiving entities mentioned provided a confirmation to it within `15` days.
As the timestamps might use different timezones, the comparison SHALL take timezones into account.
This takes indirect relations through entity groups into account.

In practice, receiving entities with categories `adversary`, `public` or `user` usually do not provide confirmations.
Therefore, missing confirmations of those entities SHALL be ignored for the test result.

> The result of the test is dependent upon the time of the execution of the test - it might change for a given CSAF document over time.
> However, the latest version of a CSAF document should pass the test.
> If no confirmation is received within 15 days, other `status` values should be considered.

The relevant path for this test is:

```list-of-jsonpaths
  $.document.involvement.actions[*]
```

*Example 1 (which fails the test):*

```
  "document": {
    // ...
    "involvement": {
      "actions": [
        {
          "acting_entity_refs": [
            "EID-0001"
          ],
          "action_id": "ACN-1",
          "category": "notification",
          "date": "2024-01-01T09:00:00Z",
          "receiving_entity_refs": [
            "EID-0002"
          ],
          "status": "completed",
          "summary": "Reported vulnerability to vendor."
        }
      ],
      "entities": [
        {
          "category": "discoverer",
          "entity_id": "EID-0001",
          "name": "Jane Researcher"
        },
        {
          "category": "vendor",
          "entity_id": "EID-0002",
          "name": "Example Company"
        }
      ]
    },
    // ...
    "tracking": {
      "current_release_date": "2024-01-24T10:00:00.000Z",
      // ...
    }
  }
```

> `ACN-1` is a notification to `EID-0002` which has a `category` value of `vendor`.
> However, there is no confirmation for `ACN-1` within the 15 days window.
