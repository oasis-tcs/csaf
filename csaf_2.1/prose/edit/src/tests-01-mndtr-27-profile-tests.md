### Profile Tests

This subsubsection structures the tests for the profiles. Not all tests apply for all profiles.
Tests SHOULD be skipped if the document category does not match the one given in the test.
Each of the following tests SHOULD be treated as they where listed similar to the other tests.

> An application MAY group these tests by profiles when providing the additional function to only run one or more selected tests.
> This results in one virtual test per profile.

#### Document Notes

It MUST be tested that at least one item in `/document/notes` exists which has a `category` of `description`, `details`, `general` or `summary`.

The relevant values for `/document/category` are:

```
  csaf_informational_advisory
  csaf_security_incident_response
```

The relevant path for this test is:

```
  /document/notes
```

*Example 1 (which fails the test):*

```
  "notes": [
    {
      "category": "legal_disclaimer",
      "text": "The CSAF document is provided to You \"AS IS\" and \"AS AVAILABLE\" and with all faults and defects without warranty of any kind.",
      "title": "Terms of Use"
    }
  ]
```

> The document notes do not contain an item which has a `category` of `description`, `details`, `general` or `summary`.

#### Document References

It MUST be tested that at least one item in `/document/references` exists that has links to an `external` source.

The relevant values for `/document/category` are:

```
  csaf_informational_advisory
  csaf_security_incident_response
```

The relevant path for this test is:

```
  /document/references
```

*Example 1 (which fails the test):*

```
  "references": [
    {
      "category": "self",
      "summary": "The canonical URL.",
      "url": "https://example.com/security/data/csaf/2024/oasis_csaf_tc-csaf_2_1-2024-6-1-27-02-01.json"
    }
  ]
```

> The document references do not contain any item which has the category `external`.

#### Vulnerabilities{#vulnerabilities-for-informational-advisory}

It MUST be tested that the element `/vulnerabilities` does not exist.

The relevant value for `/document/category` is:

```
  csaf_informational_advisory
```

The relevant path for this test is:

```
  /vulnerabilities
```

*Example 1 (which fails the test):*

```
  "vulnerabilities": [
    {
      "title": "A vulnerability item that SHALL NOT exist"
    }
  ]
```

> The element `/vulnerabilities` exists.

> A tool MAY change the `/document/category` to `csaf_base` as a quick fix.

#### Product Tree

It MUST be tested that the element `/product_tree` exists.

The relevant values for `/document/category` are:

```
  csaf_security_advisory
  csaf_vex
```

The relevant path for this test is:

```
  /product_tree
```

*Example 1 (which fails the test):*

```
  {
    "document": {
      // ...
    },
    "vulnerabilities": [
      // ...
    ]
  }
```

> The element `/product_tree` does not exist.

#### Vulnerability Notes

For each item in `/vulnerabilities` it MUST be tested that the element `notes` exists.

The relevant values for `/document/category` are:

```
  csaf_security_advisory
  csaf_vex
```

The relevant path for this test is:

```
  /vulnerabilities[]/notes
```

*Example 1 (which fails the test):*

```
  "vulnerabilities": [
    {
      "title": "A vulnerability item without a note"
    }
  ]
```

> The vulnerability item has no `notes` element.

#### Product Status

For each item in `/vulnerabilities` it MUST be tested that the element `product_status` exists.

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
      "title": "A vulnerability item without a product status"
    }
  ]
```

> The vulnerability item has no `product_status` element.

#### VEX Product Status

For each item in `/vulnerabilities` it MUST be tested that at least one of the elements `fixed`, `known_affected`, `known_not_affected`,
or `under_investigation` is present in `product_status`.

The relevant value for `/document/category` is:

```
  csaf_vex
```

The relevant paths for this test are:

```
  /vulnerabilities[]/product_status/fixed
  /vulnerabilities[]/product_status/known_affected
  /vulnerabilities[]/product_status/known_not_affected
  /vulnerabilities[]/product_status/under_investigation
```

*Example 1 (which fails the test):*

```
  "product_status": {
    "first_fixed": [
      // ...
    ],
    "recommended": [
      // ...
    ]
  }
```

> None of the elements `fixed`, `known_affected`, `known_not_affected`, or `under_investigation` is present in `product_status`.

#### Vulnerability ID

For each item in `/vulnerabilities` it MUST be tested that at least one of the elements `cve` or `ids` is present.

The relevant value for `/document/category` is:

```
  csaf_vex
```

The relevant paths for this test are:

```
  /vulnerabilities[]/cve
  /vulnerabilities[]/ids
```

*Example 1 (which fails the test):*

```
  "vulnerabilities": [
    {
      "title": "A vulnerability item without a CVE or ID"
    }
  ]
```

> None of the elements `cve` or `ids` is present.

#### Impact Statement

For each item in `/vulnerabilities[]/product_status/known_not_affected` it MUST be tested that
a corresponding impact statement exist in `/vulnerabilities[]/flags` or `/vulnerabilities[]/threats`.
For the latter one, the `category` value for such a statement MUST be `impact`.

The relevant value for `/document/category` is:

```
  csaf_vex
```

The relevant path for this test is:

```
  /vulnerabilities[]/flags
  /vulnerabilities[]/threats
```

*Example 1 (which fails the test):*

```
  "product_tree": {
    "full_product_names": [
      {
        "product_id": "CSAFPID-9080700",
        "name": "Product A"
      },
      {
        "product_id": "CSAFPID-9080701",
        "name": "Product B"
      },
      {
        "product_id": "CSAFPID-9080702",
        "name": "Product C"
      }
    ],
    "product_groups": [
      {
        "group_id": "CSAFGID-0001",
        "product_ids": [
          "CSAFPID-9080700",
          "CSAFPID-9080701"
        ]
      }
    ]
  },
  "vulnerabilities": [
    {
      // ...
      "product_status": {
        "known_not_affected": [
          "CSAFPID-9080700",
          "CSAFPID-9080701",
          "CSAFPID-9080702"
        ]
      },
      "threats": [
        {
          "category": "impact",
          "details": "The vulnerable code is not present in these products.",
          "group_ids": [
            "CSAFGID-0001"
          ]
        }
      ]
    }
  ]
```

> There is no impact statement for `CSAFPID-9080702`.
>
> Note: The impact statement for `CSAFPID-9080700` and `CSAFPID-9080701` is given through `CSAFGID-0001`.

#### Action Statement

For each item in `/vulnerabilities[]/product_status/known_affected` it MUST be tested that
a corresponding action statement exist in `/vulnerabilities[]/remediations`.

The relevant value for `/document/category` is:

```
  csaf_vex
```

The relevant path for this test is:

```
  /vulnerabilities[]/remediations
```

*Example 1 (which fails the test):*

```
  "product_tree": {
    "full_product_names": [
      {
        "product_id": "CSAFPID-9080700",
        "name": "Product A"
      },
      {
        "product_id": "CSAFPID-9080701",
        "name": "Product B"
      },
      {
        "product_id": "CSAFPID-9080702",
        "name": "Product C"
      }
    ],
    "product_groups": [
      {
        "group_id": "CSAFGID-0001",
        "product_ids": [
          "CSAFPID-9080700",
          "CSAFPID-9080701"
        ],
        "summary": "EOL products"
      }
    ]
  },
  "vulnerabilities": [
    {
      // ...
      "product_status": {
        "known_affected": [
          "CSAFPID-9080700",
          "CSAFPID-9080701",
          "CSAFPID-9080702"
        ]
      },
      "remediations": [
        {
          "category": "no_fix_planned",
          "details": "These products are end-of-life. Therefore, no fix will be provided.",
          "group_ids": [
            "CSAFGID-0001"
          ]
        }
      ]
    }
  ]
```

> There is no action statement for `CSAFPID-9080702`.
>
> Note: The action statement for `CSAFPID-9080700` and `CSAFPID-9080701` is given through `CSAFGID-0001`.

#### Vulnerabilities{#vulnerabilities-for-security-advisory-or-vex}

It MUST be tested that the element `/vulnerabilities` exists.

The relevant values for `/document/category` are:

```
  csaf_security_advisory
  csaf_vex
```

The relevant path for this test is:

```
  /vulnerabilities
```

*Example 1 (which fails the test):*

```
  {
    "document": {
      // ...
    },
    "product_tree": [
      // ...
    ]
  }
```

> The element `/vulnerabilities` does not exist.
