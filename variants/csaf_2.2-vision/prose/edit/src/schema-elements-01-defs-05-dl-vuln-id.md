### Document-local Vuln ID Type

The Document-local Vuln ID Type (`dl_vuln_id_t`) of value type `string` with `6` or more characters is a document-local
reference token for vulnerability instances.
It SHALL conform to `pattern` (regular expression):

```
    ^VULN-[0-9A-Za-z._-]+$
```

The value contains a token required to identify a vulnerability uniquely in the context of the current document so that it can be referred to from other parts in the document.
It SHOULD NOT to be used to refer to a vulnerability from outside of the CSAF document.

```yaml <!--json-path($['$defs'].dl_vuln_id_t)-->
$defs:
  # ...
  dl_vuln_id_t: String.Pattern
  # ...
```

*Examples 1:*

```
    VULN-0001
    VULN-CVE-1900-0001
```

