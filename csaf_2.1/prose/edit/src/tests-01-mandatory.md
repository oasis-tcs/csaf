## 6.1 Mandatory Tests

Mandatory tests MUST NOT fail at a valid CSAF document. A program MUST handle a test failure as an error.

### 6.1.1 Missing Definition of Product ID

For each element of type `/$defs/product_id_t` which is not inside a Full Product Name (type: `full_product_name_t`) and therefore reference an element within the `product_tree` it MUST be tested that the Full Product Name element with the matching `product_id` exists. The same applies for all items of elements of type `/$defs/products_t`.

The relevant paths for this test are:

```
  /product_tree/product_groups[]/product_ids[]
  /product_tree/relationships[]/product_reference
  /product_tree/relationships[]/relates_to_product_reference
  /vulnerabilities[]/product_status/first_affected[]
  /vulnerabilities[]/product_status/first_fixed[]
  /vulnerabilities[]/product_status/fixed[]
  /vulnerabilities[]/product_status/known_affected[]
  /vulnerabilities[]/product_status/known_not_affected[]
  /vulnerabilities[]/product_status/last_affected[]
  /vulnerabilities[]/product_status/recommended[]
  /vulnerabilities[]/product_status/under_investigation[]
  /vulnerabilities[]/remediations[]/product_ids[]
  /vulnerabilities[]/scores[]/products[]
  /vulnerabilities[]/threats[]/product_ids[]
```

*Example 49 which fails the test:*

```
  "product_tree": {
    "product_groups": [
      {
        "group_id": "CSAFGID-1020300",
        "product_ids": [
          "CSAFPID-9080700",
          "CSAFPID-9080701"
        ]
      }
    ]
  }
```

> Neither `CSAFPID-9080700` nor `CSAFPID-9080701` were defined in the `product_tree`.

### 6.1.2 Multiple Definition of Product ID

For each Product ID (type `/$defs/product_id_t`) in Full Product Name elements (type: `/$defs/full_product_name_t`) it MUST be tested that the `product_id` was not already defined within the same document.

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/product/product_id
  /product_tree/full_product_names[]/product_id
  /product_tree/relationships[]/full_product_name/product_id
```

*Example 50 which fails the test:*

```
  "product_tree": {
    "full_product_names": [
      {
        "product_id": "CSAFPID-9080700",
        "name": "Product A"
      },
      {
        "product_id": "CSAFPID-9080700",
        "name": "Product B"
      }
    ]
  }
```

> `CSAFPID-9080700` was defined twice.

### 6.1.3 Circular Definition of Product ID

For each new defined Product ID (type `/$defs/product_id_t`) in items of relationships (`/product_tree/relationships`) it MUST be tested that the `product_id` does not end up in a circle.

The relevant path for this test is:

```
  /product_tree/relationships[]/full_product_name/product_id
```

> As this can be quite complex a program for large CSAF documents, a program could check first whether a Product ID defined in a relationship item is used as `product_reference` or `relates_to_product_reference`. Only for those which fulfill this condition it is necessary to run the full check following the references.

*Example 51 which fails the test:*

```
  "product_tree": {
    "full_product_names": [
      {
        "product_id": "CSAFPID-9080700",
        "name": "Product A"
      }
    ],
    "relationships": [
      {
        "category": "installed_on",
        "full_product_name": {
          "name": "Product B",
          "product_id": "CSAFPID-9080701"
        },
        "product_reference": "CSAFPID-9080700",
        "relates_to_product_reference": "CSAFPID-9080701"
      }
    ]
  }
```

> `CSAFPID-9080701` refers to itself - this is a circular definition.

### 6.1.4 Missing Definition of Product Group ID

For each element of type `/$defs/product_group_id_t` which is not inside a Product Group (`/product_tree/product_groups[]`) and therefore reference an element within the `product_tree` it MUST be tested that the Product Group element with the matching `group_id` exists. The same applies for all items of elements of type `/$defs/product_groups_t`.

The relevant paths for this test are:

```
  /vulnerabilities[]/remediations[]/group_ids
  /vulnerabilities[]/threats[]/group_ids
```

*Example 52 which fails the test:*

```
  "product_tree": {
    "full_product_names": [
      {
        "product_id": "CSAFPID-9080700",
        "name": "Product A"
      }
    ]
  },
  "vulnerabilities": [
    {
      "threats": [
        {
          "category": "exploit_status",
          "details": "Reliable exploits integrated in Metasploit.",
          "group_ids": [
            "CSAFGID-1020301"
          ]
        }
      ]
    }
  ]
```

> `CSAFGID-1020301` was not defined in the Product Tree.

### 6.1.5 Multiple Definition of Product Group ID

For each Product Group ID (type `/$defs/product_group_id_t`) Product Group elements (`/product_tree/product_groups[]`) it MUST be tested that the `group_id` was not already defined within the same document.

The relevant path for this test is:

```
    /product_tree/product_groups[]/group_id
```

*Example 53 which fails the test:*

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
        "group_id": "CSAFGID-1020300",
        "product_ids": [
          "CSAFPID-9080700",
          "CSAFPID-9080701"
        ]
      },
      {
        "group_id": "CSAFGID-1020300",
        "product_ids": [
          "CSAFPID-9080700",
          "CSAFPID-9080702"
        ]
      }
    ]
  }
```

> `CSAFGID-1020300` was defined twice.

### 6.1.6 Contradicting Product Status

For each item in `/vulnerabilities` it MUST be tested that the same Product ID is not member of contradicting product status groups. The sets formed by the contradicting groups within one vulnerability item MUST be pairwise disjoint.

Contradiction groups are:

* Affected:

   ```
   /vulnerabilities[]/product_status/first_affected[]  
   /vulnerabilities[]/product_status/known_affected[]
   /vulnerabilities[]/product_status/last_affected[]
   ```

* Not affected:

  ```
  /vulnerabilities[]/product_status/known_not_affected[]
  ```

* Fixed:

  ```
  /vulnerabilities[]/product_status/first_fixed[]
  /vulnerabilities[]/product_status/fixed[]
  ```

* Under investigation:

  ```
  /vulnerabilities[]/product_status/under_investigation[]
  ```

> Note: An issuer might recommend (`/vulnerabilities[]/product_status/recommended`) a product version from any group - also from the affected group, i.e. if it was discovered that fixed versions introduce a more severe vulnerability.

*Example 54 which fails the test:*

```
  "product_tree": {
    "full_product_names": [
      {
        "product_id": "CSAFPID-9080700",
        "name": "Product A"
      }
    ]
  },
  "vulnerabilities": [
    {
      "product_status": {
        "known_affected": [
          "CSAFPID-9080700"
        ],
        "known_not_affected": [
          "CSAFPID-9080700"
        ]
      }
    }
  ]
```

> `CSAFPID-9080700` is a member of the two contradicting groups "Affected" and "Not affected".

### 6.1.7 Multiple Scores with same Version per Product

For each item in `/vulnerabilities` it MUST be tested that the same Product ID is not member of more than one CVSS-Vectors with the same version.

The relevant path for this test is:

```
    /vulnerabilities[]/scores[]
```

*Example 55 which fails the test:*

```
  "product_tree": {
    "full_product_names": [
      {
        "product_id": "CSAFPID-9080700",
        "name": "Product A"
      }
    ]
  },
  "vulnerabilities": [
    {
      "scores": [
        {
          "products": [
            "CSAFPID-9080700"
          ],
          "cvss_v3": {
            "version": "3.1",
            "vectorString": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H",
            "baseScore": 10,
            "baseSeverity": "CRITICAL"
          }
        },
        {
          "products": [
            "CSAFPID-9080700"
          ],
          "cvss_v3": {
            "version": "3.1",
            "vectorString": "CVSS:3.1/AV:L/AC:L/PR:H/UI:R/S:U/C:H/I:H/A:H",
            "baseScore": 6.5,
            "baseSeverity": "MEDIUM"
          }
        }
      ]
    }
  ]
```

> Two CVSS v3.1 scores are given for `CSAFPID-9080700`.

### 6.1.8 Invalid CVSS

It MUST be tested that the given CVSS object is valid according to the referenced schema.

The relevant paths for this test are:

```
  /vulnerabilities[]/scores[]/cvss_v2
  /vulnerabilities[]/scores[]/cvss_v3
```

*Example 56 which fails the test:*

```
  "cvss_v3": {
    "version": "3.1",
    "vectorString": "CVSS:3.1/AV:L/AC:L/PR:H/UI:R/S:U/C:H/I:H/A:H",
    "baseScore": 6.5
  }
```

> The required element `baseSeverity` is missing.

> A tool MAY add one or more of the missing properties `version`, `baseScore` and `baseSeverity` based on the values given in `vectorString` as quick fix.

### 6.1.9 Invalid CVSS computation

It MUST be tested that the given CVSS object has the values computed correctly according to the definition.

> The `vectorString` SHOULD take precedence.

The relevant paths for this test are:

```
  /vulnerabilities[]/scores[]/cvss_v2/baseScore
  /vulnerabilities[]/scores[]/cvss_v2/temporalScore
  /vulnerabilities[]/scores[]/cvss_v2/environmentalScore
  /vulnerabilities[]/scores[]/cvss_v3/baseScore
  /vulnerabilities[]/scores[]/cvss_v3/baseSeverity
  /vulnerabilities[]/scores[]/cvss_v3/temporalScore
  /vulnerabilities[]/scores[]/cvss_v3/temporalSeverity
  /vulnerabilities[]/scores[]/cvss_v3/environmentalScore
  /vulnerabilities[]/scores[]/cvss_v3/environmentalSeverity
```

*Example 57 which fails the test:*

```
  "cvss_v3": {
    "version": "3.1",
    "vectorString": "CVSS:3.1/AV:L/AC:L/PR:H/UI:R/S:U/C:H/I:H/A:H",
    "baseScore": 10.0,
    "baseSeverity": "LOW"
  }
```

> Neither `baseScore` nor `baseSeverity` has the correct value according to the specification.

> A tool MAY set the correct values as computed according to the specification as quick fix.

### 6.1.10 Inconsistent CVSS

It MUST be tested that the given CVSS properties do not contradict the CVSS vector.

The relevant paths for this test are:

```
  /vulnerabilities[]/scores[]/cvss_v2
  /vulnerabilities[]/scores[]/cvss_v3
```

*Example 58 which fails the test:*

```
  "cvss_v3": {
    "version": "3.1",
    "vectorString": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",
    "baseScore": 9.8,
    "baseSeverity": "CRITICAL",
    "attackVector": "LOCAL",
    "attackComplexity": "LOW",
    "privilegesRequired": "NONE",
    "userInteraction": "NONE",
    "scope": "CHANGED",
    "confidentialityImpact": "HIGH",
    "integrityImpact": "HIGH",
    "availabilityImpact": "LOW"
  }
```

> The values in CVSS vector differs from values of the properties `attackVector`, `scope` and `availabilityImpact`.

> A tool MAY overwrite contradicting values according to the `vectorString` as quick fix.

### 6.1.11 CWE

It MUST be tested that given CWE exists and is valid.

The relevant path for this test is:

```
    /vulnerabilities[]/cwe
```

*Example 59 which fails the test:*

```
  "cwe": {
    "id": "CWE-79",
    "name": "Improper Input Validation"
  }
```

> The `CWE-79` exists. However, its name is `Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')`.

### 6.1.12 Language

For each element of type `/$defs/language_t` it MUST be tested that the language code is valid and exists.

The relevant paths for this test are:

```
  /document/lang
  /document/source_lang
```

*Example 60 which fails the test:*

```
  "lang": "EZ"
```

> `EZ` is not a valid language. It is the subtag for the region "Eurozone".

> For any deprecated subtag, a tool MAY replace it with its preferred value as a quick fix.

### 6.1.13 PURL

It MUST be tested that given PURL is valid.

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/product/product_identification_helper/purl
  /product_tree/full_product_names[]/product_identification_helper/purl
  /product_tree/relationships[]/full_product_name/product_identification_helper/purl
```

*Example 61 which fails the test:*

```
  "product_tree": {
    "full_product_names": [
      {
        "name": "Product A",
        "product_id": "CSAFPID-9080700",
        "product_identification_helper": {
          "purl": "pkg:maven/@1.3.4"
        }
      }
    ]
  }
```

> Any valid purl has a name component.

### 6.1.14 Sorted Revision History

It MUST be tested that the value of `number` of items of the revision history are sorted ascending when the items are sorted ascending by `date`.

The relevant path for this test is:

```
    /document/tracking/revision_history
```

*Example 62 which fails the test:*

```
  "revision_history": [
    {
      "date": "2021-07-22T10:00:00.000Z",
      "number": "2",
      "summary": "Second version."
    },
    {
      "date": "2021-07-23T10:00:00.000Z",
      "number": "1",
      "summary": "Initial version."
    }
  ]
```

> The first item has a higher version number than the second.

### 6.1.15 Translator

It MUST be tested that `/document/source_lang` is present and set if the value `translator` is used for `/document/publisher/category`.

The relevant path for this test is:

```
    /document/source_lang
```

*Example 63 which fails the test:*

```
  "document": {
    // ...
    "publisher": {
      "category": "translator",
      "name": "CSAF TC Translator",
      "namespace": "https://csaf.io/translator"
    },
    "title": "Mandatory test: Translator (failing example 1)",
    // ...
  }
```

> The required element `source_lang` is missing.

### 6.1.16 Latest Document Version

It MUST be tested that document version has the same value as the the `number` in the last item of Revision History when it is sorted ascending by `date`. Build metadata is ignored in the comparison. Any pre-release part is also ignored if the document status is `draft`.

The relevant path for this test is:

```
    /document/tracking/version
```

*Example 64 which fails the test:*

```
  "tracking": {
    // ...
    "revision_history": [
      {
        "date": "2021-07-21T09:00:00.000Z",
        "number": "1",
        "summary": "Initial version."
      },
      {
        "date": "2021-07-21T10:00:00.000Z",
        "number": "2",
        "summary": "Second version."
      }
    ],
    // ...
    "version": "1"
  }
```

> The value of `number` of the last item after sorting is `2`. However, the document version is `1`.

### 6.1.17 Document Status Draft

It MUST be tested that document status is `draft` if the document version is `0` or `0.y.z` or contains the pre-release part.

The relevant path for this test is:

```
    /document/tracking/status
```

*Example 65 which fails the test:*

```
    "tracking": {
      // ...
      "status": "final",
      "version": "0.9.5"
    }
```

> The `/document/tracking/version` is `0.9.5` but the document status is `final`.

### 6.1.18 Released Revision History

It MUST be tested that no item of the revision history has a `number` of `0` or `0.y.z` when the document status is `final` or `interim`.

The relevant path for this test is:

```
    /document/tracking/revision_history[]/number
```

*Example 66 which fails the test:*

```
    "tracking": {
      // ...
      "revision_history": [
        {
          "date": "2021-05-17T10:00:00.000Z",
          "number": "0",
          "summary": "First draft"
        },
        {
          "date": "2021-07-21T10:00:00.000Z",
          "number": "1",
          "summary": "Initial version."
        }
      ],
      "status": "final",
      "version": "1"
    }
```

> The document status is `final` but the revision history includes an item which has `0` as value for `number`.

### 6.1.19 Revision History Entries for Pre-release Versions

It MUST be tested that no item of the revision history has a `number` which includes pre-release information.

The relevant path for this test is:

```
    /document/tracking/revision_history[]/number
```

*Example 67 which fails the test:*

```
    "revision_history": [
      {
        "date": "2021-04-22T10:00:00.000Z",
        "number": "1.0.0-rc",
        "summary": "Release Candidate for initial version."
      },
      {
        "date": "2021-04-23T10:00:00.000Z",
        "number": "1.0.0",
        "summary": "Initial version."
      }
    ]
```

> The revision history contains an item which has a `number` that indicates that this is pre-release.

### 6.1.20 Non-draft Document Version

It MUST be tested that document version does not contain a pre-release part if the document status is `final` or `interim`.

The relevant path for this test is:

```
    /document/tracking/version
```

*Example 68 which fails the test:*

```
    "tracking": {
      // ...
      "status": "interim",
      "version": "1.0.0-alpha"
    }
```

> The document status is `interim` but the document version contains the pre-release part `-alpha`.

### 6.1.21 Missing Item in Revision History

It MUST be tested that items of the revision history do not omit a version number when the items are sorted ascending by `date`. In the case of semantic versioning, this applies only to the Major version. It MUST also be tested that the first item in such a sorted list has either the version number 0 or 1 in the case of integer versioning or a Major version of 0 or 1 in the case of semantic versioning.

The relevant path for this test is:

```
    /document/tracking/revision_history
```

*Example 69 which fails the test:*

```
    "revision_history": [
      {
        "date": "2021-04-22T10:00:00.000Z",
        "number": "1",
        "summary": "Initial version."
      },
      {
        "date": "2021-07-21T10:00:00.000Z",
        "number": "3",
        "summary": "Some other changes."
      }
    ]
```

> The item for version `2` is missing.

### 6.1.22 Multiple Definition in Revision History

It MUST be tested that items of the revision history do not contain the same version number.

The relevant path for this test is:

```
    /document/tracking/revision_history
```

*Example 70 which fails the test:*

```
   "revision_history": [
      {
        "date": "2021-07-20T10:00:00.000Z",
        "number": "1",
        "summary": "Initial version."
      },
      {
        "date": "2021-07-21T10:00:00.000Z",
        "number": "1",
        "summary": "Some other changes."
      }
    ]
```

> The revision history contains two items with the version number `1`.

### 6.1.23 Multiple Use of Same CVE

It MUST be tested that a CVE is not used in multiple vulnerability items.

The relevant path for this test is:

```
    /vulnerabilities[]/cve
```

*Example 71 which fails the test:*

```
  "vulnerabilities": [
    {
      "cve": "CVE-2017-0145"
    },
    {
      "cve": "CVE-2017-0145"
    }
  ]
```

> The vulnerabilities array contains two items with the same CVE identifier `CVE-2017-0145`.

### 6.1.24 Multiple Definition in Involvements

It MUST be tested that items of the list of involvements do not contain the same `party` regardless of its `status` more than once at any `date`.

The relevant path for this test is:

```
    /vulnerabilities[]/involvements
```

*Example 72 which fails the test:*

```
  "vulnerabilities": [
    {
      "involvements": [
        {
          "date": "2021-04-23T10:00:00.000Z",
          "party": "vendor",
          "status": "completed"
        },
        {
          "date": "2021-04-23T10:00:00.000Z",
          "party": "vendor",
          "status": "in_progress",
          "summary": "The vendor has released a mitigation and is working to fully resolve the issue."
        }
      ]
    }
  ]
```

> The list of involvements contains two items with the same tuple `party` and `date`.

### 6.1.25 Multiple Use of Same Hash Algorithm

It MUST be tested that the same hash algorithm is not used multiple times in one item of hashes.

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/product/product_identification_helper/hashes[]/file_hashes
  /product_tree/full_product_names[]/product_identification_helper/hashes[]/file_hashes
  /product_tree/relationships[]/full_product_name/product_identification_helper/hashes[]/file_hashes
```

*Example 73 which fails the test:*

```
  "product_tree": {
    "full_product_names": [
      {
        "name": "Product A",
        "product_id": "CSAFPID-9080700",
        "product_identification_helper": {
          "hashes": [
            {
              "file_hashes": [
                {
                  "algorithm": "sha256",
                  "value": "026a37919b182ef7c63791e82c9645e2f897a3f0b73c7a6028c7febf62e93838"
                },
                {
                  "algorithm": "sha256",
                  "value": "0a853ce2337f0608489ac596a308dc5b7b19d35a52b10bf31261586ac368b175"
                }
              ],
              "filename": "product_a.so"
            }
          ]
         }
      }
    ]
  }
```

> The hash algorithm `sha256` is used two times in one item of hashes.

### 6.1.26 Prohibited Document Category Name

It MUST be tested that the document category is not equal to the (case insensitive) name (without the prefix `csaf_`) or value of any other profile than "CSAF Base". Any occurrences of dash, whitespace, and underscore characters are removed from the values on both sides before the match. Also the value MUST NOT start with the reserved prefix `csaf_` except if the value is `csaf_base`.

This test does only apply for CSAF documents with the profile "CSAF Base". Therefore, it MUST be skipped if the document category matches one of the values defined for the profile other than "CSAF Base".

> For CSAF 2.0, the test must be skipped for the following values in `/document/category`:
>
> ```
>   csaf_base
>   csaf_security_incident_response
>   csaf_informational_advisory
>   csaf_security_advisory
>   csaf_vex
> ```

This is the only mandatory test related to the profile "CSAF Base" as the required fields SHALL be checked by validating the JSON schema.

The relevant path for this test is:

```
  /document/category
```

*Examples 74 for currently prohibited values:*

```
  Csaf_a
  Informational Advisory
  security-incident-response
  Security      Advisory
  veX
  V_eX
```

*Example 75 which fails the test:*

```
  "category": "Security_Incident_Response"
```

> The value `Security_Incident_Response` is the name of a profile where the space was replaced with underscores.

### 6.1.27 Profile Tests

This subsubsection structures the tests for the profiles. Not all tests apply for all profiles. Tests SHOULD be skipped if the document category does not match the one given in the test. Each of the following tests SHOULD be treated as they where listed similar to the other tests.

> An application MAY group these tests by profiles when providing the additional function to only run one or more selected tests. This results in one virtual test per profile.

#### 6.1.27.1 Document Notes

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

*Example 76 which fails the test:*

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

#### 6.1.27.2 Document References

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

*Example 77 which fails the test:*

```
  "references": [
    {
      "category": "self",
      "summary": "The canonical URL.",
      "url": "https://example.com/security/data/csaf/2021/OASIS_CSAF_TC-CSAF_2_0-2021-6-1-27-02-01.json"
    }
  ]
```

> The document references do not contain any item which has the category `external`.

#### 6.1.27.3 Vulnerabilities

It MUST be tested that the element `/vulnerabilities` does not exist.

The relevant value for `/document/category` is:

```
  csaf_informational_advisory
```

The relevant path for this test is:

```
  /vulnerabilities
```

*Example 78 which fails the test:*

```
  "vulnerabilities": [
    {
      "title": "A vulnerability item that SHALL NOT exist"
    }
  ]
```

> The element `/vulnerabilities` exists.

> A tool MAY change the `/document/category` to `csaf_base` as a quick fix.

#### 6.1.27.4 Product Tree

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

*Example 79 which fails the test:*

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

#### 6.1.27.5 Vulnerability Notes

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

*Example 80 which fails the test:*

```
  "vulnerabilities": [
    {
      "title": "A vulnerability item without a note"
    }
  ]
```

> The vulnerability item has no `notes` element.

#### 6.1.27.6 Product Status

For each item in `/vulnerabilities` it MUST be tested that the element `product_status` exists.

The relevant value for `/document/category` is:

```
  csaf_security_advisory
```

The relevant path for this test is:

```
  /vulnerabilities[]/product_status
```

*Example 81 which fails the test:*

```
  "vulnerabilities": [
    {
      "title": "A vulnerability item without a product status"
    }
  ]
```

> The vulnerability item has no `product_status` element.

#### 6.1.27.7 VEX Product Status

For each item in `/vulnerabilities` it MUST be tested that at least one of the elements `fixed`, `known_affected`, `known_not_affected`, or `under_investigation` is present in `product_status`.

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

*Example 82 which fails the test:*

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

#### 6.1.27.8 Vulnerability ID

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

*Example 83 which fails the test:*

```
  "vulnerabilities": [
    {
      "title": "A vulnerability item without a CVE or ID"
    }
  ]
```

> None of the elements `cve` or `ids` is present.

#### 6.1.27.9 Impact Statement

For each item in `/vulnerabilities[]/product_status/known_not_affected` it MUST be tested that a corresponding impact statement exist in `/vulnerabilities[]/flags` or `/vulnerabilities[]/threats`. For the latter one, the `category` value for such a statement MUST be `impact`.

The relevant value for `/document/category` is:

```
  csaf_vex
```

The relevant path for this test is:

```
  /vulnerabilities[]/flags
  /vulnerabilities[]/threats
```

*Example 84 which fails the test:*

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

#### 6.1.27.10 Action Statement

For each item in `/vulnerabilities[]/product_status/known_affected` it MUST be tested that a corresponding action statement exist in `/vulnerabilities[]/remediations`.

The relevant value for `/document/category` is:

```
  csaf_vex
```

The relevant path for this test is:

```
  /vulnerabilities[]/remediations
```

*Example 85 which fails the test:*

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

#### 6.1.27.11 Vulnerabilities

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

*Example 86 which fails the test:*

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

### 6.1.28 Translation

It MUST be tested that the given source language and document language are not the same.

The relevant path for this test is:

```
  /document/lang
  /document/source_lang
```

*Example 87 which fails the test:*

```
  "document": {
    // ...
    "lang": "en-US",
    // ...
    "source_lang": "en-US",
    // ...
  }
```

> The document language and the source language have the same value `en-US`.
>
> Note: A translation from `en-US` to `en-GB` would pass the test.

> A tool MAY remove the source language as quick fix.

### 6.1.29 Remediation without Product Reference

For each item in `/vulnerabilities[]/remediations` it MUST be tested that it includes at least one of the elements `group_ids` or `product_ids`.

The relevant path for this test is:

```
  /vulnerabilities[]/remediations[]
```

*Example 88 which fails the test:*

```
      "remediations": [
        {
          "category": "no_fix_planned",
          "details": "These products are end-of-life. Therefore, no fix will be provided."
        }
      ]
```

> The given remediation does not specify to which products it should be applied.

> A tool MAY add all products of the affected group of this vulnerability to the remediation as quick fix.

### 6.1.30 Mixed Integer and Semantic Versioning

It MUST be tested that all elements of type `/$defs/version_t` follow either integer versioning or semantic versioning homogeneously within the same document.

The relevant paths for this test are:

```
  /document/tracking/revision_history[]/number
  /document/tracking/version
```

*Example 89 which fails the test:*

```
    "tracking": {
      // ...
      "revision_history": [
        {
          "date": "2021-07-21T09:00:00.000Z",
          "number": "1.0.0",
          "summary": "Initial version."
        },
        {
          "date": "2021-07-21T10:00:00.000Z",
          "number": "2",
          "summary": "Second version."
        }
      ],
      // ...
      "version": "2"
    }
```

> The document started with semantic versioning (`1.0.0`) and switched to integer versioning (`2`).

> A tool MAY assign all items their corresponding value according to integer versioning as a quick fix. In such case, the old `number` SHOULD be stored in `legacy_version`.

### 6.1.31 Version Range in Product Version

For each element of type `/$defs/branches_t` with `category` of `product_version` it MUST be tested that the value of `name` does not contain a version range.

> To implement this test it is deemed sufficient that, when converted to lower case, the value of `name` does not contain any of the following strings:
>
> ```
>   <
>   <=
>   >
>   >=
>   after
>   all
>   before
>   earlier
>   later
>   prior
>   versions
> ```

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/name
```

*Example 90 which fails the test:*

```
            "branches": [
              {
                "category": "product_version",
                "name": "prior to 4.2",
                // ...
              }
            ]
```

> The version range `prior to 4.2` is given for the branch category `product_version`.

### 6.1.32 Flag without Product Reference

For each item in `/vulnerabilities[]/flags` it MUST be tested that it includes at least one of the elements `group_ids` or `product_ids`.

The relevant path for this test is:

```
  /vulnerabilities[]/flags[]
```

*Example 91 which fails the test:*

```
      "flags": [
        {
          "label": "component_not_present"
        }
      ]
```

> The given flag does not specify to which products it should be applied.

### 6.1.33 Multiple Flags with VEX Justification Codes per Product

For each item in `/vulnerabilities[]` it MUST be tested that a Product is not member of more than one Flag item with a VEX justification code (see section 3.2.3.5). This takes indirect relations through Product Groups into account.

> Additional flags with a different purpose might be provided in later versions of CSAF. Through the explicit reference of VEX justification codes the test is specified to be forward-compatible.

The relevant path for this test is:

```
  /vulnerabilities[]/flags
```

*Example 92 which fails the test:*

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
      "flags": [
        {
          "label": "component_not_present",
          "group_ids": [
            "CSAFGID-0001"
          ]
        },
        {
          "label": "vulnerable_code_cannot_be_controlled_by_adversary",
          "product_ids": [
            "CSAFPID-9080700"
          ]
        }
      ],
      // ...
      "product_status": {
        "known_not_affected": [
          "CSAFPID-9080700",
          "CSAFPID-9080701"
        ]
      }
    }
  ]
```

> There are two flags given for for `CSAFPID-9080700` - one indirect through `CSAFGID-0001` and one direct.
