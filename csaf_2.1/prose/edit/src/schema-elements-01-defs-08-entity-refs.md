### Entity Refs Type

List of entity references (`entity_refs_t`) of value type `array` with `1` or more unique items (a `set`)
specifies a list of `entity_ids` or `entity_group_ids` to give context to the parent item.

```yaml <!--json-path($['$defs'].entity_refs_t)-->
$defs:
  # ...
  entity_refs_t: Sequence
  # ...
```

Value type of every such entity reference item is any of Entity Group ID Type (`entity_group_id_t`) or Entity ID Type (`entity_id_t`).

```yaml <!--json-path($['$defs'].entity_refs_t[*].properties)-->
$defs:
  # ...
  entity_refs_t:
  - # <entity-ref-instance>:
    # !AnyOf<
    - $defs.entity_group_id_t
    - $defs.entity_id_t
    #>
  # ...
```

This type allows to reference Entity IDs directly and indirectly via an Entity Group ID within the same data structure.

> The usage of the `anyOf` schema constraint allows for a faster evaluation.
> However, such construct needs to ensure that the schemas have no overlap.
