### Actor and Recipient

For each item in `$.document.involvement.actions` it SHALL be tested that an entity is not actor and recipient.
This takes indirect relations through entity groups into account.

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
    "receiving_entity_refs": ["EID-0001"],
    "status": "completed",
    "summary": "Reported vulnerability to vendor."
  },
```

> The action contains `EID-0001` as acting and receiving entity.

> CSAF focusses on the exchange of information.
> Consequently, for vulnerabilities found internal, i.e. a vendor finds a vulnerability in its own product,
> either the `discoverer` part is listed independent of the `vendor` part which results in two entities
> or action is omitted as no information exchange happened, i.e. both parts are the same.
