## Extensions

This standard allows for extensions to the standardized schema.

The following rules apply:

* An extension MUST NOT occur in any other place than specified.
* An extension MUST satisfy the Conformance Target "CSAF Extension".
* The schema specifying the content and properties of the CSAF Extension MUST satisfy the Conformance Target "CSAF Extension Schema".
* For official and registered extensions a CSAF Extension Package MUST be provided.

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

* a list of official CSAF Extensions and their CSAF Extension Packages,
* a list of registered CSAF Extensions and their CSAF Extension Packages,
* a list of deprecated extensions, and
* a list of deny-listed extensions.

Deprecated extensions can still be used but support for them is removed in near future. If avoidable, they SHOULD NOT be used.
Deny-listed extensions MUST NOT be used.
The lists of deprecated extensions and deny-listed extensions MAY contain extensions that do not fulfill the conformance target CSAF Extension.

The list MAY contain additional examples.

###

### Content Schema

An extension MUST contain exactly the following elements:
CSAF Extension Schema (`$schema`), Extension Category (`category`), Critical (`critical`) and Content (`content`).

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

#### Content Schema Property - Schema

CSAF Extension Schema (`$schema`) of value type CSAF Extension Content $schema Type (`content_schema_t`) contains the URL of the CSAF Extension JSON schema which the JSON object promises to be valid for.
This SHOULD also be the location where the JSON schema can be retrieved.
The value SHOULD match the `$id` of the JSON schema that defines the extension.
The URL SHOULD contain a human-readable name for the extension before the version string.
The versioning MUST use [cite](#SemVer).
URLs using a domain mentioned in [cite](#RFC2606) MUST be used according to their defined purpose.

*Examples 1:*

```
  https://www.example.com/some-path/to-a-csaf-extension/schema/manufacturer-headquarters_1.0.0.json
  https://oil-and-gas.isac.example/.well-known/csaf/extensions/schema/product-safety_17.41.0.json
```

#### Content Schema Property - Category

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
CSAF consumer SHOULD warn if they process a CSAF Document including such an extension instance and do not have the extension in
question already implemented.

#### Content Schema Property - Critical

Critical (`critical`) of value type `boolean` determines whether using the extension would fail a mandatory test.
The `default` value for this is `false`.

For any failing test, a CSAF Extension Test MUST be provided.

#### Content Schema Property - Content

Content (`content`) of value type `object` contains the additional information in its properties.
A Content object has at least `1` property.
The property names (JSON keys) can be chosen freely; they SHOULD characterize the information given in its value.
