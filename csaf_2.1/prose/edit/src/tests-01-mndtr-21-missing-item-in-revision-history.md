### Missing Item in Revision History

It SHALL be tested that items of the revision history do not omit a version number when the items are sorted ascending by `date` and as a second level criteria `number`.

> Dates are used as primary sorting criteria as they correspond to publications.
> The assigned numbers might be incorrect.
> Issuing parties are advised to investigate the issue and fix errors by providing the factual revision history with one entry per release.
> Note that this might lead to a situation where an invalid revision history is corrected by modifying the `number` in a revision history item
> to a lower value as required by this test.
> Nevertheless, the newly added item created to release the corrected version of the document to the intended target group will have a newer
> timestamp and therefore show up correctly at CSAF consumers.

As the timestamps might use different timezones, the sorting SHALL take timezones into account.
The error message SHALL differentiate between a version number not present at all and one that is missing in the sorted list.
In the case of semantic versioning in accordance with the rules from section [sec](#version-type---semantic-versioning),
Minor and Patch versions MAY end at any point if the next version has a higher Major respectively Minor version.
It SHALL also be tested that the first item in such a sorted list has either the version number 0 or 1 in the case of integer versioning or
a Major version of 0 or 1 in the case of semantic versioning.

In order to create consistent results in the case of mixed integer and semantic versioning (failing test
[sec](#mixed-integer-and-semantic-versioning)), implementations SHALL map items with integer versioning to
semantic versioning by appending `.0.0` to the corresponding values.
Any value that is not a valid integer nor semantic version SHOULD be ignored in this test as the schema test will fail.
The aforementioned rules are solely used during the processing to create consistent test results.

> This processing rules are not a suggested quick fix for test [sec](#mixed-integer-and-semantic-versioning)
> but implementation guidance for this edge case.

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
