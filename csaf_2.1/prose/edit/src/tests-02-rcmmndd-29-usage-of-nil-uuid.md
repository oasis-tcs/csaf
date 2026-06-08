### Usage of Nil UUID

It MUST be tested that the Nil UUID is not used as sharing group id.

The relevant path for this test is:

```list-of-jsonpaths
  $.document.distribution.sharing_group.id
```

*Example 1 (which fails the test):*

```
    "distribution": {
      "sharing_group": {
        "id": "00000000-0000-0000-0000-000000000000",
        "name": "No sharing allowed"
      },
      // ...
    },
```

> The sharing group id uses the Nil UUID.

> A tool MAY remove the property `sharing_group` as a quick fix.
