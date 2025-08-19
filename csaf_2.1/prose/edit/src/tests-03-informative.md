## Informative Tests

Informative tests provide insights in common mistakes and bad practices.
They MAY fail at a valid CSAF document.
It is up to the issuing party to decide whether this was an intended behavior and can be ignore or should be treated.
These tests MAY include information about recommended usage.
A program MUST handle a test failure as a information.

### Use of CVSS v2 As the Only Scoring System

For each item in the list of metrics which contains the `cvss_v2` object under `content` it MUST be tested that is not the only scoring item present.
The test SHALL pass if a second scoring object is available regarding the specific product.

> One source might just provide CVSS v2.
> As long as at least one different source provides a different scoring system for the same products, the test passes.

The relevant path for this test is:

```
    /vulnerabilities[]/metrics
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
      "metrics": [
        {
          "content": {
            "cvss_v2": {
              "version": "2.0",
              "vectorString": "AV:N/AC:L/Au:N/C:C/I:C/A:C",
              "baseScore": 10
            }
          },
          "products": [
            "CSAFPID-9080700"
          ]
        }
      ]
    }
  ]
```

> There is only a CVSS v2 score given for `CSAFPID-9080700`.

Recommendation:

It is recommended to (also) use the CVSS v4.0.

### Use of CVSS v3.0

For each item in the list of metrics which contains the `cvss_v3` object under `content` it MUST be tested that CVSS v3.0 is not used.

The relevant paths for this test are:

```
  /vulnerabilities[]/metrics[]/content/cvss_v3/version
  /vulnerabilities[]/metrics[]/content/cvss_v3/vectorString
```

*Example 1 (which fails the test):*

```
  "cvss_v3": {
    "version": "3.0",
    "vectorString": "CVSS:3.0/AV:L/AC:L/PR:H/UI:R/S:U/C:H/I:H/A:H",
    "baseScore": 6.5,
    "baseSeverity": "MEDIUM"
  }
```

> The CVSS v3.0 is used.

Recommendation:

It is recommended to upgrade to CVSS v3.1.

> A tool MAY upgrade to CVSS v3.1 as quick fix.
> However, if such quick fix is supported the tool SHALL also recompute the `baseScore` and `baseSeverity`.
> The same applies for `temporalScore` and `temporalSeverity` respectively `environmentalScore` and `environmentalSeverity` if
> the necessary fields for computing their value are present and set.

### Missing CVE

It MUST be tested that the CVE number is given.

The relevant path for this test is:

```
  /vulnerabilities[]/cve
```

*Example 1 (which fails the test):*

```
  "vulnerabilities": [
    {
      "title": "BlueKeep"
    }
  ]
```

> The CVE number is not given.

Recommendation:

It is recommended to provide a CVE number to support the users efforts to find more details about a vulnerability and
potentially track it through multiple advisories.
If no CVE exists for that vulnerability, it is recommended to get one assigned.

### Missing CWE

It MUST be tested that at least one CWE is given.

The relevant path for this test is:

```
  /vulnerabilities[]/cwes
```

*Example 1 (which fails the test):*

```
  "vulnerabilities": [
    {
      "cve": "CVE-2019-0708",
      "title": "BlueKeep"
    }
  ]
```

> No CWE number is given.

### Use of Short Hash

It MUST be tested that the length of the hash value is not shorter than 64 characters.

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/product/product_identification_helper/hashes[]/file_hashes[]/value
  /product_tree/full_product_names[]/product_identification_helper/hashes[]/file_hashes[]/value
  /product_tree/relationships[]/full_product_name/product_identification_helper/hashes[]/file_hashes[]/value
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
                  "algorithm": "md4",
                  "value": "3202b50e2e5b2fcd75e284c3d9d5f8d6"
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

> The length of the hash value is only 32 characters long.

### Use of Non-self Referencing URLs Failing to Resolve

For each URL which is not in the category `self` it MUST be tested that it resolves with a HTTP status code from
the 2xx (Successful) or 3xx (Redirection) class.

> This test does not apply for any item in an array of type `references_t` with the category `self`.
> For details about the HTTP status code classes see [cite](#RFC7231).

The relevant paths for this test are:

```
  /document/acknowledgments[]/urls[]
  /document/aggregate_severity/namespace
  /document/distribution/tlp/url
  /document/references[]/url
  /document/publisher/namespace
  /product_tree/branches[]/product/product_identification_helper/sbom_urls[]
  /product_tree/branches[]/product/product_identification_helper/x_generic_uris[]/namespace
  /product_tree/branches[]/product/product_identification_helper/x_generic_uris[]/uri
  /product_tree/branches[](/branches[])*/product/product_identification_helper/sbom_urls[]
  /product_tree/branches[](/branches[])*/product/product_identification_helper/x_generic_uris[]/namespace
  /product_tree/branches[](/branches[])*/product/product_identification_helper/x_generic_uris[]/uri
  /product_tree/full_product_names[]/product_identification_helper/sbom_urls[]
  /product_tree/full_product_names[]/product_identification_helper/x_generic_uris[]/namespace
  /product_tree/full_product_names[]/product_identification_helper/x_generic_uris[]/uri
  /product_tree/relationships[]/full_product_name/product_identification_helper/sbom_urls[]
  /product_tree/relationships[]/full_product_name/product_identification_helper/x_generic_uris[]/namespace
  /product_tree/relationships[]/full_product_name/product_identification_helper/x_generic_uris[]/uri
  /vulnerabilities[]/acknowledgments[]/urls[]
  /vulnerabilities[]/references[]/url
  /vulnerabilities[]/remediations[]/url
```

*Example 1 (which fails the test):*

```
    "references": [
      {
        "summary": "A URL that does not resolve with HTTP status code in the interval between (including) 200 and (excluding) 400.",
        "url": "https://example.invalid"
      }
    ]
```

> The `category` is not set and therefore treated as its default value `external`.
> A request to that URL does not resolve with a status code from the 2xx (Successful) or 3xx (Redirection) class.

### Use of self referencing URLs Failing to Resolve

For each item in an array of type `references_t` with the category `self` it MUST be tested that
the URL referenced resolves with a HTTP status code less than 400.

> This test will most likely fail if the CSAF document is in a status before the initial release.
> For details about the HTTP status code classes see [cite](#RFC7231).

The relevant paths for this test are:

```
  /document/references[]/url
  /vulnerabilities[]/references[]/url
```

*Example 1 (which fails the test):*

```
    "references": [
      {
        "category": "self",
        "summary": "A URL that does not resolve with HTTP status code in the interval between (including) 200 and (excluding) 400.",
        "url": "https://example.invalid"
      }
    ]
```

> The `category` is `self` and a request to that URL does not resolve with a status code from the 2xx (Successful) or 3xx (Redirection) class.

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

### Branch Categories

For each element of type `/$defs/full_product_name_t` in `/product_tree/branches` it MUST be tested that
ancestor nodes along the path exist which use the following branch categories `vendor` -> `product_name` -> `product_version` in that
order starting with the Product tree node.

> Other branch categories can be used before, after or between the aforementioned branch categories without making the test invalid.

The relevant paths for this test are:

```
  /product_tree/branches
```

*Example 1 (which fails the test):*

```
    "branches": [
      {
        "category": "vendor",
        "name": "Example Company",
        "branches": [
          {
            "category": "product_name",
            "name": "Product A",
            "branches": [
              {
                "category": "patch_level",
                "name": "91",
                "product": {
                  "product_id": "CSAFPID-0002",
                  "name": "Example Company Product A Update 91"
                }
              }
            ]
          }
        ]
      }
    ]
```

> The product `CSAFPID-9080700` does not have any ancestor with the branch category `product_version`.

### Usage of Product Version Range

For each element of type `/$defs/branches_t` it MUST be tested that the `category` is not `product_version_range`.

> It is usually hard decide for machines whether a product version matches a product version ranges.
> Therefore, it is recommended to avoid version ranges and enumerate versions wherever possible.

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/category
```

*Example 1 (which fails the test):*

```
                "category": "product_version_range",
```

> The category `product_version_range` was used.

### Usage of V as Version Indicator

For each element of type `/$defs/branches_t` with `category` of `product_version` it MUST be tested that
the value of `name` does not start with `v` or `V` before the version.

> To implement this test it is deemed sufficient that the value of `name` does not match the following regex:
>
> ```
>   ^[vV][0-9].*$
> ```

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/name
```

*Example 1 (which fails the test):*

```
            "branches": [
              {
                "category": "product_version",
                "name": "v4.2",
                // ...
              }
            ]
```

> The product version starts with a `v`.

### Missing CVSS v4.0

For each item in the list of metrics it MUST be tested that a `cvss_v4` object is present.

The relevant path for this test is:

```
    /vulnerabilities[]/metrics[]/content
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
      "metrics": [
        {
          "content": {
            "cvss_v3": {
              "version": "3.1",
              "vectorString": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H",
              "baseScore": 10,
              "baseSeverity": "CRITICAL"
            }
          },
          "products": [
            "CSAFPID-9080700"
          ]
        }
      ]
    }
  ]
```

> There is no CVSS v4.0 score given for `CSAFPID-9080700`.

### Usage of Non-Latest SSVC Decision Point Version

For each SSVC decision point given under `selections` with the `namespace` of `ssvc`, it MUST be tested the latest decision point `version` available at the time of the `timestamp` was used.
The test SHALL fail if a later `version` was used.

> A list of all valid decision points including their values is available at the [SSVC repository](https://github.com/CERTCC/SSVC/tree/main/data/json/decision_points).

The relevant path for this test is:

```
   /vulnerabilities[]/metrics[]/content/ssvc_v1/selections[]
```

*Example 1 (which fails the test):*

```
  "vulnerabilities": [
    {
      "cve": "CVE-1900-0001",
      "metrics": [
        {
          "content": {
            "ssvc_v1": {
              "id": "CVE-1900-0001",
              "schemaVersion": "1-0-1",
              "selections": [
                {
                  "name": "Mission Impact",
                  "namespace": "ssvc",
                  "values": [
                    "Non-Essential Degraded"
                  ],
                  "version": "1.0.0"
                }
              ],
              "timestamp": "2024-01-24T10:00:00.000Z"
            }
          },
          // ...
        }
      ]
    }
  ]
```

> At the timestamp `2024-01-24T10:00:00.000Z` version `2.0.0` of the SSVC decision point `Mission Impact` was already available.

### Usage of Private SSVC Decision Point Namespace in non TLP:CLEAR Document

For each SSVC decision point given under `selections`, it MUST be tested the `namespace` is not a private one if the document is not labeled `TLP:CLEAR`.

The relevant path for this test is:

```
   /vulnerabilities[]/metrics[]/content/ssvc_v1/selections[]/namespace
```

*Example 1 (which fails the test):*

```
  {
    "document": {
      // ...
      "distribution": {
        "tlp": {
          "label": "GREEN"
        }
      },
      // ...
    }
    "vulnerabilities": [
      {
        "cve": "CVE-1900-0001",
        "metrics": [
          {
            "content": {
              "ssvc_v1": {
                "id": "CVE-1900-0001",
                "schemaVersion": "1-0-1",
                "selections": [
                  {
                    "name": "Technical Impact",
                    "namespace": "x_custom",
                    "values": [
                      "Total"
                    ],
                    "version": "1.0.0"
                  }
                ],
                "timestamp": "2024-01-24T10:00:00.000Z"
              }
            },
            // ...
          }
        ]
      }
    ]
  }
```

> The namespace `x_custom` is a private namespace.
> Its decision point definitions might therefore not be known to the reader of the document.

### Usage of SSVC Decision Point Namespace with Extension in non TLP:CLEAR Document

For each SSVC decision point given under `selections`, it MUST be tested the `namespace` does not use an extension
if the document is not labeled `TLP:CLEAR`.

The relevant path for this test is:

```
   /vulnerabilities[]/metrics[]/content/ssvc_v1/selections[]/namespace
```

*Example 1 (which fails the test):*

```
  {
    "document": {
      // ...
      "distribution": {
        "tlp": {
          "label": "GREEN"
        }
      },
      // ...
    }
    "vulnerabilities": [
      {
        "cve": "CVE-1900-0001",
        "metrics": [
          {
            "content": {
              "ssvc_v1": {
                "id": "CVE-1900-0001",
                "schemaVersion": "1-0-1",
                "selections": [
                  {
                    "name": "Technical Impact",
                    "namespace": "ssvc/additional-technical-impacts",
                    "values": [
                      "Total"
                    ],
                    "version": "1.0.0"
                  }
                ],
                "timestamp": "2024-01-24T10:00:00.000Z"
              }
            },
            // ...
          }
        ]
      }
    ]
  }
```

> The namespace contains the extension `additional-technical-impacts`.
> Its decision point definitions might therefore not be known to the reader of the document.

### Grammar Check

If the document language is given it MUST be tested that a grammar check for the given language does not find any mistakes.
The test SHALL be skipped if the document language is not set.
It SHALL fail if the given language is not supported.

The relevant paths for this test are:

```
  /document/acknowledgments[]/summary
  /document/aggregate_severity/text
  /document/distribution/text
  /document/notes[]/audience
  /document/notes[]/text
  /document/notes[]/title
  /document/publisher/issuing_authority
  /document/references[]/summary
  /document/title
  /document/tracking/revision_history[]/summary
  /product_tree/product_groups[]/summary
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
        "text": "The security hardening guide must followed for ensure secure operations of a products."
      }
    ],
    // ...
  }
```

> Multiple grammar mistakes exist:
>
> - a `be` is missing between `must` and `followed`
> - the `for` needs to be a `to`
> - `a products` is also incorrect as `a` indicates singular.

### Use of Unregistered License

It MUST be tested that the all license identifiers and exceptions are listed either in the official SPDX license identifier list
or AboutCode's "ScanCode LicenseDB".

The relevant path for this test is:

```
  /document/license_expression
```

*Example 1 (which fails the test):*

```
    "license_expression": "LicenseRef-www.example.com-no-work-pd",
```

> The `license_expression` contains a license identifier that is neither listed in the official SPDX license identifier list
> nor AboutCode's "ScanCode LicenseDB".

-------
