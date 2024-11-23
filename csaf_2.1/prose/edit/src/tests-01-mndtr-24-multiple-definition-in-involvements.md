### Multiple Definition in Involvements

It MUST be tested that items of the list of involvements do not contain the same `party` regardless of its `status` more than once at any `date`.

The relevant path for this test is:

```
    /vulnerabilities[]/involvements
```

  > For the significance of the left pointing arrow character (`←`) at the end of the summary value line in the following example 1 please
  > cf. the guidance in section [sec](#typographical-conventions).

*Example 1 (which fails the test):*

```
  "vulnerabilities": [
    {
      "involvements": [
        {
          "date": "2023-08-23T10:00:00.000Z",
          "party": "vendor",
          "status": "completed"
        },
        {
          "date": "2023-08-23T10:00:00.000Z",
          "party": "vendor",
          "status": "in_progress",
          "summary": "The vendor has released a mitigation and is working to fully←
           resolve the issue."
        }
      ]
    }
  ]
```

> The list of involvements contains two items with the same tuple `party` and `date`.
