### Matching Text for Registered ID System

For each item in `/vulnerabilities[]/ids` that the value of a registered vulnerability ID system as `system_name`,
it MUST be tested that the `text` in the CSAF document matches the `text_pattern` given by the
"Registry for Vulnerability ID Systems for CSAF" (RVISC).

> The RVISC is available at [cite](#RVISC).

The relevant paths for this test are:

```
  /vulnerabilities[]/ids[]/text
```

*Example 1 (which fails the test):*

```
    "ids": [
      {
        "system_name": "https://github.com/oasis-tcs/csaf",
        "text": "Issue 1217"
      }
    ]
```

> The `system_name` contains a registered vulnerability ID system but the value of `text` does not match the `text_pattern`
> stated for "OASIS Open CSAF TC GitHub Issues" in the RVISC.
