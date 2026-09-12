### Action ID Type

The Action ID Type (`action_id_t`) of value type `string` with `1` or more characters is a reference token for action instances.
It SHALL conform to `pattern` (regular expression):

```
    ^[^\\s\\-_\\.](.*[^\\s\\-_\\.])?$
```

The value contains a token required to identify an action uniquely in the context of the current document so that it can be referred to from other parts in the document.

```yaml <!--json-path($['$defs'].action_id_t)-->
$defs:
  # ...
  action_id_t: String.Pattern
  # ...
```

*Examples 1:*

```

    1
    AID-0001
    Some ID
```
