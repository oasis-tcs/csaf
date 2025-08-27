## Extensions

This standard allows for extensions to the standardized schema.

The following rules apply:

* An extension MUST NOT occur in any other place than specified.
* An extension MUST satisfy the Conformance Target CSAF Extension.

### Classes

There three classes of extensions:

1. Official extensions: These CSAF Extensions are specified by the OASIS CSAF TC and ensure interoperability.

   > Those extensions are used to backport upcoming features or integrate new features at the OASIS CSAF TC's discretion.

2. Registered extensions: These CSAF Extensions are specified by a named party, publicly available, well-documented and
   registered with the OASIS CSAF TC.
   Collisions are avoided through being listed in the register.

   > Those extension can be used for conveying additional information to a broader community and making it available for tool
   > integration.
   > The OASIS CSAF TC may or may not consider to replace such extension with a registered one or take it as input for a future
   > version of CSAF.

3. Experimental extensions: These CSAF Extension can be used for tests and experiments.
   They SHOULD NOT be used in production.

### Lists

The OASIS CSAF TC maintains:

* a list of official CSAF Extensions,
* a list of registered CSAF Extensions,
* a list of deprecated extensions, and
* a list of deny-listed extensions.

Deprecated extensions can still be used but support for them is removed in near future. If avoidable, they SHOULD NOT be used.
Deny-listed extensions MUST NOT be used.
The lists of deprecated extensions and deny-listed extensions MAY contain extensions that do not fulfill the conformance target CSAF Extension.

### Content Schema

An extension MUST contain exactly the following elements:
CSAF Extension Schema (`$schema`), Extension Category (`category`), Critical (`critical`) and Content (`content`)

```
  properties: {
    "$schema": {
      // ...
    },
    "category": {
      // ...
    },
    "critical": {
      // ...
    },
    "content": {
      // ...
    }
  }
```

CSAF Extension Schema (`$schema`) has value type `string` with format `uri` and `pattern` (regular expression):

```
  ^(?!https:\\/\\/docs\\.oasis-open\\.org\\/csaf\\/csaf\\/v2.1\\/([^\\/\\s]+\/)*schema\\/extension-content\\.json)(https:\\/\\/[a-z0-9](([a-z0-9-]){0,61}[a-z0-9])?(\\.[a-z0-9](([a-z0-9-]){0,61}[a-z0-9])?)+\\/([^\\/\\s]+\/)*[^\\/\\s]+_(0|[1-9]\\d*)\\.(0|[1-9]\\d*)\\.(0|[1-9]\\d*)(?:-((?:0|[1-9]\\d*|\\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\\.(?:0|[1-9]\\d*|\\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\\+([0-9a-zA-Z-]+(?:\\.[0-9a-zA-Z-]+)*))?\\.json)$
```

It contains the URL of the CSAF Extension JSON schema which the JSON object promises to be valid for.
This SHOULD also be the location where the JSON schema can be retrieved.
The value SHOULD match the `$id` of the JSON schema that defines the extension.
The URL SHOULD contain a human-readable name for the extension before the version string.
The versioning MUST use SemVer.

Extension Category (`category`) of value type `string` and `enum` holds the category of the extension content.
Valid `enum` values are:

```
  critical
  high_value
  informational
```

The value `critical` indicates, that the content provided through this extension is crucial to understand of the CSAF document this extension is included in.
CSAF consumer MUST warn if they process a CSAF Document including such extension instance and do not have the extension in question already implement.

The value `high_value` indicates, that the content provided through this extension is highly relevant and significantly aids in understanding the
overall content of the CSAF document.

The value `informational` indicates, that the content provided through this extension just provides additional information.
CSAF consumer SHOULD warn if they process a CSAF Document including such sn extension instance and do not have the extension in
question already implemented.

Critical (`critical`) of value type `boolean` determines whether using the extension would fail a mandatory test.

Content (`content`) of value type `object` determines whether using the extension would fail a mandatory test."

The `default` value for this is `false`.

