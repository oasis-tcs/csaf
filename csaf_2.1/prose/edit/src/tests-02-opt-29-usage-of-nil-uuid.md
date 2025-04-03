### Usage of Nil UUID

It MUST be tested that the Nil UUID is not used as sharing group id.

The relevant path for this test is:

```
  /document/distribution/sharing_group/id
```

*Example 1 (which fails the test):*

```
    "distribution": {
      "sharing_group": {
        "id": "ffffffff-ffff-ffff-ffff-ffffffffffff",
        "name": "Public"
      },
      // ...
    },
```

> The sharing group id uses the Nil UUID.

> A tool MAY remove the property `sharing_group` as a quick fix.
