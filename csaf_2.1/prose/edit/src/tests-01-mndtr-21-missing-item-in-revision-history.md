### Missing Item in Revision History

It MUST be tested that items of the revision history do not omit a version number when the items are sorted ascending by `date` and as a second level criteria `number`.

> Dates are used as primary sorting criteria as they correspond to publications.
> The assigned numbers might be incorrect.
> Issuing parties are advised to investigate the issue and fix errors by providing the factual revision history with one entry per release.
> Note that this might lead to a situation where an invalid revision history is corrected by modifying the `number` in a revision history item
> to a lower value as required by this test.
> Nevertheless, the newly added item created to release the corrected version of the document to the intended target group will have a newer
> timestamp and therefore show up correctly at CSAF consumers.

As the timestamps might use different timezones, the sorting MUST take timezones into account.
The error message MUST differentiate between a version number not present at all and one that is missing in the sorted list.
In the case of semantic versioning, this applies only to the Major version.
It MUST also be tested that the first item in such a sorted list has either the version number 0 or 1 in the case of integer versioning or
a Major version of 0 or 1 in the case of semantic versioning.

The relevant path for this test is:

```list-of-jsonpaths
  $.document.tracking.revision_history
```

*Example 1 (which fails the test):*

```
    "revision_history": [
      {
        "date": "2023-08-22T10:00:00.000Z",
        "number": "1",
        "summary": "Initial version."
      },
      {
        "date": "2024-01-21T10:00:00.000Z",
        "number": "3",
        "summary": "Some other changes."
      }
    ]
```

> The item for version `2` is missing.

> A tool MAY add a stub for the missing item to the revision history as a quick fix.
> The stub might miss the `date` and `summary` which have to be provided by the user or other data sources.
