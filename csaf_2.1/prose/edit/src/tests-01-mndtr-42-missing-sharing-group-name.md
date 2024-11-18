### Missing Sharing Group Name

It MUST be tested that the sharing group name exists and equals the predefined reserved value from section [sec](#document-property-distribution-sharing-group) if the precondition is fulfilled.

The relevant path for this test is:

```
  /document/distribution/sharing_group/name
```

*Example 1 (which fails the test):*

```
    "distribution": {
      "sharing_group": {
        "id": "ffffffff-ffff-ffff-ffff-ffffffffffff"
      },
      // ...
    },
```

> The Max UUID is used but the sharing group name does not exist.

> A tool MAY add the corresponding sharing group name as a quick fix.
