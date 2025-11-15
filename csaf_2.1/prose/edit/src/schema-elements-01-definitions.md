## Definitions

The definitions (`$defs`) introduce the following domain specific types into the CSAF language:
Acknowledgments (`acknowledgments_t`), Branches (`branches_t`), Full Product Name (`full_product_name_t`), Language (`lang_t`), Notes (`notes_t`),
Product Group ID (`product_group_id_t`), Product Groups (`product_groups_t`), Product ID (`product_id_t`), Products (`products_t`),
References (`references_t`), and Version (`version_t`).

```yaml
$defs:
  acknowledgments_t: Sequence
  branches_t: Sequence
  full_product_name_t: Mapping
  lang_t: String.Pattern
  notes_t: Sequence
  product_group_id_t: String
  product_groups_t: Sequence
  product_id_t: String
  products_t: Sequence
  references_t: Sequence
  version_t: String.Pattern
```
