# CSAF 2.0 JSON Specification Sandbox

## Design Considerations
The Common Security Advisory Framework (CSAF) is a language to exchange Security Advisories formulated in JSON.
The term Security Advisory as used in this document describes any notification of security issues in products of and by providers. Anyone providing a product is considered in this document as a vendor, i.e. developers or maintainers of information system products or services. This includes all authoritative product vendors, Product Security Incident Response Teams (PSIRTs), and product resellers and distributors, including authoritative vendor partners.
A security issue is not necessarily constrained to a problem statement, the focus of the term is on the security aspect impacting (or not impacting) specific product-platform-version combinations. Information on presence or absence of workarounds is also considered part of the security issue.
This document is the definitive reference for the language elements of CSAF version 2.0. The encompassing JSON schema files noted in the Additional Artifacts section of the title page shall be taken as normative in the case a gap or an inconsistency in this explanatory document becomes evident.
The following presentation is grouped by schema, and is not simply derivative documentation from the schema documents themselves. The information contained aims to be more descriptive and complete. Where applicable, common conventions are stated and known common issues in usage are pointed out informatively to support implementers of document producers and consumers alike.

## ​Naming Requirements
### Property Names and String Literals
In the JSON serialization all property names and string literals MUST be exactly the same, including case, as the names listed in the property tables in this specification. For example, the SDO common property created_by_ref must result in the JSON key name "created_by_ref". Properties marked required in the property tables MUST be present in the JSON serialization.

### Reserved Names
Reserved property names are marked with a type called RESERVED and a description text of “RESERVED FOR FUTURE USE”. Any property name that is marked as RESERVED MUST NOT be present in CSAF content conforming to this version of the specification.

From a high-level perspective, any Security Advisory purported by a CSAF version adhering document MUST provide at least the following top-level elements in the displayed sequence:
* Title: document_title
* Type: document_type
* Publisher: document_publisher
* Tracking: document_tracking

This minimal required set does not provide any useful information on products, vulnerabilities, or security advisories, thus a maximal top-level set of elements is given here below:
* Title:  			document_title
* Type: 			document_type
* Publisher: 		document_publisher
* Tracking: 		document_tracking
* Notes: 		document_notes
* Distribution: 		document_distribution
* Aggregate Severity: 	aggregate_severity
* References: 		document_references
* Acknowledgements: 	acknowledgements
* Product Tree: 		product_tree
* Vulnerability: 		vulnerability

Care has been taken, to design the containers for product and vulnerability information to support fine-grained mapping of security advisories onto product and vulnerability and minimize data duplication through referencing.

The display of the elements representing Product Tree and Vulnerability information has been placed in the sections named accordingly.

### Construction Principles
A Security Advisory defined as a CSAF document is the result of complex orchestration of many players and distinct and partially difficult to play schemas.
The acronym CSAF, “Common Security Advisory Framework”, stands for the target of concerted mitigation and remediation accomplishment.
Technically the use of JSON allows validation and proof of model conformance (through established schema based validation) of the declared information inside CSAF documents.
The CSAF schema structures its derived documents into three main classes of the information conveyed:
The frame, aggregation, and reference information of the document
Product information considered relevant by the creator
Vulnerability information and its relation to the products declared in 2.
The prescribed sequence of ordered elements inside these main classes (containers) has been kept stable (e.g. no lexical sorting of sequences) to reduce the amount of changes required for upgrading.
Wherever possible repetition of data has been replaced by linkage through ID elements. Consistency on the content level thus is in the responsibility of the producer of such documents, to link e.g. vulnerability information to the matching product.
A dictionary like presentation of all defined schema elements is given in the following sections. Any expected relations to other elements (linkage) is described there. This linking relies on setting attribute values accordingly (mostly guided by industry best practice and conventions) and thus implies, that any deep validation on a semantic level is to be ensured by the producer and consumer of CSAF documents. It is out of scope for this specification.

## Domain Models
### Date and Time Model
All `datetime` values inside a CSAF document MUST adhere to the ISO 8601 [ISO8601] basic or extended Format (as given there in section 4.3.2 “Complete representations” and with the addition of decimal fractions for seconds, similar to ibid. section 4.2.2.4 “Representations with decimal fraction” but with the full stop (.) being the preferred separator for CSAF).
Many CSAF documents are considered to be shared messages with distributed incremental update and forwarding cycles. Coordinated Universal Time (UTC) is the best fit time system for world-wide exchanged and used date time information.
To ensure maximal interoperability any date time literal having an empty zone designator MUST be treated as having UTC offset 0 or equivalently as if the zone designator would have been the UTC designator (Z).
The following CSAF date time literals expressed in the language of the ISO8601 abstract representations for digits of year(Y), month(M), day(D), hour(h), minute(m), seconds(s), and the special marker (T) are suggested for maximal interoperability in exchange:
Without fractional second digits (also no “full stop” separator):
```
YYYYMMDDThhmmssZ
YYYYMMDDThhmmss+hhmm
YYYY-MM-DDThh:mm:ssZ
YYYY-MM-DDThh:mm:ss+hh:mm
```
Including fractional second digits:
```
YYYYMMDDThhmmss.sZ
YYYYMMDDThhmmss.s+hhmm
YYYY-MM-DDThh:mm:ss.sZ
YYYY-MM-DDThh:mm:ss.s+hh:mm
```
The T separator literal MUST be kept, as leaving it out it is not expected to safe significant space but instead challenge interoperability. » [CSAF-2.2.1-3]

* Note: Time zone calculations are not considered to be in scope for this specification.

* Example 2: Basic format results in April 30, 1985 at time 23:15:30.0 UTC (due to Z as zone designator for UTC)
`19850430T231530.0Z`

* Example 3: Basic format results in April 30, 1985 at time 23:15:30.0 UTC (due to +0400 offset i.e. 4 hours’ positive difference between the time scale of local time and UTC)
`19850501T031530.0+0400`

* Example 4: Extended format results in April 30, 1985 at time 23:15:30.0 UTC (due to Z as zone designator for UTC)
`1985-04-30T23:15:30.0Z`

* Example 5: Extended format for April 30, 1985 at time 23:15:30.0 UTC (due to +01:00 offset i.e. 1 hour’ positive difference between the time scale of local time and UTC)
`1985-05-01T00:15:30.0+01:00`

### Note Type Model
In the scope of CSAF, a note is considered an element, that holds all manner of text blobs related to either a surrounding part of or the entire document.
A note is anything between a concise summary of the target area and a more compartmentalized and area-specific textual discussion.
The note SHOULD contain a compartmentalized textual discussion constrained by its Type attribute.

Any value for the Type attribute of any CSAF Note element (regardless of its parent element) MUST be one of following seven categories:
* description
* details
* faq
* general
* legal_disclaimer
* other
* summary

## Document (Context) JSON Schema Elements
The nine top-level elements are defined in the CSAF JSON file and if given MUST appear in the order listed below.

These main constituents in sequence are:
* Title: `document_title`
* Type: `document_type`
* Publisher: `document_publisher`
* Tracking: `document_tracking`
* Notes: `document_notes`
* Distribution: `document_distribution`
* Aggregate Severity: `aggregate_severity`
* References: `document_references`
* Acknowledgements: `acknowledgements`

The remaining subsections will describe the elements, requirements on them and state recommendations and examples.

### Document Title
Element `document_title`
The document_title element is required exactly once and its sole content MUST be a non-empty string.
This string SHOULD be a definitive canonical name for the document, providing enough descriptive content to differentiate from other similar documents, ideally providing a unique “handle”.

* Non-normative Comment: While this element's value – often just named “the title” – is largely up to the document producer, common usage brings some recommendations:
  * The title should be succinct and promptly give the reader an idea of what is expected document content.
  * If the document producer also publishes a human-friendly document that hand-in-hand with a CSAF document, it is recommended that both documents use the same title.
  * It is further recommended to include the manufacturer name with any product names mentioned in the title.

Example 1:
```
{
  "title": “Cisco IPv6 Crafted Packet Vulnerability”
}
```
Example 2:
```
{
  "title": “CERT Vulnerabilities in Kerberos 5 Implementation”
}
```
Example 3:
```
{
  "title": “OpenSSL Remote Code Execution Vulnerability”
}
```

### Document Type
The `document_type` element is required exactly once and its sole content MUST be a non-empty string. » [CSAF-4.3-1]
The element `document_type` defines a short canonical name, chosen by the document producer, which will inform the end user as to the type of document.

* Non-normative comment: This type label is expected to be aligned with the content conveyed: If it is a “Security Advisory”, it should be named so, likewise a pure “Vulnerability Report” (see following below examples).

Example 1:
```
{
  "title": “Cisco IOS Software DHCP Remote Code Execution Vulnerability”
  “document_type”: “Security Advisory”
}
```
Example 2:
```
{
  "title": “ACME Widget Command Injection Vulnerability”
  “document_type”: “Vulnerability Report”
}
```
Example 3:
```
{
  "title": “Microsoft Windows 10 Denial of Service Vulnerability”
  “document_type”: “Security Bulletin”
}
```

### Document Publisher
The `document_publisher` element is required exactly once and it MUST provide the Type attribute.
It MAY provide the `vendor_id` attribute.
It MAY contain zero or one `contact_details` element and zero or one `issuing_authority` element.
These MUST appear in the order `contact_details` and `issuing_authority`; if both child elements are given.

#### Attribute Type
The value of `type` is a token restricted by the set publishe_enum_type

### Attribute VendorID
The value of `vendor_id` is a string that SHOULD represent a unique identifier (OID) that a vendor uses as issued by FIRST under the auspices of IETF.
* Non-normative comment: At the time of this writing, OID issuance by FIRST is still a work in progress, thus some samples are provided below, that use OIDs from other standard MIBs.

Example: Cisco Systems Inc. OID in dot notation (cf. http://oid-info.com/get/1.3.6.1.4.1.9):
```{
  "title": “Cisco IOS Software DHCP Remote Code Execution Vulnerability”,
  “document_type”: “Security Advisory”,
  “document_publisher”: {
    “type”: “Vendor”,
    “vendor_ID”: "1.3.6.1.4.1.9"
  }
}
```

### Document Publisher – Contact Details
The `contact_details` element contains as its only content a non-empty string and MUST be present zero or one time inside document_publisher to convey author contact information such as address, phone number, or email.
Example:
```
{
  "title": “Cisco IOS Software DHCP Remote Code Execution Vulnerability”,
  “document_type”: “Security Advisory”,
  “document_publisher”: {
    “type”: “Vendor”,
    “vendor_ID”: "1.3.6.1.4.1.9",
    "contact_details": {
      "name": "Birgit Mustermensch"
      "phone_number": "004912345678901"
      "email_address": "birgit.mustermensch@example.com"
    }
  }
}
```
### Document Publisher – Issuing Authority
The `issuing_authority` element contains as its only content a non-empty string and MUST be used zero or once inside `document_publisher` to store the name of the issuing party and their authority to release the document, in particular, the party's constituency and responsibilities or other obligations.

* Non-normative comment: This element is expected to also include instructions for contacting the issuer.

Example:
```
{
  "title": “Cisco IOS Software DHCP Remote Code Execution Vulnerability”,
  “document_type”: “Security Advisory”,
  “document_publisher”: {
    “type”: “Vendor”,
    “vendor_ID”: "1.3.6.1.4.1.9",
    "contact_details": {
      "name": "Birgit Mustermensch"
      "phone_number": "004912345678901"
      "email_address": "birgit.mustermensch@example.com"
    }
  "issuing_authority": "The Cisco Product Security Incident Response Team (PSIRT) is responsible for responding to Cisco product security incidents. The Cisco PSIRT is a dedicated, global team that manages the receipt, investigation, and public reporting of information about security vulnerabilities and issues related to Cisco products and networks. Additional information is available at: https://www.cisco.com/c/en/us/about/security-center/security-vulnerability-policy.html"
  }
}
```

### Document Tracking
The `document_tracking` element required exactly and MUST contain the elements identification, status, version, revision_history, initial_release_date, and current_release_date all exactly once and in that order.

The element `document_tracking` is a container designated to hold all management attributes necessary to track a CSAF document as a whole.

#### Document Tracking – Generator
The `generator` element MUST appear zero or once in `document_tracking` and MUST contain the elements `engine` and `date` all zero or once and in that order.

It is a container to hold all elements related to the generation of the document. These items will reference when the document was actually created, including the date it was generated and the entity that generated it.

#### Document Tracking – Generator – Engine
The optional `engine` element if present MUST be in `generator`.
Any instance MUST contain a non-empty string.
This string SHOULD represent the name of the engine that generated the CSAF document, and MAY additionally refer to its version.

#### Document Tracking – Generator – Date

The element `date` MUST appear zero or once in `generator`, SHOULD be the current date that the document was generated, and MUST be a valid representative of the `date` and `time` model.

Because documents are often generated internally by a document producer and exist for a nonzero amount of time before being released, this field MAY be different from the initial release date.

Example:
```
{
  "title": “Cisco IOS Software DHCP Remote Code Execution Vulnerability”,
  “document_type”: “Security Advisory”,
  “document_publisher”: {
    “type”: “Vendor”,
    “vendor_ID”: "1.3.6.1.4.1.9",
    "contact_details": {
      "name": "Birgit Mustermensch"
      "phone_number": "004912345678901"
      "email_address": "birgit.mustermensch@example.com"
    }
  "issuing_authority": "The Cisco Product Security Incident Response Team (PSIRT) is responsible for responding to Cisco product security incidents. The Cisco PSIRT is a dedicated, global team that manages the receipt, investigation, and public reporting of information about security vulnerabilities and issues related to Cisco products and networks. Additional information is available at: https://www.cisco.com/c/en/us/about/security-center/security-vulnerability-policy.html"
  }
  "document_tracking": {
    "identification": "cisco-sa-20201215-test",
    "status": "Final",
    "version": "1",
    "revision_history": {
      "revision": {
        "version": "1",
        "date": "2020-12-15T11:08:00Z",
        "description": "Current version"
      }
      "initial_release_date": "2020-12-15T11:08:00Z",
      "current_release_date": "2020-12-15T11:08:00Z",
      "generator": {
        "engine": "Cisco PSIRT Engine",
        "date": "2020-05-08T10:26:11Z"
      }
    }
  }
}
```
