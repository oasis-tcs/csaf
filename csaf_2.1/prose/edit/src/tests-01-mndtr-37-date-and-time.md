### Date and Time{#mandatory-tests--date-and-time}

For each item of type `string` and format `date-time` it MUST be tested that it conforms to the rules given in section [sec]{#date-and-time}.

The relevant path for this test is:

```
  /document/tracking/current_release_date
  /document/tracking/generator/date
  /document/tracking/initial_release_date
  /document/tracking/revision_history[]/date
  /vulnerabilities[]/disclosure_date
  /vulnerabilities[]/discovery_date
  /vulnerabilities[]/flags[]/date
  /vulnerabilities[]/involvements[]/date
  /vulnerabilities[]/remediations[]/date
  /vulnerabilities[]/threats[]/date
```

*Example 1 (which fails the test):*

```
      "current_release_date": "2024-01-24 10:00:00.000Z",
```

> The `current_release_date` uses a whitespace as separator instead the letter `T`.
