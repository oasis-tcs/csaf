### Non-Public Sharing Group with Max UUID

It MUST be tested that a CSAF document using Max UUID as sharing group ID has the TLP label `CLEAR`.

The relevant path for this test is:

```
  /document/distribution/tlp/label
```

*Example 1 (which fails the test):*

```
    "distribution": {
      "sharing_group": {
        "id": "ffffffff-ffff-ffff-ffff-ffffffffffff",
        "name": "Public"
      },
      "tlp": {
        "label": "RED"
      }
    },
```

> The sharing group uses the Max UUID but the CSAF document is labeled as `TLP:RED`.
