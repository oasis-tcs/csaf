### Branches Recursion Depth{#mandatory-tests--branches-recursion-depth}

For each product defined under `/product_tree/branches[]` it MUST be tested that the complete JSON path
does not contain more than 30 instances of `branches`.

The relevant path for this test is:

```
  /product_tree/branches[](/branches[])*/product
```

*Example 1 (which fails the test):*

```
  "product_tree": {
    "branches": [
      {
        "branches": [
          {
            "branches": [
              {
                "branches": [
                  {
                    "branches": [
                      {
                        "branches": [
                          {
                            "branches": [
                              {
                                "branches": [
                                  {
                                    "branches": [
                                      {
                                        "branches": [
                                          {
                                            "branches": [
                                              {
                                                "branches": [
                                                  {
                                                    "branches": [
                                                      {
                                                        "branches": [
                                                          {
                                                            "branches": [
                                                              {
                                                                "branches": [
                                                                  {
                                                                    "branches": [
                                                                      {
                                                                        "branches": [
                                                                          {
                                                                            "branches": [
                                                                              {
                                                                                "branches": [
                                                                                  {
                                                                                    "branches": [
                                                                                      {
                                                                                        "branches": [
                                                                                          {
                                                                                            "branches": [
                                                                                              {
                                                                                                "branches": [
                                                                                                  {
                                                                                                    "branches": [
                                                                                                      {
                                                                                                        "branches": [
                                                                                                          {
                                                                                                            "branches": [
                                                                                                              {
                                                                                                                "branches": [
                                                                                                                  {
                                                                                                                    "branches": [
                                                                                                                      {
                                                                                                                        "branches": [
                                                                                                                          {
                                                                                                                            "branches": [
                                                                                                                              {
                                                                                                                                "category": "product_name",
                                                                                                                                "name": "branches",
                                                                                                                                "product": {
                                                                                                                                  "name": "<<generate Product name>>",
                                                                                                                                  "product_id": "CSAFPID-9080700"
                                                                                                                                }
                                                                                                                              }
                                                                                                                            ],
                                                                                                                            "category": "product_family",
                                                                                                                            "name": "31"
                                                                                                                          }
                                                                                                                        ],
                                                                                                                        "category": "product_family",
                                                                                                                        "name": "with"
                                                                                                                      }
                                                                                                                    ],
                                                                                                                    "category": "product_family",
                                                                                                                    "name": "test"
                                                                                                                  }
                                                                                                                ],
                                                                                                                "category": "product_family",
                                                                                                                "name": "the"
                                                                                                              }
                                                                                                            ],
                                                                                                            "category": "product_family",
                                                                                                            "name": "fail"
                                                                                                          }
                                                                                                        ],
                                                                                                        "category": "product_family",
                                                                                                        "name": "and"
                                                                                                      }
                                                                                                    ],
                                                                                                    "category": "product_family",
                                                                                                    "name": "limits"
                                                                                                  }
                                                                                                ],
                                                                                                "category": "product_family",
                                                                                                "name": "the"
                                                                                              }
                                                                                            ],
                                                                                            "category": "product_family",
                                                                                            "name": "testing"
                                                                                          }
                                                                                        ],
                                                                                        "category": "product_family",
                                                                                        "name": "are"
                                                                                      }
                                                                                    ],
                                                                                    "category": "product_family",
                                                                                    "name": "they"
                                                                                  }
                                                                                ],
                                                                                "category": "product_family",
                                                                                "name": "but"
                                                                              }
                                                                            ],
                                                                            "category": "product_family",
                                                                            "name": "unrealistic"
                                                                          }
                                                                        ],
                                                                        "category": "product_family",
                                                                        "name": "less"
                                                                      }
                                                                    ],
                                                                    "category": "product_family",
                                                                    "name": "or"
                                                                  }
                                                                ],
                                                                "category": "product_family",
                                                                "name": "more"
                                                              }
                                                            ],
                                                            "category": "product_family",
                                                            "name": "and"
                                                          }
                                                        ],
                                                        "category": "product_family",
                                                        "name": "unnecessary"
                                                      }
                                                    ],
                                                    "category": "product_family",
                                                    "name": "seem"
                                                  }
                                                ],
                                                "category": "product_family",
                                                "name": "which"
                                              }
                                            ],
                                            "category": "product_family",
                                            "name": "product"
                                          }
                                        ],
                                        "category": "product_family",
                                        "name": "hypothetical"
                                      }
                                    ],
                                    "category": "product_family",
                                    "name": "this"
                                  }
                                ],
                                "category": "product_family",
                                "name": "for"
                              }
                            ],
                            "category": "product_family",
                            "name": "structure"
                          }
                        ],
                        "category": "product_family",
                        "name": "nested"
                      }
                    ],
                    "category": "product_family",
                    "name": "deeply"
                  }
                ],
                "category": "product_family",
                "name": "a"
              }
            ],
            "category": "product_family",
            "name": "uses"
          }
        ],
        "category": "vendor",
        "name": "Example Company"
      }
    ]
  }
```

> The complete JSON path contains 31 times `branches`.
