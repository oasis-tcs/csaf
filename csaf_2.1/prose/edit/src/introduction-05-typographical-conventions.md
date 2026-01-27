## Typographical Conventions

Keywords defined by this specification use this `monospaced` font.

```
    Normative source code uses this paragraph style.
```

The information models of the CSAF schemata are illustrated in the prose in a generic YAML format in the shape of outlines.
In contrast to extracts of JSON snippets in prior versions of this specification such YAML snippets can be annotated and validated both as being well-formed and matching the schema part.
These outlines are directly extractable per JSON Paths from the corresponding CSAF schema as documented in the normative format of this specification.
The types used are the general `Mapping`, `Sequence`, and `String` types.
The latter may be further constrained to specific facets like for example enumerations noted as `String.Enum`.
General instances (like a CSAF document) are noted as such in angle brackets to emphasize the topology.
Items of sequences are noted as YAML sequence items and annotated per comments naming the kind of sequence item they represent.

Some sections of this specification are illustrated with non-normative examples introduced with "Example" or "Examples" like so:

*Example 1:*

```
    Informative examples also use this paragraph style but preceded by the text "Example(s)".
```

All examples in this document are informative only.

All other text is normative unless otherwise labeled e.g. like the following informative comment:

> This is a pure informative comment that may be present, because the information conveyed is deemed useful advice or
> common pitfalls learned from implementer or operator experience and often given including the rationale.

-------

This document adheres to the Modern Language Association (MLA) style guidelines for formatting titles and terms.
