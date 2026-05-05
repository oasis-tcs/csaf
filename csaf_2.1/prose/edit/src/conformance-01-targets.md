## Conformance Targets

This document defines requirements for the file format and for certain software components that interact with it.
The entities ("conformance targets") for which this document defines requirements are:

* **CSAF Document**: A security advisory text document in the format defined by this document.
* **CSAF Producer**: A program which emits output in the CSAF format.
* **CSAF Direct Producer**: An analysis tool which acts as a CSAF Producer.
* **CSAF Converter**: A CSAF Producer that transforms the output of an analysis tool from its native output format into the CSAF format.
* **CVRF CSAF Converter**: A CSAF Producer which takes a CVRF document as input and converts it into a valid CSAF Document.
* **CSAF Content Management System**: A program that is able to create,
  review and manage CSAF Documents and is able to preview their details as required by CSAF Viewer.
* **CSAF Post-Processor**: A CSAF Producer that transforms an existing CSAF Document into a new CSAF Document,
  for example, by removing or redacting elements according to sharing policies.
* **CSAF Modifier**: A CSAF Post-Processor which takes a CSAF Document as input and modifies the structure or values of properties.
  The output is a valid CSAF Document.
* **CSAF Translator**: A CSAF Post-Processor which takes a CSAF Document as input and translates values of properties into another language.
  The output is a valid CSAF Document.
* **CSAF Consumer**: A program that reads and interprets a CSAF Document.
* **CSAF Viewer**: A CSAF Consumer that reads a CSAF Document, displays a list of the results it contains,
  and allows an end user to view each result in the context of the artifact in which it occurs.
* **CSAF Management System**: A program that is able to manage CSAF Documents and is able to display their details as required by CSAF Viewer.
* **CSAF Asset Matching System**: A program that connects to or is an asset database and is able to manage CSAF Documents as required
  by CSAF Management System as well as matching them to assets of the asset database.
* **CSAF Basic Validator**: A program that reads a document and checks it against the JSON schema and performs mandatory tests.
* **CSAF Extended Validator**: A CSAF Basic Validator that additionally performs recommended tests.
* **CSAF Full Validator**: A CSAF Extended Validator that additionally performs informative tests.
* **CSAF SBOM Matching System**: A program that connects to or is an SBOM database and is able to manage CSAF Documents as required
  by CSAF Management System as well as matching them to SBOM components of the SBOM database.
* **CSAF 2.0 to CSAF 2.1 Converter**: A CSAF Producer which takes a CSAF 2.0 Document as input and converts it into a valid CSAF 2.1 Document.
* **CSAF Library**: A library that implements CSAF data capabilities.
* **CSAF Library with Basic Validation**: A CSAF Library that also satisfies the conformance target "CSAF Basic Validator".
* **CSAF Library with Extended Validation**: A CSAF Library that also satisfies the conformance target "CSAF Extended Validator".
* **CSAF Library with Full Validation**: A CSAF Library that also satisfies the conformance target "CSAF Full Validator".
* **CSAF Downloader**: A program that retrieves CSAF Documents in an automated fashion.
* **CSAF Withdrawer**: A CSAF Post-Processor that transforms a given CSAF into a Withdrawn one.
* **CSAF Superseder**: A CSAF Post-Processor that transforms a given CSAF into a Superseded one.
* **CSAF RVISC ID Updater**: A CSAF Post-Processor that updates vulnerability IDs in a given CSAF based on the entries in [cite](#RVISC).
* **CSAF Additional Test**: A test that is not yet defined in section [sec](#tests).
* **CSAF Extension**: A specified JSON object conveying additional information different from the content that can be conveyed with the
  CSAF Core elements.
* **CSAF Extension Schema**: A JSON schema specifying the content and properties of a CSAF Extension.
* **CSAF Extension Overlay Test**: A test whose execution depends on the presence of the specifying CSAF Extension that extends or replaces a
  test standardized in this specification or a CSAF Additional Test.
* **CSAF Extension Additional Test**: A test whose execution depends on the presence of the specifying CSAF Extension that provides additional
  checks in the context of the CSAF Extension or the CSAF Document the extension is embedded in.
* **CSAF Extension Test**: A test that is either a CSAF Extension Overlay Test or a CSAF Extension Additional Test.
* **CSAF Extension Specification**: The specification of a single CSAF Extension and related material.
* **CSAF Extension Bundle**: A of compilation of machine-readable artifacts related to a single CSAF Extension.
* **CSAF Extension Package**: A of compilation of all artifacts related to a single CSAF Extension.
* **CSAF Extension Collection**: A set of multiple CSAF Extension Package.
