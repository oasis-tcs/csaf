### References Type

List of references (`references_t`) of value type `array` with `1` or more items of type Reference holds a list of Reference objects.

```yaml
$defs:
  # ...
  references_t: Sequence
  # ...
```

Value type of every such Reference item is `object` with the mandatory properties `url` and `summary` holding any reference to conferences,
papers, advisories, and other resources that are related and considered related to either a surrounding part of or
the entire document and to be of value to the document consumer.
A reference `object` MAY provide the optional property `category`.

```yaml
$defs:
  # ...
  references:
  - # <reference-instance>:
    category: String
    summary: String
    url: String.URI
  # ...
```

Category of reference (`category`) of value type `string` and `enum` indicates whether the reference points to the same document or
vulnerability in focus (depending on scope) or to an external resource.
Valid `enum` values are:

```
    external
    self
```

The default value for `category` is `external`.

The value `external` indicates, that this document is an external reference to a document or vulnerability in focus (depending on scope).

The value `self` indicates, that this document is a reference to this same document or vulnerability (also depending on scope).

> This includes links to documents with the same content but different file format (e.g. advisories as PDF or HTML).

Summary of the reference (`summary`) of value type `string` with `1` or more characters indicates what this reference refers to.

URL of reference (`url`) of value type `string` with format `uri` provides the URL for the reference.
