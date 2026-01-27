### Overlapping Product Version Range

This subsubsection structures the recommended tests for overlapping product version ranges.
The following definitions apply to all tests:

* Two product version ranges `a` and `b` are overlapping if the intersection of their sets of product versions `a'` and `b'` does not
  result in an empty set.

  > As the intersect operation is commutative it is sufficient to test one order.

* A product version `c` overlaps with a product version range `a` if `c` is included in `a`.
* An element of type `/$defs/full_product_name_t` which has a branch category of `product_version_range` in the path leading to it,
  is called "element with product version range" (`EPVR`).
* The corresponding Product ID identifying such an `EPVR` is called "EPVR Product ID" (`EPVRPID`).
* For each element of type `/$defs/branches_t` with `category` of `product_version_range` which is called
  "currently tested product version range" (`CTPVR`), all sibling elements on the same level form the
  "group of sibling elements of the product version range" (`GSEPVR`).
* The group `GSEPVR` is divided in three pairwise disjoint sets:
  1. Elements that have the branch category `product_version_range` form the "product version range sibling set" (`PVRSS`).
  2. Elements that have the branch category `product_version` form the "product version sibling set" (`PVSS`).
  3. Elements that do not fall into 1 or 2 form the "other branch category sibling set" (`OBCSS`).
* `PVRSS` is divided in three pairwise disjoint sets:
  1. Elements that use valid vers form the "product version range sibling set - vers" (`PVRSS-vers`).
  2. Elements that use valid vls form the "product version range sibling set - vls" (`PVRSS-vls`).
  3. Elements that do not fall into 1 or 2 form the "product version range sibling set - invalid" (`PVRSS-invalid`).
* `PVRSS` elements can also be grouped into three pairwise disjoint sets:
  1. Elements that contain the `branches` as only optional property form the "product version range sibling set with branches" (`PVRSS+b`).
  2. Elements that contain the `product` as only optional property form the "product version range sibling set with leaf" (`PVRSS+l`).
  3. Elements that do not fall into 1 or 2 form the "product version range sibling set - invalid branch" (`PVRSS+i`).
* Attributes of `PVRSS` elements can be combined:
  1. Product version range sibling set with branches - vers (`PVRSS+b-vers`): Intersection of `PVRSS+b` and `PVRSS-vers`
  2. Product version range sibling set with branches - vls (`PVRSS+b-vls`): Intersection of `PVRSS+b` and `PVRSS-vls`
  3. Product version range sibling set with leaf - vers (`PVRSS+l-vers`): Intersection of `PVRSS+l` and `PVRSS-vers`
  4. Product version range sibling set with leaf - vls (`PVRSS+l-vls`): Intersection of `PVRSS+l` and `PVRSS-vls`
  5. Product version range sibling set with branches - invalid (`PVRSS+b-invalid`): Intersection of `PVRSS+b` and `PVRSS-invalid`
  6. Product version range sibling set with leaf - invalid (`PVRSS+l-invalid`): Intersection of `PVRSS+l` and `PVRSS-invalid`
  7. Product version range sibling set - invalid branch - vers (`PVRSS+i-vers`): Intersection of `PVRSS+i` and `PVRSS-vers`
  8. Product version range sibling set - invalid branch - vls (`PVRSS+i-vls`): Intersection of `PVRSS+i` and `PVRSS-vls`
  9. Product version range sibling set - invalid branch - invalid (`PVRSS+i-invalid`): Intersection of `PVRSS+i` and `PVRSS-invalid`

> Elements in the set `PVRSS+i` are detectable via the validation of the JSON schema and therefore ignored in these tests.
> The exact characteristic of the product version range is of minor importance as the tests cannot produce any valuable result in such an
> invalid product tree.
> Elements in `PVRSS-invalid` should be detected by test [sec](#product-version-range-rules).

#### Overlapping Product Version Range with vers in Contradicting Product Status Group

For each item in `/vulnerabilities` all `EPVRPID` in the product status groups MUST be identified.
For each `EPVR` (as `CTPVR`), it MUST be tested that the Product IDs of all elements in `PVRSS+l-vers` that overlap with `CTPVR` are not
member of a contradicting product status groups (see section [sec](#vulnerabilities-property-product-status)).

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
        "known_affected": [
          "CSAFPID-9080700"
        ],
        "known_not_affected": [
          "CSAFPID-9080701"
        ]
      }
    }
  ]
```

> The product version ranges of `CSAFPID-9080700` and `CSAFPID-9080701` overlap but they are members of the contradicting groups "Affected"
> and "Not affected".
> For the version range `vers:intdot/>2.1.0|<2.4.0` it cannot be determined which product status is applicable.

> A tool MAY split overlapping product version ranges into no-overlapping ones to simplify the resolution a quick fix.
