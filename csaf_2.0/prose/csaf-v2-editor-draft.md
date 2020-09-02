
![OASIS Logo](http://docs.oasis-open.org/templates/OASISLogo-v2.0.jpg)
-------

# CSAF Common Vulnerability Reporting Framework Version 2.0

## Committee Specification Draft 01 /<br>Public Review Draft 01

## 00 Month 2020

#### Technical Committee:
[OASIS Common Security Advisory Framework (CSAF) TC](https://www.oasis-open.org/committees/csaf/)

#### Chair:
Omar Santos (osantos@cisco.com), [Cisco](https://cisco.com/)

#### Editors:
Langley Rock (lrock@redhat.com), [Red Hat](https://redhat.com/) \
Stefan Hagen (stefan@hagen.link), [Individual](https://stefan-hagen.website/)

#### Additional artifacts:
This prose specification is one component of a Work Product that also includes:
* JSON schema: csaf.json
* Other parts (list titles and/or file names)
* `(Note: Any normative computer language definitions that are part of the Work Product, such as XML instances, schemas and Java(TM) code, including fragments of such, must be (a) well formed and valid, (b) provided in separate plain text files, (c) referenced from the Work Product; and (d) where any definition in these separate files disagrees with the definition found in the specification, the definition in the separate file prevails. Remove this note before submitting for publication.)`

#### Related work:
This specification replaces or supersedes:
* The Common Vulnerability Reporting Framework (CVRF) Version 1.2., http://docs.oasis-open.org/csaf/csaf-cvrf/v1.2/csprd01/csaf-cvrf-v1.2-csprd01.html

This specification is related to:
* Related specifications (include hyperlink, preferably to HTML format) \
`(remove "Related work" section or the "replaces" or "related" subsections if no entries)`

#### Abstract:
The CSAF Common Security Advisory Framework (CSAF) Version 2.0 is the definitive reference for the  language which supports creation, update, and interoperable exchange of security advisories as structured information on products, vulnerabilities and the status of impact and remediation among interested parties.

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

**[short-title-v1.0]**

_Specification Title Version 1.0_. Edited by Dany Page and Stefan Hagen. 00 Month 2020. OASIS Committee Specification Draft 01 / Public Review Draft 01. this-version.html. Latest version: latest-version.html.

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

Here is a customized command line which will generate HTML from this markdown file (named openc2-file.md):

pandoc -f gfm -t html openc2-file.md -c styles/markdown-styles-v1.7.3.css --toc --toc-depth=5 -s -o openc2-file.html --metadata title="Title of Specification Version 1.0"

OASIS staff are currently using pandoc 2.6 from https://github.com/jgm/pandoc/releases/tag/2.6.

This also requires the presence of a .css file containing the HTML styles (like styles/markdown-styles-v1.7.3.css).

Note this command generates a Table of Contents (TOC) in HTML which is located at the top of the HTML document, and which requires additional editing in order to be published in the expected OASIS style. This editing will be handled by OASIS staff during publication.
A TC may use other ways to generate HTML from markdown, which may generate a TOC in a different way.

## 1.1 IPR Policy
This specification is provided under the [Non-Assertion](https://www.oasis-open.org/policies-guidelines/ipr#Non-Assertion-Mode) Mode of the [OASIS IPR Policy](https://www.oasis-open.org/policies-guidelines/ipr), the mode chosen when the Technical Committee was established. For information on whether any patents have been disclosed that may be essential to implementing this specification, and any offers of patent licensing terms, please refer to the Intellectual Property Rights section of the TC's web page ([https://www.oasis-open.org/committees/openc2/ipr.php](https://www.oasis-open.org/committees/openc2/ipr.php)).

## 1.2 Terminology
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 [[RFC2119](#rfc2119)] and [[RFC8174](#rfc8174)] when, and only when, they appear in all capitals, as shown here.

## 1.3 Normative References

(Reference sources:
For references to IETF RFCs, use the approved citation formats at:  
http://docs.oasis-open.org/templates/ietf-rfc-list/ietf-rfc-list.html.  
For references to W3C Recommendations, use the approved citation formats at:  
http://docs.oasis-open.org/templates/w3c-recommendations-list/w3c-recommendations-list.html.  
Remove this note before submitting for publication.)

###### [OpenC2-HTTPS-v1.0]
_Specification for Transfer of OpenC2 Messages via HTTPS Version 1.0_. Edited by David Lemire. Latest version: http://docs.oasis-open.org/openc2/open-impl-https/v1.0/open-impl-https-v1.0.html
###### [OpenC2-SLPF-v1.0]
_Open Command and Control (OpenC2) Profile for Stateless Packet Filtering Version 1.0_. Edited by Joe Brule, Duncan Sparrell, and Alex Everett. Latest version: http://docs.oasis-open.org/openc2/oc2slpf/v1.0/oc2slpf-v1.0.html
###### [RFC2119]
Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, DOI 10.17487/RFC2119, March 1997, http://www.rfc-editor.org/info/rfc2119.
###### [RFC8174]
Leiba, B., "Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words", BCP 14, RFC 8174, DOI 10.17487/RFC8174, May 2017, http://www.rfc-editor.org/info/rfc8174.

## 1.4 Non-Normative References

###### [RFC3552]
Rescorla, E. and B. Korver, "Guidelines for Writing RFC Text on Security Considerations", BCP 72, RFC 3552, DOI 10.17487/RFC3552, July 2003, https://www.rfc-editor.org/info/rfc3552.

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

## 1.6 Some markdown usage examples

**Text.**

Note that text paragraphs in markdown should be separated by a blank line between them -

Otherwise the separate paragraphs will be joined together when the HTML is generated.
Even if the text appears to be separate lines in the markdown source.

To avoid having the usual vertical space between paragraphs,  
append two or more space characters (or space-backslash) to the end of the lines  
which will generate an HTML break tag instead of a new paragraph tag \
(as demonstrated here).

### 1.6.1 Figures and Captions

FIGURE EXAMPLE:
<note caption is best placed ABOVE figure, so a hyperlink to it will actually display the figure, instead of rendering the figure off the screen above the caption. The same placement should be used for table captions>

###### Figure 1 -- Title of Figure
![image-label should be meaningful](images/image_0.png) (this image is missing)

###### Figure 2 -- OpenC2 Message Exchange
![message exchange](images/image_1.png)


### 1.6.2 Tables

#### 1.6.2.1 Basic Table
**Table 1-1. Table Label**

| Item | Description |
| :--- | :--- |
| Item 1 | Something<br>(second line) |
| Item 2 | Something |
| Item 3 | Something<br>(second line) |
| Item 4 | text |

#### 1.6.2.2 Table with Three Columns and Some Bold Text
text.

| Title 1 | Title 2 | title 3 |
| :--- | :--- | :--- |
| something | something | something else that is a long string of text that **might** need to wrap around inside the table box and will just continue until the column divider is reached |
| something | something | something |

#### 1.6.2.3 Table with a caption which can be referenced

###### Table 1-5. See reference label construction

| Name | Description |
| :--- | :--- |
| **content** | Message body as specified by content_type and msg_type. |

Here is a reference to the table caption:
Please see [Table 1-5 or other meaningful label](#table-1-5-see-reference-label-construction) 


### 1.6.3 Lists

Bulleted list:
* bullet item 1.
* **Bold** bullet item 2.
* bullet item 3.
* bullet item 4.

Indented or multi-level bullet list - add two spaces per level before bullet character (* or -):
* main bullet type
  * Example second bullet
    * See third level
      * fourth level

Numbered list:
1. item 1
2. item 2
3. item 3

Left-justified list without bullets or numbers:
To list multiple items without full paragraph breaks between items, add space-backslash after each item except the last.

### 1.6.4 Reference Label Construction

REFERENCES and ANCHORS
- in markdown source, format the Reference tags as level 6 headings like: `###### [RFC2119]`
###### [RFC2119]
Bradner, S., "Key words ..."

- reference text has to be on a separate line below the tag

- format cross-references (citations of the references) like: `see [[RFC2119](#rfc2119)]`  
"see [[RFC2119](#rfc2119)]"  
(note the outer square brackets in markdown will appear in the visible HTML text)

- The text in the Reference tag (following ###### ) will become an HTML anchor using the following conversion rules:  
-- punctuation marks will be dropped (including "[" )  
-- leading white spaces will be dropped  
-- upper case will be converted to lower  
-- spaces between letters will be converted to a single hyphen

- The same HTML anchor construction rules apply to cross-references and to section headings.  
-- Thus, a section heading like "## 1.3 Normative References"  
-- becomes an anchor in HTML like `<a href="#13-normative-references">`  
-- referenced in the markdown like: see [Section 1.3](#13-normative-references)  
-- (in markdown: `"see [Section 1.3](#13-normative-references"`)  
-- similar HTML anchors are also used in constructing the TOC

### 1.6.5 Code Blocks

Text to appear as an indented code block with grey background and monospace font - use three back-ticks before and after the code block).

Note the actual backticks will not appear in the HTML format. If it's necessary to display visible backticks, place a back-slash before them like: \``` .

```
{   
    "target": {
        "x_kmip_2.0": {
            {"kmip_type": "json"},
            {"operation": "RekeyKeyPair"},
            {"name": "publicWebKey11DEC2017"}
        }
    }
}
```

Text to be highlighted as code can also be surrounded by a single "backtick" character: 
`code text`

## 1.7 Page Breaks
Add horizontal rule lines where page breaks are desired in the PDF - before each major section
- insert the line rules in markdown by inserting 3 or more hyphens on a line by themselves:  ---
- place these before each main section in markdown (usually "#" - which generates the HTML `<h1>` tag)

-------

# 2 Design Considerations
The Common Security Advisory Framework (CSAF) is a language to exchange Security Advisories formulated in JSON.

Non-normative comment:

>The term Security Advisory as used in this document describes any notification of security issues in products of and by providers. Anyone providing a product is considered in this document as a vendor, i.e. developers or maintainers of information system products or services. This includes all authoritative product vendors, Product Security Incident Response Teams (PSIRTs), and product resellers and distributors, including authoritative vendor partners.
A security issue is not necessarily constraint to a problem statement, the focus of the term is on the security aspect impacting (or not impacting) specific product-platform-version combinations. Information on presence or absence of work-arounds is also considered part of the security issue.
This document is the definitive reference for the language elements of CSAF version 2.0. The encompassing JSON schema file noted in the Additional Artifacts section of the title page shall be taken as normative in the case a gap or an inconsistency in this explanatory document becomes evident.
The following presentation in this section is grouped by topical area, and is not simply derivative documentation from the schema document itself. The information contained aims to be more descriptive and complete. Where applicable, common conventions are stated and known common issues in usage are pointed out informatively to support implementers of document producers and consumers alike. The section SCHEMA_SECTION_NUMBER Schema derives from the JSON schema itself as a service for the reader.

« From a high-level perspective, any Security Advisory purported by a CSAF version 2.0 adhering JSON text document MUST provide the document member with at least the following five properties defined: `csaf_version`, `title`, `publisher`, `type`, and `tracking`. » [CSAF-2-1]

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
  * Common Vulnerability Scoring System (CVSS) Version 3.1 [CVSS3_1]
    * JSON Schema Reference https://www.first.org/cvss/cvss-v3.1.json
  * Common Vulnerability Scoring System (CVSS) Version 3.0 [CVSS3]
    * JSON Schema Reference https://www.first.org/cvss/cvss-v3.0.json
  * Common Vulnerability Scoring System (CVSS) Version 2.0 [CVSS2][1]
    * JSON Schema Reference https://www.first.org/cvss/cvss-v2.0.json
* Classfication for Document Distribution
  * Traffic Light Protocol (TLP)
    * Default Definition: https://www.first.org/tlp/ 

### 2.1.1 Level 3 Heading
text.

#### 2.1.1.1 Level 4 Heading
text.

##### 2.1.1.1.1 Level 5 Heading
This is the deepest level, because six # gets transformed into a Reference tag.


## 2.2 Next Heading
text.

-------

# 3 Safety, Security, and Data Protection Considerations
(Note: OASIS strongly recommends that Technical Committees consider issues that might affect safety, security, privacy, and/or data protection in implementations of their specification and document them for implementers and adopters. For some purposes, you may find it required, e.g. if you apply for IANA registration.

While it may not be immediately obvious how your specification might make systems vulnerable to attack, most specifications, because they involve communications between systems, message formats, or system settings, open potential channels for exploit. For example, IETF [[RFC3552](#rfc3552)] lists “eavesdropping, replay, message insertion, deletion, modification, and man-in-the-middle” as well as potential denial of service attacks as threats that must be considered and, if appropriate, addressed in IETF RFCs.

In addition to considering and describing foreseeable risks, this section should include guidance on how implementers and adopters can protect against these risks.

We encourage editors and TC members concerned with this subject to read _Guidelines for Writing RFC Text on Security Considerations_, IETF [[RFC3552](#rfc3552)], for more information.

Remove this note before submitting for publication.)

-------

# 4 Conformance
(Note: The [OASIS TC Process](https://www.oasis-open.org/policies-guidelines/tc-process#wpComponentsConfClause) requires that a specification approved by the TC at the Committee Specification Public Review Draft, Committee Specification or OASIS Standard level must include a separate section, listing a set of numbered conformance clauses, to which any implementation of the specification must adhere in order to claim conformance to the specification (or any optional portion thereof). This is done by listing the conformance clauses here.
For the definition of "conformance clause," see [OASIS Defined Terms](https://www.oasis-open.org/policies-guidelines/oasis-defined-terms-2017-05-26#dConformanceClause).

See "Guidelines to Writing Conformance Clauses":  
http://docs.oasis-open.org/templates/TCHandbook/ConformanceGuidelines.html.

Remove this note before submitting for publication.)


-------

# 5 Schema Elements

The CSAF schema describes how to represent security advisory information as a JSON document.

The CSAF schema Version 2.0 builds on the JSON Schema draft 07 rules.

    "$schema": "http://json-schema.org/draft-07/schema#"

The schema identifier is (before publication):

    "$id": "https://raw.githubusercontent.com/oasis-tcs/csaf/master/csaf_2.0/json_schema/csaf_json_schema.json"

The further documentation of the schema is organized via Definitions and Properties. 

* Definitions provide types that extend the JSON schema model 
* Properties use these types to support assembling security advisories

Types and properties together provide the vocabulary for the domain specific language supporting security advisories. 

The single mandatory property is the document. The optional two additional properties are product_tree and vulnerabilities.

## Definitions

### Acknowledgment Type

Acknowledgement (`acknowledgment_t`) type instances acknowledge contributions by describing those that contributed. The value type is object with 1 to 4 properties. The properties are: names, organizations, description, and urls.

    "acknowledgment_t": {
      "type": "object",
      "minProperties": 1,
      "properties": {
        "names": {
          // ...
        },
        "organizations": {
          // ...
        },
        "description": {
          // ...
        },
        "urls": {
          // ...
        }
      }
    },

#### Acknowledgment Type - Names

Names of entities being recognized is typically the name of a person belonging to an organization. Value type is string with 1 or more characters.

Examples:

    Johann Sebastian Bach
    Albert Einstein

#### Acknowledgment Type - Organizations

List of contributing organizations. The list of contributing organizations. Value type is string with 1 or more characters.

Examples:

    US-CERT
    Talos
    Google Project Zero

#### Acknowledgment Type - Description

Description of the acknowledgment SHOULD represent any contextual details the document producers wish to make known about the acknowledgment or acknowledged parties. Value type is string with 1 or more characters.

Example:

    First analysis of Coordinated Multi-Stream Attack (CMSA)

#### Acknowledgment Type - URLs

URL of acknowledgment contains the URL or location of the reference to be acknowledged. Value type is string with format URI.

### Branch Type

Branch is a part of the hierarchical structure of the product tree. Value type is object with 3 Properties. The properties name and type are mandatory. In addition the object contains either a branches or a product. 

    "branch_branches_t": {
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
    },

#### Branch Type - Name

Name of the branch contains the canonical descriptor or 'friendly name' of the branch. Value type string with 1 character or more.

Examples:

    Microsoft
    Siemens
    Windows
    Office
    SIMATIC
    10
    365
    PCS 7

#### Branch Type - Type

Type of the branch describes the characteristics of the labeled branch. Value type is string enum. Valid values are:

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

#### Branch Type - Branches

Branches have the value type array with 1 or more items of the Branch type (`branch_branches_t`). 

#### Branch Type - Product

Product has the value type Full Product Name (`full_product_name_t`).

### Full Product Name Type

Full Product Name (`full_product_name_t`) has value type object with 3 properties. The properties product_id and name are mandatory. In addition the object may contain a CPE identifier as value of the cpe property.

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

#### Full Product Name Type - Product ID

Product ID has the value type Product ID (product_id_t).

#### Full Product Name Type - Name

Textual description of the product. The value of a Full Product Name element should be the product’s full canonical name, including version number and other attributes, as it would be used in a human-friendly document. Value type is string with 1 or more characters.

Examples:

    Microsoft Host Integration Server 2006 Service Pack 1
    Cisco AnyConnect Secure Mobility Client 2.3.185

#### Full Product Name Type - CPE

Common Platform Enumeration representation. The Common Platform Enumeration (CPE) attribute refers to a method for naming platforms external to this specification. Value type is string with 1 or more characters matching the regular expression pattern:

    ^(?i)cpe:(/|\\d+\\.\\d+)[^:]*:?[^:]*:?[^:]*:?[^:]*:?[^:]*:?[^:]*:?[^:]*$

### Language Type

Language type identifies a language, corresponding to IETF BCP 47 / RFC 5646. 

See IETF language registry: [https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry)

Value type is string with 2 or 3 characters matching the regular expression pattern:

    ^[a-zA-Z]{2,3}(-.+)?$

Examples:

    de
    en
    fr
    frc
    jp

### Notes Type

Notes type (`notes_t`) is array with 1 or more items of type Note. Value type of every such Note item is object with the mandatory properties type and text. A note may provide the additional properties audience and title.

    "notes_t": {
      // ..
      "items": {
        // ...
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
        },
        // ...
      }
    },

#### Notes Type - Note

Note is a place to put all manner of text blobs related to the current context. Value type is object with the 2 mandatory properties type and text as well as the 2 optional properties audience and title. 

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
    },

##### Notes Type - Note - Audience

Audience of note indicates who is intended to read it. Value type is string with 1 or more characters.

Examples:

    all
    executives
    operational management and system administrators
    safety engineers

##### Notes Type - Note - Title

Title of note provides a concise description of what is contained in the text of the note. Value type is string with 1 or more characters.

Examples:

    Details
    Executive summary
    Technical summary
    Impact on safety systems

##### Notes Type - Note - Type

Note type. Choice of what kind of note this is. Value type is string enum. Valid values are:

    description
    details
    faq
    general
    legal_disclaimer
    other
    summary

##### Notes Type - Note - Text

Note contents are the contents of the note. Content varies depending on type. Value type is string with 1 or more characters.

### Products Type

List of Product IDs (`product_ids`) specifies a list of `product_ids` to give context to the parent item. Value type is array with 1 or more unque items (set) of type Product ID (`product_id_t`)

### Product Groups Type

List of Product Group ID (`product_group_ids`) specifies a list of `product_group_ids` to give context to the parent item. Value type is array with 1 or more unque items (set) of type Product Group ID (`product_group_id_t`)

### Product Group ID Type

The Product Group ID Type (`product_group_id_t`) is a reference token for product group instances. Token required to identify a group of products so that it can be referred to from other parts in the document. There is no predefined or required format for the Product Group ID (`product_group_id`) as long as it uniquely identifies a group in the context of the current document. Value type is string with 1 or more characters.

Examples:

    CSAFGID-0001
    CSAFGID-0002
    CSAFGID-0020

### Product ID Type

The Product ID Type (`product_id_t`) is a reference token for product instances. Token required to identify a `full_product_name` so that it can be referred to from other parts in the document. There is no predefined or required format for the Product Group ID (`product_id`) as long as it uniquely identifies a product in the context of the current document. Value type is string with 1 or more characters.

Examples:

    CVRFPID-0004
    CVRFPID-0008

### References Type

The References (`references_t`) type provides a list of Reference objects. Value type is array with 1 or more items. 

    "references_t": {
      // ...
      "items": {
        // ...
        "properties": {
          "description": {
            // ...
          },
          "type": {
            // ...
          },
          "url": {
            // ...
          }
        },
      }
    },

Any such item is a Reference that holds any reference to conferences, papers, advisories, and other resources that are related and considered related to either a surrounding part of or the entire document and to be of value to the document consumer. Value type is object with the 2 mandatory properties `url` and `description`. A third optional property `type` is available.

The Description of reference (`description`) provides an anwser to the question: "What does this reference refer to?" and is of type string with 1 or more characters.

The Type of reference (`type`) indicates whether the reference points to the same document or vulnerability in focus (depending on scope) or to an external resource. Value type is string with a fixed value set (enum). The value set of the `type` enum is:

    self
    external

The default value for `type` is:

    external

The URL of reference (`url`) provides the URL for the reference. Value type is string with format `uri`.

### Version Type

The Version (`version_t`) type specifies a version string with a simple hierarchical counter model to denote clearly the evolution of the content of the document. Format must be understood as 'major.minor.patch.build' version. Value type is string matching the regular expression pattern:

    ^(0|[1-9][0-9]*)(\\.(0|[1-9][0-9]*)){0,3}$


Examples:

    1
    0.9
    1.4.3
    2.40.0.320002

## Properties

### Document Property

Document level meta-data captures the meta-data about this document describing a particular set of security advisories. Value type is object with the 5 mandatory properties csaf_version, title, publisher, type, and tracking. 
In addition, the document object may provide the 7 optional properties acknowledgments, aggregate_severity, distribution, lang, source_lang, notes, and references. 

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

#### Document Property - Acknowledgements

    "acknowledgments": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/definitions/acknowledgment_t"
      }
    },

#### Document Property - Aggregate Severity

Aggregate severity is a vehicle that is provided by the document producer to convey the urgency and criticality with which the one or more vulnerabilities reported should be addressed. It is a document-level metric and applied to the document as a whole — not any specific vulnerability. The range of values in this field is defined according to the document producer's policies and procedures. Value type is object with 1 required property `text` and the optional property `namespace`.

    "aggregate_severity" : {
      // ...
      "properties": {
        "namespace": {
          // ...
        },
        "text": {
          // ...
        }
      },
    },

The Namespace of aggregate severity (`namespace`) points to the namespace so referenced. Value type is string with format `uri`.

The Text of aggregate severity (`text`) provides a severity which is independent of - and in addition to - any other standard metric for determining the impact or severity of a given vulnerability (such as CVSS). Value type is string with 1 or more characters.

Examples:

    Moderate
    Important
    Critical

#### Document Property - CSAF Version

CSAF version gives the version of the CSAF specification which the document was generated for. Value type is string enum. For this edition of the specification the single valid value is:

    2.0

#### Document Property - Distribution

Rules for sharing document describe any constraints on how this document might be shared. Value type is object with 1 or more properties.

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

##### Document Property - Distribution - Text

The Text member (`text`) value represents a description that provides a textual description of additional constraints. Value type is string with 1 or more characters.

Examples:

    Share only on a need-to-know-basis only.
    Distribute freely.
    Copyright 2019, Example Company, All Rights Reserved.

##### Document Property - Distribution - TLP

Traffic Light Protocol (TLP) (`tlp`) type provides details about the TLP classification of the document. Value type is object with the required property `label` and the optional property `url`.

The Label of TLP (`label`) provides the TLP label of the document. Value type is string with value from the set (enum):

    RED
    AMBER
    GREEN
    WHITE

The URL of TLP version (`url`) provides a URL where to find the textual description of the TLP version which is useed in this document. Value type is string with format `uri`. Default value is the URL to the definition by FIRST. The default value is:

    https://www.first.org/tlp/

Examples:

    https://www.us-cert.gov/tlp
    https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Kritis/Merkblatt_TLP.pdf

#### Document Property - Language

Document language identifies the language used by this document, corresponding to IETF BCP 47 / RFC 5646. Value type is the Language Type (lang_t).

#### Document Property - Source Language

Original translation. If this copy of the document is a translation, from which language was this document translated? Value type is the Language Type (lang_t).

#### Document Property - Notes

Notes associated with the whole document. Notes about this set of vulnerabilities should be added here. Value type is the Notes Type (notes_t).

#### Document Property - Publisher

Publisher (`publisher`) has value type object and provides information on the publishing entity. The single required property is `type`. The 3 other optional properties are: `contact_details`, `issuing_authority`, and `vendor_id`.

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

##### Document Property - Publisher - Contact Details

How to contact (`contact_details`)? Information on how to contact the publisher, possibly including details such as web sites, email addresses, phone numbers, and postal mail addresses. Value type is string with 1 or more characters.

Example:

    Example Company can be reached at contact_us@example.com, or via our website at https://www.example.com/contact.

##### Document Property - Publisher - Issuing Authority

What authority (`issuing_authority`)? The name of the issuing party and their authority to release the document, in particular, the party's constituency and responsibilities or other obligations. Value type is string with 1 or more characters.

##### Document Property - Publisher - Type

The Type of publisher (`type`) provides information about the type of publisher releasing the document. Value type is string with fixed value set (enum). Thes values are:

    coordinator
    discoverer
    other
    user
    vendor

##### Document Property - Publisher - Vendor ID

The Vendor releasing the document (`vendor_id`). The Vendor ID is a unique identifier (OID) that a vendor uses as issued by FIRST under the auspices of IETF. Value type is string with 1 or more characters.

#### Document Property - References

    "references": {
      "$ref": "#/definitions/references_t"
    },

#### Document Property - Title

Title of this document SHOULD be a canonical name for the document, and sufficiently unique to distinguish it from similar documents. Value type is string with 1 or more characters.

Examples:

    Example Company Cross-Site-Scripting Vulnerability in Example Generator
    Cisco IPv6 Crafted Packet Denial of Service Vulnerability

#### Document Property - Tracking

Tracking (`tracking`) provides attributes for tracking the evolution of the security advisory revisions. Value type is object with the six mandatory properties: `current_release_date`, `id`, `initial_release_date`, `revision_history`, `status`, and `version`. The two optional additional properties are `aliases` and `generator`.

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


##### Document Property - Tracking - ID

Unique identifier for the document. The ID is a simple label that provides for a wide range of numbering values, types, and schemes. Its value SHOULD be assigned and maintained by the original document issuing authority. Value type is string with 1 or more characters.

Examples:

    Example Company - 2019-YH3234
    RHBA-2019:0024
    cisco-sa-20190513-secureboot

##### Document Property - Tracking - Aliases

    "aliases": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "string",
        "title": "Alternate name",
        "description": "Alternate names for the same vulnerability.",
        "examples": [
          "CVE-2019-12345"
        ],
        "minLength": 1
      }
    },


##### Document Property - Tracking - Current Release Date

Current release date is the date of the current revision of this document was released. Value type is string of format date-time.


##### Document Property - Tracking - Generator

The Generator (`generator`) describes the engine technically creating the security advisory. Value type is object with 1 or 2 properties. The properties are `engine` and `date`.

        "generator": {
          "type": "object",
          "minProperties": 1,
          "properties": {
            "engine": {
              "type": "string",
              "minLength": 1
            },
            "date": {
              "type": "string",
              "format": "date-time"
            }
          }
        },

Engine (`engine`) is of type string with 1 or more characters.

Date (`date`) is of type string with format `date-time`.

##### Document Property - Tracking - Initial Release Date

Initial release date is the date that this document was first published. Value type is string of format date-time.

##### Document Property - Tracking - Revision History

The Revision History (`revision_history`) provides a list of information items on revisions of the security advisory. The value type is array of with 1 or more items. The items are of type object with the three mandatory properties: `number`, `date`, and `description`. 

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
              "description": {
                // ...
              }
            },
          }
        },

The `number` is of value type Version (`version_t`). 

The Date of the revision (`date`) states the date of the revision entry. Value type is strng with format `date-time`.

The Description (`description`) is of type string with 1 or more characters.

##### Document Property - Tracking - Status

Document status (`status`) defines the draft status of the document. Value type is string with fixed value set (enum). The value MUST be one of the following:

    draft
    final
    interim

##### Document Property - Tracking - Version

Version has the value type Version (`version_t`).

#### Document Property - Type

    "type": {
      "type": "string",
      "minLength": 1
    }

### Product Tree Property

Product Tree has value type object with 1 or more properties. The properties are branches, full_product_names, product_groups, and relationships.

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

#### Product Tree Property - Product Tree

    "product_tree": {
      "$comment": "Currently only supports branch_t and full_product_name_t children of product_tree",
      "type": "object",
      "minProperties": 1,
      "properties": {

#### Product Tree Property - Branches

        "branches": {
          "type": "array",
          "minItems": 1,
          "items": {
            "$ref": "#/definitions/branch_branches_t"
          }
        },

#### Product Tree Property - Full Product Names

        "full_product_names": {
          "type": "array",
          "minItems": 1,
          "items": {
            "$ref": "#/definitions/full_product_name_t"
          }
        },

#### Product Tree Property - Product Groups

        "product_groups": {
          "type": "array",
          "minItems": 1,
          "items": {
            "title": "Product group",
            "description": "Defines a new logical group of products that can then be referred to in other parts of the document to address a group of products with a single identifier.",
            "type": "object",
            "required": [
              "group_id",
              "product_ids"
            ],
            "properties": {
              "description": {
                "title": "Description of the product group",
                "description": "Gives a short, optional description of the group.",
                "examples": [
                  "The x64 versions of the operating system.",
                  "Products supporting Modbus."
                ],
                "type": "string",
                "minLength": 1
              },
              "group_id": {
                "$ref": "#/definitions/product_group_id_t"
              },
              "product_ids": {
                "title": "List of product_ids",
                "description": "Lists the product_ids of those products which known as one group in the document.",
                "type": "array",
                "minItems": 2,
                "items": {
                  "$ref": "#/definitions/product_id_t"
                }
              }
            }
          }
        },

#### Product Tree Property - Relationships

        "relationships": {
          "type": "array",
          "minItems": 1,
          "items": {
            "title": "Relationship",
            "description": "Establishes a link between two existing full_product_name_t elements, allowing the document producer to define a combination of two products that form a new full_product_name entry.",
            "type": "object",
            "properties": {
              "full_product_names": {
                "type": "array",
                "minItems": 1,
                "items": {
                  "$ref": "#/definitions/full_product_name_t"
                }
              },
              "product_reference": {
                "$ref": "#/definitions/product_id_t"
              },
              "relates_to_product_reference": {
                "$ref": "#/definitions/product_id_t"
              },
              "relationship_type": {
                "title": "Relationship type",
                "description": "Defines the type of relationship for the referenced component.",
                "type": "string",
                "enum": [
                  "default_component_of",
                  "optional_component_of",
                  "external_component_of",
                  "installed_on",
                  "installed_with"
                ]
              }
            },
            "required": [
              "product_reference",
              "relates_to_product_reference",
              "relationship_type"
            ]
          }
        }
      }
    },


### Vulnerabilities Property

Vulnerabilities represents a list of all relevant vulnerability information items. Value type is array with 1 or more objects representing vulnerabilities and providing 1 or more properties.

    "vulnerabilities": {
      "items": {
        // ...
      }
    }

#### Vulnerabilities Property - Vulnerability

Vulnerability is a container for the aggregation of all fields that are related to a single vulnerability in the document. Value type is object with 1 or more properties. Any vulnerability may provide the optional properties acknowledgments, cve, cwe, scores, discovery_date, id, involvements, notes, product_status, references, release_date, remediations, and title. 

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

##### Vulnerabilities Property - Vulnerability - Acknowledgments

Acknowledgments have value type array with 1 or more items of type Acknowledgement (acknowledgement_t).

##### Vulnerabilities Property - Vulnerability - CVE

CVE has value type string matching the regular expression pattern:

    ^CVE-[0-9]{4}-[0-9]{4,}$

##### Vulnerabilities Property - Vulnerability - CWE

    "cwe": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string",
          "pattern": "^CWE-[1-9]\\d{0,5}$"
        },
        "description": {
          "type": "string",
          "minLength": 1
        }
      }
    },

##### Vulnerabilities Property - Vulnerability - Scores

    "scores": {
      "type": "array",
      "minItems": 1,
      "items": [
        {
          "anyOf": [
            {
              "type": "array",
              "minItems": 0,
              "items": {
                "$ref": "#/definitions/products_t",
                "examples": [
                  "CVRFID_123",
                  "CSAFID_0815"
                ],
                "default": ""
              }
            },
            {
              "type": "object",
              "properties": {
                "cvss_v20": {
                  "$ref": "https://www.first.org/cvss/cvss-v2.0.json"
                }
              }
            },
            {
              "type": "object",
              "properties": {
                "cvss_v30": {
                  "$ref": "https://www.first.org/cvss/cvss-v3.0.json"
                }
              }
            },
            {
              "type": "object",
              "properties": {
                "cvss_v31": {
                  "$ref": "https://www.first.org/cvss/cvss-v3.1.json"
                }
              }
            }
          ]
        }
      ]
    },

##### Vulnerabilities Property - Vulnerability - Discovery Date

Discovery Date has value type string with format date-time.

##### Vulnerabilities Property - Vulnerability - ID

    "id": {
      "type": "object",
      "properties": {
        "system_name": {
          "title": "System name",
          "description": "Indicates the name of the vulnerability tracking or numbering system.",
          "type": "string",
          "minLength": 1
        },
        "text": {
          "type": "string",
          "minLength": 1
        }
      },
      "required": [
        "system_name",
        "text"
      ]
    },

##### Vulnerabilities Property - Vulnerability - Involvements

    "involvements": {
      "type": "array",
      "minItems": 1,
      "items": {
        "title": "Involvement",
        "description": "Is a container, that allows the document producers to comment on their level of Involvement (or engagement) in the vulnerability identification, scoping, and remediation process.",
        "type": "object",
        "required": [
          "party",
          "status"
        ],
        "properties": {
          "description": {
            "type": "string",
            "minLength": 1
          },
          "party": {
            "title": "Party type",
            "description": "Defines the type of the involved party.",
            "type": "string",
            "enum": [
              "coordinator",
              "discoverer",
              "other",
              "user",
              "vendor"
            ]
          },
          "status": {
            "title": "Party status",
            "description": "Defines contact status of the involved party.",
            "type": "string",
            "enum": [
              "completed",
              "contact_accepted",
              "disputed",
              "in_progress",
              "not_contacted",
              "open"
            ]
          }
        }
      }
    },

##### Vulnerabilities Property - Vulnerability - Notes

Notes have value type Notes (notes_t).

##### Vulnerabilities Property - Vulnerability - Product Status

Product status contains different lists of product_ids which provide details on the status of the referenced product related to the current vulnerability. Value type object with 1 or more properties.

    "product_status": {
      "title": "Product status",
      "description": "Contains different lists of product_ids which provide details on the status of the referenced product related to the current vulnerability. ",
      "type": "object",
      "minProperties": 1,
      "properties": {
        "fixed": {
          "title": "Fixed",
          "description": "These versions contain a fix for the vulnerability but may not be the recommended fixed versions.",
          "$ref": "#/definitions/products_t"
        },
        "first_fixed": {
          "title": "First fixed",
          "description": "These versions contain the first fix for the vulnerability but may not be the recommended fixed versions.",
          "$ref": "#/definitions/products_t"
        },
        "recommended": {
          "title": "Recommended",
          "description": "These versions have a fix for the vulnerability and are the vendor-recommended versions for fixing the vulnerability.",
          "$ref": "#/definitions/products_t"
        },
        "known_affected": {
          "title": "Known affected",
          "description": "These versions are known to be affected by the vulnerability.",
          "$ref": "#/definitions/products_t"
        },
        "first_affected": {
          "title": "First affected",
          "description": "These are the first versions of the releases known to be affected by the vulnerability.",
          "$ref": "#/definitions/products_t"
        },
        "last_affected": {
          "title": "Last affected",
          "description": "These are the last versions in a release train known to be affected by the vulnerability. Subsequently released versions would contain a fix for the vulnerability.",
          "$ref": "#/definitions/products_t"
        },
        "known_not_affected": {
          "title": "Known not affected",
          "description": "These versions are known not to be affected by the vulnerability.",
          "$ref": "#/definitions/products_t"
        },
        "under_investigation": {
          "title": "Under investigation",
          "description": "It is not known yet whether this version is or is not affected by the vulnerability. However, it is still under investigation - the result will be provided in a later release of the document.",
          "$ref": "#/definitions/products_t"
        }
      }
    },

##### Vulnerabilities Property - Vulnerability - References

References have value type References (references_t).

##### Vulnerabilities Property - Vulnerability - Release Date

Release Date has value type string of format date-time.

##### Vulnerabilities Property - Vulnerability - Remediations

    "remediations": {
      "type": "array",
      "minItems": 1,
      "items": {
        "title": "Remedation",
        "description": "Specifies details on how to handle (and presumably, fix) a vulnerability.",
        "type": "object",
        "required": [
          "description",
          "type"
        ],
        "properties": {
          "date": {
            "type": "string",
            "format": "date-time"
          },
          "description": {
            "title": "Description of the remediation",
            "description": "Contains a thorough human-readable discussion of the remediation.",
            "type": "string",
            "minLength": 1
          },
          "entitlements": {
            "type": "array",
            "minItems": 1,
            "items": {
              "title": "Entitlement of the remediation",
              "description": "Contains any possible vendor-defined constraints for obtaining fixed software or hardware that fully resolves the vulnerability.",
              "type": "string",
              "minLength": 1
            }
          },
          "group_ids": {
            "$ref": "#/definitions/product_groups_t"
          },
          "product_ids": {
            "$ref": "#/definitions/products_t"
          },
          "restart_required": {
            "title": "Restart required by remediation",
            "description": "Provides information on type of restart is required by this remediation to become effective.",
            "type": "object",
            "required": [
              "type"
            ],
            "properties": {
              "type": {
                "title": "Type of restart",
                "description": "Specifies what type of restart is required by this remediation to become effective.",
                "type": "string",
                "enum": [
                  "none",
                  "vulnerable_component",
                  "service",
                  "parent",
                  "dependencies",
                  "connected",
                  "machine",
                  "zone",
                  "system"
                ]
              },
              "description": {
                "title": "Additional restart information",
                "description": "Provides additional information for the restart. This can include details on procedures, scope or impact.",
                "type": "string",
                "minLength": 1
              }
            }
          },
          "type": {
            "title": "Type of the remediation",
            "description": "Specifies the type which this remediation belongs to.",
            "type": "string",
            "enum": [
              "workaround",
              "mitigation",
              "vendor_fix",
              "none_available",
              "will_not_fix"
            ]
          },
          "url": {
            "title": "URL to the remediation",
            "description": "Contains the URL where to obtain the remediation.",
            "type": "string",
            "format": "uri"
          }
        }
      }
    },

##### Vulnerabilities Property - Vulnerability - Threats

    "threats": {
      "type": "array",
      "minItems": 1,
      "items": {
        "title": "Threat",
        "description": "Contains the vulnerability kinetic information. This information can change as the vulnerability ages and new information becomes available.",
        "type": "object",
        "required": [
          "description",
          "type"
        ],
        "properties": {
          "type": {
            "title": "Type of the threat",
            "description": "Categorizes the threat according to the rules of the specification.",
            "type": "string",
            "enum": [
              "impact",
              "exploit_status",
              "target_set"
            ]
          },
          "description": {
            "title": "Description of the threat",
            "description": "Represents a thorough human-readable discussion of the threat.",
            "type": "string",
            "minLength": 1
          },
          "date": {
            "type": "string",
            "format": "date-time"
          },
          "product_ids": {
            "$ref": "#/definitions/products_t"
          },
          "group_ids": {
            "$ref": "#/definitions/product_groups_t"
          }
        }
      }
    },

##### Vulnerabilities Property - Vulnerability - Title

Title has value type string with 1 or more characters.

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
| specname-v1.0-wd01 | yyyy-mm-dd | Editor Name | Initial working draft |

