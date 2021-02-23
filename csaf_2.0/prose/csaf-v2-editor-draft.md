
![OASIS Logo](http://docs.oasis-open.org/templates/OASISLogo-v2.0.jpg)
-------


# Common Security Advisory Framework Version 2.0


## Committee Specification Draft 01 /<br>Public Review Draft 01

## 24 November 2020

#### Technical Committee:
[OASIS Common Security Advisory Framework (CSAF) TC](https://www.oasis-open.org/committees/csaf/)

#### Chair:
Omar Santos (osantos@cisco.com), [Cisco](https://cisco.com/)

#### Editors:
Langley Rock (lrock@redhat.com), [Red Hat](https://redhat.com/) \
Stefan Hagen (stefan@hagen.link), [Individual](https://stefan-hagen.website/)

In Memory of Eric Johnson, TIBCO Software inc., an active member of the OASIS CSAF Committee.

#### Additional artifacts:
This prose specification is one component of a Work Product that also includes:
* JSON schema: csaf.json
* Other parts (list titles and/or file names)
* `(Note: Any normative computer language definitions that are part of the Work Product, such as XML instances, schemas and Java(TM) code, including fragments of such, must be (a) well formed and valid, (b) provided in separate plain text files, (c) referenced from the Work Product; and (d) where any definition in these separate files disagrees with the definition found in the specification, the definition in the separate file prevails. Remove this note before submitting for publication.)`

#### Related work:
This specification replaces or supersedes:
* The CSAF Common Vulnerability Reporting Framework (CVRF) Version 1.2. http://docs.oasis-open.org/csaf/csaf-cvrf/v1.2/csprd01/csaf-cvrf-v1.2-csprd01.html

This specification is related to:
* Related specifications (include hyperlink, preferably to HTML format) \
`(remove "Related work" section or the "replaces" or "related" subsections if no entries)`

#### Abstract:
The Common Security Advisory Framework (CSAF) Version 2.0 is the definitive reference for the language which supports creation, update, and interoperable exchange of security advisories as structured information on products, vulnerabilities and the status of impact and remediation among interested parties.

#### Status:
This document was last revised or approved by the OASIS Common Security Advisory Framework (CSAF) TC on the above date. The level of approval is also listed above. Check the "Latest version" location noted above for possible later revisions of this document. Any other numbered Versions and other technical work produced by the Technical Committee (TC) are listed at https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=openc2#technical.

TC members should send comments on this specification to the TC's email list. Others should send comments to the TC's public comment list, after subscribing to it by following the instructions at the "Send A Comment" button on the TC's web page at https://www.oasis-open.org/committees/openc2/.

This specification is provided under the [Non-Assertion](https://www.oasis-open.org/policies-guidelines/ipr#Non-Assertion-Mode) Mode of the OASIS IPR Policy, the mode chosen when the Technical Committee was established. For information on whether any patents have been disclosed that may be essential to implementing this specification, and any offers of patent licensing terms, please refer to the Intellectual Property Rights section of the TC's web page (https://www.oasis-open.org/committees/openc2/ipr.php).

Note that any machine-readable content ([Computer Language Definitions](https://www.oasis-open.org/policies-guidelines/tc-process#wpComponentsCompLang)) declared Normative for this Work Product is provided in separate plain text files. In the event of a discrepancy between any such plain text file and display content in the Work Product's prose narrative document(s), the content in the separate plain text file prevails.

#### URI patterns:
Initial publication URI:  
https://docs.oasis-open.org/tc-name/wp-abbrev-xxxxx/v1.0/csd01/wp-abbrev-xxxxx-v1.0-csd01.html

Permanent "Latest version" URI:  
https://docs.oasis-open.org/tc-name/wp-abbrev-xxxxx/v1.0/wp-abbrev-xxxxx-v1.0.html

(Note: Publication URIs are managed by OASIS TC Administration; please don't modify.)

#### Citation format:
When referencing this specification the following citation format should be used:

**[csaf-v2.0]**

_Common Security Advisory Framework Version 2.0_. Edited by Langley Rock and Stefan Hagen. 00 Month 2020. OASIS Committee Specification Draft 01 / Public Review Draft 01. this-version.html. Latest version: latest-version.html.


-------

## Notices
Copyright © OASIS Open 2020. All Rights Reserved.

All capitalized terms in the following text have the meanings assigned to them in the OASIS Intellectual Property Rights Policy (the "OASIS IPR Policy"). The full [Policy](https://www.oasis-open.org/policies-guidelines/ipr) may be found at the OASIS website.

This document and translations of it may be copied and furnished to others, and derivative works that comment on or otherwise explain it or assist in its implementation may be prepared, copied, published, and distributed, in whole or in part, without restriction of any kind, provided that the above copyright notice and this section are included on all such copies and derivative works. However, this document itself may not be modified in any way, including by removing the copyright notice or references to OASIS, except as needed for the purpose of developing any document or deliverable produced by an OASIS Technical Committee (in which case the rules applicable to copyrights, as set forth in the OASIS IPR Policy, must be followed) or as required to translate it into languages other than English.

The limited permissions granted above are perpetual and will not be revoked by OASIS or its successors or assigns.

This document and the information contained herein is provided on an "AS IS" basis and OASIS DISCLAIMS ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO ANY WARRANTY THAT THE USE OF THE INFORMATION HEREIN WILL NOT INFRINGE ANY OWNERSHIP RIGHTS OR ANY IMPLIED WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.

As stated in the OASIS IPR Policy, the following three paragraphs in brackets apply to OASIS Standards Final Deliverable documents (Committee Specification, Candidate OASIS Standard, OASIS Standard, or Approved Errata).

\[OASIS requests that any OASIS Party or any other party that believes it has patent claims that would necessarily be infringed by implementations of this OASIS Standards Final Deliverable, to notify OASIS TC Administrator and provide an indication of its willingness to grant patent licenses to such patent claims in a manner consistent with the IPR Mode of the OASIS Technical Committee that produced this deliverable.\]

\[OASIS invites any party to contact the OASIS TC Administrator if it is aware of a claim of ownership of any patent claims that would necessarily be infringed by implementations of this OASIS Standards Final Deliverable by a patent holder that is not willing to provide a license to such patent claims in a manner consistent with the IPR Mode of the OASIS Technical Committee that produced this OASIS Standards Final Deliverable. OASIS may include such claims on its website, but disclaims any obligation to do so.\]

\[OASIS takes no position regarding the validity or scope of any intellectual property or other rights that might be claimed to pertain to the implementation or use of the technology described in this OASIS Standards Final Deliverable or the extent to which any license under such rights might or might not be available; neither does it represent that it has made any effort to identify any such rights. Information on OASIS' procedures with respect to rights in any document or deliverable produced by an OASIS Technical Committee can be found on the OASIS website. Copies of claims of rights made available for publication and any assurances of licenses to be made available, or the result of an attempt made to obtain a general license or permission for the use of such proprietary rights by implementers or users of this OASIS Standards Final Deliverable, can be obtained from the OASIS TC Administrator. OASIS makes no representation that any information or list of intellectual property rights will at any time be complete, or that any claims in such list are, in fact, Essential Claims.\]

The name "OASIS" is a trademark of [OASIS](https://www.oasis-open.org/), the owner and developer of this specification, and should be used only to refer to the organization and its official outputs. OASIS welcomes reference to, and implementation and use of, specifications, while reserving the right to enforce its marks against misleading uses. Please see https://www.oasis-open.org/policies-guidelines/trademark for above guidance.

-------

# Table of Contents
[[TOC will be inserted here]]

-------

# 1 Introduction

The text in this section may all be replaced, but the following three sections (1.1, 1.2, and 1.3) are required for OASIS publications. Section 1.1 (IPR Policy) must not be changed by the TC. Section 1.2 (Terminology) may be modified to include other terminology-related information used in this specification. Section 1.3 (Normative References) should be modified to include additional references, as needed. Section 1.4 (Non-Normative References) is not required, but should be modified to include additional references, as needed.

Here is a customized command line which will generate HTML from this markdown file (named prose/csaf-v2-editor-draft.md):

    $ pandoc -f gfm -t html prose/csaf-v2-editor-draft.md -c static/styles/markdown-styles-v1.7.3-patched.css \
    --toc --toc-depth=4 -s -o csaf.html --metadata title="Common Security Advisory Framework Version 2.0"


OASIS staff are currently using pandoc 2.6 from https://github.com/jgm/pandoc/releases/tag/2.6.

This also requires the presence of a .css file containing the HTML styles (like styles/markdown-styles-v1.7.3-patched.css).

Fixes in the css (shall) address:
* blockquotes shall maintain constant indentation
* code blocks shall expose block rectangle (not per line width right margin) - still unpatched
* Logo and title page shall not be within the table of content (manually removal required currently - maybe addressable by processor options or markup changes)

Note this command generates a Table of Contents (TOC) in HTML which is located at the top of the HTML document, and which requires additional editing in order to be published in the expected OASIS style. This editing will be handled by OASIS staff during publication.
A TC may use other ways to generate HTML from markdown, which may generate a TOC in a different way.

## 1.1 IPR Policy
This specification is provided under the [Non-Assertion](https://www.oasis-open.org/policies-guidelines/ipr#Non-Assertion-Mode) Mode of the [OASIS IPR Policy](https://www.oasis-open.org/policies-guidelines/ipr), the mode chosen when the Technical Committee was established. For information on whether any patents have been disclosed that may be essential to implementing this specification, and any offers of patent licensing terms, please refer to the Intellectual Property Rights section of the TC's web page ([https://www.oasis-open.org/committees/openc2/ipr.php](https://www.oasis-open.org/committees/openc2/ipr.php)).

## 1.2 Terminology
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 [[RFC2119](#rfc2119)] and [[RFC8174](#rfc8174)] when, and only when, they appear in all capitals, as shown here.

For purposes of this document, the following terms and definitions apply:

**advisory**: reporting item that describes a condition present in an artifact and that requires action by the consumers

**advisory document**: artifact in which an analysis tool reports a result

**advisory management system**: software system that consumes the documents produced by analysis tools, produces advisories that enable engineering ad operating organizations to assess the quality of these software artifacts at a point in time, and performs functions such as filing security advisories and displaying information about individual advisories.  **Note**: An advisory management system can interact with a document viewer to display information about individual advisories.

**advisory matching**: process of determining whether two advisories are targeting the same products and conditions

**artifact**: sequence of bytes addressable via a URI.  _Examples_: A physical file in a file system such as a source file, an object file, a configuration file or a data file; a specific version of a file in a version control system; a database table accessed via an HTTP request; an arbitrary stream of bytes returned from an HTTP request, a product URL, a common product enumeration value.

**converter**: CSAF producer that transforms the output of an analysis tool from its native output format into the CSAF format

**CSAF consumer**: program that reads and interprets a CSAF document

**CSAF document**: document in the format defined by this document

**CSAF post-processor**: CSAF producer that transforms an existing CSAF document into a new CSAF document, for example, by removing or redacting elements according to sharing policies.

**CSAF producer**: program that emits output in the CSAF format

**direct producer**: analysis tool which acts as a CSAF producer

**document**: output file produced by an analysis tool, which enumerates the results produced by the tool

**(document) viewer**: CSAF consumer that reads a document, displays a list of the results it contains, and allows an end user to view each result in the context of the artifact in which it occurs

**driver**: tool component containing an analysis tool’s or converter’s primary executable, which controls the tool’s or converter’s execution, and which in the case of an analysis tool typically defines a set of analysis rules

**embedded link**: syntactic construct which enables a message string to refer to a location mentioned in the document

**empty array**: array that contains no elements, and so has a length of 0

**empty object**: object that contains no properties

**empty string**: string that contains no characters, and so has a length of 0

**(end) user**: person who uses the information in a document to investigate, triage, or resolve results

**engineering system**: software analysis environment within which analysis tools execute.  **Note**: An engineering system might include a build system, a source control system, a result management system, a bug tracking system, a test execution system, and so on.

**extension**: tool component other than the driver (for example, a plugin, a configuration file, or a taxonomy)

**external property file**: file containing the values of one or more externalized properties

**externalizable property**: property that can be contained in an external property file

**externalized property**: property stored outside of the CSAF document to which it logically belongs

**false positive**: result which an end user decides does not actually represent a problem

**fingerprint**: stable value that can be used by a result management system to uniquely identify a result over time, even if a relevant artifact is modified

**formatted message**: message string which contains formatting information such as Markdown formatting characters

**fully qualified logical name**: string that fully identifies the programmatic construct specified by a logical location, typically by means of a hierarchical identifier.

**hierarchical string**: string in the format &lt;component>{/&lt;component>}*

**line**: contiguous sequence of characters, starting either at the beginning of an artifact or immediately after a newline sequence, and ending at and including the nearest subsequent newline sequence, if one is present, or else extending to the end of the artifact

**line (number)**: 1-based index of a line within a file.  **Note**: Abbreviated to "line" when there is no danger of ambiguity with "line" in the sense of a sequence of characters.

**localizable**: subject to being translated from one natural language to another

**message string**: human-readable string that conveys information relevant to an element in a CSAF document

**nested artifact**: artifact that is contained within another artifact

**newline sequence**: sequence of one or more characters representing the end of a line of text.  **Note**: Some systems represent a newline sequence with a single newline character; others represent it as a carriage return character followed by a newline character.

**notification**: reporting item that describes a condition encountered by a tool during its execution

**opaque**: neither human-readable nor machine-parsable into constituent parts

**parent (artifact)**: artifact which contains one or more nested artifacts

**plain text message**: message string which does not contain any formatting information

**plugin**: tool component that defines additional rules

**policy**: set of rule configurations that specify how results that violate the rules defined by a particular tool component are to be treated

**problem**: result which indicates a condition that has the potential to detract from the quality of the program.  _Examples_: A security vulnerability, a deviation from contractual or legal requirements.

**property**: attribute of an object consisting of a name and a value associated with the name

**redactable property**: property that potentially contains sensitive information that a CSAF direct producer or a CSAF post-processor might wish to redact

**reporting item**: unit of output produced by a tool, either a result or a notification

**reporting configuration**: the subset of reporting metadata that a tool can configure at runtime, before performing its scan.  _Examples_: severity level, rank

**repository** container for a related set of files in a version control system

**taxonomy**: classification of analysis results into a set of categories

**tag**: string that conveys additional information about the CSAF document element to which it applies

**text artifact**: artifact considered as a sequence of characters organized into lines and columns

**text region**: region representing a contiguous range of zero or more characters in a text artifact

**tool component**: component of an analysis tool or converter, either its driver or an extension, consisting of one or more files

**top-level artifact**: artifact which is not contained within any other artifact

**translation**: rendering of a tool component's localizable strings into another language

**triage**: decide whether a result indicates a problem that needs to be corrected

**user**: see end user.

**VCS**: version control system

**viewer**: see document viewer.

**web analysis tool**: analysis tool that models and analyzes the interaction between a web client and a server.


## 1.3 Normative References
###### [JSON-Schema-Core]
_JSON Schema: A Media Type for Describing JSON Documents_, draft-handrews-json-schema-02, September 2019, https://json-schema.org/draft/2019-09/json-schema-core.html.
###### [JSON-Schema-Validation]
_JSON Schema Validation: A Vocabulary for Structural Validation of JSON_, draft-handrews-json-schema-validation-02, September 2019, https://json-schema.org/draft/2019-09/json-schema-validation.html.
###### [JSON-Hyper-Schema]
_JSON Hyper-Schema: A Vocabulary for Hypermedia Annotation of JSON_, draft-handrews-json-schema-hyperschema-02, September 2019, https://json-schema.org/draft/2019-09/json-schema-hypermedia.html.
###### [Relative-JSON-Pointers]
_Relative JSON Pointers_, draft-handrews-relative-json-pointer-02, September 2019, https://json-schema.org/draft/2019-09/relative-json-pointer.html.
###### [RFC2119]
Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997. http://www.ietf.org/rfc/rfc2119.txt.
###### [RFC8174]
Leiba, B., "Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words", BCP 14, RFC 8174, DOI 10.17487/RFC8174, May 2017, http://www.rfc-editor.org/info/rfc8174.
###### [RFC8259]
T. Bray, Ed., "The JavaScript Object Notation (JSON) Data Interchange Format", RFC 8259, DOI 10.17487/RFC8259, December 2017, http://www.rfc-editor.org/info/rfc8259.

(Reference sources:
For references to IETF RFCs, use the approved citation formats at:  
http://docs.oasis-open.org/templates/ietf-rfc-list/ietf-rfc-list.html.  
For references to W3C Recommendations, use the approved citation formats at:  
http://docs.oasis-open.org/templates/w3c-recommendations-list/w3c-recommendations-list.html.  
Remove this note before submitting for publication.)

## 1.4 Non-Normative References

###### [CPE23-N]
_Common Platform Enumeration: Naming Specification Version 2.3_, B. Cheikes, D. Waltermire, K. Scarfone, Editors, NIST Interagency Report 7695, August 2011, http://dx.doi.org/10.6028/NIST.IR.7695.
###### [CPE23-M]
_Common Platform Enumeration: Naming Matching Specification Version 2.3_, M. Parmelee, H. Booth, D. Waltermire, K. Scarfone, Editors, NIST Interagency Report 7696, August 2011,http://dx.doi.org/10.6028/NIST.IR.7696.
###### [CPE23-D]
_Common Platform Enumeration: Dictionary Specification Version 2.3_, P. Cichonski, D. Waltermire, K. Scarfone, Editors, NIST Interagency Report 7697, August 2011, http://dx.doi.org/10.6028/NIST.IR.7697.
###### [CPE23-A]
_Common Platform Enumeration: Applicability Language Specification Version 2.3 (NISTIR 7698)_, D. Waltermire, P. Cichonski, K. Scarfone, Editors, NIST Interagency Report 7698, August 2011, http://dx.doi.org/10.6028/NIST.IR.7698.
###### [CVE]
_Common Vulnerability and Exposures (CVE) – The Standard for Information Security Vulnerability Names_, MITRE, 1999, https://cve.mitre.org/about/.
###### [CVE-NF]
_Common Vulnerability and Exposures (CVE) – The Standard for Information Security Vulnerability Names - CVE ID Syntax Change_, MITRE, January 01, 2014, https://cve.mitre.org/cve/identifiers/syntaxchange.html.
###### [CVRF-1-1]
_The Common Vulnerability Reporting Framework (CVRF) Version 1.1_, M. Schiffman, Editor, May 2012, Internet Consortium for Advancement of Security on the Internet (ICASI), 
http://www.icasi.org/the-common-vulnerability-reporting-framework-cvrf-v1-1/.
###### [CVRF-v1.2]
_CSAF Common Vulnerability Reporting Framework (CVRF) Version 1.2_. Edited by Stefan Hagen. 13 September 2017. OASIS Committee Specification 01. http://docs.oasis-open.org/csaf/csaf-cvrf/v1.2/cs01/csaf-cvrf-v1.2-cs01.html. Latest version: http://docs.oasis-open.org/csaf/csaf-cvrf/v1.2/csaf-cvrf-v1.2.html.
###### [CVSS2]
_A Complete Guide to the Common Vulnerability Scoring System Version 2.0_, P. Mell, K. Scarfone, S. Romanosky, Editors, First.org, Inc., June 2007, https://www.first.org/cvss/cvss-v2-guide.pdf.
###### [CVSS30]
_Common Vulnerability Scoring System v3.0: Specification Document_, FIRST.Org, Inc., June 2019, https://www.first.org/cvss/v3.0/cvss-v30-specification_v1.9.pdf.
###### [CVSS31]
_Common Vulnerability Scoring System v3.1: Specification Document_, FIRST.Org, Inc., June 2019, https://www.first.org/cvss/v3-1/cvss-v31-specification_r1.pdf.
###### [CWE]
_Common Weakness Enumeration (CWE) – A Community-Developed List of Software Weakness Types_, MITRE, 2005, http://cwe.mitre.org/about/.
###### [DCMI11]
_DCMI Metadata Terms v1.1_, Dublin Core Metadata Initiative, DCMI Rec., June 14, 2012, http://dublincore.org/documents/2012/06/14/dcmi-terms/.
Latest version available at http://dublincore.org/documents/dcmi-terms/.
###### [GFMCMARK]
_GitHub's fork of cmark, a CommonMark parsing and rendering library and program in C_, https://github.com/github/cmark.
###### [GFMENG]
_GitHub Engineering: A formal spec for GitHub Flavored Markdown_, https://githubengineering.com/a-formal-spec-for-github-markdown/.
###### [ISO8601]
_Data elements and interchange formats — Information interchange — Representation of dates and times_, International Standard, ISO 8601:2004(E), December 1, 2004, https://www.iso.org/standard/40874.html.
###### [ISO29147]
_Information technology — Security techniques — Vulnerability disclosure_, International Standard, ISO 29147:2014(E), February 15, 2014,
https://www.iso.org/standard/45170.html.
###### [RFC3552]
Rescorla, E. and B. Korver, "Guidelines for Writing RFC Text on Security Considerations", BCP 72, RFC 3552, DOI 10.17487/RFC3552, July 2003, https://www.rfc-editor.org/info/rfc3552.
###### [RFC7464]
N. Williams., "JavaScript Object Notation (JSON) Text Sequences", RFC 7464, DOI 10.17487/RFC7464, February 2015, http://www.rfc-editor.org/info/rfc7464.
###### [SCAP12]
_The Technical Specification for the Security Content Automation Protocol (SCAP): SCAP Version 1.2_, D. Waltermire, S. Quinn, K. Scarfone, A. Halbardier, Editors, NIST Spec. Publ. 800‑126 rev. 2, September 2011, 
http://dx.doi.org/10.6028/NIST.SP.800-126r2.
###### [XML]
_Extensible Markup Language (XML) 1.0 (Fifth Edition)_, T. Bray, J. Paoli, M. Sperberg-McQueen, E. Maler, F. Yergeau, Editors, W3C Recommendation, November 26, 2008, http://www.w3.org/TR/2008/REC-xml-20081126/. 
Latest version available at http://www.w3.org/TR/xml.
###### [XML-Schema-1]
_W3C XML Schema Definition Language (XSD) 1.1 Part 1: Structures_, S. Gao, M. Sperberg-McQueen, H. Thompson, N. Mendelsohn, D. Beech, M. Maloney, Editors, W3C Recommendation, April 5, 2012, 
http://www.w3.org/TR/2012/REC-xmlschema11-1-20120405/. 
Latest version available at http://www.w3.org/TR/xmlschema11-1/.
###### [XML-Schema-2]
_W3C XML Schema Definition Language (XSD) 1.1 Part 2_: Datatypes W3C XML Schema Definition Language (XSD) 1.1 Part 2: Datatypes, D. Peterson, S. Gao, A. Malhotra, M. Sperberg-McQueen, H. Thompson, Paul V. Biron, Editors, W3C Recommendation, April 5, 2012, 
http://www.w3.org/TR/2012/REC-xmlschema11-2-20120405/. 
Latest version available at http://www.w3.org/TR/xmlschema11-2/.

## 1.5 Typographical Conventions
Keywords defined by this specification use this `monospaced` font.
```
    Normative source code uses this paragraph style.
```
Text following the special symbol («) – an opening Guillemet (or French quotation mark) – within this specification identifies conformance statements. Every conformance statement is separated from the following text with the special end symbol (») – a closing Guillemet, and has been assigned a reference that follows that end symbol in the format [CSAF-section#-local#].

Some sections of this specification are illustrated with non-normative examples introduced with "Example" or "Examples" like so:

*Examples:*
```
    Non-normative examples also use this paragraph style but preceded by the text "Example(s).
```

All examples in this document are non-normative and informative only.

All other text is normative unless otherwise labeled e.g. like:

Non-normative Comment:

>This is a pure informative comment that may be present, because the information conveyed is deemed useful advice or common pitfalls learned from implementer or operator experience and often given including the rationale.

-------

# 2 Design Considerations
The Common Security Advisory Framework (CSAF) is a language to exchange Security Advisories formulated in JSON.

Non-normative comment:

>The term Security Advisory as used in this document describes any notification of security issues in products of and by providers. Anyone providing a product is considered in this document as a vendor, i.e. developers or maintainers of information system products or services. This includes all authoritative product vendors, Product Security Incident Response Teams (PSIRTs), and product resellers and distributors, including authoritative vendor partners.
A security issue is not necessarily constraint to a problem statement, the focus of the term is on the security aspect impacting (or not impacting) specific product-platform-version combinations. Information on presence or absence of work-arounds is also considered part of the security issue.
This document is the definitive reference for the language elements of CSAF version 2.0. The encompassing JSON schema file noted in the Additional Artifacts section of the title page shall be taken as normative in the case a gap or an inconsistency in this explanatory document becomes evident.
The following presentation in this section is grouped by topical area, and is not simply derivative documentation from the schema document itself. The information contained aims to be more descriptive and complete. Where applicable, common conventions are stated and known common issues in usage are pointed out informatively to support implementers of document producers and consumers alike. The section SCHEMA_SECTION_NUMBER Schema derives from the JSON schema itself as a service for the reader.

« From a high-level perspective, any Security Advisory purported by a CSAF version 2.0 adhering JSON text document MUST provide the `document` member with at least the following five properties defined: `csaf_version`, `title`, `publisher`, `type`, and `tracking`. » [CSAF-2-1]

This minimal required information set does not provide any useful information on products, vulnerabilities, or security advisories. Thus, any real-world Security Advisory will carry additional information as specified in SCHEMA_SECTION_NUMBER section Schema.

Care has been taken, to design the containers for product and vulnerability information to support fine-grained mapping of security advisories onto product and vulnerability and minimize data duplication through referencing.
The display of the elements representing Product Tree and Vulnerability information has been placed in the sections named accordingly.

As the JSON format is not primarily targeting human readers but more programs parsing, validating and transforming no example is given in this introduction but instead examples derived from several real-world security advisories are stated in the non-normative Appendix E Complete Examples.

## 2.1 Construction Principles
A Security Advisory defined as a CSAF document is the result of complex orchestration of many players and distinct and partially difficult to play schemas.

The format chosen is [JSONSchema] which allows validation and delegation to sub schema providers. The latter aligns well with separation of concerns and shares the format family of information interchange utilized by the providers of product and vulnerability information which migrated from XML to JSON since the creation of CSAF CVRF version 1.2, the predecessor of this specification.

The acronym CSAF, “Common Security Advisory Framework”, stands for the target of concerted mitigation and remediation accomplishment.

Technically the use of JSON schema allows validation and proof of model conformance (through established schema based validation) of the declared information inside CSAF documents.

The CSAF schema structures its derived documents into three main classes of the information conveyed:

1. The frame, aggregation, and reference information of the document
2. Product information considered relevant by the creator
3. Vulnerability information and its relation to the products declared in 2.

Wherever possible repetition of data has been replaced by linkage through ID elements. Consistency on the content level thus is in the responsibility of the producer of such documents, to link e.g. vulnerability information to the matching product.

A dictionary like presentation of all defined schema elements is given in the section SCHEMASECTIONNUMBER Schema. Any expected relations to other elements (linkage) is described there. This linking relies on setting attribute values accordingly (mostly guided by industry best practice and conventions) and thus implies, that any deep validation on a semantic level is to be ensured by the producer and consumer of CSAF documents. It is out of scope for this specification.

Proven and intended usage patterns from practice are given where possible. 

Delegation to industry best practices technologies is used in referencing schemas for:

* Platform Data:
  * Common Platform Enumeration (CPE) Version 2.3 [CPE23_A]
* Vulnerability Scoring:
  * Common Vulnerability Scoring System (CVSS) Version 3.1 [CVSS31]
    * JSON Schema Reference https://www.first.org/cvss/cvss-v3.1.json
  * Common Vulnerability Scoring System (CVSS) Version 3.0 [CVSS30]
    * JSON Schema Reference https://www.first.org/cvss/cvss-v3.0.json
  * Common Vulnerability Scoring System (CVSS) Version 2.0 [CVSS2]
    * JSON Schema Reference https://www.first.org/cvss/cvss-v2.0.json
* Classfication for Document Distribution
  * Traffic Light Protocol (TLP)
    * Default Definition: https://www.first.org/tlp/ 

-------

# 3 Schema Elements

The CSAF schema describes how to represent security advisory information as a JSON document.

The CSAF schema Version 2.0 builds on the JSON Schema draft 2019-09 rules.

    "$schema": "https://json-schema.org/draft/2019-09/schema"

The schema identifier is (before publication):

    "$id": "https://raw.githubusercontent.com/oasis-tcs/csaf/master/csaf_2.0/json_schema/csaf_json_schema.json"

The further documentation of the schema is organized via Definitions and Properties. 

* Definitions provide types that extend the JSON schema model 
* Properties use these types to support assembling security advisories

Types and properties together provide the vocabulary for the domain specific language supporting security advisories. 

The single mandatory property is `document`. 
The optional two additional properties are `product_tree` and `vulnerabilities`.

## 3.1 Definitions
The definitions (`$defs`) introduce the following domain specific types into the CSAF language: 
Acknowledgments (`acknowledgments_t`), Branches (`branches_t`), Full Product Name (`full_product_name_t`), Language (`lang_t`), Notes (`notes_t`), Products (`products_t`), Product Groups (`product_groups_t`), Product Group ID (`product_group_id_t`), Product ID (`product_id_t`), References (`references_t`), and Version (`version_t`).  

    "$defs": {
        "acknowledgments_t": {
            // ...
        },
        "branches_t": {
            // ...
        },
        "full_product_name_t": {
            // ...
        },
        "lang_t": {
            // ...
        },
        "notes_t": {
            // ...
        },
        "products_t": {
            // ...
        },
        "product_groups_t": {
             // ...
        },
        "product_group_id_t": {
            // ...
        },
        "product_id_t": {
            // ...
        },
        "references_t": {
            // ...
        },
        "version_t": {
            // ...
        }
    },

### 3.1.1 Acknowledgments Type
List of Acknowledgments (`acknowledgments_t`) type instances of value type array with 1 or more elements contain a list of `Acknowledgment` elements.

    "acknowledgments_t": {
      // ...
      "items": {
        // ...
        "properties": {
          "names": {
            // ...
          },
          "organizations": {
            // ...
          },
          "summary": {
            // ...
          },
          "urls": {
            // ...
          }
        }
      }
    },

#### 3.1.1.1 Acknowledgments - Acknowledgment Type
The value type of `Acknowledgment` is object with at least 1 and at most 4 properties. Every such element acknowledges contributions by describing those that contributed.
The properties are: `names`, `organizations`, `summary`, and `urls`.

##### 3.1.1.1.1 Acknowledgments - Acknowledgment Type - Names

List of acknowledged names (`names`) has value type `array` with 1 or more items holds the names of entities being recognized.
Every such item of value type `string` with 1 or more characters represents the name of entity being recognized and contains the name of a single person. 

Examples:

    Johann Sebastian Bach
    Albert Einstein

##### 3.1.1.1.2 Acknowledgments - Acknowledgment Type - Organizations

List of contributing organizations (`organizations`) has value type `array` with 1 or more items holds the names of contributing organizations being recognized.
Every such item of value type `string` with 1 or more characters represents the name of a single organization.

Examples:

    CISA
    Talos
    Google Project Zero

##### 3.1.1.1.3 Acknowledgments - Acknowledgment Type - Summary

Summary of the acknowledgment (`summary`) of value type `string` with 1 or more characters SHOULD represent any contextual details the document producers wish to make known about the acknowledgment or acknowledged parties. 

Example:

    First analysis of Coordinated Multi-Stream Attack (CMSA)

##### 3.1.1.1.4 Acknowledgments - Acknowledgment Type - URLs

List of URLs (`urls`) of acknowledgment is a container (value type `array`) for 1 or more `string` of type URL that specifies a list of URLs or location of the reference to be acknowledged.
Any URL of acknowledgment contains the URL or location of the reference to be acknowledged. 
Value type is string with format URI (`uri`).

### 3.1.2 Branches Type

List of branches (`branches_t`) with value type `array` contains 1 or more `branch` elements as children of the current element.

    "branches_t": {
      //...
      "items": {
        // ...
        "properties": {
          "name": {
            // ...
          },
          "type": {
            // ...
          },
          "branches": {
            // ...
          },
          "product": {
            // ...
          }
        }
      }
    },


#### 3.1.2.1 Branches - Branch Type

Every Branch holds exactly 3 properties and is a part of the hierarchical structure of the product tree. 
The properties `name` and `type` are mandatory. In addition, the object contains either a `branches` or a `product` property. 



##### 3.1.2.1.1 Branches - Branch Type - Name

Name of the branch (`name`) of value type string with 1 character or more contains the canonical descriptor or 'friendly name' of the branch. 

Examples:

    Microsoft
    Siemens
    Windows
    Office
    SIMATIC
    10
    365
    PCS 7

##### 3.1.2.1.2 Branches - Branch Type - Type

Type of the branch (`type`) of value type `string` as `enum` describes the characteristics of the labeled branch. 
Valid `enum` values are:

    architecture
    host_name
    language
    legacy
    patch_level
    product_family
    product_name
    product_version
    service_pack
    specification
    vendor

##### 3.1.2.1.3 Branches - Branch Type - Branches

List of branches (`branches`) has the value type `branches_t`. 

##### 3.1.2.1.4 Branches - Branch Type - Product

Product (`product`) has the value type Full Product Name (`full_product_name_t`).

### 3.1.3 Full Product Name Type
Full Product Name (`full_product_name_t`) with value type `object` specifies information about the product and assigns the product_id.
The properties `product_id` and `name` are required. The property `cpe` is optional.

    "full_product_name_t": {
      // ...
      "properties": {
        "product_id": {
          // ...
        },
        "name": {
          // ...
        },
        "cpe": {
          // ...
        }
      }
    },

#### 3.1.3.1 Full Product Name Type - Product ID

Product ID (`product_id`) holds a value of type Product ID (`product_id_t`).

#### 3.1.3.2 Full Product Name Type - Name

Textual description of the product (`name`) has value type `string` with 1 or more characters.
The value should be the product's full canonical name, including version number and other attributes, as it would be used in a human-friendly document.

Examples:

    Microsoft Host Integration Server 2006 Service Pack 1
    Cisco AnyConnect Secure Mobility Client 2.3.185

#### 3.1.3.3 Full Product Name Type - CPE

Common Platform Enumeration representation (`cpe`) of value type `string` of 5 or more characters with `pattern` (regular expression):

    ^(cpe:2\\.3:[aho\\*\\-](:(((\\?*|\\*?)([a-zA-Z0-9\\-\\._]|(\\\\[\\\\\\*\\?!\"#\\$%&'\\(\\)\\+,/:;<=>@\\[\\]\\^`\\{\\|\\}~]))+(\\?*|\\*?))|[\\*\\-])){5}(:(([a-zA-Z]{2,3}(-([a-zA-Z]{2}|[0-9]{3}))?)|[\\*\\-]))(:(((\\?*|\\*?)([a-zA-Z0-9\\-\\._]|(\\\\[\\\\\\*\\?!\"#\\$%&'\\(\\)\\+,/:;<=>@\\[\\]\\^`\\{\\|\\}~]))+(\\?*|\\*?))|[\\*\\-])){4})|([c][pP][eE]:/[AHOaho]?(:[A-Za-z0-9\\._\\-~%]*){0,6})$

The Common Platform Enumeration (CPE) attribute refers to a method for naming platforms external to this specification.

### 3.1.4 Language Type
Language type (`lang_t`) has value type `string` with `pattern` (regular expression):

    ^[a-zA-Z]{2,3}(-.+)?$

The value identifies a language, corresponding to IETF BCP 47 / RFC 5646.
See IETF language registry: [https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry)

Examples:

    de
    en
    fr
    frc
    jp

### 3.1.5 Notes Type
List of notes (`notes_t`) of value type `array` with 1 or more items of type `Note` contains notes which are specific to the current context.


    "notes_t": {
      // ..
      "items": {
        // ...
        "properties": {
          // ...
        }
      }
    },


Value type of every such Note item is `object` with the mandatory properties `type` and `text` providing a place to put all manner of text blobs related to the current context. 
A note `object` may provide the additional properties `audience` and `title`.

    "properties": {
      "audience": {
        // ...
      },
      "title": {
        // ...
      },
      "type": {
        // ...
      },
      "text": {
        // ...
      }
    }

Audience of note (`audience`) of value type `string` with 1 or more characters indicates who is intended to read it.

Examples:

    all
    executives
    operational management and system administrators
    safety engineers

Title of note (`title`) of value type `string` with 1 or more characters provides a concise description of what is contained in the text of the note.

Examples:

    Details
    Executive summary
    Technical summary
    Impact on safety systems

Note type (`type`) of value type `string` as `enum` indicates the choice of what kind of note this is. 
Valid `enum` values are:

    description
    details
    faq
    general
    legal_disclaimer
    other
    summary

Note contents (`text`) of value type `string` 1 or more characters holds the contents of the note. Content varies depending on type.

### 3.1.6 Products Type
List of Product IDs (`products_t`) of value type `array` with 1 or more unique items (a `set`) of type Product ID (`product_id_t`) specifies a list of `product_ids` to give context to the parent item.

    "products_t": {
      // ...
      "items": {
        // ...
      }      
    },

### 3.1.7 Product Groups Type
List of Product Group ID (`product_groups_t`) of value type `array` with 1 or more unique items (a `set`) of type Product Group ID (`product_group_id_t`) specifies a list of `product_group_ids` to give context to the parent item. 

    "product_groups_t": {
      // ...
      "items": {
        // ...
      }
    },

### 3.1.8 Product Group ID Type
The Product Group ID Type (`product_group_id_t`) of value type `string` with 1 or more characters is a reference token for product group instances. 
The value is a token required to identify a group of products so that it can be referred to from other parts in the document.
There is no predefined or required format for the Product Group ID (`product_group_id`) as long as it uniquely identifies a group in the context of the current document. 

    "product_group_id_t": {
      // ...
    },

Examples:

    CSAFGID-0001
    CSAFGID-0002
    CSAFGID-0020

### 3.1.9 Product ID Type
The Product ID Type (`product_id_t`) of value type `string` with 1 or more characters is a reference token for product instances. 
The value is a token required to identify a `full_product_name` so that it can be referred to from other parts in the document. There is no predefined or required format for the Product Group ID (`product_id`) as long as it uniquely identifies a product in the context of the current document.

    "product_id_t": {
      // ...
    },

Examples:

    CVRFPID-0004
    CVRFPID-0008

### 3.1.10 References Type
List of references (`references_t`) of value type `array` with 1 or more items of type Reference holds a list of Reference objects. 

    "references_t": {
      // ...
      "items": {
        // ...
        "properties": {
          // ...
        }
      }
    },

Value type of every such Reference item is `object` with the mandatory properties `url` and `summary` holding any reference to conferences, papers, advisories, and other resources that are related and considered related to either a surrounding part of or the entire document and to be of value to the document consumer. 
A reference `object` may provide the additional property `type`.

    "properties": {
      "summary": {
        // ...
      },
      "type": {
        // ...
      },
      "url": {
        // ...
      }
    }

Summary of the reference (`summary`) of value type `string` with 1 or more characters indicates what this reference refers to.

Type of reference (`type`) of value type `string` as `enum` indicates whether the reference points to the same document or vulnerability in focus (depending on scope) or to an external resource.
Valid `enum` values are:

    external
    self

The default value for `type` is `external`.

URL of reference (`url`) of value type `string` and format `uri` provides the URL for the reference.

### 3.1.11 Version Type
The Version (`version_t`) type has value type `string` with `pattern` (regular expression):

    ^(0|[1-9][0-9]*)(\\.(0|[1-9][0-9]*)){0,3}$

The `Version` specifies a version string with a simple hierarchical counter model to denote clearly the evolution of the content of the document. Format must be understood as 'major\[.minor\[.patch\[.build\]\]\]' version.

Examples:

    1
    0.9
    1.4.3
    2.40.0.320002

## 3.2 Properties

These final three subsections document the three properties of a CSAF document. The single mandatory property `document`, as well as the optional properties `product_tree` and `vulnerabilities` in that order.

### 3.2.1 Document Property

Document level meta-data (`document`) of value type `object` with the 5 mandatory properties CSAF Version (`csaf_version`), Title (`title`), Publisher (`publisher`), Type (`type`), and Tracking (`tracking`) captures the meta-data about this document describing a particular set of security advisories. 
In addition, the `document` object may provide the 7 optional properties Acknowledgments (`acknowledgments`), Aggregate Severity (`aggregate_severity`), Distribution (`distribution`), Language (`lang`), Source Language (`source_lang`), Notes (`notes`), and References (`references`). 

    "document": {
      // ...
      "properties": {
        "acknowledgments": {
          // ...
        },
        "aggregate_severity" : {
          // ...
        },
        "csaf_version": {
          // ...
        },
        "distribution": {
          // ...
        },
        "lang": {
          // ...
        },
        "source_lang": {
          // ...
        },
        "notes": {
          // ...
        },
        "publisher": {
          // ...
        },
        "references": {
          // ...
        },
        "title": {
          // ...
        },
        "tracking": {
          // ...
        },
        "type": {
          // ...
        }
      }
    },

#### 3.2.1.1 Document Property - Acknowledgments
List of acknowledgments (`acknowledgments`) of value type `array` with 1 or more items of type Acknowledgment contains a list of acknowledgment elements.
 
    "acknowledgments": {
      // ...
      "items": {
        // ...
      }
    },

#### 3.2.1.2 Document Property - Aggregate Severity

Aggregate severity (`aggregate_severity`) of value type `object` with the mandatory property `text` and the optional property `namespace` is a vehicle that is provided by the document producer to convey the urgency and criticality with which the one or more vulnerabilities reported should be addressed. It is a document-level metric and applied to the document as a whole — not any specific vulnerability. The range of values in this field is defined according to the document producer's policies and procedures. 

    "aggregate_severity" : {
      // ...
      "properties": {
        "namespace": {
          // ...
        },
        "text": {
          // ...
        }
      }
    },

The Namespace of aggregate severity (`namespace`) of value type `string` and format `uri` points to the namespace so referenced.

The Text of aggregate severity (`text`) of value type `string` with 1 or more characters provides a severity which is independent of - and in addition to - any other standard metric for determining the impact or severity of a given vulnerability (such as CVSS).

Examples:

    Moderate
    Important
    Critical

#### 3.2.1.3 Document Property - CSAF Version

CSAF version (`csaf_version`) of value type `string` and `enum` gives the version of the CSAF specification which the document was generated for. 
The single valid value for this `enum` is:

    2.0

#### 3.2.1.4 Document Property - Distribution

Rules for sharing document ( `distribution`) of value type `object` with at least 1 of the 2 properties Text (`text`) and Traffic Light Protocol TLP (`tlp`) describes any constraints on how this document might be shared.

    "distribution": {
      // ...
      "properties": {
        "text": {
          // ...
        },
        "tlp": {
          // ...
        }
      }
    },

##### 3.2.1.4.1 Document Property - Distribution - Text

The Textual description (`text`) of value type `string` with 1 or more characters provides a textual description of additional constraints.

Examples:

    Share only on a need-to-know-basis only.
    Distribute freely.
    Copyright 2019, Example Company, All Rights Reserved.

##### 3.2.1.4.2 Document Property - Distribution - TLP

Traffic Light Protocol (TLP) (`tlp`) of value type `object` with the mandatory property Label (`label`) and the optional property URL (`url`) provides details about the TLP classification of the document.

    "tlp": {
      // ...
      "properties": {
        "label": {
          // ...
        },
        "url": {
          // ...
        }
      }
    }

The Label of TLP (`label`) with value type `string` and `enum` provides the TLP label of the document. 
Valid values of the `enum` are:

    RED
    AMBER
    GREEN
    WHITE

The URL of TLP version (`url`) with value type `string` and format `uri` provides a URL where to find the textual description of the TLP version which is used in this document. Default value is the URL to the definition by FIRST. 
The default value is:

    https://www.first.org/tlp/

Examples:

    https://www.us-cert.gov/tlp
    https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Kritis/Merkblatt_TLP.pdf

#### 3.2.1.5 Document Property - Language

Document language (`lang`) of Language Type (`lang_t`) identifies the language used by this document, corresponding to IETF BCP 47 / RFC 5646.

#### 3.2.1.6 Document Property - Source Language

Source language (`source_lang`) of Language Type (`lang_t`) identifies if this copy of the document is a translation then the value of this property describes from which language this document was translated.

#### 3.2.1.7 Document Property - Notes

Notes (`notes`) associated with the whole document of Notes Type (`notes_t`) holds notes about this set of vulnerabilities.

#### 3.2.1.8 Document Property - Publisher

Publisher (`publisher`) has value type `object` with the mandatory property Type (`type`) and provides information on the publishing entity. 
The 3 other optional properties are: `contact_details`, `issuing_authority`, and `vendor_id`.

    "publisher": {
      // ...
      "properties": {
        "contact_details": {
          // ...
        },
        "issuing_authority": {
          // ...
        },
        "type": {
          // ...
        },
        "vendor_id": {
          // ...
        }
      }
    },

##### 3.2.1.8.1 Document Property - Publisher - Contact Details

Contact details (`contact_details`) of value type `string` with 1 or more characters provides information on how to contact the publisher, possibly including details such as web sites, email addresses, phone numbers, and postal mail addresses.

Example:

    Example Company can be reached at contact_us@example.com, or via our website at https://www.example.com/contact.

##### 3.2.1.8.2 Document Property - Publisher - Issuing Authority

Issuing authority (`issuing_authority`) of value type `string`with 1 or more characters provides the name of the issuing party and their authority to release the document, in particular, the party's constituency and responsibilities or other obligations.

##### 3.2.1.8.3 Document Property - Publisher - Type

The Type of publisher (`type`) of type `string`and `enum` provides information about the type of publisher releasing the document. 
The valid values are:

    coordinator
    discoverer
    other
    user
    vendor

##### 3.2.1.8.4 Document Property - Publisher - Vendor ID

The Vendor releasing the document (`vendor_id`) of value type `string` with 1 or more characters provides the Vendor ID which is a unique identifier (OID) that a vendor uses as issued by FIRST under the auspices of IETF.

#### 3.2.1.9 Document Property - References
References (`references`) of References type (`references_t`).

    "references": {
      // ...
    },

#### 3.2.1.10 Document Property - Title

Title of this document (`title`) of value type `string` with 1 or more characters SHOULD be a canonical name for the document, and sufficiently unique to distinguish it from similar documents.

Examples:

    Example Company Cross-Site-Scripting Vulnerability in Example Generator
    Cisco IPv6 Crafted Packet Denial of Service Vulnerability

#### 3.2.1.11 Document Property - Tracking

Tracking (`tracking`) of value type `object` with the six mandatory properties: Current Release Date (`current_release_date`), Identifier (`id`), Initial Release Date (`initial_release_date`), Revision History (`revision_history`), Status (`status`), and Version (`version`) is a container designated to hold all management attributes necessary to track a CSAF document as a whole.
The two optional additional properties are Aliases (`aliases`) and Generator (`generator`).

    "tracking": {
      // ...
      "properties": {
        "id": {
          // ...
        },
        "aliases": {
          // ...
        },
        "current_release_date": {
          // ...
        },
        "generator": {
          // ...
        },
        "initial_release_date": {
          // ...
        },
        "revision_history": {
          // ...
        },
        "status": {
          // ...
        },
        "version": {
          // ...
        }
      }
    },


##### 3.2.1.11.1 Document Property - Tracking - ID

Unique identifier for the document (`id`) of value type `string` with 1 or more characters holds the Identifier.
The ID is a simple label that provides for a wide range of numbering values, types, and schemes. 
Its value SHOULD be assigned and maintained by the original document issuing authority.

Examples:

    Example Company - 2019-YH3234
    RHBA-2019:0024
    cisco-sa-20190513-secureboot

##### 3.2.1.11.2 Document Property - Tracking - Aliases
Aliases (`aliases`) of value type `array` with 1 or more unique items (a `set`) representing Alternate Names contains a list of alternate names for the same document.

    "aliases": {
      // ...
      "items": {
        // ...
      }
    },

Every such Alternate Name of value type `string` with 1 or more characters specifies a non-empty string that represents a distinct optional alternative ID used to refer to the document.

Example:

    CVE-2019-12345

##### 3.2.1.11.3 Document Property - Tracking - Current Release Date

Current release date (`current_release_date`) with value type `string` and format `date-time` holds the date when the current revision of this document was released.


##### 3.2.1.11.4 Document Property - Tracking - Generator

Document Generator (`generator`) of value type `object` with mandatory property Engine (`engine`) and optional property Date (`date`) is a container to hold all elements related to the generation of the document. These items will reference when the document was actually created, including the date it was generated and the entity that generated it.. 

        "generator": {
          // ...
          "properties": {
            "engine": {
              // ...
            },
            "date": {
              // ...
            }
          }
        },

Engine of document generation (`engine`) of value type `string` with 1 or more characters SHOULD represent the name of the engine that generated the CSAF document, and MAY additionally refer to its version.

Examples:

    TVCE
    Red Hat rhsa-to-cvrf 2.1
    CMPFA Core Converter CVRF->CSAF Version 0.6


Date of document generation (`date`) of value type `string` with format `date-time` SHOULD be the current date that the document was generated. 
Because documents are often generated internally by a document producer and exist for a nonzero amount of time before being released, this field MAY be different from the Initial Release Date and Current Release Date.

##### 3.2.1.11.5 Document Property - Tracking - Initial Release Date

Initial release date (`initial_release_date`) with value type `string` and format `date-time` holds the date when this document was first published.

##### 3.2.1.11.6 Document Property - Tracking - Revision History

The Revision History (`revision_history`) with value type `array` of 1 or more Revision History Entries holds one revision item for each version of the CSAF document, including the initial one. 

        "revision_history": {
          // ...
          "items": {
            "type": "object",
            "properties": {
              "number": {
                // ...
              },
              "date": {
                // ...
              },
              "summary": {
                // ...
              }
            }
          }
        },

Each Revision contains all the information elements required to track the evolution of a CSAF document. Revision History Entry items are of type `object` with the three mandatory properties: Number (`number`), Date (`date`), and Summary (`summary`). 

The Number (`number`) has value type Version (`version_t`). 

The Date of the revision (`date`) of value type `string` with format `date-time` states the date of the revision entry.

The Summary of the revision (`summary`) of value type `string` with 1 or more characters holds a single non-empty string representing a short description of the changes.

##### 3.2.1.11.7 Document Property - Tracking - Status

Document status (`status`) of value type `string` and `enum` defines the draft status of the document.
The value MUST be one of the following:

    draft
    final
    interim

##### 3.2.1.11.8 Document Property - Tracking - Version

Version has the value type Version (`version_t`).

#### 3.2.1.12 Document Property - Type
Document type (`type`) with value type `string` of 1 or more characters defines a short canonical name, chosen by the document producer, which will inform the end user as to the type of document.

    "type": {
      // ...
    }

Examples:

    Security Advisory
    Security Notice
    Vulnerability Report

### 3.2.2 Product Tree Property

Product Tree (`product_tree`) has value type `object` with 1 or more properties is a container for all fully qualified product names that can be referenced elsewhere in the document. 
The properties are Branches (`branches`), Full Product Names (`full_product_names`), Product Groups (`product_groups`), and Relationships (`relationships`).

    "product_tree": {
      // ...
      "properties": {
        "branches": {
          // ...
        },
        "full_product_names": {
          // ...
        },
        "product_groups": {
          // ...
        },
        "relationships": {
          // ...
      }
    },

#### 3.2.2.1 Product Tree Property - Branches
List of branches (`branches`) of value type `branches_t`.

#### 3.2.2.2 Product Tree Property - Full Product Names
List of full product names (`full_product_names`) of value type `array` with 1 or more items of type `full_product_name_t` contains a list of full product names.

#### 3.2.2.3 Product Tree Property - Product Groups
List of product groups (`product_groups`) of value type `array` with 1 or more items of type `object` contains a list of product groups.

    "product_groups": {
      // ...
      "items": {
        // ...
        "properties": {
          "summary": {
            // ...
          },
          "group_id": {
            // ...
          },
          "product_ids": {
            // ...
          }
        }
      }
    },

The product group items are of value type `object` with the 2 mandatory properties Group ID (`group_id`) and Product IDs (`product_ids`) and the optional Summary (`summary`) property.

The summary of the product group (`summary`) of type `string` with 1 or more characters gives a short, optional description of the group.

Examples:

    The x64 versions of the operating system.
    Products supporting Modbus.

Group ID (`group_id`) has value type Product Group ID (`product_group_id_t`).

List of Product IDs (`product_ids`) of value type array with 2 or more items of type Product ID (`product_id_t`) lists the product_ids of those products which known as one group in the document.

#### 3.2.2.4 Product Tree Property - Relationships
List of relationships (`relationships`) of value type `array`with 1 or more items contains a list of relationships.

    "relationships": {
      // ...
      "items": {
        // ...
        "properties": {
          "full_product_names": {
            // ...
          },
          "product_reference": {
            // ...
          },
          "relates_to_product_reference": {
            // ...
          },
          "relationship_type": {
            // ...
          }
        }
      }
    }

The Relationship item is of value type `object` with the three mandatory properties Product Reference (`product_reference`), Relates to Product Reference (`relates_to_product_reference`), and Relationship Type (`relationship_type`) as well as the optional property Full Product Names (`full_product_names`) establishes a link between two existing `full_product_name_t` elements, allowing the document producer to define a combination of two products that form a new `full_product_name` entry.

Full Product Names (`full_product_names`) of value type array with 1 or more items of Full Product Name type (`full_product_name_t`).

Product Reference (`product_reference`) holds a Product ID (`product_id_t`) value.

Relates to Product Reference (`relates_to_product_reference`) holds also a Product ID (`product_id_t`) value.

Relationship type (`relationship_type`) of value `string`and `enum` defines the type of relationship for the referenced component.
The valid values are:

    default_component_of
    optional_component_of
    external_component_of
    installed_on
    installed_with


### 3.2.3 Vulnerabilities Property
Vulnerabilities (`vulnerabilities`) of value type `array` with 1 or more objects representing vulnerabilities and providing 1 or more properties represents a list of all relevant vulnerability information items. 

    "vulnerabilities": {
      // ...
      "items": {
        // ...
        "properties": {
          "acknowledgments": {
            // ...
          },
          "cve": {
            // ...
          },
          "cwe": {
            // ...
          },
          "scores": {
            // ...
          },
          "discovery_date": {
            // ...
          },
          "id": {
            // ...
          },
          "involvements": {
            // ...
          },
          "notes": {
            // ...
          },
          "product_status": {
            // ...
          },
          "references": {
            // ...
          },
          "release_date": {
            // ...
          },
          "remediations": {
            // ...
          },
          "threats": {
            // ...
          },
          "title": {
            // ...
          }
        }
      }
    }

#### 3.2.3.1 Vulnerabilities Property - Vulnerability
Vulnerability ( `vulnerability`) of value type `object` with 1 or more properties is a container for the aggregation of all fields that are related to a single vulnerability in the document. 
Any vulnerability may provide the optional properties Acknowledgments (`acknowledgments`), Common Vulnerabilities and Exposures (CVE) (`cve`), Common Weakness Enumeration (CWE) (`cwe`), Scores (`scores`), Discovery Date (`discovery_date`), ID (`id`), Involvements (`involvements`), Notes (`notes`), Product Status (`product_status`), References (`references`), Release Date (`release_date`), Remediations (`remediations`), Threats (`threats`),and Title (`title`). 

##### 3.2.3.1.1 Vulnerabilities Property - Vulnerability - Acknowledgments
List of acknowledgments (`acknowledgments`) of value type `array` with 1 or more items of type Acknowledgment contains a list of acknowledgment elements.

##### 3.2.3.1.2 Vulnerabilities Property - Vulnerability - CVE
CVE (`cve`) of value type `string` with `pattern` (regular expression):

    ^CVE-[0-9]{4}-[0-9]{4,}$

holds the MITRE standard Common Vulnerabilities and Exposures (CVE) tracking number for the vulnerability.

##### 3.2.3.1.3 Vulnerabilities Property - Vulnerability - CWE
CWE (`cwe`) of value type `object` with the 2 mandatory properties Weakness ID (`id`) and Weakness Name (`name`) holds the MITRE standard Common Weakness Enumeration (CWE) for the weakness associated.

    "cwe": {
      // ...
      "properties": {
        "id": {
          // ...
        },
        "name": {
          // ...
        }
      }
    },

The Weakness ID (`id`) has value type `string` with `pattern` (regular expression):

    ^CWE-[1-9]\\d{0,5}$

and holds the ID for the weakness associated.

Examples:

    CWE-79
    CWE-22
    CWE-352

The Weakness name (`name`) has value type `string` with 1 or more characters and holds the full name of the weakness as given in the CWE specification.

Examples:

    Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')
    Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')
    Cross-Site Request Forgery (CSRF)


##### 3.2.3.1.4 Vulnerabilities Property - Vulnerability - Scores
List of scores (`scores`) of value type `array` with 1 or more items of type score holds a list of score objects for the current vulnerability.

    "scores": {
      // ...
      "items": {
        // ...
        }
      }
    },


Value type of every such Score item is `object` with the mandatory property `products` and the optional properties `cvss_v2` and `cvss_v3` specifies information about (at least one) score of the vulnerability and for which products the given value applies. Each Score item has at least 2 properties.

        "properties": {
          "products": {
            // ...
          },
          "cvss_v2": {
            // ...
          },
          "cvss_v3": {
            "oneOf": [
              // ...
            ]
          }

Product IDs (`products`) of value type `products_t` with 1 or more items indicates for which products the given scores apply.

The property CVSS v2 (`cvss_v2`) holding a CVSS v2.0 value abiding by the schema at [https://www.first.org/cvss/cvss-v2.0.json](https://www.first.org/cvss/cvss-v2.0.json).

The property CVSS v3 (`cvss_v3`) holding a CVSS v3.x value abiding by one of the schemes at [https://www.first.org/cvss/cvss-v3.0.json](https://www.first.org/cvss/cvss-v3.0.json) or [https://www.first.org/cvss/cvss-v3.1.json](https://www.first.org/cvss/cvss-v3.1.json).

##### 3.2.3.1.5 Vulnerabilities Property - Vulnerability - Discovery Date
Discovery date (`discovery_date`) of value type `string` with format `date-time` holds the date and time the vulnerability was originally discovered.

##### 3.2.3.1.6 Vulnerabilities Property - Vulnerability - ID
ID (`id`) of value type `object`with the two mandatory properties System Name (`system_name`) and Text (`text`) gives the document producer a place to publish a unique label or tracking ID for the vulnerability (if such information exists).

    "id": {
      // ...
      "properties": {
        "system_name": {
          // ...
        },
        "text": {
          // ...
        }
      }
    },

System name (`system_name`) of value type `string` with 1 or more characters indicates the name of the vulnerability tracking or numbering system.

Example:

    Cisco Bug ID

Text (`text`) of value type `string` with 1 or more characters is unique label or tracking ID for the vulnerability (if such information exists).

Example:

    CSCso66472

##### 3.2.3.1.7 Vulnerabilities Property - Vulnerability - Involvements
List of involvements (`involvements`) of value type `array` with 1 or more items of type `object` contains a list of involvements.

    "involvements": {
      // ...
      "items": {
        // ...
        "properties": {
          "summary": {
            // ...
          },
          "party": {
            // ...
          },
          "status": {
            // ...
          }
        }
      }
    },

Involvement (`involvement`) of value type `object` with the 2 mandatory properties Party (`party`), Status (`status`) and the optional property Summary (`summary`) is a container, that allows the document producers to comment on their level of Involvement (or engagement) in the vulnerability identification, scoping, and remediation process. 

Summary of involvement ( `summary`) of value type `string` with 1 or more characters contains additional context regarding what is going on.

Party type (`party`) of value type `string`and `enum` defines the type of the involved party.
Valid values are:

    coordinator
    discoverer
    other
    user
    vendor

Party status (`status`) of value type `string`and `enum` defines contact status of the involved party.
Valid values are:

    completed
    contact_accepted
    disputed
    in_progress
    not_contacted
    open

##### 3.2.3.1.8 Vulnerabilities Property - Vulnerability - Notes
Notes (`notes`) have value type Notes (notes_t).

##### 3.2.3.1.9 Vulnerabilities Property - Vulnerability - Product Status
Product status (`product_status`) of value type `object` with 1 or more properties contains different lists of product_ids which provide details on the status of the referenced product related to the current vulnerability.
The eight defined properties are Fixed (`fixed`), First fixed (`first_fixed`), Recommended (`recommended`), Known affected (`known_affected`), First affected (`first_affected`), Last affected (`last_affected`), Known not affected (`known_not_affected`), and Under investigation (`under_investigation`) are all of value type Products (`products_t`).

    "product_status": {
      // ...
      "properties": {
        "fixed": {
          // ...
        },
        "first_fixed": {
          // ...
        },
        "recommended": {
          // ...
        },
        "known_affected": {
          // ...
        },
        "first_affected": {
          // ...
        },
        "last_affected": {
          // ...
        },
        "known_not_affected": {
          // ...
        },
        "under_investigation": {
          // ..
        }
      }
    },

Fixed (`fixed`) of value type Products (`products_t`) represents that these versions contain a fix for the vulnerability but may not be the recommended fixed versions.

First fixed (`first_fixed`) of value type Products (`products_t`) represents that these versions contain the first fix for the vulnerability but may not be the recommended fixed versions.

Recommended (`recommended`) of value type Products (`products_t`) represents that these versions have a fix for the vulnerability and are the vendor-recommended versions for fixing the vulnerability.

Known affected (`known_affected`) of value type Products (`products_t`) represents that these versions are known to be affected by the vulnerability.

First affected (`first_affected`) of value type Products (`products_t`) represents that these are the first versions of the releases known to be affected by the vulnerability.

Last affected (`last_affected`) of value type Products (`products_t`) represents that these are the last versions in a release train known to be affected by the vulnerability. Subsequently released versions would contain a fix for the vulnerability.

Known not affected (`known_not_affected`) of value type Products (`products_t`) represents that these versions are known not to be affected by the vulnerability.

Under investigation (`under_investigation`) of value type Products (`products_t`) represents that it is not known yet whether this version is or is not affected by the vulnerability. However, it is still under investigation - the result will be provided in a later release of the document.

##### 3.2.3.1.10 Vulnerabilities Property - Vulnerability - References
References (`references`) have value type References (`references_t`).

##### 3.2.3.1.11 Vulnerabilities Property - Vulnerability - Release Date
Release date (`release_date`) with value type `string` of format `date-time` holds the date and time the vulnerability was originally released into the wild.

##### 3.2.3.1.12 Vulnerabilities Property - Vulnerability - Remediations
List of remediations (`remediations`) of value type `array`with 1 or more Remediation items of type `object` contains a list of remediations.
Remediation of value type `object` with the 2 mandatory properties Details (`details`) and Type (`type`) specifies details on how to handle (and presumably, fix) a vulnerability.
In addition, any Remediation may expose the six optional properties Date (`date`), Entitlements (`entitlements`), Group IDs (`group_ids`), Product IDs (`product_ids`), Restart required (`restart_required`), and URL (`url`).

    "remediations": {
      // ...
      "items": {
        // ...
        "properties": {
          "date": {
            // ...
          },
          "details": {
            // ...
          },
          "entitlements": {
            // ...
          },
          "group_ids": {
            // ...
          },
          "product_ids": {
            // ...
          },
          "restart_required": {
            // ...
            "properties": {
              "type": {
                // ...
              },
              "details": {
                // ...
              }
            }
          },
          "type": {
            // ...
          },
          "url": {
            // ...
          }
        }
      }
    },

Date of the remediation (`date`) of value type `string` with format `date-time` contains the date from which the remediation is available.

Details of the remediation (`details`) of value type `string` with 1 or more characters contains a thorough human-readable discussion of the remediation.

List of entitlements (`entitlements`) of value type `array` with 1 or more items of type Entitlement of the remediation as `string` with 1 or more characters contains a list of entitlements.
Every Entitlement of the remediation contains any possible vendor-defined constraints for obtaining fixed software or hardware that fully resolves the vulnerability.

Group IDs (`group_ids`) are of value type Product Groups (`product_groups_t`).

Product IDs (`product_ids`) are of value type Products (`products_t`).

Restart required by remediation (`restart_required`) of value type `object` with the 1 mandatory property Type (`type`) and the optional property Details (`details`) provides information on type of restart is required by this remediation to become effective.
Type of restart (`type`) of value type `string` and `enum` specifies what type of restart is required by this remediation to become effective.
Valid values are:

    none
    vulnerable_component
    service
    parent
    dependencies
    connected
    machine
    zone
    system

The values must be used as follows:
- `none`: No restart required.
- `vulnerable_component`: Only the vulnerable component (as given by the elements of `product_ids` or `group_ids` in the current remediation item) needs to be restarted.
- `service`: The vulnerable component and the background service used by the vulnerable component need to be restarted.
- `parent`: The vulnerable component and its parent process need to be restarted. This could be the case if the parent process has no build-in way to restart the vulnerable component or process values / context is only given at the start of the parent process.
- `dependencies`: The vulnerable component and all components which require the vulnerable component to work need to be restarted. This could be the case e.g. for a core service of a software.
- `connected`: The vulnerable component and all components connected (via network or any type of inter-process communication) to the vulnerable component need to be restarted.
- `machine`: The machine on which the vulnerable component is installed on needs to be restarted. This is the value which should be used if an OS needs to be restarted. It is typically the case for OS upgrades.
- `zone`: The security zone in which the machine resides on which the vulnerable component is installed needs to be restarted. This value might be useful for a remediation if no patch is available. If the malware can be wiped out by restarting the infected machines but the infection spreads fast the controlled shutdown of all machines at the same time and restart afterwards can leave one with a clean system.
- `system`: The whole system which the machine resides on which the vulnerable component is installed needs to be restarted. This may include multiple security zones. This could be the case for a major system upgrade in an ICS system or a protocol change.



Additional restart information (`details`) of value type `string` with 1 or more characters provides additional information for the restart. This can include details on procedures, scope or impact.

Type of the remediation (`type`) of value type `string` and `enum` specifies the type which this remediation belongs to.
Valid values are:

    workaround
    mitigation
    vendor_fix
    none_available
    no_fix_planned


URL (`url`) of value type `string`with format `uri` contains the URL where to obtain the remediation.

##### 3.2.3.1.13 Vulnerabilities Property - Vulnerability - Threats
List of threats (`threats`) of value type `array` with 1 or more items of `object` type representing Threats contains information about a vulnerability that can change with time.
A Threat item is of value type `object` with the two mandatory properties Details (`details`) and Type (`type`) and contains the vulnerability kinetic information. 
This information can change as the vulnerability ages and new information becomes available.
In addition, threat items may provide the three optional properties Date (`date`), Product IDs (`product_ids`) and Group IDs (`group_ids`). 

    "threats": {
      // ...
      "items": {
        // ...
        "properties": {
          "type": {
            // ...
          },
          "details": {
            // ...
          },
          "date": {
            // ...
          },
          "product_ids": {
            // ...
          },
          "group_ids": {
            // ...
          }
        }
      }
    },

Type of the threat (`type`) of value type `string` and `enum` categorizes the threat according to the rules of the specification.
Valid values are:

    impact
    exploit_status
    target_set

Details of the threat (`details`) of value type `string` with 1 or more characters represents a thorough human-readable discussion of the threat.

Date of the threat (`date`) of value type `string` with format `date-time` contains the date when the assessment was done or the threat appeared.

Product IDs (`product_ids`) are of value type Products (`products_t`).

Group IDs (`group_ids`) are of value type Product Groups (`product_groups_t`).

##### 3.2.3.1.14 Vulnerabilities Property - Vulnerability - Title
Title (`title`) has value type `string` with 1 or more characters and gives the document producer the ability to apply a canonical name or title to the vulnerability.

# 4 Safety, Security, and Data Protection Considerations
CSAF documents are based on JSON, thus the security considerations of [RFC8259] apply and are repeated here as service for the reader:
>Generally, there are security issues with scripting languages.  JSON is a subset of JavaScript but excludes assignment and invocation.
>
>Since JSON's syntax is borrowed from JavaScript, it is possible to use that language's `eval()` function to parse most JSON texts (but not all; certain characters such as `U+2028 LINE SEPARATOR` and `U+2029 PARAGRAPH SEPARATOR` are legal in JSON but not JavaScript).  This generally constitutes an unacceptable security risk, since the text could contain executable code along with data declarations.  The same consideration applies to the use of eval()-like functions in any other programming language in which JSON texts conform to that language's syntax.

In addition, CSAF documents may be rendered by consumers in various human readable formats like HTML or PDF.
Thus, for security reasons, CSAF producers and consumers SHALL adhere to the following:
* CSAF producers SHALL NOT emit messages that contain HTML, even though all variants of Markdown permit it.
* Deeply nested markup can cause a stack overflow in the Markdown processor [GFMENG]. To reduce this risk, CSAF consumers SHALL use a Markdown processor that is hardened against such attacks.
  **Note**: One example is the GitHub fork of the cmark Markdown processor [GFMCMARK].
* To reduce the risk posed by possibly malicious CSAF files that do contain arbitrary HTML (including, for example, javascript: links), CSAF consumers SHALL either disable HTML processing (for example, by using an option such as the --safe option in the cmark Markdown processor) or run the resulting HTML through an HTML sanitizer.
CSAF consumers that are not prepared to deal with the security implications of formatted messages SHALL NOT attempt to render them and SHALL instead fall back to the corresponding plain text messages.


(Note: OASIS strongly recommends that Technical Committees consider issues that might affect safety, security, privacy, and/or data protection in implementations of their specification and document them for implementers and adopters. For some purposes, you may find it required, e.g. if you apply for IANA registration.

While it may not be immediately obvious how your specification might make systems vulnerable to attack, most specifications, because they involve communications between systems, message formats, or system settings, open potential channels for exploit. For example, IETF [[RFC3552](#rfc3552)] lists “eavesdropping, replay, message insertion, deletion, modification, and man-in-the-middle” as well as potential denial of service attacks as threats that must be considered and, if appropriate, addressed in IETF RFCs.

In addition to considering and describing foreseeable risks, this section should include guidance on how implementers and adopters can protect against these risks.

We encourage editors and TC members concerned with this subject to read _Guidelines for Writing RFC Text on Security Considerations_, IETF [[RFC3552](#rfc3552)], for more information.

Remove this note before submitting for publication.)

-------

# 5 Conformance
## 5.1 Conformance Targets
This document defines requirements for the CSAF file format and for certain software components that interact with it. The entities ("conformance targets") for which this document defines requirements are:
* **CSAF document**: A security advisory text document in the format defined by this document.
* **CSAF producer**: A program which emits output in the CSAF format.
* **Direct producer**: An analysis tool which acts as a CSAF producer.
* **Converter**: A CSAF producer that transforms the output of an analysis tool from its native output format into the CSAF format.
* **CSAF post-processor**: A CSAF producer that transforms an existing CSAF document into a new CSAF document, for example, by removing or redacting security-sensitive elements.
* **CSAF consumer**: A program that reads and interprets a CSAF document.
* **Viewer**: A CSAF consumer that reads a CSAF document, displays a list of the results it contains, and allows an end user to view each result in the context of the artifact in which it occurs.
* **Result management system**: A software system that consumes the documents produced by analysis tools, produces reports that enable engineering teams to assess the quality of their software artifacts at a point in time and to observe trends in the quality over time, and performs functions such as filing bugs and displaying information about individual results.
* **Engineering system**: A software development environment within which analysis tools execute. It might include a build system, a source control system, a result management system, a bug tracking system, a test execution system, and so on.
The normative content in this document defines requirements for CSAF documents, except for those normative requirements that are explicitly designated as defining the behavior of another conformance target.

## 5.2 Conformance Clause 1: CSAF document
A text file satisfies the "CSAF document"”" conformance profile if:
* It conforms to the syntax and semantics defined in section 3.

## 5.3 Conformance Clause 2: CSAF producer
A program satisfies the "CSAF producer" conformance profile if:
* It produces output in the CSAF format, according to the semantics defined in section 3.
* It satisfies those normative requirements in section 3 that are designated as applying to CSAF producers.

## 5.4 Conformance Clause 3: Direct producer
An analysis tool satisfies the "Direct producer" conformance profile if:
* It satisfies the "CSAF producer" conformance profile.
* It additionally satisfies those normative requirements in section 3 that are designated as applying to "direct producers" or to "analysis tools".
* It does not emit any objects, properties, or values which, according to section 3, are intended to be produced only by converters.

## 5.5 Conformance Clause 4: Converter
A converter satisfies the “Converter” conformance profile if:
* It satisfies the "CSAF producer" conformance profile.
* It additionally satisfies those normative requirements in section 3 that are designated as applying to converters.
* It does not emit any objects, properties, or values which, according to section 3, are intended to be produced only by direct producers.

## 5.6 Conformance Clause 5: CSAF post-processor
A CSAF post-processor satisfies the "CSAF post-processor" conformance profile if:
* It satisfies the "CSAF consumer" conformance profile.
* It satisfies the "CSAF producer" conformance profile.
* It additionally satisfies those normative requirements in section 3 that are designated as applying to post-processors.

## 5.7 Conformance Clause 6: CSAF consumer
A consumer satisfies the "CSAF consumer" conformance profile if:
* It reads CSAF documents and interprets them according to the semantics defined in section 3.
* It satisfies those normative requirements in section 3 that are designated as applying to CSAF consumers.

## 5.8 Conformance Clause 7: Viewer
A viewer satisfies the "viewer" conformance profile if:
* It satisfies the "CSAF consumer" conformance profile.
* It additionally satisfies the normative requirements in section 3 that are designated as applying to viewers.

## 5.9 Conformance Clause 8: Result management system
A result management system satisfies the "result management system" conformance profile if:
* It satisfies the "CSAF consumer" conformance profile.
* It additionally satisfies the normative requirements in section 3 and Appendix B ("Use of fingerprints by result management systems") that are designated as applying to result management systems.

## 5.10 Conformance Clause 9: Engineering system
An engineering system satisfies the "engineering system" conformance profile if:
* It satisfies the normative requirements in section 3 that are designated as applying to engineering systems.

(Note: The [OASIS TC Process](https://www.oasis-open.org/policies-guidelines/tc-process#wpComponentsConfClause) requires that a specification approved by the TC at the Committee Specification Public Review Draft, Committee Specification or OASIS Standard level must include a separate section, listing a set of numbered conformance clauses, to which any implementation of the specification must adhere in order to claim conformance to the specification (or any optional portion thereof). This is done by listing the conformance clauses here.
For the definition of "conformance clause," see [OASIS Defined Terms](https://www.oasis-open.org/policies-guidelines/oasis-defined-terms-2017-05-26#dConformanceClause).

See "Guidelines to Writing Conformance Clauses":  
http://docs.oasis-open.org/templates/TCHandbook/ConformanceGuidelines.html.

Remove this note before submitting for publication.)


-------
# Appendix A. Acknowledgments

(Note: A Work Product approved by the TC must include a list of people who participated in the development of the Work Product. This is generally done by collecting the list of names in this appendix. This list shall be initially compiled by the Chair, and any Member of the TC may add or remove their names from the list by request.  
Remove this note before submitting for publication.)

The following individuals were members of the OASIS CSAF Technical Committee during the creation of this specification and their contributions are gratefully acknowledged:

**CSAF TC Members:**

| First Name | Last Name | Company |
| :--- | :--- | :--- |
Participated | in meetings | Something Company
Alex | Amirnovman | Company B
Kris | Anderman | Mini Micro
Darren | Anstman | Big Networks

The following individuals were members of the OASIS CSAF Technical Committee during the creation of the previous version (CVRF v1.2) of this specification and their contributions are gratefully acknowledged:

**CSAF TC Members:**

| First Name | Last Name | Company |
| :--- | :--- | :--- |
Adam | Montville | CIS                                          
Allan | Thomson | LookingGlass                            
Anthony | Berglas | Cryptsoft Pty Ltd.                    
Art | Manion | Carnegie Mellon University              
Aukjan | van Belkum | EclecticIQ                           
Ben | Sooter | Electric Power Research Institute     
Bernd | Grobauer | Siemens AG                             
Beth | Pumo | Kaiser Permanente                          
Bret | Jordan | Symantec Corp.                             
Bruce | Rich | Cryptsoft Pty Ltd.                            
Chet | Ensign | OASIS                                          
Chok | Poh | Oracle                                              
Chris | Rouland | Individual
David | Waltermire | NIST
Denny | Page | TIBCO Software Inc.
Doron | Shiloach | IBM
Duncan | Sparrell | sFractal Consulting LLC
Eric | Johnson | TIBCO Software Inc.
Feng | Cao | Oracle
Greg | Reaume | TELUS
Greg | Scott | Cryptsoft Pty Ltd.
Harold | Booth | NIST
Jamison | Day | LookingGlass
Jared | Semrau | "FireEye, Inc."
Jason | Masters | TELUS
Jerome | Athias | Individual
Jessica | Fitzgerald-McKay | National Security Agency
Jonathan | Bitle | Kaiser Permanente
Justin | Corlett | Cryptsoft Pty Ltd.
Karen | Scarfone | Individual
Kazuo | Noguchi | "Hitachi, Ltd."
Kent | Landfield | McAfee
Lothar | Braun | Siemens AG
Louis | Ronnau | Cisco Systems
Mark | Davidson | NC4
Mark-David | McLaughlin | Cisco Systems
Masato | Terada | "Hitachi, Ltd."
Masood | Nasir | TELUS
Nicole | Gong | Mitre Corporation
Omar | Santos | Cisco Systems
Patrick | Maroney | Wapack Labs LLC
Paul | Patrick | "FireEye, Inc."
Peter | Allor | IBM
Phillip | Boles | "FireEye, Inc."
Ravi | Balupari | Netskope
Rich | Reybok | ServiceNow
Richard | Struse | DHS Office of Cybersecurity and Communications (CS&C)
Ritwik | Ghoshal | Oracle
Robert | Coderre | VeriSign
Robin | Cover | OASIS
Rupert | Wimmer | Siemens AG
Sanjiv | Kalkar | Individual
Sean | Barnum | Mitre Corporation
Stefan | Hagen | Individual
Ted | Bedwell | Cisco Systems
Thomas | Schreck | Siemens AG
Tim | Hudson | Cryptsoft Pty Ltd.
Tony | Cox | Cryptsoft Pty Ltd.
Trey | Darley | "Kingfisher Operations, sprl"
Troy | Fridley | Cisco Systems
Vincent | Danen | Red Hat
Zach | Turk | Microsoft

-------

# Appendix B. Revision History
| Revision | Date | Editor | Changes Made |
| :--- | :--- | :--- | :--- |
| csaf-v2.0-wd20200929 | 2020-09-29 | Stefan Hagen | Initial working draft |
