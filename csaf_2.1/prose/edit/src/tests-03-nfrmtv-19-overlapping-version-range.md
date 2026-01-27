### Overlapping Product Version Range{informative-tests--overlapping-product-version-range}

This subsubsection structures the informative tests for overlapping product version ranges.
These tests provide weak indicators of potential errors in the construction of the product tree.

#### Overlapping Product Version Range with vers in Same Product Status Group

For each item in `/vulnerabilities` all `EPVRPID` in the product status groups MUST be identified.
For each `EPVR` (as `CTPVR`), it MUST be tested that the Product IDs of all elements in `PVRSS+l-vers` that overlap with `CTPVR` are not
member of the same product status group (see section [sec](#vulnerabilities-property-product-status)).

The relevant path for this test is:

```
    /vulnerabilities[]/product_status
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
                "category": "product_version_range",
                "name": "vers:intdot/>2.1.0|<4.2.0",
                "product": {
                  "name": "Example Company Product A >2.1.0|<4.2.0",
                  "product_id": "CSAFPID-9080700"
                }
              },
              {
                "category": "product_version_range",
                "name": "vers:intdot/>1.2.0|<2.4.0",
                "product": {
                  "name": "Example Company Product A >1.2.0|<2.4.0",
                  "product_id": "CSAFPID-9080701"
                }
              }
            ],
            "category": "product_name",
            "name": "Product A"
          }
        ],
        "category": "vendor",
        "name": "Example Company"
      }
    ]
  },
  "vulnerabilities": [
    {
      "product_status": {
        "first_fixed": [
          "CSAFPID-9080701"
        ],
        "fixed": [
          "CSAFPID-9080700"
        ]
      }
    }
  ]
```

> The product version ranges of `CSAFPID-9080700` and `CSAFPID-9080701` overlap and they are members of the same group "Fixed".

> A tool MAY split overlapping product version ranges into non-overlapping ones to simplify the resolution as a quick fix.

#### Overlapping Product Version Range with vls in Same Product Status Group

For each item in `/vulnerabilities` all `EPVRPID` in the product status groups MUST be identified.
For each `EPVR` (as `CTPVR`), it MUST be tested that the Product IDs of all elements in `PVRSS+l-vls` that overlap with `CTPVR` are not
member of the same product status group (see section [sec](#vulnerabilities-property-product-status)).

The relevant path for this test is:

```
    /vulnerabilities[]/product_status
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
                "category": "product_version_range",
                "name": ">2.1.0|<4.2.0",
                "product": {
                  "name": "Example Company Product A >2.1.0|<4.2.0",
                  "product_id": "CSAFPID-9080700"
                }
              },
              {
                "category": "product_version_range",
                "name": ">1.2.0|<2.4.0",
                "product": {
                  "name": "Example Company Product A >1.2.0|<2.4.0",
                  "product_id": "CSAFPID-9080701"
                }
              }
            ],
            "category": "product_name",
            "name": "Product A"
          }
        ],
        "category": "vendor",
        "name": "Example Company"
      }
    ]
  },
  "vulnerabilities": [
    {
      "product_status": {
        "first_fixed": [
          "CSAFPID-9080701"
        ],
        "fixed": [
          "CSAFPID-9080700"
        ]
      }
    }
  ]
```

> The product version ranges of `CSAFPID-9080700` and `CSAFPID-9080701` overlap and they are members of the same group "Fixed".

> A tool MAY split overlapping product version ranges into non-overlapping ones to simplify the resolution as a quick fix.

#### Overlapping Product Version Range with Product Version in Same Product Status Group

For each item in `/vulnerabilities` all `EPVRPID` in the product status groups MUST be identified.
For each `EPVR` (as `CTPVR`), it MUST be tested that the Product IDs of all elements in `PVSS` that overlap with `CTPVR` are not
member of the same product status group (see section [sec](#vulnerabilities-property-product-status)).

The relevant path for this test is:

```
    /vulnerabilities[]/product_status
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
                "category": "product_version_range",
                "name": "vers:intdot/>2.1.0|<4.2.0",
                "product": {
                  "name": "Example Company Product A >2.1.0|<4.2.0",
                  "product_id": "CSAFPID-9080700"
                }
              },
              {
                "category": "product_version",
                "name": "2.4.0",
                "product": {
                  "name": "Example Company Product A 2.4.0",
                  "product_id": "CSAFPID-9080701"
                }
              }
            ],
            "category": "product_name",
            "name": "Product A"
          }
        ],
        "category": "vendor",
        "name": "Example Company"
      }
    ]
  },
  "vulnerabilities": [
    {
      "product_status": {
        "first_fixed": [
          "CSAFPID-9080701"
        ],
        "fixed": [
          "CSAFPID-9080700"
        ]
      }
    }
  ]
```

> The product version ranges of `CSAFPID-9080700` and `CSAFPID-9080701` overlap and they are members of the same group "Fixed".

> A tool MAY exclude the overlapping product version from the product version range as a quick fix.

#### Overlapping Product Version Range with Product Version Range in Branch

For each item in `/vulnerabilities` all `EPVRPID` in the product status groups MUST be identified.
For each `EPVR` (as `CTPVR`), it MUST be tested that all product version ranges of elements in `PVRSS+b` do not overlap with `CTPVR`.

The relevant path for this test is:

```
     /product_tree/branches[](/branches[])*/name
```

*Example 1 (which fails the test):*

```
    {
      "branches": [
        {
          "branches": [
            // ...
          ],
          "category": "product_version_range",
          "name": "vers:intdot/>2.1.0|<4.2.0"
        },
        {
          "branches": [
            // ...
          ],
          "category": "product_version_range",
          "name": "vers:intdot/>1.2.0|<2.4.0"
        }
      ],
      // ...
    }
```

> The product version ranges overlap.

> A tool MAY split overlapping product version ranges into non-overlapping ones to simplify the resolution as a quick fix.
