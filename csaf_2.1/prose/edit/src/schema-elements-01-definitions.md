## Definitions

The definitions (`$defs`) introduce the following domain specific types into the CSAF language:
Acknowledgments (`acknowledgments_t`), Action ID (`action_id_t`), Branches (`branches_t`), Contact (`contact_t`),
Document-local Vuln ID (`dl_vuln_id_t`), Entity Group ID (`entity_group_id_t`), Entity ID (`entity_id_t`),
Entity Refs (`entity_refs_t`), Extensions (`extensions_t`), Full Product Name (`full_product_name_t`),
Language (`lang_t`), Notes (`notes_t`), Product Group ID (`product_group_id_t`), Product Groups (`product_groups_t`),
Product ID (`product_id_t`), Products (`products_t`), References (`references_t`), Subpath (`subpath_t`) and Version (`version_t`).

```yaml <!--json-path($['$defs'])-->
$defs:
  acknowledgments_t: Sequence
  action_id_t: String.Pattern
  branches_t: Sequence
  contact_t: Mapping
  dl_vuln_id_t: String.Pattern
  entity_group_id_t: String.Pattern
  entity_id_t: String.Pattern
  entity_refs_t: Sequence
  extensions_t: Sequence
  full_product_name_t: Mapping
  lang_t: String.Pattern
  notes_t: Sequence
  product_group_id_t: String
  product_groups_t: Sequence
  product_id_t: String
  products_t: Sequence
  references_t: Sequence
  subpath_t: Mapping
  version_t: String.Pattern
```
