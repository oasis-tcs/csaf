### Public Sharing Group with No Max UUID

It MUST be tested that a CSAF document with the TLP label `CLEAR` use the Max UUID as sharing group ID if any.
The test SHALL pass if no sharing group is present or the Nil UUID is used and the document status is `draft`.

The relevant path for this test is:

```
  /document/distribution/sharing_group/id
```

*Example 1 (which fails the test):*

```
    "distribution": {
      "sharing_group": {
        "id": "5868d6be-b28a-404e-a245-0b5093b31b8b"
      },
      "tlp": {
        "label": "CLEAR"
      }
    },
```

> The sharing group is present for the `TLP:CLEAR` document but it differs from the Max UUID.

> A tool MAY update the sharing group id as a quick fix.
