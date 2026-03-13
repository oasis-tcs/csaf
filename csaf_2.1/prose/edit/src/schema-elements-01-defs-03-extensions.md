### Extensions Type

List of extensions (`extensions_t`) of value type `array` with `1` or more unique items (a `set`) contains a list of extension elements
for the current context.

```yaml <!--json-path($['$defs'].extensions_t)-->
$defs:
  # ...
  extensions_t: Sequence
  # ...
```

Each item MUST comply with the rules for CSAF Extensions and validate against the
[CSAF Extension Content schema](https://docs.oasis-open.org/csaf/csaf/v2.1/schema/extension-content.json) as well as the schema given
through its `$schema` property.
