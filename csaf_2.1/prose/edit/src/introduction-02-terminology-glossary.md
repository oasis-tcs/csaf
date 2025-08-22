Advisory
:    reporting item that describes a condition present in an artifact and that requires action by the consumers.

Advisory Document
:    artifact in which an analysis tool reports a result.

Advisory Management System
:    software system that consumes the documents produced by analysis tools,
produces advisories that enable engineering and operating organizations to assess the quality of these
software artifacts at a point in time, and performs functions such as filing security advisories and
displaying information about individual advisories.
**Note**: An Advisory Management System can interact with a document viewer to display information about individual advisories.

Advisory Matching
:    process of determining whether two advisories are targeting the same products and conditions

Artifact
:    sequence of bytes addressable via a URI.
_Examples_: A physical file in a file system such as a source file, an object file, a configuration file or a data file;
a specific version of a file in a version control system; a database table accessed via an HTTP request;
an arbitrary stream of bytes returned from an HTTP request, a product URL, a common product enumeration value.

CSAF 2.0 to CSAF 2.1 Converter
:    A CSAF Producer which takes a CSAF 2.0 Document as input and converts it into a valid CSAF 2.1 Document.

CSAF Asset Matching System
:    program that connects to or is an asset database and is able to manage CSAF Documents as
required by CSAF Management System
as well as matching them to assets of the asset database.

CSAF Basic Validator
:    A program that reads a document and checks it against the JSON schema and performs mandatory tests.

CSAF Consumer
:    program that reads and interprets a CSAF Document.

CSAF Content Management System
:    program that is able to create, review and manage CSAF Documents and is able to preview their details as
required by CSAF Viewer.

CSAF Converter
:    CSAF Producer that transforms the output of an analysis tool from its native output format into the CSAF format.

CSAF Direct Producer
:    analysis tool which acts as a CSAF Producer.

CSAF Document
:    security advisory text document in the format defined by this document.

CSAF Downloader
:    A program that retrieves CSAF Documents in an automated fashion.

CSAF Extended Validator
:    A CSAF Basic Validator that additionally performs recommended tests.

CSAF Full Validator
:    A CSAF Extended Validator that additionally performs informative tests.

CSAF Library
:    A library that implements CSAF data capabilities.

CSAF Library with Basic Validation
:    A CSAF Library that also satisfies the conformance target "CSAF Basic Validator".

CSAF Library with Extended Validation
:    A CSAF Library that also satisfies the conformance target "CSAF Extended Validator".

CSAF Library with Full Validation
:    A CSAF Library that also satisfies the conformance target "CSAF Full Validator".

CSAF Management System
:    program that is able to manage CSAF Documents and is able to display their details as required by CSAF Viewer.

CSAF Modifier
:    CSAF Post-Processor which takes a CSAF Document as input and modifies the structure or values of properties.
The output is a valid CSAF Document.

CSAF Post-Processor
:    CSAF Producer that transforms an existing CSAF Document into a new CSAF Document,
for example, by removing or redacting elements according to sharing policies.

CSAF SBOM Matching System
:    A program that connects to or is an SBOM database and is able to manage CSAF Documents as
required by CSAF Management System as well as matching them to SBOM components of the SBOM database.

CSAF Producer
:    program that emits output in the CSAF format

CSAF Superseder
:    A CSAF Post-Processor that transforms a given CSAF into a superseded one.

CSAF Translator
:    CSAF Post-Processor which takes a CSAF Document as input and translates values of properties into another language.
The output is a valid CSAF Document.

CSAF Viewer
:    CSAF Consumer that reads a CSAF Document, displays a list of the results it contains,
and allows an end user to view each result in the context of the artifact in which it occurs.

CSAF Withdrawer
:    A CSAF Post-Processor that transforms a given CSAF into a withdrawn one.

CVRF CSAF Converter
:    CSAF Producer which takes a CVRF document as input and converts it into a valid CSAF Document.

Document
:    output file produced by an analysis tool, which enumerates the results produced by the tool.

Driver
:    tool component containing an analysis tool’s or converter’s primary executable,
which controls the tool’s or converter’s execution,
and which in the case of an analysis tool typically defines a set of analysis rules.

Embedded Link
:    syntactic construct which enables a message string to refer to a location mentioned in the document.

Empty Array
:    array that contains no elements, and so has a length of 0.

Empty Object
:    object that contains no properties.

Empty String
:    string that contains no characters, and so has a length of 0.

(End) User
:    person who uses the information in a document to investigate, triage, or resolve results.

Engineering System
:    software analysis environment within which analysis tools execute.
**Note**: An engineering system might include a build system, a source control system, a result management system,
a bug tracking system, a test execution system, and so on.

Extension
:    tool component other than the driver (for example, a plugin, a configuration file, or a taxonomy).

External Property File
:    file containing the values of one or more externalized properties.

Externalizable Property
:    property that can be contained in an external property file.

Externalized Property
:    property stored outside of the CSAF Document to which it logically belongs.

False Positive
:    result which an end user decides does not actually represent a problem.

Filter
:    refine a list by selecting entries that match given criteria.

Fingerprint
:    stable value that can be used by a result management system to uniquely identify a result over time,
even if a relevant artifact is modified.

Formatted Message
:     message string which contains formatting information such as Markdown formatting characters.

Fully Qualified Logical Name
:    string that fully identifies the programmatic construct specified by a logical location,
typically by means of a hierarchical identifier.

Hierarchical String
:    string in the format &lt;component>{/&lt;component>}*.

Line
:    contiguous sequence of characters, starting either at the beginning of an artifact or immediately after
a newline sequence, and ending at and including the nearest subsequent newline sequence, if one is present,
or else extending to the end of the artifact.

Line (Number)
:    1-based index of a line within a file.
**Note**: Abbreviated to "line" when there is no danger of ambiguity with "line" in the sense of a sequence of characters.

Localizable
:    subject to being translated from one natural language to another.

Message String
:    human-readable string that conveys information relevant to an element in a CSAF Document.

Nested Artifact
:    artifact that is contained within another artifact.

Newline Sequence
:    sequence of one or more characters representing the end of a line of text.
**Note**: Some systems represent a newline sequence with a single newline character; others represent it as
a carriage return character followed by a newline character.

Notification
:    reporting item that describes a condition encountered by a tool during its execution.

Opaque
:    neither human-readable nor machine-parsable into constituent parts.

Parent (Artifact)
:    artifact which contains one or more nested artifacts.

Plain Text Message
:    message string which does not contain any formatting information.

Plugin
:    tool component that defines additional rules.

Policy
:    set of rule configurations that specify how results that
violate the rules defined by a particular tool component are to be treated.

Problem
:    result which indicates a condition that has the potential to detract from the quality of the program.
_Examples_: A security vulnerability, a deviation from contractual or legal requirements.

Product
:    is any deliverable (e.g. software, hardware, specification, or service) which can be referred to with a name.
This applies regardless of the origin, the license model, or the mode of distribution of the deliverable.

Property
:    attribute of an object consisting of a name and a value associated with the name.

Redactable Property
:    property that potentially contains sensitive information that a CSAF Direct Producer or
a CSAF Post-Processor might wish to redact.

Reporting Item
:    unit of output produced by a tool, either a result or a notification.

Reporting Configuration
:    the subset of reporting metadata that a tool can configure at runtime, before performing its scan.
_Examples_: severity level, rank

Repository
:    container for a related set of files in a version control system.

Search
:    compile a list of entries that match given criteria.

Taxonomy
:    classification of analysis results into a set of categories.

Tag
:    string that conveys additional information about the CSAF Document element to which it applies.

Text Artifact
:    artifact considered as a sequence of characters organized into lines and columns.

Text Region
:    region representing a contiguous range of zero or more characters in a text artifact.

Tool Component
:    component of an analysis tool or converter, either its driver or an extension, consisting of one or more files.

Top-Level Artifact
:     artifact which is not contained within any other artifact.

Translation
:    rendering of a tool component's localizable strings into another language.

Triage
:    decide whether a result indicates a problem that needs to be corrected.

User
:    see end user.

VCS
:    version control system.

Vendor
:    the community, individual, or organization that created or maintains a product
(including open source software and hardware providers).

VEX
:    Vulnerability Exploitability eXchange - enables a supplier or other party to assert whether or not
a particular product is affected by a specific vulnerability, especially helpful in efficiently consuming SBOM data.

Viewer
:     see CSAF Viewer.

Vulnerability
:    functional behavior of a product or service that violates an implicit or explicit security policy
(conforming to ISO/IEC 29147 [[ISO29147](#ISO29147)]).

White Space
:    code point used to improve text readability or token separation as defined in section 12.2 of [cite](#ECMA-262).

XML
:    eXtensible Markup Language - the format used by the predecessors of this standard, namely CVRF 1.1 and CVRF 1.2.
