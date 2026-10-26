### Non-Draft Initial Release Date

It SHALL be tested that the value of `$.document.tracking.initial_release_date` is equal to the value of `date` of the revision history item
that has a `number` of `1` or `1.0.0` when the document status is `final` or `interim`.
As the timestamps might use different timezones, the comparison SHALL take timezones into account.
The test SHALL fail with a different error message if the `date` of the revision history item that has a `number` of `1` or `1.0.0`
cannot be determined.

The relevant path for this test is:

```{.text sequence-of="jsonpath"}
  $.document.tracking.initial_release_date
```

*Example 1 (which fails the test):*

```
  "tracking": {
    // ...
    "initial_release_date": "2024-01-22T10:00:00.000Z",
    "revision_history": [
      // ...
      {
        "date": "2024-01-21T10:00:00.000Z",
        "number": "1",
        "summary": "Initial version."
      }
    ],
    "status": "final",
    // ...
  }
```

> The document status is `final` but the revision history item which has `1` as value for `number` has a different `date`
> than given through the `initial_release_date`.

> A tool MAY set the `initial_release_date` from the `date` of the revision history item with a `number` of `1` or `1.0.0` as a quick fix.
