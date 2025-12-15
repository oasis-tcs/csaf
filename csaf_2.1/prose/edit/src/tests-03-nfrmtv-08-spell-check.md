### Spell Check

If the document language is given it MUST be tested that a spell check for the given language does not find any mistakes.
The test SHALL be skipped if the document language is not set.
It SHALL fail if the given language is not supported.
The value of `/document/category` SHOULD NOT be tested if the CSAF document does not use the profile "CSAF Base".

The relevant paths for this test are:

```
  /document/acknowledgments[]/names[]
  /document/acknowledgments[]/organization
  /document/acknowledgments[]/summary
  /document/aggregate_severity/text
  /document/category
  /document/distribution/text
  /document/notes[]/audience
  /document/notes[]/text
  /document/notes[]/title
  /document/publisher/issuing_authority
  /document/publisher/name
  /document/references[]/summary
  /document/title
  /document/tracking/aliases[]
  /document/tracking/generator/engine/name
  /document/tracking/revision_history[]/summary
  /product_tree/branches[](/branches[])*/name
  /product_tree/branches[](/branches[])*/product/name
  /product_tree/branches[]/name
  /product_tree/branches[]/product/name
  /product_tree/full_product_names[]/name
  /product_tree/product_groups[]/summary
  /product_tree/relationships[]/full_product_name/name
  /vulnerabilities[]/acknowledgments[]/names[]
  /vulnerabilities[]/acknowledgments[]/organization
  /vulnerabilities[]/acknowledgments[]/summary
  /vulnerabilities[]/involvements[]/summary
  /vulnerabilities[]/notes[]/audience
  /vulnerabilities[]/notes[]/text
  /vulnerabilities[]/notes[]/title
  /vulnerabilities[]/references[]/summary
  /vulnerabilities[]/remediations[]/details
  /vulnerabilities[]/remediations[]/entitlements[]
  /vulnerabilities[]/remediations[]/restart_required/details
  /vulnerabilities[]/threats[]/details
  /vulnerabilities[]/title
```

*Example 1 (which fails the test):*

```
  "document": {
    // ...
    "lang": "en",
    "notes": [
      {
        "category": "summary",
        "text": "Secruity researchers found multiple vulnerabilities in XYZ."
      }
    ],
    // ...
  }
```

> There is a spelling mistake in `Secruity`.
