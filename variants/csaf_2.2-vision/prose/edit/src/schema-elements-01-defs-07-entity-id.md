### Entity ID Type

The Entity ID Type (`entity_id_t`) of value type `string` with `5` or more characters is a reference token for entity instances.
It SHALL conform to `pattern` (regular expression):

```
    ^EID-[0-9A-Za-z][0-9A-Za-z._-]*$
```

The value contains a token required to identify an entity uniquely in the context of the current document
so that it can be referred to from other parts in the document.

```yaml <!--json-path($['$defs'].entity_id_t)-->
$defs:
  # ...
  entity_id_t: String.Pattern
  # ...
```

*Examples 1:*

```
    EID-0001
    EID-CERT
    EID-Example_Company
    EID-org.example
```
