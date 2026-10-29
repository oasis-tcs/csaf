#### Explicit Reference to all Vulnerabilities

For each item in `$.document.involvement.actions`
it SHALL be tested that the action does not mention all vulnerability items of the document explicitly.

> If all vulnerabilities are referenced through the `dl_vuln_ids` element,
> it is semantically identical to an action without the `dl_vuln_ids` element.
> As the latter is shorter, it is the preferred way in CSAF to represent this scenario.
>
> Note to implementers:
> This test cannot fail, if
>
> 1. at least one vulnerability item exists that does not define a `dl_vuln_id` element (as such item cannot be mention in an action) or
> 2. the length of the `dl_vuln_ids` array in the action is smaller that the length of the array `$.vulnerabilities`.

The relevant path for this test is:

```{.text sequence-of="jsonpath"}
  $.document.involvement.actions[*].dl_vuln_ids[*]
```

*Example 1 (which fails the test):*

```
  {
    // ...
    "document": {
      // ...
      "involvement": {
        "actions": [
          {
            // ...
            "action_id": "ACN-1",
            // ...
            "dl_vuln_ids": [
              "VULN-1"
            ],
            // ...
          },
          // ...
        ],
        // ...
      },
      // ...
    },
    "vulnerabilities": [
      {
        "dl_vuln_id": "VULN-1",
        "title": "A vulnerability explicitly referenced."
      }
    ]
  }
```

> `ACN-1` mentions all vulnerabilites from the CSAF document explicitly.

> A tool MAY remove such `dl_vuln_ids` element as a quick fix.
