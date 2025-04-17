### Profile Tests{#optional-profile-tests}

This subsubsection structures the optional tests for the profiles. Not all tests apply for all profiles.
Tests SHOULD be skipped if the document category does not match the one given in the test.
Each of the following tests SHOULD be treated as they where listed similar to the other tests.

#### Missing Fixed Product

For each product listed in the product status group affected in any vulnerability,
it MUST be tested that a corresponding version of the product is listed as fixed in the same vulnerability.
The test MUST be skipped if there is a clear indication, that such a version of the product does not exist.
Indicators include a remediation item with one of the categories `fix_planned`, `no_fix_planned` or `none_available` referring to the affected product.
The test MUST NOT be skipped, if there is an indication, that such a version of the product might exist.
Indicators include an affected product version range with the comparator `<` in the last version constraint and
a remediation item with the categories `vendor_fix` referring to the affected product.

The relevant value for `/document/category` is:

```
  csaf_security_advisory
```

The relevant path for this test is:

```
  /vulnerabilities[]/product_status
```

*Example 1 (which fails the test):*

```
  "vulnerabilities": [
    {
      // ...
      "product_status": {
        "known_affected": [
          "CSAFPID-9080700"
        ]
      },
      "remediations": [
        {
          "category": "vendor_fix",
          "details": "Update to the latest version, at least version 4.2.",
          "product_ids": [
            "CSAFPID-9080700"
          ]
        }
      ]
    }
  ]
```

> The fixed product is not listed in the advisory but there is a clear indication that such product exists as there is a remediation
> with category `vendor_fix`.

> A tool MAY create the missing fixed product based on the data available in the advisory as a quick fix.

#### Language Specific Reasoning for Withdrawal

If the document language is not English or unspecified, it MUST be tested that exactly one item in document notes exists
that has the language specific translation of the term `Reasoning for Withdrawal` as `title`.
The `category` of this item MUST be `description`.
If no language specific translation has been recorded, the test MUST be skipped and output an information to the user that no such translation is known.

> A list of the language specific translations is kept at the OASIS CSAF TC.

The relevant value for `/document/category` is:

```
  csaf_withdrawn
```

The relevant path for this test is:

```
  /document/notes
```

*Example 1 (which fails the test):*

```
  {
    "category": "summary",
    "text": "Das CSAF Document enthielt Beispieldaten und wurde zurückgezogen, um Testdaten zu erzeugen.",
    "title": "Begründung für die Zurückziehung"
  }
```

> The note has the correct title. However, it uses the wrong category.