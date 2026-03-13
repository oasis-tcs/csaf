### Extensions Property

Root-level Extensions (`x_extensions`) of value type Extensions Type (`extensions_t`) contains a list of extensions valid
at the root-level of the CSAF document and associated with this CSAF document.

```yaml <!--json-paths($..x_extensions, $['$defs'].extensions_t..properties)-->
<csaf-instance>:
  # ...
  x_extensions:  # $defs.extensions_t
  - # <x_extension-instance>:
    $schema: String
    category: String.Enum
    content: Mapping
    critical: Boolean
    # ...
```

-------
