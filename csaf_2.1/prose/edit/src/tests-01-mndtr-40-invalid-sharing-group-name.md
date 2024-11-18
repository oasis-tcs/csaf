### Invalid Sharing Group Name

It MUST be tested that the value of sharing group name does not equal the reserved values from section [#cite](document-property---distribution---sharing-group) if the precondition is not fulfilled.

The relevant path for this test is:

```
  /document/distribution/sharing_group/name
```

*Example 1 (which fails the test):*

```
    "distribution": {
      "sharing_group": {
        "id": "5868d6be-b28a-404e-a245-0b5093b31b8b",
        "name": "Public"
      },
      // ...
    },
```

> The sharing group name is `Public` but it does not use the Max UUID.
