advisory
:    reporting item that describes a condition present in an artifact and that requires action by the consumers

advisory document
:    artifact in which an analysis tool reports a result

advisory management system
:    software system that consumes the documents produced by analysis tools,
produces advisories that enable engineering and operating organizations to assess the quality of these
software artifacts at a point in time, and performs functions such as filing security advisories and
displaying information about individual advisories.
**Note**: An advisory management system can interact with a document viewer to display information about individual advisories.

advisory matching
:    process of determining whether two advisories are targeting the same products and conditions

artifact
:    sequence of bytes addressable via a URI.
_Examples_: A physical file in a file system such as a source file, an object file, a configuration file or a data file;
a specific version of a file in a version control system; a database table accessed via an HTTP request;
an arbitrary stream of bytes returned from an HTTP request, a product URL, a common product enumeration value.

CSAF asset matching system
:    program that connects to or is an asset database and is able to manage CSAF documents as
required by CSAF management system
as well as matching them to assets of the asset database.

CSAF basic validator
:    A program that reads a document and checks it against the JSON schema and performs mandatory tests.

CSAF consumer
:    program that reads and interprets a CSAF document

CSAF content management system
:    program that is able to create, review and manage CSAF documents and is able to preview their details as
required by CSAF viewer.

CSAF converter
:    CSAF producer that transforms the output of an analysis tool from its native output format into the CSAF format

CSAF direct producer
:    analysis tool which acts as a CSAF producer

CSAF document
:    security advisory text document in the format defined by this document.

CSAF extended validator
:    A CSAF basic validator that additionally performs optional tests.

CSAF full validator
:    A CSAF extended validator that additionally performs informative tests.

CSAF management system
:    program that is able to manage CSAF documents and is able to display their details as required by CSAF viewer.

CSAF modifier
:    CSAF post-processor which takes a CSAF document as input and modifies the structure or values of properties.
The output is a valid CSAF document.

CSAF post-processor
:    CSAF producer that transforms an existing CSAF document into a new CSAF document,
for example, by removing or redacting elements according to sharing policies.

CSAF SBOM matching system
:    A program that connects to or is an SBOM database and is able to manage CSAF documents as
required by CSAF management system as well as matching them to SBOM components of the SBOM database.

CSAF producer
:    program that emits output in the CSAF format

CSAF translator
:    CSAF post-processor which takes a CSAF document as input and translates values of properties into another language.
The output is a valid CSAF document.

CSAF viewer
:    CSAF consumer that reads a CSAF document, displays a list of the results it contains,
and allows an end user to view each result in the context of the artifact in which it occurs.

CVRF CSAF converter
:    CSAF producer which takes a CVRF document as input and converts it into a valid CSAF document.

document
:    output file produced by an analysis tool, which enumerates the results produced by the tool

driver
:    tool component containing an analysis tool’s or converter’s primary executable,
which controls the tool’s or converter’s execution,
and which in the case of an analysis tool typically defines a set of analysis rules

embedded link
:    syntactic construct which enables a message string to refer to a location mentioned in the document

empty array
:    array that contains no elements, and so has a length of 0

empty object
:    object that contains no properties

empty string
:    string that contains no characters, and so has a length of 0

(end) user
:    person who uses the information in a document to investigate, triage, or resolve results

engineering system
:    software analysis environment within which analysis tools execute.
**Note**: An engineering system might include a build system, a source control system, a result management system,
a bug tracking system, a test execution system, and so on.

extension
:    tool component other than the driver (for example, a plugin, a configuration file, or a taxonomy)

external property file
:    file containing the values of one or more externalized properties

externalizable property
:    property that can be contained in an external property file

externalized property
:    property stored outside of the CSAF document to which it logically belongs

false positive
:    result which an end user decides does not actually represent a problem

fingerprint
:    stable value that can be used by a result management system to uniquely identify a result over time,
even if a relevant artifact is modified

formatted message
:     message string which contains formatting information such as Markdown formatting characters

fully qualified logical name
:    string that fully identifies the programmatic construct specified by a logical location,
typically by means of a hierarchical identifier.

hierarchical string
:    string in the format &lt;component>{/&lt;component>}*

line
:    contiguous sequence of characters, starting either at the beginning of an artifact or immediately after
a newline sequence, and ending at and including the nearest subsequent newline sequence, if one is present,
or else extending to the end of the artifact

line (number)
:    1-based index of a line within a file.
**Note**: Abbreviated to "line" when there is no danger of ambiguity with "line" in the sense of a sequence of characters.

localizable
:    subject to being translated from one natural language to another

message string
:    human-readable string that conveys information relevant to an element in a CSAF document

nested artifact
:    artifact that is contained within another artifact

newline sequence
:    sequence of one or more characters representing the end of a line of text.
**Note**: Some systems represent a newline sequence with a single newline character; others represent it as
a carriage return character followed by a newline character.

notification
:    reporting item that describes a condition encountered by a tool during its execution

opaque
:    neither human-readable nor machine-parsable into constituent parts

parent (artifact)
:    artifact which contains one or more nested artifacts

plain text message
:    message string which does not contain any formatting information

plugin
:    tool component that defines additional rules

policy
:    set of rule configurations that specify how results that
violate the rules defined by a particular tool component are to be treated

problem
:    result which indicates a condition that has the potential to detract from the quality of the program.
_Examples_: A security vulnerability, a deviation from contractual or legal requirements.

product
:    is any deliverable (e.g. software, hardware, specification,...) which can be referred to with a name.
This applies regardless of the origin, the license model, or the mode of distribution of the deliverable.

property
:    attribute of an object consisting of a name and a value associated with the name

redactable property
:    property that potentially contains sensitive information that a CSAF direct producer or
a CSAF post-processor might wish to redact

reporting item
:    unit of output produced by a tool, either a result or a notification

reporting configuration
:    the subset of reporting metadata that a tool can configure at runtime, before performing its scan.
_Examples_: severity level, rank

repository
:    container for a related set of files in a version control system

taxonomy
:    classification of analysis results into a set of categories

tag
:    string that conveys additional information about the CSAF document element to which it applies

text artifact
:    artifact considered as a sequence of characters organized into lines and columns

text region
:    region representing a contiguous range of zero or more characters in a text artifact

tool component
:    component of an analysis tool or converter, either its driver or an extension, consisting of one or more files

top-level artifact
:     artifact which is not contained within any other artifact

translation
:    rendering of a tool component's localizable strings into another language

triage
:    decide whether a result indicates a problem that needs to be corrected

user
:    see end user.

VCS
:    version control system

vendor
:    the community, individual, or organization that created or maintains a product
(including open source software and hardware providers)

VEX
:    Vulnerability Exploitability eXchange - enables a supplier or other party to assert whether or not
a particular product is affected by a specific vulnerability, especially helpful in efficiently consuming SBOM data.

viewer
:     see CSAF viewer.

vulnerability
:    functional behavior of a product or service that violates an implicit or explicit security policy
(conforming to ISO/IEC 29147 [cite](#ISO29147))

XML
:    eXtensible Markup Language - the format used by the predecessors of this standard, namely CVRF 1.1 and CVRF 1.2.
