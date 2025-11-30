### Hardware and Software

For each product containing at least one of the Product Identification Helpers `serial_numbers` or `model_numbers` it MUST be tested that a relationship exists referencing this product.

> This tests detects a potential situation where hardware and software have been mixed in the `product_tree`.
> Note: This test will fail if the CSAF document contains in its `product_tree` only hardware.
> However, this is expected and considered a good reason for the test to fail.
> This does not make the CSAF document invalid.

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/product
  /product_tree/full_product_names[]
  /product_tree/relationships[]/full_product_name
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
                "category": "product_version",
                "name": "4.1",
                "product": {
                  "name": "Example Company Controller A Firmware 4.1",
                  "product_id": "CSAFPID-908070601",
                  "product_identification_helper": {
                    "serial_numbers": [
                      "143-D-354"
                    ]
                  }
                }
              }
            ],
            "category": "product_name",
            "name": "Controller A"
          }
        ],
        "category": "vendor",
        "name": "Example Company"
      }
    ]
  }
```

> The `product_tree` mentions the hardware product Example Company Controller A and combines it with the Firmware version 4.1.

> A correct representation for hardware and software in the `product_tree` is given in example 1 in section [sec](#hardware-and-software-within-the-product-tree).
