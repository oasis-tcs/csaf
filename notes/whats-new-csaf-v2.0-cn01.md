
![OASIS Logo](https://docs.oasis-open.org/templates/OASISLogo-v3.0.png)
# OASIS Committee Note
-------

# What's New in CSAF Version 2.0

## Committee Note 01

## 05 November 2021

&nbsp;

<!-- URI list start (commented out except during publication by OASIS TC Admin)

#### This stage:
https://docs.oasis-open.org/csaf/whats-new-csaf/v2.0/cn01/whats-new-csaf-v2.0-cn01.md (Authoritative) \
https://docs.oasis-open.org/csaf/whats-new-csaf/v2.0/cn01/whats-new-csaf-v2.0-cn01.html \
https://docs.oasis-open.org/csaf/whats-new-csaf/v2.0/cn01/whats-new-csaf-v2.0-cn01.pdf

#### Previous stage:
N/A

#### Latest stage:
https://docs.oasis-open.org/csaf/whats-new-csaf/v2.0/whats-new-csaf-v2.0.md (Authoritative) \
https://docs.oasis-open.org/csaf/whats-new-csaf/v2.0/whats-new-csaf-v2.0.html \
https://docs.oasis-open.org/csaf/whats-new-csaf/v2.0/whats-new-csaf-v2.0.pdf

URI list end (commented out except during publication by OASIS TC Admin) -->

#### Technical Committee:
[OASIS Common Security Advisory Framework (CSAF) TC](https://www.oasis-open.org/committees/csaf/)

#### Chair:
Omar Santos (osantos@cisco.com), [Cisco Systems](https://cisco.com/)

#### Editors:
Martin Prpic (mprpic@redhat.com), [Red Hat](https://redhat.com/) \
Stefan Hagen (stefan@hagen.link), [Individual](https://stefan-hagen.website/) \
Thomas Schmidt (thomas.schmidt@bsi.bund.de), [Federal Office for Information Security (BSI) Germany](https://www.bsi.bund.de/)

#### Related work:
This document is related to:
* _Common Security Advisory Framework Version 2.0_. Edited by Langley Rock, Stefan Hagen, and Thomas Schmidt. Latest stage: https://docs.oasis-open.org/csaf/csaf/v2.0/csaf-v2.0.html.
* _CSAF Common Vulnerability Reporting Framework (CVRF) Version 1.2_. Edited by Stefan Hagen. Latest version: http://docs.oasis-open.org/csaf/csaf-cvrf/v1.2/csaf-cvrf-v1.2.html.

#### Abstract:
This document describes the changes between _Common Security Advisory Framework Version 2.0_ and earlier related specifications.

#### Status:
This is a Non-Standards Track Work Product. The patent provisions of the OASIS IPR Policy do not apply.

This document was last revised or approved by the OASIS Common Security Advisory Framework (CSAF) TC on the above date. The level of approval is also listed above. Check the "Latest stage" location noted above for possible later revisions of this document. Any other numbered Versions and other technical work produced by the Technical Committee (TC) are listed at https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=csaf#technical.

TC members should send comments on this document to the TC's email list. Others should send comments to the TC's public comment list, after subscribing to it by following the instructions at the "Send A Comment" button on the TC's web page at https://www.oasis-open.org/committees/csaf/.

#### Citation format:
When referencing this document the following citation format should be used:

**[What's-New-v2.0]**

_What's New in CSAF Version 2.0_. Edited by Martin Prpic, Stefan Hagen, and Thomas Schmidt. 05 November 2021. OASIS Committee Note 01. https://docs.oasis-open.org/csaf/whats-new-csaf/v2.0/cn01/whats-new-csaf-v2.0-cn01.html. Latest stage: https://docs.oasis-open.org/csaf/whats-new-csaf/v2.0/whats-new-csaf-v2.0.html.

#### Notices
Copyright &copy; OASIS Open 2021. All Rights Reserved.

Distributed under the terms of the OASIS [IPR Policy](https://www.oasis-open.org/policies-guidelines/ipr).

The name "OASIS" is a trademark of [OASIS](https://www.oasis-open.org/), the owner and developer of this specification, and should be used only to refer to the organization and its official outputs.

For complete copyright information please see the full Notices section in an Appendix below.

-------

# Table of Contents
[[TOC will be inserted here]]

-------

<!-- Insert a "line rule" (three or more hyphens alone on a new line, following a blank line) before each major section. This is used to generate a page break in the PDF format. -->

# 1 Introduction

Introductory material.

## 1.1 One way to produce OASIS-formatted HTML from Markdown

Here is a customized command line which will generate HTML from this markdown file (named whats-new-csaf-v2.0-cn01.md):

pandoc -f gfm -t html whats-new-csaf-v2.0-cn01.md -c styles/markdown-styles-v1.8a-cn.css --toc --toc-depth=5 -s -o whats-new-csaf-v2.0-cn01.html --metadata title="What's New in CSAF Version 2.0"

We are currently using pandoc 2.6 from https://github.com/jgm/pandoc/releases/tag/2.6.

This also requires the presence of a .css file containing the HTML styles (like styles/markdown-styles-v1.8a-cn.css).

Note this command generates a Table of Contents (TOC) in HTML which is located at the top of the HTML document, and which requires additional editing in order to be published in the expected OASIS style. This editing can be handled by OASIS staff during publication. Alternatively, the TC may generate a TOC via other tools or processes.

## 1.2 Glossary

<!-- Optional section with suggested subsections -->

### 1.2.1 Definitions of terms

### 1.2.2 Acronyms and abbreviations

### 1.2.3 Document conventions

- Naming conventions
- Font colors and styles
- Typographic conventions

## 1.3 Some markdown usage examples

**Text.**

Note that text paragraphs in markdown should be separated by a blank line between them -

Otherwise the separate paragraphs will be joined together when the HTML is generated.
Even if the text appears to be separate lines in the markdown source.

To avoid having the usual vertical space between paragraphs,  
append two or more space characters to the end of the lines  
which will generate an HTML break tag instead of a new paragraph tag  
(as demonstrated here).

### 1.3.1 Figures and Captions

FIGURE EXAMPLE:
<note caption is best ABOVE figure, to allow a link to it to display image - same for table captions>

###### Figure 1 -- Title of Figure
![image-label should be meaningful](images/image_0.png) (this image is missing)

###### Figure 2 -- OpenC2 Message Exchange
![message exchange](images/image_1.png)


### 1.3.2 Tables

#### 1.3.2.1 Basic Table
**Table 1-1. Table Label**

| Item | Description |
| :--- | :--- |
| Item 1 | Something<br>(second line) |
| Item 2 | Something |
| Item 3 | Something<br>(second line) |
| Item 4 | text |

#### 1.3.2.2 Table with Three Columns and Some Bold Text
text.

| Title 1 | Title 2 | title 3 |
| :--- | :--- | :--- |
| something | something | something else that is a long string of text that **might** need to wrap around inside the table box and will just continue until the column divider is reached |
| something | something | something |

#### 1.3.2.3 Table with a caption which can be referenced

###### Table 1-5. See reference label construction

| Name | Description |
| :--- | :--- |
| **content** | Message body as specified by content_type and msg_type. |

Here is a reference to the table caption:
Please see [Table 1-5 or other meaningful label](#table-1-5-see-reference-label-construction) 


### 1.3.3 Lists

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

### 1.3.4 Reference Label Construction

REFERENCES and ANCHORS
- in markdown source, format the Reference tags as level 6 headings like: `###### [OpenC2-HTTPS-v1.0]`
###### [OpenC2-HTTPS-v1.0]
_Specification for Transfer of OpenC2 Messages via HTTPS Version 1.0_. Edited by...

- reference text has to be on a separate line below the tag

- format cross-references (citations of the references) like: `see [[OpenC2-HTTPS-v1.0](#openc2-https-v10)]`  
"see [[OpenC2-HTTPS-v1.0](#openc2-https-v10)]"  
(note the outer square brackets in markdown will appear in the visible HTML text)

- The text in the Reference tag (following ###### ) will become an HTML anchor using the following conversion rules:
  - punctuation marks will be dropped (including "[" )
  - leading white spaces will be dropped
  - upper case will be converted to lower
  - spaces between letters will be converted to a single hyphen

- The same HTML anchor construction rules apply to cross-references and to section headings.
  - Thus, a section heading like "## 1.2 References"
  - becomes an anchor in HTML like `<a href="#12-references">`
  - referenced in the markdown like: see [Section 1.2](#12-references)
  - (in markdown: `"see [Section 1.2](#12-references"`)
  - similar HTML anchors are also used in constructing the TOC

### 1.3.5 Code Blocks

Text to appear as an indented code block with grey background and monospace font - use three back-ticks before and after the code block).

Note the actual backticks will not appear in the HTML version. If it's necessary to display visible backticks, place a back-slash before them like: \``` .

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

## 1.4 Page Breaks
Add horizontal rule lines where page breaks are desired in the PDF - before each major section
- insert the line rules in markdown by inserting 3 or more hyphens on a line by themselves:  ---
- place these before each main section in markdown (usually "#" - which generates the HTML `<h1>` tag)

-------

# 2 Section Heading
text.

## 2.1 Level 2 Heading
text.

### 2.1.1 Level 3 Heading
text.

#### 2.1.1.1 Level 4 Heading
text.

##### 2.1.1.1.1 Level 5 Heading
This is the deepest level, because six # gets transformed into a Reference tag.


## 2.2 Next Heading
text.

-------

# Appendix A. Informative References

<!-- Required section -->

This appendix contains the informative references that are used in this document.

While any hyperlinks included in this appendix were valid at the time of publication, OASIS cannot guarantee their long-term validity.

(Reference sources:
For references to IETF RFCs, use the approved citation formats at:  
http://docs.oasis-open.org/templates/ietf-rfc-list/ietf-rfc-list.html.  
For references to W3C Recommendations, use the approved citation formats at:  
http://docs.oasis-open.org/templates/w3c-recommendations-list/w3c-recommendations-list.html.  
Remove this note before submitting for publication.)

###### [CSAF-v2.0]
_Common Security Advisory Framework Version 2.0_. Edited by Langley Rock, Stefan Hagen, and Thomas Schmidt. Latest stage: https://docs.oasis-open.org/csaf/csaf/v2.0/csaf-v2.0.html
###### [CVRF-v1.2]
_CSAF Common Vulnerability Reporting Framework (CVRF) Version 1.2_. Edited by Stefan Hagen. Latest version: http://docs.oasis-open.org/csaf/csaf-cvrf/v1.2/csaf-cvrf-v1.2.html

-------

# Appendix B. Acknowledgments

(Note: A Work Product approved by the TC must include a list of people who participated in the development of the Work Product. This is generally done by collecting the list of names in this appendix. This list shall be initially compiled by the Chair, and any Member of the TC may add or remove their names from the list by request.  
Remove this note before submitting for publication.)

## B.1 Special Thanks

<!-- This is an optional subsection to call out contributions from TC members. If a TC wants to thank non-TC members then they should avoid using the term "contribution" and instead thank them for their "expertise" or "assistance". -->

Substantial contributions to this document from the following individuals are gratefully acknowledged:

Participant Name, Affiliation or "Individual Member"

## B.2 Participants

<!-- A TC can determine who they list here, however, TC Observers must not be listed. It is common practice for TCs to list everyone that was part of the TC during the creation of the document, but this is ultimately a TC decision on who they want to list and not list, and in what order. -->

The following individuals have participated in the creation of this document and are gratefully acknowledged:

**tc-full-name TC Members:**

| First Name | Last Name | Company |
| :--- | :--- | :--- |
Philippe | Alcon | Marvelous Networks
Alex | Amir | Viacat
Kris | Anders | Trend Mission
Darren | Anysteel | Macro Networks

-------

# Appendix C. Revision History
| Revision | Date | Editor | Changes Made |
| :--- | :--- | :--- | :--- |
| filename-v1.0-wd01 | yyyy-mm-dd | Editor Name | Initial working draft |

------

# Appendix D. Notices

Copyright &copy; OASIS Open 2021. All Rights Reserved.

All capitalized terms in the following text have the meanings assigned to them in the OASIS Intellectual Property Rights Policy (the "OASIS IPR Policy"). The full [Policy](https://www.oasis-open.org/policies-guidelines/ipr) may be found at the OASIS website.

This document and translations of it may be copied and furnished to others, and derivative works that comment on or otherwise explain it or assist in its implementation may be prepared, copied, published, and distributed, in whole or in part, without restriction of any kind, provided that the above copyright notice and this section are included on all such copies and derivative works. However, this document itself may not be modified in any way, including by removing the copyright notice or references to OASIS, except as needed for the purpose of developing any document or deliverable produced by an OASIS Technical Committee (in which case the rules applicable to copyrights, as set forth in the OASIS IPR Policy, must be followed) or as required to translate it into languages other than English.

The limited permissions granted above are perpetual and will not be revoked by OASIS or its successors or assigns.

This document and the information contained herein is provided on an "AS IS" basis and OASIS DISCLAIMS ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO ANY WARRANTY THAT THE USE OF THE INFORMATION HEREIN WILL NOT INFRINGE ANY OWNERSHIP RIGHTS OR ANY IMPLIED WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.

The name "OASIS" is a trademark of [OASIS](https://www.oasis-open.org/), the owner and developer of this specification, and should be used only to refer to the organization and its official outputs. OASIS welcomes reference to, and implementation and use of, specifications, while reserving the right to enforce its marks against misleading uses. Please see https://www.oasis-open.org/policies-guidelines/trademark for above guidance.

# Appendix E. Mapping

This informative appendix provides a mapping by path between the elements in CSAF CVRF 1.2 and CSAF 2.0. It is intended to aid in the transition to CSAF 2.0.

## E.1 Newly introduced elements

* `document`: Groups the document-level metadata elements. Previously, these elements were grouped through the namespace `cvrf`.
* `document.csaf_version`: Gives the version of the CSAF specification which the document was generated for.
* `document.distribution.tlp`: Provides details about the TLP classification of the document.
* `document.lang`: Identifies the language used by this document, corresponding to IETF BCP 47 / RFC 5646. Previously, this was done through `xml:lang` attributes per element.
* `document.publisher.name`: Contains the name of the issuing party. Previously, this was included in `/cvrf:cvrfdoc/cvrf:DocumentPublisher/cvrf:IssuingAuthority/text()`. See conversion rule in [section 9.1.5 of CSAF specification](https://docs.oasis-open.org/csaf/csaf/v2.0/csaf-v2.0.html#915-conformance-clause-5-cvrf-csaf-converter).
* `document.publisher.namespace`: Contains a URL which is under control of the issuing party and can be used as a globally unique identifier for that issuing party. It replaces the `//cvrf:DocumentPublisher/@VendorID`. See conversion rule in [section 9.1.5 of CSAF specification](https://docs.oasis-open.org/csaf/csaf/v2.0/csaf-v2.0.html#915-conformance-clause-5-cvrf-csaf-converter).
* `document.source_lang`: If this copy of the document is a translation then the value of this property describes from which language this document was translated.
* `document.tracking.generator.engine`: Contains information about the engine that generated the CSAF document. This was introduced as intermediate level to group `name` and `version` of `engine` logically. In a CVRF-CSAF conversion, the converter SHOULD replace this objects according to its own values.
* `document.tracking.generator.engine.version`: Contains the version of the engine that generated the CSAF document. Previously, this was part of the `cvrf:Engine` element.
* `product_tree.*.product.product_identification_helper`: Provides at least one method which aids in identifying the product in an asset database. It was introduced to group different ways to identify a product.
* `product_tree.*.product.product_identification_helper.hashes`: Contains a list of cryptographic hashes usable to identify files.
* `product_tree.*.product.product_identification_helper.purl`: The package URL (purl) attribute refers to a method for reliably identifying and locating software packages external to this specification.
* `product_tree.*.product.product_identification_helper.sbom_urls`: Contains a list of URLs where SBOMs for this product can be retrieved.
* `product_tree.*.product.product_identification_helper.serial_numbers`: Contains a list of parts, or full serial numbers.
* `product_tree.*.product.product_identification_helper.skus`: Contains a list of parts, or full stock keeping units.
* `product_tree.*.product.product_identification_helper.x_generic_uris`: Contains a list of identifiers which are either vendor-specific or derived from a standard not yet supported.
* `vulnerabilities[].involvements[].date`: Holds the date and time of the involvement entry.

## E.2 Changed elements

* `*.acknowledgments[].organization`: See conversion rule in [section 9.1.5 of CSAF specification](https://docs.oasis-open.org/csaf/csaf/v2.0/csaf-v2.0.html#915-conformance-clause-5-cvrf-csaf-converter).
* `document.publisher.issuing_authority`: Name of the issuing party is now a separate field. See E.1
* `document.tracking.generator.engine.name`: Version of the engine is now a separate field. See E.1
* `document.tracking.revision_history[].number`: See conversion rule in [section 9.1.5 of CSAF specification](https://docs.oasis-open.org/csaf/csaf/v2.0/csaf-v2.0.html#915-conformance-clause-5-cvrf-csaf-converter).
* `document.tracking.version`: See conversion rule in [section 9.1.5 of CSAF specification](https://docs.oasis-open.org/csaf/csaf/v2.0/csaf-v2.0.html#915-conformance-clause-5-cvrf-csaf-converter).
* `product_tree.relationships[i].full_product_name`: See conversion rule in [section 9.1.5 of CSAF specification](https://docs.oasis-open.org/csaf/csaf/v2.0/csaf-v2.0.html#915-conformance-clause-5-cvrf-csaf-converter).

## E.3 Obsolete CVRF elements

* `//cvrf:Note/@Ordinal`
* `//cvrf:DocumentPublisher/@VendorID`
* `//vuln:Vulnerability/@Ordinal`

## E.4 Mapped elements

| CSAF Attribute                                                          | CSAF CVRF 1.2 Path                                                                                                                                                                                                                                                                                                                                                                             | Note                                                                                                                                                                                          |
| ------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `.` | `/cvrf:cvrfdoc` | |
| `document` |  | see E.1 |
| `document.acknowledgments` | `/cvrf:cvrfdoc/cvrf:Acknowledgments` | |
| `document.acknowledgments[i]` | `/cvrf:cvrfdoc/cvrf:Acknowledgments/cvrf:Acknowledgment[i+1]` | |
| `document.acknowledgments[i].names` | `/cvrf:cvrfdoc/cvrf:Acknowledgments/cvrf:Acknowledgment[i+1]/cvrf:Name`| |
| `document.acknowledgments[i].names[j]` | `/cvrf:cvrfdoc/cvrf:Acknowledgments/cvrf:Acknowledgment[i+1]/cvrf:Name[j+1]/text()` |  |
| `document.acknowledgments[i].organization` | `/cvrf:cvrfdoc/cvrf:Acknowledgments/cvrf:Acknowledgment[i+1]/cvrf:Organization[1]/text()` | see E.2 |
| `document.acknowledgments[i].summary` | `/cvrf:cvrfdoc/cvrf:Acknowledgments/cvrf:Acknowledgment[i+1]/cvrf:Description/text()` |  |
| `document.acknowledgments[i].urls` | `/cvrf:cvrfdoc/cvrf:Acknowledgments/cvrf:Acknowledgment[i+1]/cvrf:URL` |  |
| `document.acknowledgments[i].urls[j]` | `/cvrf:cvrfdoc/cvrf:Acknowledgments/cvrf:Acknowledgment[i+1]/cvrf:URL[j+1]/text()` | |
| `document.aggregate_severity` | `/cvrf:cvrfdoc/cvrf:AggregateSeverity` |  |
| `document.aggregate_severity.namespace` | `/cvrf:cvrfdoc/cvrf:AggregateSeverity/@Namespace` |  |
| `document.aggregate_severity.text` | `/cvrf:cvrfdoc/cvrf:AggregateSeverity/text()` |  |
| `document.category` | `/cvrf:cvrfdoc/cvrf:DocumentType/text()` |  |
| `document.csaf_version` |  | see E.1 |
| `document.distribution` | `/cvrf:cvrfdoc/cvrf:DocumentDistribution` |  |
| `document.distribution.text` | `/cvrf:cvrfdoc/cvrf:DocumentDistribution/text()`  |  |
| `document.distribution.tlp` |  | see E.1 |
| `document.distribution.tlp.label` |  | see parent |
| `document.distribution.tlp.url` |  | see parent |
| `document.lang` |  | see E.1 |
| `document.notes` | `/cvrf:cvrfdoc/cvrf:DocumentNotes` |  |
| `document.notes[i]` | `/cvrf:cvrfdoc/cvrf:DocumentNotes/cvrf:Note[i+1]` |  |
| `document.notes[i].audience` | `/cvrf:cvrfdoc/cvrf:DocumentNotes/cvrf:Note[i+1]/@Audience` |  |
| `document.notes[i].category` | `/cvrf:cvrfdoc/cvrf:DocumentNotes/cvrf:Note[i+1]/@Type` |  |
| `document.notes[i].text` | `/cvrf:cvrfdoc/cvrf:DocumentNotes/cvrf:Note[i+1]/text()` |  |
| `document.notes[].title` | `/cvrf:cvrfdoc/cvrf:DocumentNotes/cvrf:Note[i+1]/@Title` |  |
| `document.publisher` | `/cvrf:cvrfdoc/cvrf:DocumentPublisher` |  |
| `document.publisher.category` | `/cvrf:cvrfdoc/cvrf:DocumentPublisher/@Type` |  |
| `document.publisher.contact_details` | `/cvrf:cvrfdoc/cvrf:DocumentPublisher/cvrf:ContactDetails/text()` |  |
| `document.publisher.issuing_authority` | `/cvrf:cvrfdoc/cvrf:DocumentPublisher/cvrf:IssuingAuthority/text()` | see E.2 |
| `document.publisher.name` |  | see E.1 |
| `document.publisher.namespace` |  | see E.1 |
| `document.references` | `/cvrf:cvrfdoc/cvrf:DocumentReferences` |  |
| `document.references[i]` | `/cvrf:cvrfdoc/cvrf:DocumentReferences/cvrf:Reference[i+1]` |  |
| `document.references[i].category` | `/cvrf:cvrfdoc/cvrf:DocumentReferences/cvrf:Reference[i+1]/@Type` |  |
| `document.references[i].summary` | `/cvrf:cvrfdoc/cvrf:DocumentReferences/cvrf:Reference[i+1]/cvrf:Description/text()` |  |
| `document.references[].url` | `/cvrf:cvrfdoc/cvrf:DocumentReferences/cvrf:Reference[i+1]/cvrf:URL/text()` |  |
| `document.source_lang` |  | see E.1 |
| `document.title` | `/cvrf:cvrfdoc/cvrf:DocumentTitle/text()` |  |
| `document.tracking` | `/cvrf:cvrfdoc/cvrf:DocumentTracking` |  |
| `document.tracking.aliases` | `/cvrf:cvrfdoc/cvrf:DocumentTracking/cvrf:Identification/cvrf:Alias` | |
| `document.tracking.aliases[i]` | `/cvrf:cvrfdoc/cvrf:DocumentTracking/cvrf:Identification/cvrf:Alias[i+1]/text()` |  |
| `document.tracking.current_release_date` | `/cvrf:cvrfdoc/cvrf:DocumentTracking/cvrf:CurrentReleaseDate/text()` | |
| `document.tracking.generator` | `/cvrf:cvrfdoc/cvrf:DocumentTracking/cvrf:Generator` |  |
| `document.tracking.generator.date` | `/cvrf:cvrfdoc/cvrf:DocumentTracking/cvrf:Generator/cvrf:Date/text()` |  |
| `document.tracking.generator.engine` |  | see E.1 |
| `document.tracking.generator.engine.name` | `/cvrf:cvrfdoc/cvrf:DocumentTracking/cvrf:Generator/cvrf:Engine/text()` | see E.2 |
| `document.tracking.generator.engine.version` |  | see E.1 |
| `document.tracking.id` | `/cvrf:cvrfdoc/cvrf:DocumentTracking/cvrf:Identification/cvrf:ID/text()` |  |
| `document.tracking.initial_release_date` | `/cvrf:cvrfdoc/cvrf:DocumentTracking/cvrf:InitialReleaseDate/text()` |  |
| `document.tracking.revision_history` | `/cvrf:cvrfdoc/cvrf:DocumentTracking/cvrf:RevisionHistory` |  |
| `document.tracking.revision_history[i]` | `/cvrf:cvrfdoc/cvrf:DocumentTracking/cvrf:RevisionHistory/cvrf:Revision[i+1]` |  |
| `document.tracking.revision_history[].date` | `/cvrf:cvrfdoc/cvrf:DocumentTracking/cvrf:RevisionHistory/cvrf:Revision[i+1]/cvrf:Date/text()` |  |
| `document.tracking.revision_history[].number` | `/cvrf:cvrfdoc/cvrf:DocumentTracking/cvrf:RevisionHistory/cvrf:Revision[i+1]/cvrf:Number/text()` | see E.2 |
| `document.tracking.revision_history[].summary` | `/cvrf:cvrfdoc/cvrf:DocumentTracking/cvrf:RevisionHistory/cvrf:Revision[i+1]/cvrf:Description/text()` |  |
| `document.tracking.status` | `/cvrf:cvrfdoc/cvrf:DocumentTracking/cvrf:Status/text()` |  |
| `document.tracking.version` | `/cvrf:cvrfdoc/cvrf:DocumentTracking/cvrf:Version/text()` | see E.2 |
| `product_tree` | `/cvrf:cvrfdoc/prod:ProductTree` |  |
| `product_tree.branches` | `/cvrf:cvrfdoc/prod:ProductTree/prod:Branch` |  |
| `product_tree.branches[i]` | `/cvrf:cvrfdoc/prod:ProductTree/prod:Branch[i+1]` |  |
| `product_tree.branches[i].branches` | `/cvrf:cvrfdoc/prod:ProductTree/prod:Branch[i+1]/prod:Branch` |  |
| `product_tree.branches[i].branches[j]` | `/cvrf:cvrfdoc/prod:ProductTree/prod:Branch[i+1]/prod:Branch[j+1]` |  |
| `product_tree.branches[i].branches[j].branches` | `/cvrf:cvrfdoc/prod:ProductTree/prod:Branch[i+1]/prod:Branch[j+1]/prod:Branch` |  |
| `product_tree.branches[i].branches[j].branches[k]` | `/cvrf:cvrfdoc/prod:ProductTree/prod:Branch[i+1]/prod:Branch[j+1]/prod:Branch[k+1]` |  |
| `product_tree.branches[i].branches[j].branches[k].branches` | `/cvrf:cvrfdoc/prod:ProductTree/prod:Branch[i+1]/prod:Branch[j+1]/prod:Branch[k+1]/prod:Branch` | |
| `product_tree.branches[i].branches[j].branches[k].branches[l]` | `/cvrf:cvrfdoc/prod:ProductTree/prod:Branch[i+1]/prod:Branch[j+1]/prod:Branch[k+1]/prod:Branch[l+1]` |  |
| `product_tree.branches[i].branches[j].branches[k].branches[l].category` | `/cvrf:cvrfdoc/prod:ProductTree/prod:Branch[i+1]/prod:Branch[j+1]/prod:Branch[k+1]/prod:Branch[l+1]/@Type` |  |
| `product_tree.branches[i].branches[j].branches[k].branches[l].name` | `/cvrf:cvrfdoc/prod:ProductTree/prod:Branch[i+1]/prod:Branch[j+1]/prod:Branch[k+1]/prod:Branch[l+1]/@Name` |  |
| `product_tree.branches[i].branches[j].branches[k].category` | `/cvrf:cvrfdoc/prod:ProductTree/prod:Branch[i+1]/prod:Branch[j+1]/prod:Branch[k+1]/@Type` | |
| `product_tree.branches[i].branches[j].branches[k].name` | `/cvrf:cvrfdoc/prod:ProductTree/prod:Branch[i+1]/prod:Branch[j+1]/prod:Branch[k+1]/@Name` |  |
| `product_tree.branches[i].branches[j].branches[k].product` | `/cvrf:cvrfdoc/prod:ProductTree/prod:Branch[i+1]/prod:Branch[j+1]/prod:Branch[k+1]/prod:FullProductName` | |
| `product_tree.branches[i].branches[j].branches[k].product.name` | `/cvrf:cvrfdoc/prod:ProductTree/prod:Branch[i+1]/prod:Branch[j+1]/prod:Branch[k+1]/prod:FullProductName/text()` |  |
| `product_tree.branches[i].branches[j].branches[k].product.product_id` | `/cvrf:cvrfdoc/prod:ProductTree/prod:Branch[i+1]/prod:Branch[j+1]/prod:Branch[k+1]/prod:FullProductName/@ProductID` |  |
| `product_tree.branches[i].branches[j].branches[k].product.product_identification_helper` |  | See E.1 |
| `product_tree.branches[i].branches[j].branches[k].product.product_identification_helper.cpe` | `/cvrf:cvrfdoc/prod:ProductTree/prod:Branch[i+1]/prod:Branch[j+1]/prod:Branch[k+1]/prod:FullProductName/@CPE` |  |
| `product_tree.branches[i].branches[j].branches[k].product.product_identification_helper.hashes` |  | See E.1 |
| `product_tree.branches[i].branches[j].branches[k].product.product_identification_helper.purl` |  | See E.1 |
| `product_tree.branches[i].branches[j].branches[k].product.product_identification_helper.sbom_urls` |  | See E.1 |
| `product_tree.branches[i].branches[j].branches[k].product.product_identification_helper.serial_numbers` | | See E.1 |
| `product_tree.branches[i].branches[j].branches[k].product.product_identification_helper.skus` | | See E.1 |
| `product_tree.branches[i].branches[j].branches[k].product.product_identification_helper.x_generic_uris` | | See E.1 |
| `product_tree.branches[i].branches[j].category` | `/cvrf:cvrfdoc/prod:ProductTree/prod:Branch[i+1]/prod:Branch[j+1]/@Type` | |
| `product_tree.branches[i].branches[j].name` | `/cvrf:cvrfdoc/prod:ProductTree/prod:Branch[i+1]/prod:Branch[j+1]/@Name` |  |
| `product_tree.branches[i].branches[j].product` | `/cvrf:cvrfdoc/prod:ProductTree/prod:Branch[i+1]/prod:Branch[j+1]/prod:FullProductName` | |
| `product_tree.branches[i].branches[j].product.name` | `/cvrf:cvrfdoc/prod:ProductTree/prod:Branch[i+1]/prod:Branch[j+1]/prod:FullProductName/text()` |  |
| `product_tree.branches[i].branches[j].product.product_id` | `/cvrf:cvrfdoc/prod:ProductTree/prod:Branch[i+1]/prod:Branch[j+1]/prod:FullProductName/@ProductID` |  |
| `product_tree.branches[i].branches[j].product.product_identification_helper` |  | See E.1 |
| `product_tree.branches[i].branches[j].product.product_identification_helper.cpe` | `/cvrf:cvrfdoc/prod:ProductTree/prod:Branch[i+1]/prod:Branch[j+1]/prod:FullProductName/@CPE` | |
| `product_tree.branches[i].branches[j].product.product_identification_helper.hashes` |  | See E.1 |
| `product_tree.branches[i].branches[j].product.product_identification_helper.hashes[]` |  | See E.1 |
| `product_tree.branches[i].branches[j].product.product_identification_helper.hashes[].file_hashes` | | see parent |
| `product_tree.branches[i].branches[j].product.product_identification_helper.hashes[].filename` |  | see parent |
| `product_tree.branches[i].branches[j].product.product_identification_helper.purl` |  | See E.1 |
| `product_tree.branches[i].branches[j].product.product_identification_helper.sbom_urls` |  | See E.1 |
| `product_tree.branches[i].branches[j].product.product_identification_helper.sbom_urls[]` |  | See E.1 |
| `product_tree.branches[i].branches[j].product.product_identification_helper.serial_numbers` | | See E.1 |
| `product_tree.branches[i].branches[j].product.product_identification_helper.serial_numbers[]` |  | See E.1 |
| `product_tree.branches[i].branches[j].product.product_identification_helper.skus` |  | See E.1 |
| `product_tree.branches[i].branches[j].product.product_identification_helper.skus[]` |  | See E.1 |
| `product_tree.branches[i].branches[j].product.product_identification_helper.x_generic_uris` | | See E.1 |
| `product_tree.branches[i].branches[j].product.product_identification_helper.x_generic_uris[]` |  | See E.1 |
| `product_tree.branches[i].branches[j].product.product_identification_helper.x_generic_uris[].namespace` |  | see parent |
| `product_tree.branches[i].branches[j].product.product_identification_helper.x_generic_uris[].uri` |  | see parent |
| `product_tree.branches[i].category` | `/cvrf:cvrfdoc/prod:ProductTree/prod:Branch[i+1]/@Type` |  |
| `product_tree.branches[i].name` | `/cvrf:cvrfdoc/prod:ProductTree/prod:Branch[i+1]/@Name` |  |
| `product_tree.branches[i].product` | `/cvrf:cvrfdoc/prod:ProductTree/prod:Branch[i+1]/prod:FullProductName` | |
| `product_tree.branches[i].product.name` |  `/cvrf:cvrfdoc/prod:ProductTree/prod:Branch[i+1]/prod:FullProductName/text()` |  |
| `product_tree.branches[i].product.product_id` | `/cvrf:cvrfdoc/prod:ProductTree/prod:Branch[i+1]/prod:FullProductName/@ProductID` |  |
| `product_tree.branches[i].product.product_identification_helper` |  | See E.1 |
| `product_tree.branches[i].product.product_identification_helper.cpe` | `/cvrf:cvrfdoc/prod:ProductTree/prod:Branch[i+1]/prod:FullProductName/@CPE` |  |
| `product_tree.branches[i].product.product_identification_helper.hashes` | | See E.1 |
| `product_tree.branches[i].product.product_identification_helper.hashes[]` |  | See E.1 |
| `product_tree.branches[i].product.product_identification_helper.hashes[].file_hashes` | | see parent |
| `product_tree.branches[i].product.product_identification_helper.hashes[].file_hashes[]` |  | see parent |
| `product_tree.branches[i].product.product_identification_helper.hashes[].file_hashes[].algorithm` |  | see parent |
| `product_tree.branches[i].product.product_identification_helper.hashes[].file_hashes[].value` |  | see parent |
| `product_tree.branches[i].product.product_identification_helper.hashes[].filename` |  | see parent |
| `product_tree.branches[i].product.product_identification_helper.purl` |  | See E.1 |
| `product_tree.branches[i].product.product_identification_helper.sbom_urls` |  | See E.1 |
| `product_tree.branches[i].product.product_identification_helper.sbom_urls[]` |  | See E.1 |
| `product_tree.branches[i].product.product_identification_helper.serial_numbers` | | See E.1 |
| `product_tree.branches[i].product.product_identification_helper.serial_numbers[]` |  | See E.1 |
| `product_tree.branches[i].product.product_identification_helper.skus` | | See E.1 |
| `product_tree.branches[i].product.product_identification_helper.skus[]` |  | See E.1 |
| `product_tree.branches[i].product.product_identification_helper.x_generic_uris` | | See E.1 |
| `product_tree.branches[i].product.product_identification_helper.x_generic_uris[]` |  | See E.1 |
| `product_tree.branches[i].product.product_identification_helper.x_generic_uris[].namespace` |  | see parent |
| `product_tree.branches[i].product.product_identification_helper.x_generic_uris[].uri` |  | see parent |
| `product_tree.full_product_names` | `/cvrf:cvrfdoc/prod:ProductTree/prod:FullProductName` | |
| `product_tree.full_product_names[i]` | `/cvrf:cvrfdoc/prod:ProductTree/prod:FullProductName[i+1]` | |
| `product_tree.full_product_names[i].name` | `/cvrf:cvrfdoc/prod:ProductTree/prod:FullProductName[i+1]/text()` |  |
| `product_tree.full_product_names[i].product_id` | `/cvrf:cvrfdoc/prod:ProductTree/prod:FullProductName[i+1]/@ProductID` |  |
| `product_tree.full_product_names[i].product_identification_helper` |  | See E.1 |
| `product_tree.full_product_names[i].product_identification_helper.cpe` | `/cvrf:cvrfdoc/prod:ProductTree/prod:FullProductName[i+1]/@CPE` | |
| `product_tree.full_product_names[i].product_identification_helper.hashes` | | See E.1 |
| `product_tree.full_product_names[i].product_identification_helper.hashes[]` |  | See E.1 |
| `product_tree.full_product_names[i].product_identification_helper.hashes[].file_hashes` | | see parent |
| `product_tree.full_product_names[i].product_identification_helper.hashes[].file_hashes[]` |  | see parent |
| `product_tree.full_product_names[i].product_identification_helper.hashes[].file_hashes[].algorithm` |  | see parent |
| `product_tree.full_product_names[i].product_identification_helper.hashes[].file_hashes[].value` |  | see parent |
| `product_tree.full_product_names[i].product_identification_helper.hashes[].filename` |  | see parent |
| `product_tree.full_product_names[i].product_identification_helper.purl` |  | See E.1 |
| `product_tree.full_product_names[i].product_identification_helper.sbom_urls` | | See E.1 |
| `product_tree.full_product_names[i].product_identification_helper.sbom_urls[]` |  | See E.1 |
| `product_tree.full_product_names[i].product_identification_helper.serial_numbers` | | See E.1 |
| `product_tree.full_product_names[i].product_identification_helper.serial_numbers[]` | | See E.1 |
| `product_tree.full_product_names[i].product_identification_helper.skus` | | See E.1 |
| `product_tree.full_product_names[i].product_identification_helper.skus[]` |  | See E.1 |
| `product_tree.full_product_names[i].product_identification_helper.x_generic_uris` | | See E.1 |
| `product_tree.full_product_names[i].product_identification_helper.x_generic_uris[]` |  | See E.1 |
| `product_tree.full_product_names[i].product_identification_helper.x_generic_uris[].namespace` |  | see parent |
| `product_tree.full_product_names[i].product_identification_helper.x_generic_uris[].uri` |  | see parent |
| `product_tree.product_groups` | `/cvrf:cvrfdoc/prod:ProductTree/prod:ProductGroups` | |
| `product_tree.product_groups[i]` | `/cvrf:cvrfdoc/prod:ProductTree/prod:ProductGroups/prod:Group[i+1]` | |
| `product_tree.product_groups[i].group_id` | `/cvrf:cvrfdoc/prod:ProductTree/prod:ProductGroups/prod:Group[i+1]/@GroupID` |  |
| `product_tree.product_groups[i].product_ids` | `/cvrf:cvrfdoc/prod:ProductTree/prod:ProductGroups/prod:Group[i+1]/prod:ProductID` | |
| `product_tree.product_groups[i].product_ids[j]` | `/cvrf:cvrfdoc/prod:ProductTree/prod:ProductGroups/prod:Group[i+1]/prod:ProductID[j+1]/text()` |  |
| `product_tree.product_groups[i].summary` | `/cvrf:cvrfdoc/prod:ProductTree/prod:ProductGroups/prod:Group[i+1]/prod:Description/text()` |  |
| `product_tree.relationships` | `/cvrf:cvrfdoc/prod:ProductTree/prod:Relationship` | |
| `product_tree.relationships[i]` | `/cvrf:cvrfdoc/prod:ProductTree/prod:Relationship[i+1]` | |
| `product_tree.relationships[i].category` | `/cvrf:cvrfdoc/prod:ProductTree/prod:Relationship[i+1]/@RelationType` | |
| `product_tree.relationships[i].full_product_name` | `/cvrf:cvrfdoc/prod:ProductTree/prod:Relationship[i+1]/prod:FullProductName[1]` | See E.2 |
| `product_tree.relationships[i].full_product_name.name` | `/cvrf:cvrfdoc/prod:ProductTree/prod:Relationship[i+1]/prod:FullProductName[1]/text()` | See E.2 |
| `product_tree.relationships[i].full_product_name.product_id` | `/cvrf:cvrfdoc/prod:ProductTree/prod:Relationship[i+1]/prod:FullProductName[1]/@ProductID` | See E.2 |
| `product_tree.relationships[i].full_product_name.product_identification_helper` |  | See E.1 |
| `product_tree.relationships[i].full_product_name.product_identification_helper.cpe` | `/cvrf:cvrfdoc/prod:ProductTree/prod:Relationship[i+1]/prod:FullProductName[1]/@CPE` | See E.2 |
| `product_tree.relationships[i].full_product_name.product_identification_helper.hashes` |  | See E.1 |
| `product_tree.relationships[i].full_product_name.product_identification_helper.hashes[]` |  | See E.1 |
| `product_tree.relationships[i].full_product_name.product_identification_helper.hashes[].file_hashes` |  | see parent |
| `product_tree.relationships[i].full_product_name.product_identification_helper.hashes[].file_hashes[]` |  | see parent |
| `product_tree.relationships[i].full_product_name.product_identification_helper.hashes[].file_hashes[].algorithm` |  | see parent |
| `product_tree.relationships[i].full_product_name.product_identification_helper.hashes[].file_hashes[].value` |  | see parent |
| `product_tree.relationships[i].full_product_name.product_identification_helper.hashes[].filename` | | see parent |
| `product_tree.relationships[i].full_product_name.product_identification_helper.purl` |  | See E.1 |
| `product_tree.relationships[i].full_product_name.product_identification_helper.sbom_urls` |  | See E.1 |
| `product_tree.relationships[i].full_product_name.product_identification_helper.sbom_urls[]` |  | See E.1 |
| `product_tree.relationships[i].full_product_name.product_identification_helper.serial_numbers` |  | See E.1 |
| `product_tree.relationships[i].full_product_name.product_identification_helper.serial_numbers[]` |  | See E.1 |
| `product_tree.relationships[i].full_product_name.product_identification_helper.skus` |  | See E.1 |
| `product_tree.relationships[i].full_product_name.product_identification_helper.skus[]` |  | See E.1 |
| `product_tree.relationships[i].full_product_name.product_identification_helper.x_generic_uris` |  | See E.1 |
| `product_tree.relationships[i].full_product_name.product_identification_helper.x_generic_uris[]` |  | See E.1 |
| `product_tree.relationships[i].full_product_name.product_identification_helper.x_generic_uris[].namespace` |  | see parent |
| `product_tree.relationships[i].full_product_name.product_identification_helper.x_generic_uris[].uri` |  | see parent |
| `product_tree.relationships[i].product_reference` | `/cvrf:cvrfdoc/prod:ProductTree/prod:Relationship[i+1]/@ProductReference` |  |
| `product_tree.relationships[i].relates_to_product_reference` | `/cvrf:cvrfdoc/prod:ProductTree/prod:Relationship[i+1]/@RelatesToProductReference` |  |
| `vulnerabilities` | `/cvrf:cvrfdoc/vuln:Vulnerability` | |
| `vulnerabilities[i]` | `/cvrf:cvrfdoc/vuln:Vulnerability[i+1]` | |
| `vulnerabilities[i].acknowledgments` | `/cvrf:cvrfdoc/vuln:Vulnerability[i+1]/vuln:Acknowledgments` | |
| `vulnerabilities[i].acknowledgments[j]` | `/cvrf:cvrfdoc/vuln:Vulnerability[i+1]/vuln:Acknowledgments/vuln:Acknowledgment[j+1]` | |
| `vulnerabilities[i].acknowledgments[j].names` | `/cvrf:cvrfdoc/vuln:Vulnerability[i+1]/vuln:Acknowledgments/vuln:Acknowledgment[j+1]/vuln:Name` | |
| `vulnerabilities[i].acknowledgments[j].names[k]` | `/cvrf:cvrfdoc/vuln:Vulnerability[i+1]/vuln:Acknowledgments/vuln:Acknowledgment[j+1]/vuln:Name[k+1]/text()`  | |
| `vulnerabilities[i].acknowledgments[j].organization` | `/cvrf:cvrfdoc/vuln:Vulnerability[i+1]/vuln:Acknowledgments/vuln:Acknowledgment[j+1]/vuln:Organization[1]/text()` | see E.2 |
| `vulnerabilities[i].acknowledgments[j].summary` | `/cvrf:cvrfdoc/vuln:Vulnerability[i+1]/vuln:Acknowledgments/vuln:Acknowledgment[j+1]/vuln:Description/text()` | |
| `vulnerabilities[i].acknowledgments[j].urls` | `/cvrf:cvrfdoc/vuln:Vulnerability[i+1]/vuln:Acknowledgments/vuln:Acknowledgment[j+1]/vuln:URL`| |
| `vulnerabilities[i].acknowledgments[j].urls[k]` | `/cvrf:cvrfdoc/vuln:Vulnerability[i+1]/vuln:Acknowledgments/vuln:Acknowledgment[j+1]/vuln:URL[k+1]/text()` | |
| `vulnerabilities[i].cve` | `/cvrf:cvrfdoc/vuln:Vulnerability[i+1]/vuln:CVE/text()` | |
| `vulnerabilities[i].cwe` | `/cvrf:cvrfdoc/vuln:Vulnerability[i+1]/vuln:CWE` | |
| `vulnerabilities[i].cwe.id` | `/cvrf:cvrfdoc/vuln:Vulnerability[i+1]/vuln:CWE/@ID` |  |
| `vulnerabilities[i].cwe.name` | `/cvrf:cvrfdoc/vuln:Vulnerability[i+1]/vuln:CWE/text()` |  |
| `vulnerabilities[i].discovery_date` | `/cvrf:cvrfdoc/vuln:Vulnerability[i+1]/vuln:DiscoveryDate/text()` | |
| `vulnerabilities[i].id` | `/cvrf:cvrfdoc/vuln:Vulnerability[i+1]/vuln:ID` | |
| `vulnerabilities[i].id.system_name` | `/cvrf:cvrfdoc/vuln:Vulnerability[i+1]/vuln:ID/@SystemName` |  |
| `vulnerabilities[i].id.text` | `/cvrf:cvrfdoc/vuln:Vulnerability[i+1]/vuln:ID/text()` |  |
| `vulnerabilities[i].involvements` | `/cvrf:cvrfdoc/vuln:Vulnerability[i+1]/vuln:Involvements` |  |
| `vulnerabilities[i].involvements[j]` | `/cvrf:cvrfdoc/vuln:Vulnerability[i+1]/vuln:Involvements/vuln:Involvement[j+1]` | |
| `vulnerabilities[i].involvements[j].date` |  | see E.1 |
| `vulnerabilities[i].involvements[j].party` | `/cvrf:cvrfdoc/vuln:Vulnerability[i+1]/vuln:Involvements/vuln:Involvement[j+1]/@Party` | |
| `vulnerabilities[i].involvements[j].status` | `/cvrf:cvrfdoc/vuln:Vulnerability[i+1]/vuln:Involvements/vuln:Involvement[j+1]/@Status` | |
| `vulnerabilities[i].involvements[j].summary` | `/cvrf:cvrfdoc/vuln:Vulnerability[i+1]/vuln:Involvements/vuln:Involvement[j+1]/vuln:Description/text()` | |
