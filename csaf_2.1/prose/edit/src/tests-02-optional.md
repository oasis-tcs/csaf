## 6.2 Optional Tests

Optional tests SHOULD NOT fail at a valid CSAF document without a good reason. Failing such a test does not make the CSAF document invalid. These tests may include information about features which are still supported but expected to be deprecated in a future version of CSAF. A program MUST handle a test failure as a warning.

### 6.2.1 Unused Definition of Product ID

For each Product ID (type `/$defs/product_id_t`) in Full Product Name elements (type: `/$defs/full_product_name_t`) it MUST be tested that the `product_id` is referenced somewhere within the same document.

This test SHALL be skipped for CSAF documents conforming the profile "Informational Advisory".

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/product/product_id
  /product_tree/full_product_names[]/product_id
  /product_tree/relationships[]/full_product_name/product_id
```

*Example 93 which fails the test:*

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

### 6.2.2 Missing Remediation

For each Product ID (type `/$defs/product_id_t`) in the Product Status groups Affected and Under investigation it MUST be tested that a remediation exists.

> The remediation might be of the category `none_available` or `no_fix_planned`.

The relevant paths for this test are:

```
  /vulnerabilities[]/product_status/first_affected[]  
  /vulnerabilities[]/product_status/known_affected[]
  /vulnerabilities[]/product_status/last_affected[]
  /vulnerabilities[]/product_status/under_investigation[]
```

*Example 94 which fails the test:*

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

### 6.2.3 Missing Score

For each Product ID (type `/$defs/product_id_t`) in the Product Status groups Affected it MUST be tested that a score object exists which covers this product.

The relevant paths for this test are:

```
  /vulnerabilities[]/product_status/first_affected[]  
  /vulnerabilities[]/product_status/known_affected[]
  /vulnerabilities[]/product_status/last_affected[]
```

*Example 95 which fails the test:*

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

> `CSAFPID-9080700` has in Product Status `first_affected` but there is no score object which covers this Product ID.

### 6.2.4 Build Metadata in Revision History

For each item in revision history it MUST be tested that `number` does not include build metadata.

The relevant path for this test is:

```
    /document/tracking/revision_history[]/number
```

*Example 96 which fails the test:*

```
    "revision_history": [
      {
        "date": "2021-04-23T10:00:00.000Z",
        "number": "1.0.0+exp.sha.ac00785",
        "summary": "Initial version."
      }
    ]
```

> The revision history contains an item which has a `number` that includes the build metadata `+exp.sha.ac00785`.

### 6.2.5 Older Initial Release Date than Revision History

It MUST be tested that the Initial Release Date is not older than the `date` of the oldest item in Revision History.

The relevant path for this test is:

```
    /document/tracking/initial_release_date
```

*Example 97 which fails the test:*

```
    "tracking": {
      // ...
      "initial_release_date": "2021-04-22T10:00:00.000Z",
      "revision_history": [
        {
          "date": "2021-05-06T10:00:00.000Z",
          "number": "1",
          "summary": "Initial version."
        },
        {
          "date": "2021-07-21T11:00:00.000Z",
          "number": "2",
          "summary": "Second version."
        }
      ],
      // ...
    }
```

> The initial release date `2021-04-22T10:00:00.000Z` is older than `2021-05-06T10:00:00.000Z` which is the `date` of the oldest item in Revision History.

### 6.2.6 Older Current Release Date than Revision History

It MUST be tested that the Current Release Date is not older than the `date` of the newest item in Revision History.

The relevant path for this test is:

```
    /document/tracking/current_release_date
```

*Example 98 which fails the test:*

```
    "tracking": {
      "current_release_date": "2021-05-06T10:00:00.000Z",
      // ...
      "revision_history": [
        {
          "date": "2021-05-06T10:00:00.000Z",
          "number": "1",
          "summary": "Initial version."
        },
        {
          "date": "2021-07-21T11:00:00.000Z",
          "number": "2",
          "summary": "Second version."
        }
      ],
      // ...
    }
```

> The current release date `2021-05-06T10:00:00.000Z` is older than `2021-05-23T1100:00.000Z` which is the `date` of the newest item in Revision History.

### 6.2.7 Missing Date in Involvements

For each item in the list of involvements it MUST be tested that it includes the property `date`.

The relevant path for this test is:

```
    /vulnerabilities[]/involvements
```

*Example 99 which fails the test:*

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

### 6.2.8 Use of MD5 as the only Hash Algorithm

It MUST be tested that the hash algorithm `md5` is not the only one present.

> Since collision attacks exist for MD5 such value should be accompanied by a second cryptographically stronger hash. This will allow users to double check the results.

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/product/product_identification_helper/hashes[]/file_hashes
  /product_tree/full_product_names[]/product_identification_helper/hashes[]/file_hashes
  /product_tree/relationships[]/full_product_name/product_identification_helper/hashes[]/file_hashes
```

*Example 100 which fails the test:*

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

### 6.2.9 Use of SHA-1 as the only Hash Algorithm

It MUST be tested that the hash algorithm `sha1` is not the only one present.

> Since collision attacks exist for SHA-1 such value should be accompanied by a second cryptographically stronger hash. This will allow users to double check the results.

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/product/product_identification_helper/hashes[]/file_hashes
  /product_tree/full_product_names[]/product_identification_helper/hashes[]/file_hashes
  /product_tree/relationships[]/full_product_name/product_identification_helper/hashes[]/file_hashes
```

*Example 101 which fails the test:*

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

### 6.2.10 Missing TLP label

It MUST be tested that `/document/distribution/tlp/label` is present and valid.

> TLP labels support the machine-readability and automated distribution.

The relevant path for this test is:

```
  /document/distribution/tlp/label
```

*Example 102 which fails the test:*

```
    "distribution": {
      "text": "Distribute freely."
    }
```

> The CSAF document has no TLP label.

### 6.2.11 Missing Canonical URL

It MUST be tested that the CSAF document has a canonical URL.

> To implement this test it is deemed sufficient that one item in `/document/references` fulfills all of the following:
>
> * It has the category `self`.
> * The `url` starts with `https://`.
> * The `url` ends with the valid filename for the CSAF document according to the rules in section 5.1.

The relevant path for this test is:

```
  /document/references
```

*Example 103 which fails the test:*

```
  "document": {
    // ...
    "references": [
      {
        "category": "self",
        "summary": "A non-canonical URL.",
        "url": "https://example.com/security/data/csaf/2021/OASIS_CSAF_TC-CSAF_2.0-2021-6-2-11-01_1.json"
      }
    ],
    // ...
    "tracking": {
      // ...
      "id": "OASIS_CSAF_TC-CSAF_2.0-2021-6-2-11-01",
      // ...
      "version": "1"
    },
    // ...
  }
```

> The only element where the `category` is `self` has a URL that does not fulfill the requirement of a valid filename for a CSAF document.

### 6.2.12 Missing Document Language

It MUST be tested that the document language is present and set.

The relevant path for this test is:

```
  /document/lang
```

*Example 104 which fails the test:*

```
  "document": {
    "category": "csaf_base",
    "csaf_version": "2.0",
    "publisher": {
      // ...
    },
    // ...
  }
```

> The document language is not defined.

### 6.2.13 Sorting

It MUST be tested that all keys in a CSAF document are sorted alphabetically.

The relevant path for this test is:

```
  /
```

*Example 105 which fails the test:*

```
  "document": {
    "csaf_version": "2.0",
    "category": "csaf_base",
    // ...
  }
```

> The key `csaf_version` is not at the right place.

> A tool MAY sort the keys as a quick fix.

### 6.2.14 Use of Private Language

For each element of type `/$defs/language_t` it MUST be tested that the language code does not contain subtags reserved for private use.

The relevant paths for this test are:

```
  /document/lang
  /document/source_lang
```

*Example 106 which fails the test:*

```
  "lang": "qtx"
```

> The language code `qtx` is reserved for private use.

> A tool MAY remove such subtag as a quick fix.

### 6.2.15 Use of Default Language

For each element of type `/$defs/language_t` it MUST be tested that the language code is not `i-default`.

The relevant paths for this test are:

```
  /document/lang
  /document/source_lang
```

*Example 107 which fails the test:*

```
  "lang": "i-default"
```

> The language code `i-default` is used.

> A tool MAY remove such element as a quick fix.

### 6.2.16 Missing Product Identification Helper

For each element of type `/$defs/full_product_name_t` it MUST be tested that it includes the property `product_identification_helper`.

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/product
  /product_tree/full_product_names[]
  /product_tree/relationships[]/full_product_name
```

*Example 108 which fails the test:*

```
    "full_product_names": [
      {
        "product_id": "CSAFPID-9080700",
        "name": "Product A"
      }
    ]
```

> The product `CSAFPID-9080700` does not provide any Product Identification Helper at all.

### 6.2.17 CVE in field IDs

For each item in `/vulnerabilities[]/ids` it MUST be tested that it is not a CVE ID.

> It is sufficient to check, whether the property `text` matches the regex `^CVE-[0-9]{4}-[0-9]{4,}$`.

The relevant paths for this test are:

```
  /vulnerabilities[]/ids[]
```

*Example 109 which fails the test:*

```
      "ids": [
        {
          "system_name": "CVE Project",
          "text": "CVE-2021-44228"
        }
      ]
```

> The `CVE-2021-44228` is listed in an item of the `ids` array instead under `cve`.

> A tool MAY set such element as value for the `cve` property as a quick fix, if that didn't exist before. Alternatively, it MAY remove such element as a quick fix.

### 6.2.18 Product Version Range without vers

For each element of type `/$defs/branches_t` with `category` of `product_version_range` it MUST be tested that the value of `name` conforms the vers specification.

> To implement this test it is deemed sufficient that the value of `name` matches the following regex:
>
> ```
>   ^vers:[a-z\\.\\-\\+][a-z0-9\\.\\-\\+]*/.+
> ```

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/name
```

*Example 110 which fails the test:*

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

### 6.2.19 CVSS for Fixed Products

For each item the fixed products group (`first_fixed` and `fixed`) it MUST be tested that a CVSS applying to this product has an environmental score of `0`. The test SHALL pass if none of the Product IDs listed within product status `fixed` or `first_fixed` is found in `products` of any item of the `scores` element.

The relevant path for this test is:

```
  /vulnerabilities[]/product_status/first_fixed[]
  /vulnerabilities[]/product_status/fixed[]
```

*Example 111 which fails the test:*

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
      "scores": [
        {
          "cvss_v3": {
            "baseScore": 6.5,
            "baseSeverity": "MEDIUM",
            "vectorString": "CVSS:3.1/AV:L/AC:L/PR:H/UI:R/S:U/C:H/I:H/A:H",
            "version": "3.1"
          },
          "products": [
            "CSAFPID-9080700"
          ]
        }
      ]
    }
  ]
```

> Neither the `environmentalScore` nor the properties `modifiedIntegrityImpact`, `modifiedAvailabilityImpact`, `modifiedConfidentialityImpact` nor the corresponding attributes in the `vectorString` have been set.

> A tool MAY set the properties `modifiedIntegrityImpact`, `modifiedAvailabilityImpact`, `modifiedConfidentialityImpact` accordingly and compute the `environmentalScore` as quick fix.

### 6.2.20 Additional Properties

It MUST be tested that there is no additional property in the CSAF document that was not defined in the CSAF JSON schema.

The relevant path for this test is:

```
  /
```

> To implement this test it is deemed sufficient to validate the CSAF document against a "strict" version schema that sets `additionalProperties` to `false` for every key of type `object`.

*Example 112 which fails the test:*

```
  "document": {
    "category": "csaf_base",
    "csaf_version": "2.0",
    "custom_property": "any",
    // ...
  }
```

> The key `custom_property` is not defined in the JSON schema.

> A tool MAY remove such keys as a quick fix.

