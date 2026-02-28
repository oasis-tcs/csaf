<!--
---
toc:
  auto: false
  label: Collapsing Product Paths
  enumerate: Appendix D.
---
-->
# Collapsing Product Paths

The following examples are intended to aid in understanding under which circumstances product paths can be collapsed.

*Example 1 (which is not collapsed but collapsible)*:

```
  "product_tree": {
    "branches": [
      {
        "branches": [
          {
            "branches": [
              {
                "category": "product_version",
                "name": "1.0.0",
                "product": {
                  "name": "Example Company Product A 1.0.0",
                  "product_id": "CSAFPID-908070601"
                }
              },
              // ...
            ],
            "category": "product_name",
            "name": "Product A"
          },
          {
            "branches": [
              {
                "category": "product_version",
                "name": "2023",
                "product": {
                  "name": "Example Company Product B 2023",
                  "product_id": "CSAFPID-908070603"
                }
              },
              // ...
            ],
            "category": "product_name",
            "name": "Product B"
          },
          {
            "branches": [
              {
                "category": "product_version",
                "name": "EU",
                "product": {
                  "name": "Example Company Product C EU",
                  "product_id": "CSAFPID-908070605"
                }
              },
              // ...
            ],
            "category": "product_name",
            "name": "Product C"
          }
        ],
        "category": "vendor",
        "name": "Example Company"
      }
    ],
    "product_paths": [
      {
        "beginning_product_reference": "CSAFPID-908070601",
        "full_product_name": {
          "name": "Example Company Product A 1.0.0 installed on Example Company Product B 2023",
          "product_id": "CSAFPID-908070607"
        },
        "subpaths": [
          {
            "category": "installed_on",
            "next_product_reference": "CSAFPID-908070603"
          }
        ]
      },
      // ...
      {
        "beginning_product_reference": "CSAFPID-908070607",
        "full_product_name": {
          "name": "Example Company Product A 1.0.0 installed on Example Company Product B 2023 installed on Example Company Product C EU",
          "product_id": "CSAFPID-908070611"
        },
        "subpaths": [
          {
            "category": "installed_on",
            "next_product_reference": "CSAFPID-908070605"
          }
        ]
      },
      // ...
    ]
  }
```

> Product paths in example 1 above can be collapse as shown in example 2 below.

*Example 2 (which is collapsed)*:

```
  "product_tree": {
    "branches": [
      {
        "branches": [
          {
            "branches": [
              {
                "category": "product_version",
                "name": "1.0.0",
                "product": {
                  "name": "Example Company Product A 1.0.0",
                  "product_id": "CSAFPID-908070601"
                }
              },
              // ...
            ],
            "category": "product_name",
            "name": "Product A"
          },
          {
            "branches": [
              {
                "category": "product_version",
                "name": "2023",
                "product": {
                  "name": "Example Company Product B 2023",
                  "product_id": "CSAFPID-908070603"
                }
              },
              // ...
            ],
            "category": "product_name",
            "name": "Product B"
          },
          {
            "branches": [
              {
                "category": "product_version",
                "name": "EU",
                "product": {
                  "name": "Example Company Product C EU",
                  "product_id": "CSAFPID-908070605"
                }
              },
              // ...
            ],
            "category": "product_name",
            "name": "Product C"
          }
        ],
        "category": "vendor",
        "name": "Example Company"
      }
    ],
    "product_paths": [
      {
        "beginning_product_reference": "CSAFPID-908070601",
        "full_product_name": {
          "name": "Example Company Product A 1.0.0 installed on Example Company Product B 2023 installed on Example Company Product C EU",
          "product_id": "CSAFPID-908070611"
        },
        "subpaths": [
          {
            "category": "installed_on",
            "next_product_reference": "CSAFPID-908070603"
          },
          {
            "category": "installed_on",
            "next_product_reference": "CSAFPID-908070605"
          }
        ]
      },
      // ...
    ]
  }
```

*Example 3 (which is not collapsed nor collapsible without information loss)*:

```
  "product_tree": {
    "branches": [
      {
        "branches": [
          {
            "branches": [
              {
                "category": "product_version",
                "name": "1.0.0",
                "product": {
                  "name": "Example Company Product A 1.0.0",
                  "product_id": "CSAFPID-908070601",
                  "product_identification_helper": {
                    "cpe": "cpe:2.3:a:example_company:product_a:1.0.0:*:*:*:*:*:*:*"
                  }
                }
              },
              {
                "category": "product_version",
                "name": "1.1.0",
                "product": {
                  "name": "Example Company Product A 1.1.0",
                  "product_id": "CSAFPID-908070602",
                  "product_identification_helper": {
                    "cpe": "cpe:2.3:a:example_company:product_a:1.1.0:*:*:*:*:*:*:*"
                  }
                }
              }
            ],
            "category": "product_name",
            "name": "Product A"
          },
          {
            "branches": [
              {
                "category": "product_version",
                "name": "2023",
                "product": {
                  "name": "Example Company Product B 2023",
                  "product_id": "CSAFPID-908070603",
                  "product_identification_helper": {
                    "cpe": "cpe:2.3:o:example_company:product_b:2023:*:*:*:*:*:*:*"
                  }
                }
              },
              {
                "category": "product_version",
                "name": "2024",
                "product": {
                  "name": "Example Company Product B 2024",
                  "product_id": "CSAFPID-908070604",
                  "product_identification_helper": {
                    "cpe": "cpe:2.3:o:example_company:product_b:2024:*:*:*:*:*:*:*"
                  }
                }
              }
            ],
            "category": "product_name",
            "name": "Product B"
          },
          {
            "branches": [
              {
                "category": "product_version",
                "name": "EU",
                "product": {
                  "name": "Example Company Product C EU",
                  "product_id": "CSAFPID-908070605",
                  "product_identification_helper": {
                    "cpe": "cpe:2.3:h:example_company:product_c:eu:*:*:*:*:*:*:*"
                  }
                }
              },
              {
                "category": "product_version",
                "name": "US",
                "product": {
                  "name": "Example Company Product C US",
                  "product_id": "CSAFPID-908070606",
                  "product_identification_helper": {
                    "cpe": "cpe:2.3:h:example_company:product_c:us:*:*:*:*:*:*:*"
                  }
                }
              }
            ],
            "category": "product_name",
            "name": "Product C"
          }
        ],
        "category": "vendor",
        "name": "Example Company"
      }
    ],
    "product_paths": [
      {
        "beginning_product_reference": "CSAFPID-908070601",
        "full_product_name": {
          "name": "Example Company Product A 1.0.0 installed on Example Company Product B 2023",
          "product_id": "CSAFPID-908070607",
          "product_identification_helper": {
            "cpe": "cpe:2.3:a:example_company:product_a:1.0.0:*:*:*:*:product_b_2023:*:*"
          }
        },
        "subpaths": [
          {
            "category": "installed_on",
            "next_product_reference": "CSAFPID-908070603"
          }
        ]
      },
      // ...
      {
        "beginning_product_reference": "CSAFPID-908070607",
        "full_product_name": {
          "name": "Example Company Product A 1.0.0 installed on Example Company Product B 2023 installed on Example Company Product C EU",
          "product_id": "CSAFPID-908070611",
          "product_identification_helper": {
            "cpe": "cpe:2.3:a:example_company:product_a:1.0.0:*:*:*:*:product_b_2023:product_c_eu:*"
          }
        },
        "subpaths": [
          {
            "category": "installed_on",
            "next_product_reference": "CSAFPID-908070605"
          }
        ]
      },
      // ...
    ]
  }
```

> Product paths in example 3 cannot be collapsed without information loss.
> For example, the `cpe` of the product identified by `CSAFPID-908070607` would be lost.

*Example 4 (which is not collapsed nor collapsible as products are referenced)*:

```
  {
    // ...
    "product_tree": {
      "branches": [
        {
          "branches": [
            {
              "branches": [
                {
                  "category": "product_version",
                  "name": "1.0.0",
                  "product": {
                    "name": "Example Company Product A 1.0.0",
                    "product_id": "CSAFPID-908070601"
                  }
                },
                // ...
              ],
              "category": "product_name",
              "name": "Product A"
            },
            {
              "branches": [
                {
                  "category": "product_version",
                  "name": "2023",
                  "product": {
                    "name": "Example Company Product B 2023",
                    "product_id": "CSAFPID-908070603"
                  }
                },
                // ...
              ],
              "category": "product_name",
              "name": "Product B"
            },
            {
              "branches": [
                {
                  "category": "product_version",
                  "name": "EU",
                  "product": {
                    "name": "Example Company Product C EU",
                    "product_id": "CSAFPID-908070605"
                  }
                },
                // ...
              ],
              "category": "product_name",
              "name": "Product C"
            }
          ],
          "category": "vendor",
          "name": "Example Company"
        }
      ],
      // ...
      "product_paths": [
        {
          "beginning_product_reference": "CSAFPID-908070601",
          "full_product_name": {
            "name": "Example Company Product A 1.0.0 installed on Example Company Product B 2023",
            "product_id": "CSAFPID-908070607"
          },
          "subpaths": [
            {
              "category": "installed_on",
              "next_product_reference": "CSAFPID-908070603"
            }
          ]
        },
        // ...
        {
          "beginning_product_reference": "CSAFPID-908070607",
          "full_product_name": {
            "name": "Example Company Product A 1.0.0 installed on Example Company Product B 2023 installed on Example Company Product C EU",
            "product_id": "CSAFPID-908070611"
          },
          "subpaths": [
            {
              "category": "installed_on",
              "next_product_reference": "CSAFPID-908070605"
            }
          ]
        },
        // ...
      ]
    },
    "vulnerabilities": [
      {
        "product_status": {
          "under_investigation": [
            "CSAFPID-908070607",
            // ...
          ]
        }
      },
      {
        "threats": [
          {
            "category": "target_set",
            "details": "These products are known to be specifically targeted by APT-00.",
            "product_ids": [
              "CSAFPID-908070607",
              // ...
            ]
          }
        ]
      }
    ]
  }
```

> Product paths in example 4 cannot be collapsed as the products inside the path are referenced elsewhere in the document.
> For example, `CSAFPID-908070607` is also referenced in the product status and threats.
