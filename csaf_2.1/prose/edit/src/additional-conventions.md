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
/product_tree/branches[]/branches[]/branches[]/branches[]/branches[]/branches[]/←
branches[]/branches[]/branches[]/branches[]/branches[]/branches[]/branches[]/←
branches[]/branches[]/branches[]/branches[]/branches[]/branches[]/branches[]/←
branches[]/branches[]/branches[]/branches[]/branches[]/branches[]/branches[]/←
branches[]/branches[]/branches[]/product
```

  > For the significance of the left pointing arrow character (`←`) at the end of lines in the preceding longest path to a leaf please
  > cf. the guidance in section [sec](#typographical-conventions).

-------
