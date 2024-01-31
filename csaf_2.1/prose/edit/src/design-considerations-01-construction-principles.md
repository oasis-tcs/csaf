## Construction Principles

A Security Advisory defined as a CSAF document is the result of complex orchestration of many players and distinct and
partially difficult to play schemas.

The format chosen is [JSONSchema] which allows validation and delegation to sub schema providers.
The latter aligns well with separation of concerns and shares the format family of information interchange utilized by
the providers of product and vulnerability information which migrated from XML to JSON since the creation of CSAF CVRF version 1.2,
the pre-predecessor of this specification.

The acronym CSAF, “Common Security Advisory Framework”, stands for the target of concerted mitigation and remediation accomplishment.

Technically, the use of JSON schema allows validation and proof of model conformance (through established schema based validation)
of the declared information inside CSAF documents.

The CSAF schema structures its derived documents into three main classes of the information conveyed:

1. The frame, aggregation, and reference information of the document
2. Product information considered relevant by the creator
3. Vulnerability information and its relation to the products declared in 2.

Wherever possible repetition of data has been replaced by linkage through ID elements.
Consistency on the content level thus is in the responsibility of the producer of such documents,
to link e.g. vulnerability information to the matching product.

A dictionary like presentation of all defined schema elements is given in the section [sec](#schema-elements).
Any expected relations to other elements (linkage) is described there. This linking relies on setting attribute values accordingly
(mostly guided by industry best practice and conventions) and thus implies,
that any deep validation on a semantic level (e.g. does the CWE match the described vulnerability)
is to be ensured by the producer and consumer of CSAF documents.
It is out of scope for this specification.

Proven and intended usage patterns from practice are given where possible.

Delegation to industry best practices technologies is used in referencing schemas for:

* Platform Data:
  * Common Platform Enumeration (CPE) Version 2.3 [cite](#CPE23-N)
* Vulnerability Scoring:
  * Common Vulnerability Scoring System (CVSS) Version 3.1 [cite](#CVSS31)
    * JSON Schema Reference https://www.first.org/cvss/cvss-v3.1.json
  * Common Vulnerability Scoring System (CVSS) Version 3.0 [cite](#CVSS30)
    * JSON Schema Reference https://www.first.org/cvss/cvss-v3.0.json
  * Common Vulnerability Scoring System (CVSS) Version 2.0 [cite](#CVSS2)
    * JSON Schema Reference https://www.first.org/cvss/cvss-v2.0.json
* Vulnerability Classification
  * Common Weakness Enumeration (CWE) [cite](#CWE)
    * CWE List: http://cwe.mitre.org/data/index.html
* Classification for Document Distribution
  * Traffic Light Protocol (TLP)
    * Default Definition: https://www.first.org/tlp/

Even though the JSON schema does not prohibit specifically additional properties and custom keywords,
it is strongly recommended not to use them. Suggestions for new fields SHOULD be made through issues in the TC's GitHub.

> The standardized fields allow for scalability across different issuing parties and dramatically reduce the human effort and
> need for dedicated parsers as well as other tools on the side of the consuming parties.

Section [sec](#profiles) defined profiles that are used to ensure a common understanding of which fields are required in a given use case.
Additional conventions are stated in section [sec](#additional-conventions).
The tests given in section [sec](#tests) support CSAF producers and
consumers to verify rules from the specification which can not be tested by the schema.
Section [sec](#distributing-csaf-documents) states how to distribute and where to find CSAF documents.
Safety, Security and Data Protection are considered in section [sec](#safety-security-and-data-protection-considerations).
Finally, a set of conformance targets describes tools in the ecosystem.

-------
