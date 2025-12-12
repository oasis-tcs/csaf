# List of known issues in CSAF CVRF 1.2

## List of issues not addressed in an Errata

- The Aggregate Severity Namespace attribute is documented incorrectly.
  It does not clearly state that the value MUST be an URI of type `xs:anyURI` as enforce by the schema but SHOULD be a URL.
  See [#15](https://github.com/oasis-tcs/csaf/issues/15)
