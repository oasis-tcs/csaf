## Optional Tests

Optional tests SHOULD NOT fail at a valid CSAF document without a good reason. Failing such a test does not make the CSAF document invalid.
These tests may include information about features which are still supported but expected to be deprecated in a future version of CSAF.
A program MUST handle a test failure as a warning.

### Unused Definition of Product ID

For each Product ID (type `/$defs/product_id_t`) in Full Product Name elements (type: `/$defs/full_product_name_t`) it MUST be tested that
the `product_id` is referenced somewhere within the same document.

This test SHALL be skipped for CSAF documents conforming the profile "Informational Advisory".

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/product/product_id
  /product_tree/full_product_names[]/product_id
  /product_tree/relationships[]/full_product_name/product_id
```

*Example 1 (which fails the test):*

```
  "product_tree": {
    "full_product_names": [
      {
        "product_id": "CSAFPID-9080700",
        "name": "Product A"
      }
    ]
  }
```

> `CSAFPID-9080700` was defined but never used.

> A tool MAY remove the unused definition as quick fix. However, such quick fix shall not be applied if the test was skipped.

### Missing Remediation

For each Product ID (type `/$defs/product_id_t`) in the Product Status groups Affected and Under investigation it MUST be tested that
a remediation exists.

> The remediation might be of the category `none_available` or `no_fix_planned`.

The relevant paths for this test are:

```
  /vulnerabilities[]/product_status/first_affected[]  
  /vulnerabilities[]/product_status/known_affected[]
  /vulnerabilities[]/product_status/last_affected[]
  /vulnerabilities[]/product_status/under_investigation[]
```

*Example 1 (which fails the test):*

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
        "last_affected": [
          "CSAFPID-9080700"
        ]
      }
    }
  ]
```

> `CSAFPID-9080700` has in Product Status `last_affected` but there is no remediation object for this Product ID.

### Missing Metric

For each Product ID (type `/$defs/product_id_t`) in the Product Status groups Affected it MUST be tested that
a metric object exists which covers this product.

The relevant paths for this test are:

```
  /vulnerabilities[]/product_status/first_affected[]  
  /vulnerabilities[]/product_status/known_affected[]
  /vulnerabilities[]/product_status/last_affected[]
```

*Example 1 (which fails the test):*

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
        "first_affected": [
          "CSAFPID-9080700"
        ]
      }
    }
  ]
```

> `CSAFPID-9080700` has in Product Status `first_affected` but there is no metric object which covers this Product ID.

### Build Metadata in Revision History

For each item in revision history it MUST be tested that `number` does not include build metadata.

The relevant path for this test is:

```
    /document/tracking/revision_history[]/number
```

*Example 1 (which fails the test):*

```
    "revision_history": [
      {
        "date": "2023-08-23T10:00:00.000Z",
        "number": "1.0.0+exp.sha.ac00785",
        "summary": "Initial version."
      }
    ]
```

> The revision history contains an item which has a `number` that includes the build metadata `+exp.sha.ac00785`.

### Older Initial Release Date than Revision History

It MUST be tested that the Initial Release Date is not older than the `date` of the oldest item in Revision History.
As the timestamps might use different timezones, the sorting and comparison MUST take timezones into account.

The relevant path for this test is:

```
    /document/tracking/initial_release_date
```

*Example 1 (which fails the test):*

```
    "tracking": {
      // ...
      "initial_release_date": "2023-08-22T10:00:00.000Z",
      "revision_history": [
        {
          "date": "2023-09-06T10:00:00.000Z",
          "number": "1",
          "summary": "Initial version."
        },
        {
          "date": "2024-01-21T11:00:00.000Z",
          "number": "2",
          "summary": "Second version."
        }
      ],
      // ...
    }
```

> The initial release date `2023-08-22T10:00:00.000Z` is older than `2023-09-06T10:00:00.000Z` which is the `date` of
> the oldest item in Revision History.

### Older Current Release Date than Revision History

It MUST be tested that the Current Release Date is not older than the `date` of the newest item in Revision History.
As the timestamps might use different timezones, the sorting and comparison MUST take timezones into account.

The relevant path for this test is:

```
    /document/tracking/current_release_date
```

*Example 1 (which fails the test):*

```
    "tracking": {
      "current_release_date": "2023-09-06T10:00:00.000Z",
      // ...
      "revision_history": [
        {
          "date": "2023-09-06T10:00:00.000Z",
          "number": "1",
          "summary": "Initial version."
        },
        {
          "date": "2024-01-21T11:00:00.000Z",
          "number": "2",
          "summary": "Second version."
        }
      ],
      // ...
    }
```

> The current release date `2023-09-06T10:00:00.000Z` is older than `2023-09-23T1100:00.000Z` which is the `date` of
> the newest item in Revision History.

### Missing Date in Involvements

For each item in the list of involvements it MUST be tested that it includes the property `date`.

The relevant path for this test is:

```
    /vulnerabilities[]/involvements
```

*Example 1 (which fails the test):*

```
  "vulnerabilities": [
    {
      "involvements": [
        {
          "party": "vendor",
          "status": "in_progress"
        }
      ]
    }
  ]
```

> The list of involvements contains an item which does not contain the property `date`.

### Use of MD5 as the only Hash Algorithm

It MUST be tested that the hash algorithm `md5` is not the only one present.

> Since collision attacks exist for MD5 such value should be accompanied by a second cryptographically stronger hash.
> This will allow users to double check the results.

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/product/product_identification_helper/hashes[]/file_hashes
  /product_tree/full_product_names[]/product_identification_helper/hashes[]/file_hashes
  /product_tree/relationships[]/full_product_name/product_identification_helper/hashes[]/file_hashes
```

*Example 1 (which fails the test):*

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
                  "algorithm": "md5",
                  "value": "6ae24620ea9656230f49234efd078935"
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

> The hash algorithm `md5` is used in one item of hashes without being accompanied by a second hash algorithm.

### Use of SHA-1 as the only Hash Algorithm

It MUST be tested that the hash algorithm `sha1` is not the only one present.

> Since collision attacks exist for SHA-1 such value should be accompanied by a second cryptographically stronger hash.
> This will allow users to double check the results.

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/product/product_identification_helper/hashes[]/file_hashes
  /product_tree/full_product_names[]/product_identification_helper/hashes[]/file_hashes
  /product_tree/relationships[]/full_product_name/product_identification_helper/hashes[]/file_hashes
```

*Example 1 (which fails the test):*

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
                  "algorithm": "sha1",
                  "value": "e067035314dd8673fe1c9fc6b01414fe0950fdc4"
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

> The hash algorithm `sha1` is used in one item of hashes without being accompanied by a second hash algorithm.

### Missing TLP label (obsolete){#missing-tlp-label}

> The TLP label is now required by the schema. Therefore, the optional test is obsolete.
> This section is kept to document that change and keep the numbering of the remaining sections stable.

### Missing Canonical URL

It MUST be tested that the CSAF document has a canonical URL.

> To implement this test it is deemed sufficient that one item in `/document/references` fulfills all of the following:
>
> * It has the category `self`.
> * The `url` starts with `https://`.
> * The `url` ends with the valid filename for the CSAF document according to the rules in section [sec](#filename).

The relevant path for this test is:

```
  /document/references
```

*Example 1 (which fails the test):*

```
  "document": {
    // ...
    "references": [
      {
        "category": "self",
        "summary": "A non-canonical URL.",
        "url": "https://example.com/security/data/csaf/2024/oasis_csaf_tc-csaf_2.1-2024-6-2-11-01_1.json"
      }
    ],
    // ...
    "tracking": {
      // ...
      "id": "OASIS_CSAF_TC-CSAF_2.1-2024-6-2-11-01",
      // ...
      "version": "1"
    },
    // ...
  }
```

> The only element where the `category` is `self` has a URL that does not fulfill the requirement of a valid filename for a CSAF document.

### Missing Document Language

It MUST be tested that the document language is present and set.

The relevant path for this test is:

```
  /document/lang
```

*Example 1 (which fails the test):*

```
  "document": {
    "category": "csaf_base",
    "csaf_version": "2.1",
    "distribution": {
      "tlp": {
        "label": "CLEAR"
      }
    },
    "publisher": {
      // ...
    },
    // ...
  }
```

> The document language is not defined.

### Sorting{#optional-tests--sorting}

It MUST be tested that all keys in a CSAF document are sorted alphabetically.

The relevant path for this test is:

```
  /
```

*Example 1 (which fails the test):*

```
  "document": {
    "csaf_version": "2.1",
    "category": "csaf_base",
    // ...
  }
```

> The key `csaf_version` is not at the right place.

> A tool MAY sort the keys as a quick fix.

### Use of Private Language

For each element of type `/$defs/language_t` it MUST be tested that the language code does not contain subtags reserved for private use.

The relevant paths for this test are:

```
  /document/lang
  /document/source_lang
```

*Example 1 (which fails the test):*

```
  "lang": "qtx"
```

> The language code `qtx` is reserved for private use.

> A tool MAY remove such subtag as a quick fix.

### Use of Default Language

For each element of type `/$defs/language_t` it MUST be tested that the language code is not `i-default`.

The relevant paths for this test are:

```
  /document/lang
  /document/source_lang
```

*Example 1 (which fails the test):*

```
  "lang": "i-default"
```

> The language code `i-default` is used.

> A tool MAY remove such element as a quick fix.

### Missing Product Identification Helper

For each element of type `/$defs/full_product_name_t` it MUST be tested that it includes the property `product_identification_helper`.

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/product
  /product_tree/full_product_names[]
  /product_tree/relationships[]/full_product_name
```

*Example 1 (which fails the test):*

```
    "full_product_names": [
      {
        "product_id": "CSAFPID-9080700",
        "name": "Product A"
      }
    ]
```

> The product `CSAFPID-9080700` does not provide any Product Identification Helper at all.

### CVE in field IDs

For each item in `/vulnerabilities[]/ids` it MUST be tested that it is not a CVE ID.

> It is sufficient to check, whether the property `text` matches the regex `^CVE-[0-9]{4}-[0-9]{4,}$`.

The relevant paths for this test are:

```
  /vulnerabilities[]/ids[]
```

*Example 1 (which fails the test):*

```
      "ids": [
        {
          "system_name": "CVE Project",
          "text": "CVE-2021-44228"
        }
      ]
```

> The `CVE-2021-44228` is listed in an item of the `ids` array instead under `cve`.

> A tool MAY set such element as value for the `cve` property as a quick fix, if that didn't exist before.
> Alternatively, it MAY remove such element as a quick fix.

### Product Version Range without vers

For each element of type `/$defs/branches_t` with `category` of `product_version_range` it MUST be tested that
the value of `name` conforms the vers specification.

> To implement this test it is deemed sufficient that the value of `name` matches the following regex:
>
> ```
>   ^vers:[a-z\\.\\-\\+][a-z0-9\\.\\-\\+]*/.+
> ```

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/name
```

*Example 1 (which fails the test):*

```
            "branches": [
              {
                "category": "product_version_range",
                "name": ">4.2",
                // ...
              }
            ]
```

> The version range `>4.2` is a valid vsl but not valid according to the vers specification.

### CVSS for Fixed Products

For each item the fixed products group (`first_fixed` and `fixed`) it MUST be tested that
a CVSS applying to this product has an environmental score of `0`.
The test SHALL pass if none of the Product IDs listed within product status `fixed` or
`first_fixed` is found in `products` of any item of the `metrics` element.

The relevant path for this test is:

```
  /vulnerabilities[]/product_status/first_fixed[]
  /vulnerabilities[]/product_status/fixed[]
```

*Example 1 (which fails the test):*

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
        "fixed": [
          "CSAFPID-9080700"
        ]
      },
      "metrics": [
        {
          "content": {
            "cvss_v3": {
              "baseScore": 6.5,
              "baseSeverity": "MEDIUM",
              "vectorString": "CVSS:3.1/AV:L/AC:L/PR:H/UI:R/S:U/C:H/I:H/A:H",
              "version": "3.1"
            }
          }          ,
          "products": [
            "CSAFPID-9080700"
          ]
        }
      ]
    }
  ]
```

> Neither the `environmentalScore` nor the properties `modifiedIntegrityImpact`, `modifiedAvailabilityImpact`, `modifiedConfidentialityImpact` nor
> the corresponding attributes in the `vectorString` have been set.

> A tool MAY set the properties `modifiedIntegrityImpact`, `modifiedAvailabilityImpact`, `modifiedConfidentialityImpact` (respectively their
> equivalents according to the CVSS version used) accordingly and compute the `environmentalScore` as quick fix.

### Additional Properties

It MUST be tested that there is no additional property in the CSAF document that was not defined in the CSAF JSON schema.

The relevant path for this test is:

```
  /
```

> To implement this test it is deemed sufficient to validate the CSAF document against a "strict" version schema that
> sets `additionalProperties` to `false` for every key of type `object`.

*Example 1 (which fails the test):*

```
  "document": {
    "category": "csaf_base",
    "csaf_version": "2.1",
    "custom_property": "any",
    // ...
  }
```

> The key `custom_property` is not defined in the JSON schema.

> A tool MAY remove such keys as a quick fix.

### Same Timestamps in Revision History

It MUST be tested that the timestamps of all items in the revision history are pairwise disjoint.
As the timestamps might use different timezones, the comparison MUST take timezones into account.

The relevant path for this test is:

```
  /document/tracking/revision_history[]/date
```

*Example 1 (which fails the test):*

```
  "revision_history": [
    {
      "date": "2024-01-21T10:00:00.000Z",
      "number": "2.0.0",
      "summary": "Second version."
    },
    {
      "date": "2024-01-21T10:00:00.000Z",
      "number": "1.0.0",
      "summary": "Initial version."
    }
  ]
```

> The first and second revision have the same timestamp.

### Document Tracking ID in Title

It MUST be tested that the `/document/title` does not contain the `/document/tracking/id`.

The relevant path for this test is:

```
  /document/title
```

*Example 1 (which fails the test):*

```
    "title": "OASIS_CSAF_TC-CSAF_2.1-2024-6-2-22-01: Optional test: Document Tracking ID in Title (failing example 1)",
    "tracking": {
      // ...
      "id": "OASIS_CSAF_TC-CSAF_2.1-2024-6-2-22-01",
      // ...
    }
```

> The document title contains the document tracking id.

> A tool MAY remove the document tracking id from the document title.
> It SHOULD also remove any separating characters including whitespace, colon, dash and brackets.

### Usage of Deprecated CWE

For each item in the CWE array it MUST be tested that the CWE is not deprecated in the given version.

The relevant path for this test is:

```
  /vulnerabilities[]/cwes[]
```

*Example 1 (which fails the test):*

```
     "cwes": [
        {
          "id": "CWE-596",
          "name": "DEPRECATED: Incorrect Semantic Object Comparison",
          "version": "4.13"
        }
      ]
```

> The `CWE-596` is deprecated in version `4.13`.

> A tool MAY suggest to replace the deprecated CWE with its replacement or closest equivalent.

### Usage of Non-Latest CWE Version

For each item in the CWE array it MUST be tested that the latest CWE version available at the time of the last revision was used.
The test SHALL fail if a later CWE version was used.

The relevant path for this test is:

```
  /vulnerabilities[]/cwes[]
```

*Example 1 (which fails the test):*

```
  "document": {
    // ...
    "tracking": {
      "current_release_date": "2024-01-21T10:00:00.000Z",
      // ...
    }
  },
  "vulnerabilities": [
    {
      "cwes": [
        {
          "id": "CWE-256",
          "name": "Plaintext Storage of a Password",
          "version": "4.12"
        }
      ]
    }
  ]
```

> The CWE version listed is `4.12`. However, version `4.13` was most recent version when the document was released on `2024-01-21T10:00:00.000Z`.

> A tool MAY suggest to use the latest version available at the time of the `current_release_date`.
> This is most likely also the overall latest CWE version as modifications to a CSAF document lead to a new `current_release_date`.

### Usage of CWE Not Allowed for Vulnerability Mapping

For each item in the CWE array it MUST be tested that the vulnerability mapping is allowed.

> Currently, this includes the two usage state `Allowed` and `Allowed-with-Review`.

The relevant path for this test is:

```
  /vulnerabilities[]/cwes[]
```

*Example 1 (which fails the test):*

```
      "cwes": [
        {
          "id": "CWE-20",
          "name": "Improper Input Validation",
          "version": "4.13"
        }
      ]
```

> The usage of CWE-20 is discouraged as "is commonly misused in low-information vulnerability reports when lower-level CWEs could be used instead, or when more details about the vulnerability are available". [cite](https://cwe.mitre.org/data/definitions/20.html#Vulnerability_Mapping_Notes_20)

### Usage of CWE Allowed with Review for Vulnerability Mapping

For each item in the CWE array it MUST be tested that the vulnerability mapping is allowed without review.

> Reasoning: CWEs marked with a vulnerability mapping state of `Allowed-with-Review` should only be used if a thorough review was done.
> This test helps to flag such mappings which can be used to trigger processes that ensure the extra review, e.g. by a senior analyst.

The relevant path for this test is:

```
  /vulnerabilities[]/cwes[]
```

*Example 1 (which fails the test):*

```
      "cwes": [
        {
          "id": "CWE-1023",
          "name": "Incomplete Comparison with Missing Factors",
          "version": "4.13"
        }
      ]
```

> The usage of CWE-1023 is allowed with review as the "CWE entry is a Class and might have Base-level children that would be more appropriate". [cite](https://cwe.mitre.org/data/definitions/1023.html#Vulnerability_Mapping_Notes_1023)

### Discouraged Product Status Remediation Combination

For each item in `/vulnerabilities[]/remediations` it MUST be tested that a Product is not member of a discouraged product status group
remediation category combination.
This takes indirect relations through Product Groups into account.

The relevant path for this test is:

```
  /vulnerabilities[]/remediations[]
```

*Example 1 (which fails the test):*

```
      "product_status": {
        "known_not_affected": [
          "CSAFPID-9080700"
        ]
      },
      "remediations": [
        {
          "category": "fix_planned",
          "details": "The fix should be available in Q4 2024.",
          "product_ids": [
            "CSAFPID-9080700"
          ]
        }
      ]
```

> For the product with product ID `CSAFPID-908070` a fix is planned but the product was not affected at all.

### Usage of Max UUID

It MUST be tested that the Max UUID is not used as sharing group id.

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
      "tlp": {
        "label": "CLEAR"
      }
    },
```

> The sharing group id uses the Max UUID.
