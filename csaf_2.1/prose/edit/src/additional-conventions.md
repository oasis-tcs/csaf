# Additional Conventions

This section provides additional rules for handling CSAF documents.

## Filename

The following rules MUST be applied to determine the filename for the CSAF document:

1. The value `/document/tracking/id` is converted into lower case.
2. Any character sequence which is not part of one of the following groups MUST be replaced by a single underscore (`_`):
   * Lower case ASCII letters (0x61 - 0x7A)
   * digits (0x30 - 0x39)
   * special characters: `+` (0x2B), `-` (0x2D)
   > The regex `[^+\-a-z0-9]+` can be used to find a character sequence which has to be replaced by an underscore.
   > However, it SHALL NOT be applied before completing the first step.
   >
   > Even though the underscore `_` (0x5F) is a valid character in the filename it is replaced to avoid situations
   > where the conversion rule might lead to multiple consecutive underscores.
   > As a result, a `/document/tracking/id` with the value `2022_#01-A` is converted into `2022_01-a` instead of `2022__01-a`.
3. The file extension `.json` MUST be appended.

*Examples 1:*

```
  cisco-sa-20190513-secureboot.json
  example_company_-_2019-yh3234.json
  rhba-2019_0024.json
```

> It is currently considered best practice to indicate that a CSAF document is invalid by
> inserting `_invalid` into the filename in front of the file extension.

*Examples 2:*

```
  cisco-sa-20190513-secureboot_invalid.json
  example_company_-_2019-yh3234_invalid.json
  rhba-2019_0024_invalid.json
```

## Separation in Data Stream

If multiple CSAF documents are transported via a data stream in a sequence without requests inbetween,
they MUST be separated by the Record Separator in accordance with [cite](#RFC7464).

## Sorting{#additional-conventions--sorting}

The keys within a CSAF document SHOULD be sorted alphabetically.

## Usage of Markdown

The use of GitHub-flavoured Markdown is permitted in the following fields:

```
  /document/acknowledgments[]/summary
  /document/distribution/text
  /document/notes[]/text
  /document/publisher/issuing_authority
  /document/references[]/summary
  /document/tracking/revision_history[]/summary
  /product_tree/product_groups[]/summary
  /vulnerabilities[]/acknowledgments[]/summary
  /vulnerabilities[]/involvements[]/summary
  /vulnerabilities[]/notes[]/text
  /vulnerabilities[]/references[]/summary
  /vulnerabilities[]/remediations[]/details
  /vulnerabilities[]/remediations[]/entitlements[]
  /vulnerabilities[]/remediations[]/restart_required/details
  /vulnerabilities[]/threats[]/details
```

Other fields MUST NOT contain Markdown.

## Branch recursion

The `/product_tree` uses a nested structure for `branches`. Along a single path to a leaf, the recursion of `branches` is limited to 30 repetitions. Therefore, the longest path to a leaf is:

```
/product_tree/branches[]/branches[]/branches[]/branches[]/branches[]/branches[]/branches[]/branches[]/branches[]/branches[]/branches[]/branches[]/branches[]/branches[]/branches[]/branches[]/branches[]/branches[]/branches[]/branches[]/branches[]/branches[]/branches[]/branches[]/branches[]/branches[]/branches[]/branches[]/branches[]/branches[]/product
```

## Hardware and Software within the Product Tree

If a product consists of hardware and software, the hardware part MUST be presented as one product in the product tree and the software part as another one.
To form the overall product, both parts MUST be combined through a relationship.

*Examples 1:*

```
  "product_tree": {
    "branches": [
      {
        "branches": [
          {
            "branches": [
              {
                "category": "product_version",
                "name": "1.0",
                "product": {
                  "name": "Example Company Controller A 1.0",
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
          },
          {
            "branches": [
              {
                "category": "product_version",
                "name": "4.1",
                "product": {
                  "name": "Example Company Controller A Firmware 4.1",
                  "product_id": "CSAFPID-908070602",
                  "product_identification_helper": {
                    "hashes": [
                      {
                        "file_hashes": [
                          {
                            "algorithm": "sha256",
                            "value": "3fb9d502d096b1dfbcdfe60eed80ddecd98c8771bf21a82bbe1752735c4dc9e2"
                          }
                        ],
                        "filename": "a_4-1.bin"
                      }
                    ]
                  }
                }
              },
              {
                "category": "product_version",
                "name": "4.2",
                "product": {
                  "name": "Example Company Controller A Firmware 4.2",
                  "product_id": "CSAFPID-908070603",
                  "product_identification_helper": {
                    "hashes": [
                      {
                        "file_hashes": [
                          {
                            "algorithm": "sha256",
                            "value": "0a853ce2337f0608489ac596a308dc5b7b19d35a52b10bf31261586ac368b175"
                          }
                        ],
                        "filename": "a_4-2.bin"
                      }
                    ]
                  }
                }
              }
            ],
            "category": "product_name",
            "name": "Controller A Firmware"
          }
        ],
        "category": "vendor",
        "name": "Example Company"
      }
    ],
    "relationships": [
      {
        "category": "installed_on",
        "full_product_name": {
          "name": "Example Company Controller A Firmware 4.1 installed on Example Company Controller A 1.0",
          "product_id": "CSAFPID-908070604"
        },
        "product_reference": "CSAFPID-908070602",
        "relates_to_product_reference": "CSAFPID-908070601"
      },
      {
        "category": "installed_on",
        "full_product_name": {
          "name": "Example Company Controller A Firmware 4.2 installed on Example Company Controller A 1.0",
          "product_id": "CSAFPID-908070605"
        },
        "product_reference": "CSAFPID-908070603",
        "relates_to_product_reference": "CSAFPID-908070601"
      }
    ]
  }
```

> This requirement is important to allow for correct matching.
> The serial number `143-D-354` identifies the `Example Company Controller A 1.0` which is in this example the hardware in its version 1.0.
> The hash `3fb9d502d096b1dfbcdfe60eed80ddecd98c8771bf21a82bbe1752735c4dc9e2` identifies the software in the version 4.1;
> the hash `0a853ce2337f0608489ac596a308dc5b7b19d35a52b10bf31261586ac368b175` identifies the software in the version 4.2.
> The relationships combine the software and hardware part and form new products.
> These are used e.g. to assign the product status in the vulnerability section.
>
> A matching tool can search for the serial number in an asset database and identify the asset that has this specific hardware.
> Afterwards, the software can be matched separately.
>
> Representing the software version as a child element under elements representing hardware unsettles the consumer whether the version
> applies to the software or hardware.
> Also, this would violate the rule regarding the full identification of a product by the `product_identification_helper` from section
> [sec](#full-product-name-type-product-identification-helper).
>
> Based on the CVE statistics up to and including the year 2024, in the majority of cases the vulnerabilities reside in software or
> are remediated via software.
> Having multiple products with the same `product_identification_helper` in different `product_status` for the same vulnerability
> would make it undecidable for machines what the `product_status` actually is.

-------
