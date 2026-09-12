### Entity Group ID Type

The Entity Group ID Type (`entity_group_id_t`) of value type `string` with `6` or more characters is a reference token for
entity group instances.
It SHALL conform to `pattern` (regular expression):

```
    ^EGID-[0-9A-Za-z][0-9A-Za-z._-]*$
```

The value contains a token required to identify a group of entities uniquely in the context of the current document
so that it can be referred to from other parts in the document.

```yaml <!--json-path($['$defs'].entity_group_id_t)-->
$defs:
  # ...
  entity_group_id_t: String.Pattern
  # ...
```

*Examples 1:*

```
    EGID-0001
    EGID-CERTs
    EGID-Coordinators
    EGID-vendors
```
