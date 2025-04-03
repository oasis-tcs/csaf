### Usage of Sharing Group on TLP:CLEAR{#usage-of-sharing-group-on-tlp-clear}

It MUST be tested that no sharing group is used if the document is `TLP:CLEAR`.

The relevant path for this test is:

```
  /document/distribution/sharing_group
```

*Example 1 (which fails the test):*

```
    "distribution": {
      "sharing_group": {
        "id": "ffffffff-ffff-ffff-ffff-ffffffffffff",
        "name": "Public"
      },
      "tlp": {
        "label": "CLEAR"
      }
    },
```

> The CSAF document is `TLP:CLEAR` but a sharing group is given.

> A tool MAY remove the property `sharing_group` as a quick fix.
