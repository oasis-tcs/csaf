### Multiple Flags with VEX Justification Codes per Product

For each item in `/vulnerabilities[]` it MUST be tested that a Product is not member of more than one Flag item with
a VEX justification code (see section [sec](#vulnerabilities-property-flags)).
This takes indirect relations through Product Groups into account.

> Additional flags with a different purpose might be provided in later versions of CSAF.
> Through the explicit reference of VEX justification codes the test is specified to be forward-compatible.

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

> There are two flags given for `CSAFPID-9080700` - one indirect through `CSAFGID-0001` and one direct.
