### Use of Unregistered ID System

For each item in `/vulnerabilities[]/ids` it MUST be tested that the the value of `system_name` belongs to a
registered vulnerability ID system in RVISC.

> The RVISC is available at [cite](#RVISC).

The relevant paths for this test are:

```
  /vulnerabilities[]/ids[]/system_name
```

*Example 1 (which fails the test):*

```
    "ids": [
      {
        "system_name": "OASIS Open CSAF TC GitHub Issues",
        "text": "Issue 1217"
      }
    ]
```

> The `system_name` is not one that is registered in RVISC.
