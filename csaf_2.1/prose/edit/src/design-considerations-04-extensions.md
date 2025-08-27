## Extensions

This standard allows for extensions to the standardized schema.

The following rules apply:

* An extension MUST NOT occur in any other place than specified.
* TODO: add content

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

-------
