
![OASIS Logo](https://docs.oasis-open.org/templates/OASISLogo-v3.0.png)

-------

# Common Security Advisory Framework Version 2.0

## OASIS Standard

## 18 November 2022

#### This stage:
https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.md (Authoritative) \
https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html \
https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.pdf

#### Previous stage:
https://docs.oasis-open.org/csaf/csaf/v2.0/cs03/csaf-v2.0-cs03.md (Authoritative) \
https://docs.oasis-open.org/csaf/csaf/v2.0/cs03/csaf-v2.0-cs03.html \
https://docs.oasis-open.org/csaf/csaf/v2.0/cs03/csaf-v2.0-cs03.pdf

#### Latest stage:
https://docs.oasis-open.org/csaf/csaf/v2.0/csaf-v2.0.md (Authoritative) \
https://docs.oasis-open.org/csaf/csaf/v2.0/csaf-v2.0.html \
https://docs.oasis-open.org/csaf/csaf/v2.0/csaf-v2.0.pdf

#### Technical Committee:
[OASIS Common Security Advisory Framework (CSAF) TC](https://www.oasis-open.org/committees/csaf/)

#### Chair:
Omar Santos (osantos@cisco.com), [Cisco Systems](https://cisco.com/)

#### Editors:
Langley Rock (lrock@redhat.com), [Red Hat](https://redhat.com/) \
Stefan Hagen (stefan@hagen.link), [Individual](https://stefan-hagen.website/) \
Thomas Schmidt (thomas.schmidt@bsi.bund.de), [Federal Office for Information Security (BSI) Germany](https://www.bsi.bund.de/)

In Memory of Eric Johnson, TIBCO Software Inc. and Mike Gorski, Cisco Systems both active members of the OASIS CSAF Technical Committee.

#### Additional artifacts:
This prose specification is one component of a Work Product that also includes:

* Aggregator JSON schema: https://docs.oasis-open.org/csaf/csaf/v2.0/os/schemas/aggregator_json_schema.json. \
Latest stage: https://docs.oasis-open.org/csaf/csaf/v2.0/aggregator_json_schema.json.
* CSAF JSON schema: https://docs.oasis-open.org/csaf/csaf/v2.0/os/schemas/csaf_json_schema.json. \
Latest stage: https://docs.oasis-open.org/csaf/csaf/v2.0/csaf_json_schema.json.
* Provider JSON schema: https://docs.oasis-open.org/csaf/csaf/v2.0/os/schemas/provider_json_schema.json. \
Latest stage: https://docs.oasis-open.org/csaf/csaf/v2.0/provider_json_schema.json.

#### Related work:
This specification replaces or supersedes:

* _CSAF Common Vulnerability Reporting Framework (CVRF) Version 1.2_. Edited by Stefan Hagen. Latest stage:  https://docs.oasis-open.org/csaf/csaf-cvrf/v1.2/csaf-cvrf-v1.2.html.

#### Declared JSON namespaces:

* [https://docs.oasis-open.org/csaf/csaf/v2.0/aggregator_json_schema.json](https://docs.oasis-open.org/csaf/csaf/v2.0/aggregator_json_schema.json)
* [https://docs.oasis-open.org/csaf/csaf/v2.0/csaf_json_schema.json](https://docs.oasis-open.org/csaf/csaf/v2.0/csaf_json_schema.json)
* [https://docs.oasis-open.org/csaf/csaf/v2.0/provider_json_schema.json](https://docs.oasis-open.org/csaf/csaf/v2.0/provider_json_schema.json)


#### Abstract:
The Common Security Advisory Framework (CSAF) Version 2.0 is the definitive reference for the language which supports creation, update, and interoperable exchange of security advisories as structured information on products, vulnerabilities and the status of impact and remediation among interested parties.

#### Status:
This document was last revised or approved by the membership of OASIS on the above date. The level of approval is also listed above. Check the "Latest stage" location noted above for possible later revisions of this document. Any other numbered Versions and other technical work produced by the Technical Committee (TC) are listed at https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=csaf#technical.

TC members should send comments on this specification to the TC's email list. Others should send comments to the TC's public comment list, after subscribing to it by following the instructions at the "Send A Comment" button on the TC's web page at https://www.oasis-open.org/committees/csaf/.

This specification is provided under the [Non-Assertion](https://www.oasis-open.org/policies-guidelines/ipr/#Non-Assertion-Mode) Mode of the [OASIS IPR Policy](https://www.oasis-open.org/policies-guidelines/ipr/), the mode chosen when the Technical Committee was established. For information on whether any patents have been disclosed that may be essential to implementing this specification, and any offers of patent licensing terms, please refer to the Intellectual Property Rights section of the TC's web page (https://www.oasis-open.org/committees/csaf/ipr.php).

Note that any machine-readable content ([Computer Language Definitions](https://www.oasis-open.org/policies-guidelines/tc-process-2017-05-26/#wpComponentsCompLang)) declared Normative for this Work Product is provided in separate plain text files. In the event of a discrepancy between any such plain text file and display content in the Work Product's prose narrative document(s), the content in the separate plain text file prevails.

#### Citation format:
When referencing this specification the following citation format should be used:

**[csaf-v2.0]**

_Common Security Advisory Framework Version 2.0_. Edited by Langley Rock, Stefan Hagen, and Thomas Schmidt. 18 November 2022. OASIS Standard. https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html. Latest stage: https://docs.oasis-open.org/csaf/csaf/v2.0/csaf-v2.0.html.


-------

## Notices

Copyright © OASIS Open 2022. All Rights Reserved.

All capitalized terms in the following text have the meanings assigned to them in the OASIS Intellectual Property Rights Policy (the "OASIS IPR Policy"). The full [Policy](https://www.oasis-open.org/policies-guidelines/ipr/) may be found at the OASIS website.

This document and translations of it may be copied and furnished to others, and derivative works that comment on or otherwise explain it or assist in its implementation may be prepared, copied, published, and distributed, in whole or in part, without restriction of any kind, provided that the above copyright notice and this section are included on all such copies and derivative works. However, this document itself may not be modified in any way, including by removing the copyright notice or references to OASIS, except as needed for the purpose of developing any document or deliverable produced by an OASIS Technical Committee (in which case the rules applicable to copyrights, as set forth in the OASIS IPR Policy, must be followed) or as required to translate it into languages other than English.

The limited permissions granted above are perpetual and will not be revoked by OASIS or its successors or assigns.

This document and the information contained herein is provided on an "AS IS" basis and OASIS DISCLAIMS ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO ANY WARRANTY THAT THE USE OF THE INFORMATION HEREIN WILL NOT INFRINGE ANY OWNERSHIP RIGHTS OR ANY IMPLIED WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.

As stated in the OASIS IPR Policy, the following three paragraphs in brackets apply to OASIS Standards Final Deliverable documents (Committee Specification, Candidate OASIS Standard, OASIS Standard, or Approved Errata).

\[OASIS requests that any OASIS Party or any other party that believes it has patent claims that would necessarily be infringed by implementations of this OASIS Standards Final Deliverable, to notify OASIS TC Administrator and provide an indication of its willingness to grant patent licenses to such patent claims in a manner consistent with the IPR Mode of the OASIS Technical Committee that produced this deliverable.\]

\[OASIS invites any party to contact the OASIS TC Administrator if it is aware of a claim of ownership of any patent claims that would necessarily be infringed by implementations of this OASIS Standards Final Deliverable by a patent holder that is not willing to provide a license to such patent claims in a manner consistent with the IPR Mode of the OASIS Technical Committee that produced this OASIS Standards Final Deliverable. OASIS may include such claims on its website, but disclaims any obligation to do so.\]

\[OASIS takes no position regarding the validity or scope of any intellectual property or other rights that might be claimed to pertain to the implementation or use of the technology described in this OASIS Standards Final Deliverable or the extent to which any license under such rights might or might not be available; neither does it represent that it has made any effort to identify any such rights. Information on OASIS' procedures with respect to rights in any document or deliverable produced by an OASIS Technical Committee can be found on the OASIS website. Copies of claims of rights made available for publication and any assurances of licenses to be made available, or the result of an attempt made to obtain a general license or permission for the use of such proprietary rights by implementers or users of this OASIS Standards Final Deliverable, can be obtained from the OASIS TC Administrator. OASIS makes no representation that any information or list of intellectual property rights will at any time be complete, or that any claims in such list are, in fact, Essential Claims.\]

The name "OASIS" is a trademark of [OASIS](https://www.oasis-open.org/), the owner and developer of this specification, and should be used only to refer to the organization and its official outputs. OASIS welcomes reference to, and implementation and use of, specifications, while reserving the right to enforce its marks against misleading uses. Please see https://www.oasis-open.org/policies-guidelines/trademark/ for above guidance.

-------

# Table of Contents

1. [Introduction](#introduction)  
	1.1 [IPR Policy](#ipr-policy)  
	1.2 [Terminology](#terminology)  
	1.3 [Normative References](#normative-references)  
	1.4 [Informative References](#informative-references)  
	1.5 [Typographical Conventions](#typographical-conventions)  
2. [Design Considerations](#design-considerations)  
	2.1 [Construction Principles](#construction-principles)  
3. [Schema Elements](#schema-elements)  
	3.1 [Definitions](#definitions)  
		3.1.1 [Acknowledgments Type](#acknowledgments-type)  
			3.1.1.1 [Acknowledgments Type - Names](#acknowledgments-type-names)  
			3.1.1.2 [Acknowledgments Type - Organization](#acknowledgments-type-organization)  
			3.1.1.3 [Acknowledgments Type - Summary](#acknowledgments-type-summary)  
			3.1.1.4 [Acknowledgments Type - URLs](#acknowledgments-type-urls)  
			3.1.1.5 [Acknowledgments Type - Example](#acknowledgments-type-example)  
		3.1.2 [Branches Type](#branches-type)  
			3.1.2.1 [Branches Type - Branches](#branches-type-branches)  
			3.1.2.2 [Branches Type - Category](#branches-type-category)  
			3.1.2.3 [Branches Type - Name](#branches-type-name)  
				3.1.2.3.1 [Branches Type - Name under Product Version](#branches-type-name-under-product-version)  
				3.1.2.3.2 [Branches Type - Name under Product Version Range](#branches-type-name-under-product-version-range)  
			3.1.2.4 [Branches Type - Product](#branches-type-product)  
		3.1.3 [Full Product Name Type](#full-product-name-type)  
			3.1.3.1 [Full Product Name Type - Name](#full-product-name-type-name)  
			3.1.3.2 [Full Product Name Type - Product ID](#full-product-name-type-product-id)  
			3.1.3.3 [Full Product Name Type - Product Identification Helper](#full-product-name-type-product-identification-helper)  
				3.1.3.3.1 [Full Product Name Type - Product Identification Helper - CPE](#full-product-name-type-product-identification-helper-cpe)  
				3.1.3.3.2 [Full Product Name Type - Product Identification Helper - Hashes](#full-product-name-type-product-identification-helper-hashes)  
				3.1.3.3.3 [Full Product Name Type - Product Identification Helper - Model Numbers](#full-product-name-type-product-identification-helper-model-numbers)  
				3.1.3.3.4 [Full Product Name Type - Product Identification Helper - PURL](#full-product-name-type-product-identification-helper-purl)  
				3.1.3.3.5 [Full Product Name Type - Product Identification Helper - SBOM URLs](#full-product-name-type-product-identification-helper-sbom-urls)  
				3.1.3.3.6 [Full Product Name Type - Product Identification Helper - Serial Numbers](#full-product-name-type-product-identification-helper-serial-numbers)  
				3.1.3.3.7 [Full Product Name Type - Product Identification Helper - SKUs](#full-product-name-type-product-identification-helper-skus)  
				3.1.3.3.8 [Full Product Name Type - Product Identification Helper - Generic URIs](#full-product-name-type-product-identification-helper-generic-uris)  
		3.1.4 [Language Type](#language-type)  
		3.1.5 [Notes Type](#notes-type)  
		3.1.6 [Product Group ID Type](#product-group-id-type)  
		3.1.7 [Product Groups Type](#product-groups-type)  
		3.1.8 [Product ID Type](#product-id-type)  
		3.1.9 [Products Type](#products-type)  
		3.1.10 [References Type](#references-type)  
		3.1.11 [Version Type](#version-type)  
			3.1.11.1 [Version Type - Integer versioning](#version-type-integer-versioning)  
			3.1.11.2 [Version Type - Semantic versioning](#version-type-semantic-versioning)  
	3.2 [Properties](#properties)  
		3.2.1 [Document Property](#document-property)  
			3.2.1.1 [Document Property - Acknowledgments](#document-property-acknowledgments)  
			3.2.1.2 [Document Property - Aggregate Severity](#document-property-aggregate-severity)  
			3.2.1.3 [Document Property - Category](#document-property-category)  
			3.2.1.4 [Document Property - CSAF Version](#document-property-csaf-version)  
			3.2.1.5 [Document Property - Distribution](#document-property-distribution)  
				3.2.1.5.1 [Document Property - Distribution - Text](#document-property-distribution-text)  
				3.2.1.5.2 [Document Property - Distribution - TLP](#document-property-distribution-tlp)  
			3.2.1.6 [Document Property - Language](#document-property-language)  
			3.2.1.7 [Document Property - Notes](#document-property-notes)  
			3.2.1.8 [Document Property - Publisher](#document-property-publisher)  
				3.2.1.8.1 [Document Property - Publisher - Category](#document-property-publisher-category)  
				3.2.1.8.2 [Document Property - Publisher - Contact Details](#document-property-publisher-contact-details)  
				3.2.1.8.3 [Document Property - Publisher - Issuing Authority](#document-property-publisher-issuing-authority)  
				3.2.1.8.4 [Document Property - Publisher - Name](#document-property-publisher-name)  
				3.2.1.8.5 [Document Property - Publisher - Namespace](#document-property-publisher-namespace)  
			3.2.1.9 [Document Property - References](#document-property-references)  
			3.2.1.10 [Document Property - Source Language](#document-property-source-language)  
			3.2.1.11 [Document Property - Title](#document-property-title)  
			3.2.1.12 [Document Property - Tracking](#document-property-tracking)  
				3.2.1.12.1 [Document Property - Tracking - Aliases](#document-property-tracking-aliases)  
				3.2.1.12.2 [Document Property - Tracking - Current Release Date](#document-property-tracking-current-release-date)  
				3.2.1.12.3 [Document Property - Tracking - Generator](#document-property-tracking-generator)  
				3.2.1.12.4 [Document Property - Tracking - ID](#document-property-tracking-id)  
				3.2.1.12.5 [Document Property - Tracking - Initial Release Date](#document-property-tracking-initial-release-date)  
				3.2.1.12.6 [Document Property - Tracking - Revision History](#document-property-tracking-revision-history)  
				3.2.1.12.7 [Document Property - Tracking - Status](#document-property-tracking-status)  
				3.2.1.12.8 [Document Property - Tracking - Version](#document-property-tracking-version)  
		3.2.2 [Product Tree Property](#product-tree-property)  
			3.2.2.1 [Product Tree Property - Branches](#product-tree-property-branches)  
			3.2.2.2 [Product Tree Property - Full Product Names](#product-tree-property-full-product-names)  
			3.2.2.3 [Product Tree Property - Product Groups](#product-tree-property-product-groups)  
			3.2.2.4 [Product Tree Property - Relationships](#product-tree-property-relationships)  
		3.2.3 [Vulnerabilities Property](#vulnerabilities-property)  
			3.2.3.1 [Vulnerabilities Property - Acknowledgments](#vulnerabilities-property-acknowledgments)  
			3.2.3.2 [Vulnerabilities Property - CVE](#vulnerabilities-property-cve)  
			3.2.3.3 [Vulnerabilities Property - CWE](#vulnerabilities-property-cwe)  
			3.2.3.4 [Vulnerabilities Property - Discovery Date](#vulnerabilities-property-discovery-date)  
			3.2.3.5 [Vulnerabilities Property - Flags](#vulnerabilities-property-flags)  
			3.2.3.6 [Vulnerabilities Property - IDs](#vulnerabilities-property-ids)  
			3.2.3.7 [Vulnerabilities Property - Involvements](#vulnerabilities-property-involvements)  
			3.2.3.8 [Vulnerabilities Property - Notes](#vulnerabilities-property-notes)  
			3.2.3.9 [Vulnerabilities Property - Product Status](#vulnerabilities-property-product-status)  
			3.2.3.10 [Vulnerabilities Property - References](#vulnerabilities-property-references)  
			3.2.3.11 [Vulnerabilities Property - Release Date](#vulnerabilities-property-release-date)  
			3.2.3.12 [Vulnerabilities Property - Remediations](#vulnerabilities-property-remediations)  
				3.2.3.12.1 [Vulnerabilities Property - Remediations - Category](#vulnerabilities-property-remediations-category)  
				3.2.3.12.2 [Vulnerabilities Property - Remediations - Date](#vulnerabilities-property-remediations-date)  
				3.2.3.12.3 [Vulnerabilities Property - Remediations - Details](#vulnerabilities-property-remediations-details)  
				3.2.3.12.4 [Vulnerabilities Property - Remediations - Entitlements](#vulnerabilities-property-remediations-entitlements)  
				3.2.3.12.5 [Vulnerabilities Property - Remediations - Group IDs](#vulnerabilities-property-remediations-group-ids)  
				3.2.3.12.6 [Vulnerabilities Property - Remediations - Product IDs](#vulnerabilities-property-remediations-product-ids)  
				3.2.3.12.7 [Vulnerabilities Property - Remediations - Restart Required](#vulnerabilities-property-remediations-restart-required)  
				3.2.3.12.8 [Vulnerabilities Property - Remediations - URL](#vulnerabilities-property-remediations-url)  
			3.2.3.13 [Vulnerabilities Property - Scores](#vulnerabilities-property-scores)  
			3.2.3.14 [Vulnerabilities Property - Threats](#vulnerabilities-property-threats)  
			3.2.3.15 [Vulnerabilities Property - Title](#vulnerabilities-property-title)  
4. [Profiles](#profiles)  
	4.1 [Profile 1: CSAF Base](#profile-1-csaf-base)  
	4.2 [Profile 2: Security incident response](#profile-2-security-incident-response)  
	4.3 [Profile 3: Informational Advisory](#profile-3-informational-advisory)  
	4.4 [Profile 4: Security Advisory](#profile-4-security-advisory)  
	4.5 [Profile 5: VEX](#profile-5-vex)  
5. [Additional Conventions](#additional-conventions)  
	5.1 [Filename](#filename)  
	5.2 [Separation in Data Stream](#separation-in-data-stream)  
	5.3 [Sorting](#additional-conventions--sorting)  
6. [Tests](#tests)  
	6.1 [Mandatory Tests](#mandatory-tests)  
		6.1.1 [Missing Definition of Product ID](#missing-definition-of-product-id)  
		6.1.2 [Multiple Definition of Product ID](#multiple-definition-of-product-id)  
		6.1.3 [Circular Definition of Product ID](#circular-definition-of-product-id)  
		6.1.4 [Missing Definition of Product Group ID](#missing-definition-of-product-group-id)  
		6.1.5 [Multiple Definition of Product Group ID](#multiple-definition-of-product-group-id)  
		6.1.6 [Contradicting Product Status](#contradicting-product-status)  
		6.1.7 [Multiple Scores with same Version per Product](#multiple-scores-with-same-version-per-product)  
		6.1.8 [Invalid CVSS](#invalid-cvss)  
		6.1.9 [Invalid CVSS computation](#invalid-cvss-computation)  
		6.1.10 [Inconsistent CVSS](#inconsistent-cvss)  
		6.1.11 [CWE](#cwe)  
		6.1.12 [Language](#language)  
		6.1.13 [PURL](#purl)  
		6.1.14 [Sorted Revision History](#sorted-revision-history)  
		6.1.15 [Translator](#translator)  
		6.1.16 [Latest Document Version](#latest-document-version)  
		6.1.17 [Document Status Draft](#document-status-draft)  
		6.1.18 [Released Revision History](#released-revision-history)  
		6.1.19 [Revision History Entries for Pre-release Versions](#revision-history-entries-for-pre-release-versions)  
		6.1.20 [Non-draft Document Version](#non-draft-document-version)  
		6.1.21 [Missing Item in Revision History](#missing-item-in-revision-history)  
		6.1.22 [Multiple Definition in Revision History](#multiple-definition-in-revision-history)  
		6.1.23 [Multiple Use of Same CVE](#multiple-use-of-same-cve)  
		6.1.24 [Multiple Definition in Involvements](#multiple-definition-in-involvements)  
		6.1.25 [Multiple Use of Same Hash Algorithm](#multiple-use-of-same-hash-algorithm)  
		6.1.26 [Prohibited Document Category Name](#prohibited-document-category-name)  
		6.1.27 [Profile Tests](#profile-tests)  
			6.1.27.1 [Document Notes](#document-notes)  
			6.1.27.2 [Document References](#document-references)  
			6.1.27.3 [Vulnerabilities](#vulnerabilities-for-informational-advisory)  
			6.1.27.4 [Product Tree](#product-tree)  
			6.1.27.5 [Vulnerability Notes](#vulnerability-notes)  
			6.1.27.6 [Product Status](#product-status)  
			6.1.27.7 [VEX Product Status](#vex-product-status)  
			6.1.27.8 [Vulnerability ID](#vulnerability-id)  
			6.1.27.9 [Impact Statement](#impact-statement)  
			6.1.27.10 [Action Statement](#action-statement)  
			6.1.27.11 [Vulnerabilities](#vulnerabilities-for-security-advisory-or-vex)  
		6.1.28 [Translation](#translation)  
		6.1.29 [Remediation without Product Reference](#remediation-without-product-reference)  
		6.1.30 [Mixed Integer and Semantic Versioning](#mixed-integer-and-semantic-versioning)  
		6.1.31 [Version Range in Product Version](#version-range-in-product-version)  
		6.1.32 [Flag without Product Reference](#flag-without-product-reference)  
		6.1.33 [Multiple Flags with VEX Justification Codes per Product](#multiple-flags-with-vex-justification-codes-per-product)  
	6.2 [Optional Tests](#optional-tests)  
		6.2.1 [Unused Definition of Product ID](#unused-definition-of-product-id)  
		6.2.2 [Missing Remediation](#missing-remediation)  
		6.2.3 [Missing Score](#missing-score)  
		6.2.4 [Build Metadata in Revision History](#build-metadata-in-revision-history)  
		6.2.5 [Older Initial Release Date than Revision History](#older-initial-release-date-than-revision-history)  
		6.2.6 [Older Current Release Date than Revision History](#older-current-release-date-than-revision-history)  
		6.2.7 [Missing Date in Involvements](#missing-date-in-involvements)  
		6.2.8 [Use of MD5 as the only Hash Algorithm](#use-of-md5-as-the-only-hash-algorithm)  
		6.2.9 [Use of SHA-1 as the only Hash Algorithm](#use-of-sha-1-as-the-only-hash-algorithm)  
		6.2.10 [Missing TLP label](#missing-tlp-label)  
		6.2.11 [Missing Canonical URL](#missing-canonical-url)  
		6.2.12 [Missing Document Language](#missing-document-language)  
		6.2.13 [Sorting](#optional-tests--sorting)  
		6.2.14 [Use of Private Language](#use-of-private-language)  
		6.2.15 [Use of Default Language](#use-of-default-language)  
		6.2.16 [Missing Product Identification Helper](#missing-product-identification-helper)  
		6.2.17 [CVE in field IDs](#cve-in-field-ids)  
		6.2.18 [Product Version Range without vers](#product-version-range-without-vers)  
		6.2.19 [CVSS for Fixed Products](#cvss-for-fixed-products)  
		6.2.20 [Additional Properties](#additional-properties)  
	6.3 [Informative Test](#informative-test)  
		6.3.1 [Use of CVSS v2 as the only Scoring System](#use-of-cvss-v2-as-the-only-scoring-system)  
		6.3.2 [Use of CVSS v3.0](#use-of-cvss-v3-0)  
		6.3.3 [Missing CVE](#missing-cve)  
		6.3.4 [Missing CWE](#missing-cwe)  
		6.3.5 [Use of Short Hash](#use-of-short-hash)  
		6.3.6 [Use of non-self referencing URLs Failing to Resolve](#use-of-non-self-referencing-urls-failing-to-resolve)  
		6.3.7 [Use of self referencing URLs Failing to Resolve](#use-of-self-referencing-urls-failing-to-resolve)  
		6.3.8 [Spell check](#spell-check)  
		6.3.9 [Branch Categories](#branch-categories)  
		6.3.10 [Usage of Product Version Range](#usage-of-product-version-range)  
		6.3.11 [Usage of V as Version Indicator](#usage-of-v-as-version-indicator)  
7. [Distributing CSAF documents](#distributing-csaf-documents)  
	7.1 [Requirements](#requirements)  
		7.1.1 [Requirement 1: Valid CSAF document](#requirement-1-valid-csaf-document)  
		7.1.2 [Requirement 2: Filename](#requirement-2-filename)  
		7.1.3 [Requirement 3: TLS](#requirement-3-tls)  
		7.1.4 [Requirement 4: TLP:WHITE](#requirement-4-tlp-white)  
		7.1.5 [Requirement 5: TLP:AMBER and TLP:RED](#requirement-5-tlp-amber-and-tlp-red)  
		7.1.6 [Requirement 6: No Redirects](#requirement-6-no-redirects)  
		7.1.7 [Requirement 7: provider-metadata.json](#requirement-7-provider-metadata-json)  
		7.1.8 [Requirement 8: security.txt](#requirement-8-security-txt)  
		7.1.9 [Requirement 9: Well-known URL for provider-metadata.json](#requirement-9-well-known-url-for-provider-metadata-json)  
		7.1.10 [Requirement 10: DNS path](#requirement-10-dns-path)  
		7.1.11 [Requirement 11: One folder per year](#requirement-11-one-folder-per-year)  
		7.1.12 [Requirement 12: index.txt](#requirement-12-index-txt)  
		7.1.13 [Requirement 13: changes.csv](#requirement-13-changes-csv)  
		7.1.14 [Requirement 14: Directory listings](#requirement-14-directory-listings)  
		7.1.15 [Requirement 15: ROLIE feed](#requirement-15-rolie-feed)  
		7.1.16 [Requirement 16: ROLIE service document](#requirement-16-rolie-service-document)  
		7.1.17 [Requirement 17: ROLIE category document](#requirement-17-rolie-category-document)  
		7.1.18 [Requirement 18: Integrity](#requirement-18-integrity)  
		7.1.19 [Requirement 19: Signatures](#requirement-19-signatures)  
		7.1.20 [Requirement 20: Public OpenPGP Key](#requirement-20-public-openpgp-key)  
		7.1.21 [Requirement 21: List of CSAF providers](#requirement-21-list-of-csaf-providers)  
		7.1.22 [Requirement 22: Two disjoint issuing parties](#requirement-22-two-disjoint-issuing-parties)  
		7.1.23 [Requirement 23: Mirror](#requirement-23-mirror)  
	7.2 [Roles](#roles)  
		7.2.1 [Role: CSAF publisher](#role-csaf-publisher)  
		7.2.2 [Role: CSAF provider](#role-csaf-provider)  
		7.2.3 [Role: CSAF trusted provider](#role-csaf-trusted-provider)  
		7.2.4 [Role: CSAF lister](#role-csaf-lister)  
		7.2.5 [Role: CSAF aggregator](#role-csaf-aggregator)  
	7.3 [Retrieving rules](#retrieving-rules)  
		7.3.1 [Finding provider-metadata.json](#finding-provider-metadata-json)  
		7.3.2 [Retrieving CSAF documents](#retrieving-csaf-documents)  
8. [Safety, Security, and Data Protection Considerations](#safety-security-and-data-protection-considerations)  
9. [Conformance](#conformance)  
	9.1 [Conformance Targets](#conformance-targets)  
		9.1.1 [Conformance Clause 1: CSAF document](#conformance-clause-1-csaf-document)  
		9.1.2 [Conformance Clause 2: CSAF producer](#conformance-clause-2-csaf-producer)  
		9.1.3 [Conformance Clause 3: CSAF direct producer](#conformance-clause-3-csaf-direct-producer)  
		9.1.4 [Conformance Clause 4: CSAF converter](#conformance-clause-4-csaf-converter)  
		9.1.5 [Conformance Clause 5: CVRF CSAF converter](#conformance-clause-5-cvrf-csaf-converter)  
		9.1.6 [Conformance Clause 6: CSAF content management system](#conformance-clause-6-csaf-content-management-system)  
		9.1.7 [Conformance Clause 7: CSAF post-processor](#conformance-clause-7-csaf-post-processor)  
		9.1.8 [Conformance Clause 8: CSAF modifier](#conformance-clause-8-csaf-modifier)  
		9.1.9 [Conformance Clause 9: CSAF translator](#conformance-clause-9-csaf-translator)  
		9.1.10 [Conformance Clause 10: CSAF consumer](#conformance-clause-10-csaf-consumer)  
		9.1.11 [Conformance Clause 11: CSAF viewer](#conformance-clause-11-csaf-viewer)  
		9.1.12 [Conformance Clause 12: CSAF management system](#conformance-clause-12-csaf-management-system)  
		9.1.13 [Conformance Clause 13: CSAF asset matching system](#conformance-clause-13-csaf-asset-matching-system)  
		9.1.14 [Conformance Clause 14: CSAF basic validator](#conformance-clause-14-csaf-basic-validator)  
		9.1.15 [Conformance Clause 15: CSAF extended validator](#conformance-clause-15-csaf-extended-validator)  
		9.1.16 [Conformance Clause 16: CSAF full validator](#conformance-clause-16-csaf-full-validator)  
		9.1.17 [Conformance Clause 17: CSAF SBOM matching system](#conformance-clause-17-csaf-sbom-matching-system)  

Appendix A. [Acknowledgments](#acknowledgments)  
Appendix B. [Revision History](#revision-history)  
Appendix C. [Guidance on the Size of CSAF Documents](#guidance-on-the-size-of-csaf-documents)  
	C.1 [File size](#file-size)  
	C.2 [Array length](#array-length)  
	C.3 [String length](#string-length)  
	C.4 [URI length](#uri-length)  
	C.5 [Enum](#enum)  
	C.6 [Date](#date)  
-------

# 1. Introduction <a id='introduction'></a>

## 1.1 IPR Policy <a id='ipr-policy'></a>

This specification is provided under the [Non-Assertion](https://www.oasis-open.org/policies-guidelines/ipr/#Non-Assertion-Mode) Mode of
the [OASIS IPR Policy](https://www.oasis-open.org/policies-guidelines/ipr/), the mode chosen when the Technical Committee was established.
For information on whether any patents have been disclosed that may be essential to implementing this specification,
and any offers of patent licensing terms, please refer to the Intellectual Property Rights section of the TC's
web page ([https://www.oasis-open.org/committees/csaf/ipr.php](https://www.oasis-open.org/committees/csaf/ipr.php)).

## 1.2 Terminology <a id='terminology'></a>

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED",
"MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 \[[RFC2119](#RFC2119)\] and \[[RFC8174](#RFC8174)\] when,
and only when, they appear in all capitals, as shown here.

For purposes of this document, the following terms and definitions apply:

<dl>
  <dt id="def;advisory">advisory</dt>
  <dd>reporting item that describes a condition present in an artifact and that requires action by the consumers</dd>
  <dt id="def;advisory-document">advisory document</dt>
  <dd>artifact in which an analysis tool reports a result</dd>
  <dt id="def;advisory-management-system">advisory management system</dt>
  <dd>software system that consumes the documents produced by analysis tools,
      produces advisories that enable engineering and operating organizations to assess the quality of these
      software artifacts at a point in time, and performs functions such as filing security advisories and
      displaying information about individual advisories.
      <strong>Note</strong>: An advisory management system can interact with a document viewer to display information about individual advisories.</dd>
  <dt id="def;advisory-matching">advisory matching</dt>
  <dd>process of determining whether two advisories are targeting the same products and conditions</dd>
  <dt id="def;artifact">artifact</dt>
  <dd>sequence of bytes addressable via a URI.
      <em>Examples</em>: A physical file in a file system such as a source file, an object file, a configuration file or a data file;
      a specific version of a file in a version control system; a database table accessed via an HTTP request;
      an arbitrary stream of bytes returned from an HTTP request, a product URL, a common product enumeration value.</dd>
  <dt id="def;csaf-asset-matching-system">CSAF asset matching system</dt>
  <dd>program that connects to or is an asset database and is able to manage CSAF documents as
      required by CSAF management system
      as well as matching them to assets of the asset database.</dd>
  <dt id="def;csaf-basic-validator">CSAF basic validator</dt>
  <dd>A program that reads a document and checks it against the JSON schema and performs mandatory tests.</dd>
  <dt id="def;csaf-consumer">CSAF consumer</dt>
  <dd>program that reads and interprets a CSAF document</dd>
  <dt id="def;csaf-content-management-system">CSAF content management system</dt>
  <dd>program that is able to create, review and manage CSAF documents and is able to preview their details as
      required by CSAF viewer.</dd>
  <dt id="def;csaf-converter">CSAF converter</dt>
  <dd>CSAF producer that transforms the output of an analysis tool from its native output format into the CSAF format</dd>
  <dt id="def;csaf-direct-producer">CSAF direct producer</dt>
  <dd>analysis tool which acts as a CSAF producer</dd>
  <dt id="def;csaf-document">CSAF document</dt>
  <dd>security advisory text document in the format defined by this document.</dd>
  <dt id="def;csaf-extended-validator">CSAF extended validator</dt>
  <dd>A CSAF basic validator that additionally performs optional tests.</dd>
  <dt id="def;csaf-full-validator">CSAF full validator</dt>
  <dd>A CSAF extended validator that additionally performs informative tests.</dd>
  <dt id="def;csaf-management-system">CSAF management system</dt>
  <dd>program that is able to manage CSAF documents and is able to display their details as required by CSAF viewer.</dd>
  <dt id="def;csaf-modifier">CSAF modifier</dt>
  <dd>CSAF post-processor which takes a CSAF document as input and modifies the structure or values of properties.
      The output is a valid CSAF document.</dd>
  <dt id="def;csaf-post-processor">CSAF post-processor</dt>
  <dd>CSAF producer that transforms an existing CSAF document into a new CSAF document,
      for example, by removing or redacting elements according to sharing policies.</dd>
  <dt id="def;csaf-sbom-matching-system">CSAF SBOM matching system</dt>
  <dd>A program that connects to or is an SBOM database and is able to manage CSAF documents as
      required by CSAF management system as well as matching them to SBOM components of the SBOM database.</dd>
  <dt id="def;csaf-producer">CSAF producer</dt>
  <dd>program that emits output in the CSAF format</dd>
  <dt id="def;csaf-translator">CSAF translator</dt>
  <dd>CSAF post-processor which takes a CSAF document as input and translates values of properties into another language.
      The output is a valid CSAF document.</dd>
  <dt id="def;csaf-viewer">CSAF viewer</dt>
  <dd>CSAF consumer that reads a CSAF document, displays a list of the results it contains,
      and allows an end user to view each result in the context of the artifact in which it occurs.</dd>
  <dt id="def;cvrf-csaf-converter">CVRF CSAF converter</dt>
  <dd>CSAF producer which takes a CVRF document as input and converts it into a valid CSAF document.</dd>
  <dt id="def;document">document</dt>
  <dd>output file produced by an analysis tool, which enumerates the results produced by the tool</dd>
  <dt id="def;driver">driver</dt>
  <dd>tool component containing an analysis tool’s or converter’s primary executable,
      which controls the tool’s or converter’s execution,
      and which in the case of an analysis tool typically defines a set of analysis rules</dd>
  <dt id="def;embedded-link">embedded link</dt>
  <dd>syntactic construct which enables a message string to refer to a location mentioned in the document</dd>
  <dt id="def;empty-array">empty array</dt>
  <dd>array that contains no elements, and so has a length of 0</dd>
  <dt id="def;empty-object">empty object</dt>
  <dd>object that contains no properties</dd>
  <dt id="def;empty-string">empty string</dt>
  <dd>string that contains no characters, and so has a length of 0</dd>
  <dt id="def;end-user">(end) user</dt>
  <dd>person who uses the information in a document to investigate, triage, or resolve results</dd>
  <dt id="def;engineering-system">engineering system</dt>
  <dd>software analysis environment within which analysis tools execute.
      <strong>Note</strong>: An engineering system might include a build system, a source control system, a result management system,
      a bug tracking system, a test execution system, and so on.</dd>
  <dt id="def;extension">extension</dt>
  <dd>tool component other than the driver (for example, a plugin, a configuration file, or a taxonomy)</dd>
  <dt id="def;external-property-file">external property file</dt>
  <dd>file containing the values of one or more externalized properties</dd>
  <dt id="def;externalizable-property">externalizable property</dt>
  <dd>property that can be contained in an external property file</dd>
  <dt id="def;externalized-property">externalized property</dt>
  <dd>property stored outside of the CSAF document to which it logically belongs</dd>
  <dt id="def;false-positive">false positive</dt>
  <dd>result which an end user decides does not actually represent a problem</dd>
  <dt id="def;fingerprint">fingerprint</dt>
  <dd>stable value that can be used by a result management system to uniquely identify a result over time,
      even if a relevant artifact is modified</dd>
  <dt id="def;formatted-message">formatted message</dt>
  <dd>message string which contains formatting information such as Markdown formatting characters</dd>
  <dt id="def;fully-qualified-logical-name">fully qualified logical name</dt>
  <dd>string that fully identifies the programmatic construct specified by a logical location,
      typically by means of a hierarchical identifier.</dd>
  <dt id="def;hierarchical-string">hierarchical string</dt>
  <dd>string in the format &lt;component>{/&lt;component>}*</dd>
  <dt id="def;line">line</dt>
  <dd>contiguous sequence of characters, starting either at the beginning of an artifact or immediately after
      a newline sequence, and ending at and including the nearest subsequent newline sequence, if one is present,
      or else extending to the end of the artifact</dd>
  <dt id="def;line-number">line (number)</dt>
  <dd>1-based index of a line within a file.
      <strong>Note</strong>: Abbreviated to "line" when there is no danger of ambiguity with "line" in the sense of a sequence of characters.</dd>
  <dt id="def;localizable">localizable</dt>
  <dd>subject to being translated from one natural language to another</dd>
  <dt id="def;message-string">message string</dt>
  <dd>human-readable string that conveys information relevant to an element in a CSAF document</dd>
  <dt id="def;nested-artifact">nested artifact</dt>
  <dd>artifact that is contained within another artifact</dd>
  <dt id="def;newline-sequence">newline sequence</dt>
  <dd>sequence of one or more characters representing the end of a line of text.
      <strong>Note</strong>: Some systems represent a newline sequence with a single newline character; others represent it as
      a carriage return character followed by a newline character.</dd>
  <dt id="def;notification">notification</dt>
  <dd>reporting item that describes a condition encountered by a tool during its execution</dd>
  <dt id="def;opaque">opaque</dt>
  <dd>neither human-readable nor machine-parsable into constituent parts</dd>
  <dt id="def;parent-artifact">parent (artifact)</dt>
  <dd>artifact which contains one or more nested artifacts</dd>
  <dt id="def;plain-text-message">plain text message</dt>
  <dd>message string which does not contain any formatting information</dd>
  <dt id="def;plugin">plugin</dt>
  <dd>tool component that defines additional rules</dd>
  <dt id="def;policy">policy</dt>
  <dd>set of rule configurations that specify how results that
      violate the rules defined by a particular tool component are to be treated</dd>
  <dt id="def;problem">problem</dt>
  <dd>result which indicates a condition that has the potential to detract from the quality of the program.
      <em>Examples</em>: A security vulnerability, a deviation from contractual or legal requirements.</dd>
  <dt id="def;product">product</dt>
  <dd>is any deliverable (e.g. software, hardware, specification,...) which can be referred to with a name.
      This applies regardless of the origin, the license model, or the mode of distribution of the deliverable.</dd>
  <dt id="def;property">property</dt>
  <dd>attribute of an object consisting of a name and a value associated with the name</dd>
  <dt id="def;redactable-property">redactable property</dt>
  <dd>property that potentially contains sensitive information that a CSAF direct producer or
      a CSAF post-processor might wish to redact</dd>
  <dt id="def;reporting-item">reporting item</dt>
  <dd>unit of output produced by a tool, either a result or a notification</dd>
  <dt id="def;reporting-configuration">reporting configuration</dt>
  <dd>the subset of reporting metadata that a tool can configure at runtime, before performing its scan.
      <em>Examples</em>: severity level, rank</dd>
  <dt id="def;repository">repository</dt>
  <dd>container for a related set of files in a version control system</dd>
  <dt id="def;taxonomy">taxonomy</dt>
  <dd>classification of analysis results into a set of categories</dd>
  <dt id="def;tag">tag</dt>
  <dd>string that conveys additional information about the CSAF document element to which it applies</dd>
  <dt id="def;text-artifact">text artifact</dt>
  <dd>artifact considered as a sequence of characters organized into lines and columns</dd>
  <dt id="def;text-region">text region</dt>
  <dd>region representing a contiguous range of zero or more characters in a text artifact</dd>
  <dt id="def;tool-component">tool component</dt>
  <dd>component of an analysis tool or converter, either its driver or an extension, consisting of one or more files</dd>
  <dt id="def;top-level-artifact">top-level artifact</dt>
  <dd>artifact which is not contained within any other artifact</dd>
  <dt id="def;translation">translation</dt>
  <dd>rendering of a tool component's localizable strings into another language</dd>
  <dt id="def;triage">triage</dt>
  <dd>decide whether a result indicates a problem that needs to be corrected</dd>
  <dt id="def;user">user</dt>
  <dd>see end user.</dd>
  <dt id="def;vcs">VCS</dt>
  <dd>version control system</dd>
  <dt id="def;vendor">vendor</dt>
  <dd>the community, individual, or organization that created or maintains a product
      (including open source software and hardware providers)</dd>
  <dt id="def;vex">VEX</dt>
  <dd>Vulnerability Exploitability eXchange - enables a supplier or other party to assert whether or not
      a particular product is affected by a specific vulnerability, especially helpful in efficiently consuming SBOM data.</dd>
  <dt id="def;viewer">viewer</dt>
  <dd>see CSAF viewer.</dd>
  <dt id="def;vulnerability">vulnerability</dt>
  <dd>functional behavior of a product or service that violates an implicit or explicit security policy
      (conforming to ISO/IEC 29147 <a href="#ISO29147">cite</a>)</dd>
  <dt id="def;xml">XML</dt>
  <dd>eXtensible Markup Language - the format used by the predecessors of this standard, namely CVRF 1.1 and CVRF 1.2.</dd>
</dl>

## 1.3 Normative References <a id='normative-references'></a>

**\[**<span id="https;//datatracker.ietf.org/doc/html/draft-bhutton-json-schema-00." class="anchor"></span>**https://datatracker.ietf.org/doc/html/draft-bhutton-json-schema-00.\]** 

**\[**<span id="https;//datatracker.ietf.org/doc/html/draft-bhutton-json-schema-validation-00." class="anchor"></span>**https://datatracker.ietf.org/doc/html/draft-bhutton-json-schema-validation-00.\]** 

**\[**<span id="https;//json-schema.org/draft/2019-09/json-schema-hypermedia.html." class="anchor"></span>**https://json-schema.org/draft/2019-09/json-schema-hypermedia.html.\]** 

**\[**<span id="https;//datatracker.ietf.org/doc/html/draft-bhutton-relative-json-pointer-00." class="anchor"></span>**https://datatracker.ietf.org/doc/html/draft-bhutton-relative-json-pointer-00.\]** 

**\[**<span id="https;//www.rfc-editor.org/info/rfc2119." class="anchor"></span>**https://www.rfc-editor.org/info/rfc2119.\]** 

**\[**<span id="https;//www.rfc-editor.org/info/rfc7464." class="anchor"></span>**https://www.rfc-editor.org/info/rfc7464.\]** 

**\[**<span id="https;//www.rfc-editor.org/info/rfc8174." class="anchor"></span>**https://www.rfc-editor.org/info/rfc8174.\]** 

**\[**<span id="https;//www.rfc-editor.org/info/rfc8259." class="anchor"></span>**https://www.rfc-editor.org/info/rfc8259.\]** 

## 1.4 Informative References <a id='informative-references'></a>

**\[**<span id="CPE23-A" class="anchor"></span>**CPE23-A\]** _Common Platform Enumeration: Applicability Language Specification Version 2.3 (NISTIR 7698)_, D. Waltermire, P. Cichonski, K. Scarfone, Editors, NIST Interagency Report 7698, August 2011, https://dx.doi.org/10.6028/NIST.IR.7698.

**\[**<span id="CPE23-D" class="anchor"></span>**CPE23-D\]** _Common Platform Enumeration: Dictionary Specification Version 2.3_, P. Cichonski, D. Waltermire, K. Scarfone, Editors, NIST Interagency Report 7697, August 2011, https://dx.doi.org/10.6028/NIST.IR.7697.

**\[**<span id="CPE23-M" class="anchor"></span>**CPE23-M\]** _Common Platform Enumeration: Naming Matching Specification Version 2.3_, M. Parmelee, H. Booth, D. Waltermire, K. Scarfone, Editors, NIST Interagency Report 7696, August 2011, https://dx.doi.org/10.6028/NIST.IR.7696.

**\[**<span id="CPE23-N" class="anchor"></span>**CPE23-N\]** _Common Platform Enumeration: Naming Specification Version 2.3_, B. Cheikes, D. Waltermire, K. Scarfone, Editors, NIST Interagency Report 7695, August 2011, https://dx.doi.org/10.6028/NIST.IR.7695.

**\[**<span id="CVE" class="anchor"></span>**CVE\]** _Common Vulnerability and Exposures (CVE) – The Standard for Information Security Vulnerability Names_, MITRE, 1999, https://cve.mitre.org/about/.

**\[**<span id="CVE-NF" class="anchor"></span>**CVE-NF\]** _Common Vulnerability and Exposures (CVE) – The Standard for Information Security Vulnerability Names - CVE ID Syntax Change_, MITRE, January 01, 2014, https://cve.mitre.org/cve/identifiers/syntaxchange.html.

**\[**<span id="CVRF-1-1" class="anchor"></span>**CVRF-1-1\]** _The Common Vulnerability Reporting Framework (CVRF) Version 1.1_, M. Schiffman, Editor, May 2012, Internet Consortium for Advancement of Security on the Internet (ICASI), https://www.icasi.org/the-common-vulnerability-reporting-framework-cvrf-v1-1/.

**\[**<span id="CVRF-v1.2" class="anchor"></span>**CVRF-v1.2\]** _CSAF Common Vulnerability Reporting Framework (CVRF) Version 1.2_. Edited by Stefan Hagen. 13 September 2017. OASIS Committee Specification 01. https://docs.oasis-open.org/csaf/csaf-cvrf/v1.2/cs01/csaf-cvrf-v1.2-cs01.html. Latest version: https://docs.oasis-open.org/csaf/csaf-cvrf/v1.2/csaf-cvrf-v1.2.html.

**\[**<span id="CVSS2" class="anchor"></span>**CVSS2\]** _A Complete Guide to the Common Vulnerability Scoring System Version 2.0_, P. Mell, K. Scarfone, S. Romanosky, Editors, First.org, Inc., June 2007, https://www.first.org/cvss/cvss-v2-guide.pdf.

**\[**<span id="CVSS30" class="anchor"></span>**CVSS30\]** _Common Vulnerability Scoring System v3.0: Specification Document_, FIRST.Org, Inc., June 2019, https://www.first.org/cvss/v3.0/cvss-v30-specification_v1.9.pdf.

**\[**<span id="CVSS31" class="anchor"></span>**CVSS31\]** _Common Vulnerability Scoring System v3.1: Specification Document_, FIRST.Org, Inc., June 2019, https://www.first.org/cvss/v3-1/cvss-v31-specification_r1.pdf.

**\[**<span id="CWE" class="anchor"></span>**CWE\]** _Common Weakness Enumeration (CWE) – A Community-Developed List of Software Weakness Types_, MITRE, 2005, http://cwe.mitre.org/about/.

**\[**<span id="CYCLONEDX13" class="anchor"></span>**CYCLONEDX13\]** _CycloneDX Software Bill-of-Material Specification JSON schema version 1.3_, cyclonedx.org, May 2021, https://github.com/CycloneDX/specification/blob/1.3/schema/bom-1.3.schema.json.

**\[**<span id="GFMCMARK" class="anchor"></span>**GFMCMARK\]** _GitHub's fork of cmark, a CommonMark parsing and rendering library and program in C_, https://github.com/github/cmark.

**\[**<span id="GFMENG" class="anchor"></span>**GFMENG\]** _GitHub Engineering: A formal spec for GitHub Flavored Markdown_, https://githubengineering.com/a-formal-spec-for-github-markdown/.

**\[**<span id="ISO8601" class="anchor"></span>**ISO8601\]** _Data elements and interchange formats — Information interchange — Representation of dates and times_, International Standard, ISO 8601:2004(E), December 1, 2004, https://www.iso.org/standard/40874.html.

**\[**<span id="ISO19770-2" class="anchor"></span>**ISO19770-2\]** _Information technology — IT asset management — Part 2: Software identification tag_, International Standard, ISO 19770-2:2015, September 30, 2015, <https://www.iso.org/standard/65666.html>.

**\[**<span id="<https;//www.iso.org/standard/72311.html>." class="anchor"></span>**<https://www.iso.org/standard/72311.html>.\]** 

**\[**<span id="OPENSSL" class="anchor"></span>**OPENSSL\]** _GTLS/SSL and crypto library_, OpenSSL Software Foundation, https://www.openssl.org/.

**\[**<span id="PURL" class="anchor"></span>**PURL\]** _Package URL (PURL)_, GitHub Project, https://github.com/package-url/purl-spec.

**\[**<span id="https;//www.rfc-editor.org/info/rfc3339." class="anchor"></span>**https://www.rfc-editor.org/info/rfc3339.\]** 

**\[**<span id="https;//www.rfc-editor.org/info/rfc3552." class="anchor"></span>**https://www.rfc-editor.org/info/rfc3552.\]** 

**\[**<span id="January 2005, https;//www.rfc-editor.org/info/rfc3986." class="anchor"></span>**January 2005, https://www.rfc-editor.org/info/rfc3986.\]** 

**\[**<span id="https;//www.rfc-editor.org/info/rfc4880." class="anchor"></span>**https://www.rfc-editor.org/info/rfc4880.\]** 

**\[**<span id="June 2014, https;//www.rfc-editor.org/info/rfc7231." class="anchor"></span>**June 2014, https://www.rfc-editor.org/info/rfc7231.\]** 

**\[**<span id="https;//www.rfc-editor.org/info/rfc7464." class="anchor"></span>**https://www.rfc-editor.org/info/rfc7464.\]** 

**\[**<span id="https;//www.rfc-editor.org/info/rfc8615." class="anchor"></span>**https://www.rfc-editor.org/info/rfc8615.\]** 

**\[**<span id="https;//www.rfc-editor.org/info/rfc9116." class="anchor"></span>**https://www.rfc-editor.org/info/rfc9116.\]** 

**\[**<span id="S. Quinn, K. Scarfone, A. Halbardier, Editors, NIST Spec. Publ. 800‑126 rev. 2, September 2011, https;//dx.doi.org/10.6028/NIST.SP.800-126r2." class="anchor"></span>**S. Quinn, K. Scarfone, A. Halbardier, Editors, NIST Spec. Publ. 800‑126 rev. 2, September 2011, https://dx.doi.org/10.6028/NIST.SP.800-126r2.\]** 

**\[**<span id="SECURITY-TXT" class="anchor"></span>**SECURITY-TXT\]** Foudil, E. and Shafranovich, Y., _Security.txt Project_, https://securitytxt.org/.

**\[**<span id="SemVer" class="anchor"></span>**SemVer\]** _Semantic Versioning 2.0.0_, T. Preston-Werner, June 2013, https://semver.org/.

**\[**<span id="https;//spdx.github.io/spdx-spec/." class="anchor"></span>**https://spdx.github.io/spdx-spec/.\]** 

**\[**<span id="https;//github.com/package-url/purl-spec/blob/version-range-spec/VERSION-RANGE-SPEC.rst." class="anchor"></span>**https://github.com/package-url/purl-spec/blob/version-range-spec/VERSION-RANGE-SPEC.rst.\]** 

**\[**<span id="27 September 2021, <https;//ntia.gov/files/ntia/publications/vex_one-page_summary.pdf>." class="anchor"></span>**27 September 2021, <https://ntia.gov/files/ntia/publications/vex_one-page_summary.pdf>.\]** 

**\[**<span id="XX May 2022, https;//www.cisa.gov/sites/default/files/publications/VEX_Status_Justification_Jun22.pdf." class="anchor"></span>**XX May 2022, https://www.cisa.gov/sites/default/files/publications/VEX_Status_Justification_Jun22.pdf.\]** 

**\[**<span id="W3C Recommendation, November 26, 2008, https;//www.w3.org/TR/2008/REC-xml-20081126/. Latest version available at <https;//www.w3.org/TR/xml>." class="anchor"></span>**W3C Recommendation, November 26, 2008, https://www.w3.org/TR/2008/REC-xml-20081126/. Latest version available at <https://www.w3.org/TR/xml>.\]** 

**\[**<span id="Latest version available at <https;//www.w3.org/TR/xmlschema11-1/>." class="anchor"></span>**Latest version available at <https://www.w3.org/TR/xmlschema11-1/>.\]** 

**\[**<span id="https;//www.w3.org/TR/2012/REC-xmlschema11-2-20120405/. Latest version available at <https;//www.w3.org/TR/xmlschema11-2/>." class="anchor"></span>**https://www.w3.org/TR/2012/REC-xmlschema11-2-20120405/. Latest version available at <https://www.w3.org/TR/xmlschema11-2/>.\]** 

## 1.5 Typographical Conventions <a id='typographical-conventions'></a>

Keywords defined by this specification use this `monospaced` font.

```
    Normative source code uses this paragraph style.
```

Some sections of this specification are illustrated with non-normative examples introduced with "Example" or "Examples" like so:

*Example 1:*<a id='typographical-conventions-eg-1'></a><a id='sec-1-5-eg-1'></a><a id='example-4321'></a>

```
    Informative examples also use this paragraph style but preceded by the text "Example(s)".
```

All examples in this document are informative only.

All other text is normative unless otherwise labeled e.g. like the following informative comment:

> This is a pure informative comment that may be present, because the information conveyed is deemed useful advice or
> common pitfalls learned from implementer or operator experience and often given including the rationale.

-------

# 2. Design Considerations <a id='design-considerations'></a>

The Common Security Advisory Framework (CSAF) is a language to exchange Security Advisories formulated in JSON.

The term Security Advisory as used in this document describes any notification of security issues in products of and by providers.
Anyone providing a product is considered in this document as a vendor, i.e. developers or maintainers of information system products or services.
This includes all authoritative product vendors, Product Security Incident Response Teams (PSIRTs), and product resellers and distributors,
including authoritative vendor partners.
A security issue is not necessarily constrained to a problem statement, the focus of the term is on the security aspect impacting
(or not impacting) specific product-platform-version combinations.
Information on presence or absence of workarounds is also considered part of the security issue.
This document is the definitive reference for the language elements of CSAF version 2.0.
The encompassing JSON schema file noted in the Additional Artifacts section of the title page SHALL be taken as normative in the case
a gap or an inconsistency in this explanatory document becomes evident.
The following presentation in this section is grouped by topical area, and is not simply derivative documentation from the schema document itself.
The information contained aims to be more descriptive and complete.
Where applicable, common conventions are stated and known common issues in usage are pointed out informatively to support
implementers of document producers and consumers alike.

This minimal required information set does not provide any useful information on products, vulnerabilities, or security advisories.
Thus, any real-world Security Advisory will carry additional information as specified in section 3 Schema elements.

Care has been taken, to design the containers for product and vulnerability information to support fine-grained mapping of
security advisories onto product and vulnerability and minimize data duplication through referencing.
The display of the elements representing Product Tree and Vulnerability information has been placed in the sections named accordingly.

## 2.1 Construction Principles <a id='construction-principles'></a>

A Security Advisory defined as a CSAF document is the result of complex orchestration of many players and distinct and
partially difficult to play schemas.

The format chosen is [JSONSchema] which allows validation and delegation to sub schema providers.
The latter aligns well with separation of concerns and shares the format family of information interchange utilized by
the providers of product and vulnerability information which migrated from XML to JSON since the creation of CSAF CVRF version 1.2,
the predecessor of this specification.

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

A dictionary like presentation of all defined schema elements is given in the section [3](#schema-elements).
Any expected relations to other elements (linkage) is described there. This linking relies on setting attribute values accordingly
(mostly guided by industry best practice and conventions) and thus implies,
that any deep validation on a semantic level (e.g. does the CWE match the described vulnerability)
is to be ensured by the producer and consumer of CSAF documents.
It is out of scope for this specification.

Proven and intended usage patterns from practice are given where possible.

Delegation to industry best practices technologies is used in referencing schemas for:

* Platform Data:
  * Common Platform Enumeration (CPE) Version 2.3 \[[CPE23-N](#CPE23-N)\]
* Vulnerability Scoring:
  * Common Vulnerability Scoring System (CVSS) Version 3.1 \[[CVSS31](#CVSS31)\]
    * JSON Schema Reference https://www.first.org/cvss/cvss-v3.1.json
  * Common Vulnerability Scoring System (CVSS) Version 3.0 \[[CVSS30](#CVSS30)\]
    * JSON Schema Reference https://www.first.org/cvss/cvss-v3.0.json
  * Common Vulnerability Scoring System (CVSS) Version 2.0 \[[CVSS2](#CVSS2)\]
    * JSON Schema Reference https://www.first.org/cvss/cvss-v2.0.json
* Vulnerability Classification
  * Common Weakness Enumeration (CWE) \[[CWE](#CWE)\]
    * CWE List: http://cwe.mitre.org/data/index.html
* Classification for Document Distribution
  * Traffic Light Protocol (TLP)
    * Default Definition: https://www.first.org/tlp/

Even though the JSON schema does not prohibit specifically additional properties and custom keywords,
it is strongly recommended not to use them. Suggestions for new fields SHOULD be made through issues in the TC's GitHub.

> The standardized fields allow for scalability across different issuing parties and dramatically reduce the human effort and
> need for dedicated parsers as well as other tools on the side of the consuming parties.

Section [4](#profiles) defined profiles that are used to ensure a common understanding of which fields are required in a given use case.
Additional conventions are stated in section [5](#additional-conventions).
The tests given in section [6](#tests) support CSAF producers and
consumers to verify rules from the specification which can not be tested by the schema.
Section [7](#distributing-csaf-documents) states how to distribute and where to find CSAF documents.
Safety, Security and Data Protection are considered in section [8](#safety-security-and-data-protection-considerations).
Finally, a set of conformance targets describes tools in the ecosystem.

-------

# 3. Schema Elements <a id='schema-elements'></a>

The CSAF schema describes how to represent security advisory information as a JSON document.

The CSAF schema Version 2.0 builds on the JSON Schema draft 2020-12 rules.

```
    "$schema": "https://json-schema.org/draft/2020-12/schema"
```

The schema identifier is:

```
    "$id": "https://docs.oasis-open.org/csaf/csaf/v2.0/csaf_json_schema.json"
```

The further documentation of the schema is organized via Definitions and Properties.

* Definitions provide types that extend the JSON schema model
* Properties use these types to support assembling security advisories

Types and properties together provide the vocabulary for the domain specific language supporting security advisories.

The single mandatory property is `document`.
The optional two additional properties are `product_tree` and `vulnerabilities`.

## 3.1 Definitions <a id='definitions'></a>

The definitions (`$defs`) introduce the following domain specific types into the CSAF language:
Acknowledgments (`acknowledgments_t`), Branches (`branches_t`), Full Product Name (`full_product_name_t`), Language (`lang_t`), Notes (`notes_t`),
Product Group ID (`product_group_id_t`), Product Groups (`product_groups_t`), Product ID (`product_id_t`), Products (`products_t`),
References (`references_t`), and Version (`version_t`).

```
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
        "product_group_id_t": {
            // ...
        },
        "product_groups_t": {
             // ...
        },
        "product_id_t": {
            // ...
        },
        "products_t": {
            // ...
        },
        "references_t": {
            // ...
        },
        "version_t": {
            // ...
        }
    },
```

### 3.1.1 Acknowledgments Type <a id='acknowledgments-type'></a>

List of Acknowledgments (`acknowledgments_t`) type instances of value type `array` with 1 or more elements contain
a list of `Acknowledgment` elements.

```
    "acknowledgments_t": {
      // ...
      "items": {
        // ...
      }
    },
```

The value type of Acknowledgment is `object` with at least 1 and at most 4 properties. Every such element acknowledges contributions by
describing those that contributed.
The properties are: `names`, `organization`, `summary`, and `urls`.

```
        "properties": {
          "names": {
            // ...
          },
          "organization": {
            // ...
          },
          "summary": {
            // ...
          },
          "urls": {
            // ...
          }
        }
```

#### 3.1.1.1 Acknowledgments Type - Names <a id='acknowledgments-type-names'></a>

List of acknowledged names (`names`) has value type `array` with 1 or more items holds the names of contributors being recognized.
Every such item of value type `string` with 1 or more characters represents the name of the contributor and contains the name of
a single contributor being recognized.

*Examples 1:*<a id='acknowledgments-type-names-eg-1'></a><a id='sec-3-1-1-1-eg-1'></a><a id='example-1'></a>

```
    Albert Einstein
    Johann Sebastian Bach
```

#### 3.1.1.2 Acknowledgments Type - Organization <a id='acknowledgments-type-organization'></a>

The contributing organization (`organization`) has value type `string` with 1 or more characters and holds the name of
the contributing organization being recognized.

*Examples 1:*<a id='acknowledgments-type-organization-eg-1'></a><a id='sec-3-1-1-2-eg-1'></a><a id='example-2'></a>

```
    CISA
    Google Project Zero
    Talos
```

#### 3.1.1.3 Acknowledgments Type - Summary <a id='acknowledgments-type-summary'></a>

Summary of the acknowledgment (`summary`) of value type `string` with 1 or more characters SHOULD represent any contextual details
the document producers wish to make known about the acknowledgment or acknowledged parties.

*Example 1:*<a id='acknowledgments-type-summary-eg-1'></a><a id='sec-3-1-1-3-eg-1'></a><a id='example-3'></a>

```
    First analysis of Coordinated Multi-Stream Attack (CMSA)
```

#### 3.1.1.4 Acknowledgments Type - URLs <a id='acknowledgments-type-urls'></a>

List of URLs (`urls`) of acknowledgment is a container (value type `array`) for 1 or more `string` of type URL that specifies
a list of URLs or location of the reference to be acknowledged.
Any URL of acknowledgment contains the URL or location of the reference to be acknowledged.
Value type is string with format URI (`uri`).

#### 3.1.1.5 Acknowledgments Type - Example <a id='acknowledgments-type-example'></a>

*Example 1:*<a id='acknowledgments-type-example-eg-1'></a><a id='sec-3-1-1-5-eg-1'></a><a id='example-4'></a>

```
  "acknowledgments": [
    {
      "names": [
        "Johann Sebastian Bach",
        "Georg Philipp Telemann",
        "Georg Friedrich Händel"
      ],
      "organization": "Baroque composers",
      "summary": "wonderful music"
    },
    {
      "organization": "CISA",
      "summary": "coordination efforts",
      "urls": [
        "https://cisa.gov"
      ]
    },
    {
      "organization": "BSI",
      "summary": "assistance in coordination"
    },
    {
      "names": [
        "Antonio Vivaldi"
      ],
      "summary": "influencing other composers"
    }
  ],
```

The example \[[1](#acknowledgments-type-example-eg-1)\] above SHOULD lead to the following outcome in a human-readable advisory:

> We thank the following parties for their efforts:
>
> * Johann Sebastian Bach, Georg Philipp Telemann, Georg Friedrich Händel from Baroque composers for wonderful music
> * CISA for coordination efforts (see: https://cisa.gov)
> * BSI for assistance in coordination
> * Antonio Vivaldi for influencing other composers

### 3.1.2 Branches Type <a id='branches-type'></a>

List of branches (`branches_t`) with value type `array` contains 1 or more branch elements as children of the current element.

```
    "branches_t": {
      //...
      "items": {
        // ...
      }
    },
```

Every Branch holds exactly 3 properties and is a part of the hierarchical structure of the product tree.
The properties `name` and `category` are mandatory. In addition, the object contains either a `branches` or a `product` property.

```
        "properties": {
          "branches": {
            // ...
          },
          "category": {
            // ...
          },
          "name": {
            // ...
          },
          "product": {
            // ...
          }
        }
```

> `branches_t` supports building a hierarchical structure of products that allows to indicate the relationship of products to each other and
> enables grouping for simpler referencing.
> As an example, the structure MAY use the following levels: `vendor` -> `product_family` -> `product_name` -> `product_version`.
> It is recommended to use the hierarchical structure of `vendor` -> `product_name` -> `product_version` whenever possible to support
> the identification and matching of products on the consumer side.

#### 3.1.2.1 Branches Type - Branches <a id='branches-type-branches'></a>

List of branches (`branches`) has the value type `branches_t`.

#### 3.1.2.2 Branches Type - Category <a id='branches-type-category'></a>

Category of the branch (`category`) of value type `string` and `enum` describes the characteristics of the labeled branch.
Valid `enum` values are:

```
    architecture
    host_name
    language
    legacy
    patch_level
    product_family
    product_name
    product_version
    product_version_range
    service_pack
    specification
    vendor
```

The value `architecture` indicates the architecture for which the product is intended.

The value `host_name` indicates the host name of a system/service.

The value `language` indicates the language of the product.

The value `legacy` indicates an entry that has reached its end of life.

The value `patch_level` indicates the patch level of the product.

The value `product_family` indicates the product family that the product falls into.

The value `product_name` indicates the name of the product.

The value `product_version` indicates exactly a single version of the product.
The value of the adjacent `name` property can be numeric or some other descriptor.
However, it MUST NOT contain version ranges of any kind.

> It is recommended to enumerate versions wherever possible. Nevertheless, the TC understands that this is sometimes impossible.
> To reflect that in the specification and aid in automatic processing of CSAF documents the value `product_version_range` was introduced.
> See next section for details.

The value `product_version_range` indicates a range of versions for the product.
The value of the adjacent `name` property SHOULD NOT be used to convey a single version.

The value `service_pack` indicates the service pack of the product.

The value `specification` indicates the specification such as a standard, best common practice, etc.

The value `vendor` indicates the name of the vendor or manufacturer that makes the product.

#### 3.1.2.3 Branches Type - Name <a id='branches-type-name'></a>

Name of the branch (`name`) of value type `string` with 1 or more characters contains the canonical descriptor or 'friendly name' of the branch.

*Examples 1:*<a id='branches-type-name-eg-1'></a><a id='sec-3-1-2-3-eg-1'></a><a id='example-5'></a>

```
    10
    365
    Microsoft
    Office
    PCS 7
    SIMATIC
    Siemens
    Windows
```

A leading `v` or `V` in the value of `name` SHOULD only exist for the categories `product_version` or `product_version_range` if it is
part of the product version as given by the vendor.

##### 3.1.2.3.1 Branches Type - Name under Product Version <a id='branches-type-name-under-product-version'></a>

If adjacent property `category` has the value `product_version`, the value of `name` MUST NOT contain version ranges of any kind.

*Examples 1 (for `name` when using `product_version`):*<a id='branches-type-name-under-product-version-eg-1'></a><a id='sec-3-1-2-3-1-eg-1'></a><a id='example-6'></a>

```
    10
    17.4
    v3
```

> The `product_version` is the easiest way for users to determine whether their version is meant
> (provided that the given ancestors in the product tree matched):
> If both version strings are the same, it is a match - otherwise not.
> Therefore, it is always recommended to enumerate product versions instead of providing version ranges.

*Examples 2 (for `name` when using `product_version` which are invalid):*<a id='branches-type-name-under-product-version-eg-2'></a><a id='sec-3-1-2-3-1-eg-2'></a><a id='example-7'></a>

```
    8.0.0 - 8.0.1
    8.1.5 and later
    <= 2
    prior to 4.2
    All versions < V3.0.29
    V3.0, V4.0, V4.1, V4.2
```

> All the examples above contain some kind of a version range and are therefore invalid under the category `product_version`.

##### 3.1.2.3.2 Branches Type - Name under Product Version Range <a id='branches-type-name-under-product-version-range'></a>

If adjacent property `category` has the value `product_version_range`, the value of `name` MUST contain version ranges.
The value of MUST obey to exactly one of the following options:

1. Version Range Specifier (vers)

    > vers is an ongoing community effort to address the problem of version ranges. Its draft specification is available at \[[VERS](#VERS)\].

    vers MUST be used in its canonical form. To convey the term "all versions" the special string `vers:all/*` MUST be used.

    *Examples 1 (for `name` when using `product_version_range` with vers):*<a id='branches-type-name-under-product-version-range-eg-1'></a><a id='sec-3-1-2-3-2-eg-1'></a><a id='example-8'></a>

    ```
        vers:gem/>=2.2.0|!= 2.2.1|<2.3.0
        vers:npm/1.2.3|>=2.0.0|<5.0.0
        vers:pypi/0.0.0|0.0.1|0.0.2|0.0.3|1.0|2.0pre1
        vers:tomee/>=8.0.0-M1|<=8.0.1
    ```

    > Through the definitions of the vers specification a user can compute whether a given version is in a given range.

2. Vers-like Specifier (vls)

    This option uses only the `<version-constraint>` part from the vers specification. It MUST NOT have an URI nor the `<versioning-scheme>` part.
    It is a fallback option and SHOULD NOT be used unless really necessary.
    > The reason for that is, that it is nearly impossible for tools to reliable determine whether a given version is in the range or not.

    Tools MAY support this on best effort basis.

    *Examples 2 (for `name` when using `product_version_range` with vls):*<a id='branches-type-name-under-product-version-range-eg-2'></a><a id='sec-3-1-2-3-2-eg-2'></a><a id='example-9'></a>

    ```
        <=2
        <4.2
        <V3.0.29
        >=8.1.5
    ```

#### 3.1.2.4 Branches Type - Product <a id='branches-type-product'></a>

Product (`product`) has the value type Full Product Name (`full_product_name_t`).

### 3.1.3 Full Product Name Type <a id='full-product-name-type'></a>

Full Product Name (`full_product_name_t`) with value type `object` specifies information about the product and assigns the product ID.
The properties `name` and `product_id` are required. The property `product_identification_helper` is optional.

```
    "full_product_name_t": {
      // ...
      "properties": {
        "name": {
          // ...
        },
        "product_id": {
          // ...
        },
        "product_identification_helper": {
          // ...
        }
      }
    },
```

#### 3.1.3.1 Full Product Name Type - Name <a id='full-product-name-type-name'></a>

Textual description of the product (`name`) has value type `string` with 1 or more characters.
The value SHOULD be the product's full canonical name, including version number and other attributes,
as it would be used in a human-friendly document.

*Examples 1:*<a id='full-product-name-type-name-eg-1'></a><a id='sec-3-1-3-1-eg-1'></a><a id='example-10'></a>

```
    Cisco AnyConnect Secure Mobility Client 2.3.185
    Microsoft Host Integration Server 2006 Service Pack 1
```

#### 3.1.3.2 Full Product Name Type - Product ID <a id='full-product-name-type-product-id'></a>

Product ID (`product_id`) holds a value of type Product ID (`product_id_t`).

#### 3.1.3.3 Full Product Name Type - Product Identification Helper <a id='full-product-name-type-product-identification-helper'></a>

Helper to identify the product (`product_identification_helper`) of value type `object` provides in its properties at least
one method which aids in identifying the product in an asset database.
Of the given eight properties `cpe`, `hashes`, `model_numbers`, `purl`, `sbom_urls`, `serial_numbers`, `skus`,
and `x_generic_uris`, one is mandatory.

```
    "product_identification_helper": {
      // ...
      "properties": { 
        "cpe": {
          // ...
        },
        "hashes": {
          // ...
        },
        "model_numbers": {
          // ...
        },
        "purl": {
          // ...
        },
        "sbom_urls": {
          // ...
        },
        "serial_numbers": {
          // ...
        },
        "skus": {
          // ...
        },
        "x_generic_uris": {
          // ...
        }
      }
```

##### 3.1.3.3.1 Full Product Name Type - Product Identification Helper - CPE <a id='full-product-name-type-product-identification-helper-cpe'></a>

Common Platform Enumeration representation (`cpe`) of value type `string` of 5 or more characters with `pattern` (regular expression):

```
    ^(cpe:2\\.3:[aho\\*\\-](:(((\\?*|\\*?)([a-zA-Z0-9\\-\\._]|(\\\\[\\\\\\*\\?!\"#\\$%&'\\(\\)\\+,/:;<=>@\\[\\]\\^`\\{\\|\\}~]))+(\\?*|\\*?))|[\\*\\-])){5}(:(([a-zA-Z]{2,3}(-([a-zA-Z]{2}|[0-9]{3}))?)|[\\*\\-]))(:(((\\?*|\\*?)([a-zA-Z0-9\\-\\._]|(\\\\[\\\\\\*\\?!\"#\\$%&'\\(\\)\\+,/:;<=>@\\[\\]\\^`\\{\\|\\}~]))+(\\?*|\\*?))|[\\*\\-])){4})|([c][pP][eE]:/[AHOaho]?(:[A-Za-z0-9\\._\\-~%]*){0,6})$
```

The Common Platform Enumeration (CPE) attribute refers to a method for naming platforms external to this specification.
See [CPE23-N] for details.

##### 3.1.3.3.2 Full Product Name Type - Product Identification Helper - Hashes <a id='full-product-name-type-product-identification-helper-hashes'></a>

List of hashes (`hashes`) of value type `array` holding at least one item contains a list of cryptographic hashes usable to identify files.

```
    "hashes": {
      // ...
      "items": {
        // ...
      }
    },
```

Cryptographic hashes of value type `object` contains all information to identify a file based on its cryptographic hash values.
Any cryptographic hashes object has the 2 mandatory properties `file_hashes` and `filename`.

```
        "properties": {
          "file_hashes": {
            // ...
          },
          "filename": {
            // ...
          }
        }
```

List of file hashes (`file_hashes`) of value type `array` holding at least one item contains a list of cryptographic hashes for this file.

```
    "file_hashes": {
      // ...
      "items": {
        // ...
      }
    },
```

Each File hash of value type `object` contains one hash value and algorithm of the file to be identified.
Any File hash object has the 2 mandatory properties `algorithm` and `value`.

```
        "properties": {
          "algorithm": {
            // ...
          },
          "value": {
            // ...
          }
        }
```

The algorithm of the cryptographic hash representation (`algorithm`) of value type `string` with one or more characters contains
the name of the cryptographic hash algorithm used to calculate the value.
The default value for `algorithm` is `sha256`.

*Examples 1:*<a id='full-product-name-type-product-identification-helper-hashes-eg-1'></a><a id='sec-3-1-3-3-2-eg-1'></a><a id='example-11'></a>

```
      blake2b512
      sha256
      sha3-512
      sha384
      sha512
```

These values are derived from the currently supported digests OpenSSL \[[OPENSSL](#OPENSSL)\]. Leading dashes were removed.

> The command `openssl dgst -list` (Version 1.1.1f from 2020-03-31) outputs the following:
>
>```
>  Supported digests:
>  -blake2b512                -blake2s256                -md4                      
>  -md5                       -md5-sha1                  -ripemd                   
>  -ripemd160                 -rmd160                    -sha1                     
>  -sha224                    -sha256                    -sha3-224                 
>  -sha3-256                  -sha3-384                  -sha3-512                 
>  -sha384                    -sha512                    -sha512-224               
>  -sha512-256                -shake128                  -shake256                 
>  -sm3                       -ssl3-md5                  -ssl3-sha1                
>  -whirlpool
>```

The Value of the cryptographic hash representation (`value`) of value type `string` of 32 or more characters with `pattern` (regular expression):

```
    ^[0-9a-fA-F]{32,}$
```

The Value of the cryptographic hash attribute contains the cryptographic hash value in hexadecimal representation.

*Examples 2:*<a id='full-product-name-type-product-identification-helper-hashes-eg-2'></a><a id='sec-3-1-3-3-2-eg-2'></a><a id='example-12'></a>

```
    37df33cb7464da5c7f077f4d56a32bc84987ec1d85b234537c1c1a4d4fc8d09dc29e2e762cb5203677bf849a2855a0283710f1f5fe1d6ce8d5ac85c645d0fcb3
    4775203615d9534a8bfca96a93dc8b461a489f69124a130d786b42204f3341cc
    9ea4c8200113d49d26505da0e02e2f49055dc078d1ad7a419b32e291c7afebbb84badfbd46dec42883bea0b2a1fa697c
```

The filename representation (`filename`) of value type `string` with one or more characters contains the name of
the file which is identified by the hash values.

*Examples 3:*<a id='full-product-name-type-product-identification-helper-hashes-eg-3'></a><a id='sec-3-1-3-3-2-eg-3'></a><a id='example-13'></a>

```
    WINWORD.EXE
    msotadddin.dll
    sudoers.so
```

If the value of the hash matches and the filename does not, a user SHOULD prefer the hash value.
In such cases, the filename SHOULD be used as informational property.

##### 3.1.3.3.3 Full Product Name Type - Product Identification Helper - Model Numbers <a id='full-product-name-type-product-identification-helper-model-numbers'></a>

The list of models (`model_numbers`) of value type `array` with 1 or more unique items contains a list of full or
abbreviated (partial) model numbers.

A list of models SHOULD only be used if a certain range of model numbers with its corresponding software version is affected,
or the model numbers change during update.

This can also be used to identify hardware.
If necessary, the software, or any other related part, SHALL be bind to that via a product relationship.

```
    "model_numbers": {
        //...
      "items": {
        //...
      }
    },
```

Any given model number of value type `string` with at least 1 character represents a full or abbreviated (partial) model number of
the component to identify.

> The terms "model", "model number" and "model variant" are mostly used synonymously.
> Often it is abbreviated as "MN", M/N" or "model no.".

If a part of a model number of the component to identify is given,
it SHOULD begin with the first character of the model number and stop at any point.
Characters which SHOULD NOT be matched MUST be replaced by either `?` (for a single character) or `*` (for zero or more characters).  
Two `*` MUST NOT follow each other.

*Examples 1:*<a id='full-product-name-type-product-identification-helper-model-numbers-eg-1'></a><a id='sec-3-1-3-3-3-eg-1'></a><a id='example-14'></a>

```
    6RA8096-4MV62-0AA0
    6RA801?-??V62-0AA0
    IC25T060ATCS05-0
```

##### 3.1.3.3.4 Full Product Name Type - Product Identification Helper - PURL <a id='full-product-name-type-product-identification-helper-purl'></a>

The package URL (PURL) representation (`purl`) is a `string` of 7 or more characters with `pattern` (regular expression):

```
    ^pkg:[A-Za-z\\.\\-\\+][A-Za-z0-9\\.\\-\\+]*/.+
```

> The given pattern does not completely evaluate whether a PURL is valid according to the \[[PURL](#PURL)\] specification.
> It provides a more generic approach and general guidance to enable forward compatibility.
> CSAF uses only the canonical form of PURL to conform with section 3.3 of \[[RFC3986](#RFC3986)\].
> Therefore, URLs starting with `pkg://` are considered invalid.

This package URL (PURL) attribute refers to a method for reliably identifying and locating software packages external to this specification.
See \[[PURL](#PURL)\] for details.

##### 3.1.3.3.5 Full Product Name Type - Product Identification Helper - SBOM URLs <a id='full-product-name-type-product-identification-helper-sbom-urls'></a>

The list of SBOM URLs (`sbom_urls`) of value type `array` with 1 or more items contains
a list of URLs where SBOMs for this product can be retrieved.

> The SBOMs might differ in format or depth of detail. Currently supported formats are SPDX, CycloneDX, and SWID.

```
    "sbom_urls": {
        //...
      "items": {
        //...
      }
    },
```

Any given SBOM URL of value type `string` with format `uri` contains a URL of one SBOM for this product.

*Examples 1:*<a id='full-product-name-type-product-identification-helper-sbom-urls-eg-1'></a><a id='sec-3-1-3-3-5-eg-1'></a><a id='example-15'></a>

```
    https://raw.githubusercontent.com/CycloneDX/bom-examples/master/SBOM/keycloak-10.0.2/bom.json
    https://swinslow.net/spdx-examples/example4/main-bin-v2
```

##### 3.1.3.3.6 Full Product Name Type - Product Identification Helper - Serial Numbers <a id='full-product-name-type-product-identification-helper-serial-numbers'></a>

The list of serial numbers (`serial_numbers`) of value type `array` with 1 or more unique items contains
a list of full or abbreviated (partial) serial numbers.

A list of serial numbers SHOULD only be used if a certain range of serial numbers with its corresponding software version is affected,
or the serial numbers change during update.

```
    "serial_numbers": {
        //...
      "items": {
        //...
      }
    },
```

Any given serial number of value type `string` with at least 1 character represents a full or
abbreviated (partial) serial number of the component to identify.

If a part of a serial number of the component to identify is given,
it SHOULD begin with the first character of the serial number and stop at any point.
Characters which SHOULD NOT be matched MUST be replaced by either `?` (for a single character) or `*` (for zero or more characters).  
Two `*` MUST NOT follow each other.

##### 3.1.3.3.7 Full Product Name Type - Product Identification Helper - SKUs <a id='full-product-name-type-product-identification-helper-skus'></a>

The list of stock keeping units (`skus`) of value type `array` with 1 or more items contains a list of full or
abbreviated (partial) stock keeping units.

A list of stock keeping units SHOULD only be used if the list of relationships is used to decouple e.g. hardware from the software,
or the stock keeping units change during update.
In the latter case the remediations SHALL include the new stock keeping units is or a description how it can be obtained.

> The use of the list of relationships in the first case is important.
> Otherwise, the end user is unable to identify which version (the affected or the not affected / fixed one) is used.

```
    "skus": {
        //...  
      "items": {
        //...  
      }
    },
```

Any given stock keeping unit of value type `string` with at least 1 character represents a full or
abbreviated (partial) stock keeping unit (SKU) of the component to identify.

> Sometimes this is also called "item number", "article number" or "product number".

If a part of a stock keeping unit of the component to identify is given, it SHOULD begin with the first character of
the stock keeping unit and stop at any point.
Characters which SHOULD NOT be matched MUST be replaced by either `?` (for a single character) or `*` (for zero or more characters).  
Two `*` MUST NOT follow each other.

##### 3.1.3.3.8 Full Product Name Type - Product Identification Helper - Generic URIs <a id='full-product-name-type-product-identification-helper-generic-uris'></a>

List of generic URIs (`x_generic_uris`) of value type `array` with at least 1 item contains a list of identifiers which are
either vendor-specific or derived from a standard not yet supported.

```
    "x_generic_uris": {
      // ...
      "items": {
        // ...
      }
    }  
```

Any such Generic URI item of value type `object` provides the two mandatory properties Namespace (`namespace`) and URI (`uri`).

```
        "properties": {
          "namespace": {
            // ...
          },
          "uri": {
            // ...
          }
        }
```

The namespace of the generic URI (`namespace`) of value type `string` with format `uri` refers to a URL which provides
the name and knowledge about the specification used or is the namespace in which these values are valid.

The URI (`uri`) of value type `string` with format `uri` contains the identifier itself.

> These elements can be used to reference a specific component from an SBOM:

*Example 1 (linking a component from a CycloneDX SBOM using the bomlink mechanism):*<a id='full-product-name-type-product-identification-helper-generic-uris-eg-1'></a><a id='sec-3-1-3-3-8-eg-1'></a><a id='example-16'></a>

```
          "x_generic_uris": [
            {
              "namespace": "https://cyclonedx.org/capabilities/bomlink/",
              "uri": "urn:cdx:411dafd2-c29f-491a-97d7-e97de5bc2289/1#pkg:maven/org.jboss.logging/jboss-logging@3.4.1.Final?type=jar"
            }
          ]
```

*Example 2 (linking a component from an SPDX SBOM):*<a id='full-product-name-type-product-identification-helper-generic-uris-eg-2'></a><a id='sec-3-1-3-3-8-eg-2'></a><a id='example-17'></a>

```
          "x_generic_uris": [
            {
              "namespace": "https://spdx.github.io/spdx-spec/document-creation-information/#65-spdx-document-namespace-field",
              "uri": "https://swinslow.net/spdx-examples/example4/main-bin-v2#SPDXRef-libc"
            }
          ]
```

### 3.1.4 Language Type <a id='language-type'></a>

Language type (`lang_t`) has value type `string` with `pattern` (regular expression):

```
    ^(([A-Za-z]{2,3}(-[A-Za-z]{3}(-[A-Za-z]{3}){0,2})?|[A-Za-z]{4,8})(-[A-Za-z]{4})?(-([A-Za-z]{2}|[0-9]{3}))?(-([A-Za-z0-9]{5,8}|[0-9][A-Za-z0-9]{3}))*(-[A-WY-Za-wy-z0-9](-[A-Za-z0-9]{2,8})+)*(-[Xx](-[A-Za-z0-9]{1,8})+)?|[Xx](-[A-Za-z0-9]{1,8})+|[Ii]-[Dd][Ee][Ff][Aa][Uu][Ll][Tt]|[Ii]-[Mm][Ii][Nn][Gg][Oo])$
```

The value identifies a language, corresponding to IETF BCP 47 / RFC 5646.
See IETF language registry: <https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry>

> CSAF skips those grandfathered language tags that are deprecated at the time of writing the specification.
> Even though the private use language tags are supported they should not be used to ensure readability across the ecosystem.
> It is recommended to follow the conventions for the capitalization of the subtags even though it is not mandatory as most users are used to that.

*Examples 1:*<a id='language-type-eg-1'></a><a id='sec-3-1-4-eg-1'></a><a id='example-18'></a>

```
    de
    en
    fr
    frc
    jp
```

### 3.1.5 Notes Type <a id='notes-type'></a>

List of notes (`notes_t`) of value type `array` with 1 or more items of type `Note` contains notes which are specific to the current context.

```
    "notes_t": {
      // ...
      "items": {
        // ...
      }
    },
```

Value type of every such Note item is `object` with the mandatory properties `category` and `text` providing a place to put
all manner of text blobs related to the current context.
A Note `object` MAY provide the optional properties `audience` and `title`.

```
    "properties": {
      "audience": {
        // ...
      },
      "category": {
        // ...
      },
      "text": {
        // ...
      },
      "title": {
        // ...
      }
    }
```

Audience of note (`audience`) of value type `string` with 1 or more characters indicates who is intended to read it.

*Examples 1:*<a id='notes-type-eg-1'></a><a id='sec-3-1-5-eg-1'></a><a id='example-19'></a>

```
    all
    executives
    operational management and system administrators
    safety engineers
```

Note category (`category`) of value type `string` and `enum` contains the information of what kind of note this is.
Valid `enum` values are:

```
    description
    details
    faq
    general
    legal_disclaimer
    other
    summary
```

The value `description` indicates the note is a description of something.
The optional sibling property `title` MAY have more information in this case.

The value `details` indicates the note is a low-level detailed discussion.
The optional sibling property `title` MAY have more information in this case.

The value `faq` indicates the note is a list of frequently asked questions.

The value `general` indicates the note is a general, high-level note.
The optional sibling property `title` MAY have more information in this case.

The value `legal_disclaimer` indicates the note represents any possible legal discussion, including constraints, surrounding the document.

The value `other` indicates the note is something that doesn’t fit the other categories.
The optional sibling attribute `title` SHOULD have more information to indicate clearly what kind of note to expect in this case.

The value `summary` indicates the note is a summary of something.
The optional sibling property `title` MAY have more information in this case.

Note content (`text`) of value type `string` with 1 or more characters holds the content of the note.
Content varies depending on type.

Title of note (`title`) of value type `string` with 1 or more characters provides a concise description of what
is contained in the text of the note.

*Examples 2:*<a id='notes-type-eg-2'></a><a id='sec-3-1-5-eg-2'></a><a id='example-20'></a>

```
    Details
    Executive summary
    Technical summary
    Impact on safety systems
```

### 3.1.6 Product Group ID Type <a id='product-group-id-type'></a>

The Product Group ID Type (`product_group_id_t`) of value type `string` with 1 or more characters is a reference token for product group instances.
The value is a token required to identify a group of products so that it can be referred to from other parts in the document.
There is no predefined or required format for the Product Group ID (`product_group_id`) as long as it uniquely identifies
a product group in the context of the current document.

```
    "product_group_id_t": {
      // ...
    },
```

*Examples 1:*<a id='product-group-id-type-eg-1'></a><a id='sec-3-1-6-eg-1'></a><a id='example-21'></a>

```
    CSAFGID-0001
    CSAFGID-0002
    CSAFGID-0020
```

> Even though the standard does not require a specific format it is recommended to use different prefixes for the Product ID and
> the Product Group ID to support reading and parsing the document.

### 3.1.7 Product Groups Type <a id='product-groups-type'></a>

List of Product Group ID (`product_groups_t`) of value type `array` with 1 or more unique items (a `set`) of type
Product Group ID (`product_group_id_t`) specifies a list of `product_group_ids` to give context to the parent item.

```
    "product_groups_t": {
      // ...
      "items": {
        // ...
      }
    },
```

### 3.1.8 Product ID Type <a id='product-id-type'></a>

The Product ID Type (`product_id_t`) of value type `string` with 1 or more characters is a reference token for product instances.
The value is a token required to identify a `full_product_name` so that it can be referred to from other parts in the document.
There is no predefined or required format for the Product ID (`product_id`) as long as it uniquely identifies a product in the context of
the current document.

```
    "product_id_t": {
      // ...
    },
```

*Examples 1:*<a id='product-id-type-eg-1'></a><a id='sec-3-1-8-eg-1'></a><a id='example-22'></a>

```
    CSAFPID-0004
    CSAFPID-0008
```

> Even though the standard does not require a specific format it is recommended to use different prefixes for the Product ID and
> the Product Group ID to support reading and parsing the document.

### 3.1.9 Products Type <a id='products-type'></a>

List of Product IDs (`products_t`) of value type `array` with 1 or more unique items (a `set`) of type
Product ID (`product_id_t`) specifies a list of `product_ids` to give context to the parent item.

```
    "products_t": {
      // ...
      "items": {
        // ...
      }
    },
```

### 3.1.10 References Type <a id='references-type'></a>

List of references (`references_t`) of value type `array` with 1 or more items of type Reference holds a list of Reference objects.

```
    "references_t": {
      // ...
      "items": {
        // ...
      }
    },
```

Value type of every such Reference item is `object` with the mandatory properties `url` and `summary` holding any reference to conferences,
papers, advisories, and other resources that are related and considered related to either a surrounding part of or
the entire document and to be of value to the document consumer.
A reference `object` MAY provide the optional property `category`.

```
    "properties": {
      "category": {
        // ...
      },
      "summary": {
        // ...
      },
      "url": {
        // ...
      }
    }
```

Category of reference (`category`) of value type `string` and `enum` indicates whether the reference points to the same document or
vulnerability in focus (depending on scope) or to an external resource.
Valid `enum` values are:

```
    external
    self
```

The default value for `category` is `external`.

The value `external` indicates, that this document is an external reference to a document or vulnerability in focus (depending on scope).

The value `self` indicates, that this document is a reference to this same document or vulnerability (also depending on scope).

> This includes links to documents with the same content but different file format (e.g. advisories as PDF or HTML).

Summary of the reference (`summary`) of value type `string` with 1 or more characters indicates what this reference refers to.

URL of reference (`url`) of value type `string` with format `uri` provides the URL for the reference.

### 3.1.11 Version Type <a id='version-type'></a>

The Version (`version_t`) type has value type `string` with `pattern` (regular expression):

```
    ^(0|[1-9][0-9]*)$|^((0|[1-9]\\d*)\\.(0|[1-9]\\d*)\\.(0|[1-9]\\d*)(?:-((?:0|[1-9]\\d*|\\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\\.(?:0|[1-9]\\d*|\\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\\+([0-9a-zA-Z-]+(?:\\.[0-9a-zA-Z-]+)*))?)$
```

The version specifies a version string to denote clearly the evolution of the content of the document.
There are two options how it can be used:

* semantic versioning (preferred; according to the rules below)
* integer versioning

A CSAF document MUST use only one versioning system.

*Examples 1:*<a id='version-type-eg-1'></a><a id='sec-3-1-11-eg-1'></a><a id='example-23'></a>

```
    1
    4
    0.9.0
    1.4.3
    2.40.0+21AF26D3
```

#### 3.1.11.1 Version Type - Integer versioning <a id='version-type-integer-versioning'></a>

Integer versioning increments for each version where the `/document/tracking/status` is `final` the version number by one.
The regular expression for this type is:

```
^(0|[1-9][0-9]*)$
```

The following rules apply:

1. Once a versioned document has been released, the contents of that version MUST NOT be modified.
   Any modifications MUST be released as a new version.
2. Version zero (0) is for initial development before the `initial_release_date`.
   The document status MUST be `draft`. Anything MAY change at any time. The document SHOULD NOT be considered stable.
3. Version 1 defines the initial public release.
   Each new version where `/document/tracking/status` is `final` has a version number incremented by one.
4. Pre-release versions (document status `draft`) MUST carry the new version number.
   Sole exception is before the initial release (see rule 2).
   The combination of document status `draft` and version 1 MAY be used to indicate that the content is unlikely to change.
5. Build metadata is never included in the version.
6. Precedence MUST be calculate by integer comparison.

#### 3.1.11.2 Version Type - Semantic versioning <a id='version-type-semantic-versioning'></a>

Semantic versioning derived the rules from [SemVer]. The regular expression for this type is:

```
^((0|[1-9]\\d*)\\.(0|[1-9]\\d*)\\.(0|[1-9]\\d*)(?:-((?:0|[1-9]\\d*|\\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\\.(?:0|[1-9]\\d*|\\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\\+([0-9a-zA-Z-]+(?:\\.[0-9a-zA-Z-]+)*))?)$
```

The goal of this structure is to provide additional information to the end user whether a new comparison with the asset database is needed.
The "public API" in regards to CSAF is the CSAF document with its structure and content.
This results in the following rules:

1. A normal version number MUST take the form X.Y.Z where X, Y, and Z are non-negative integers, and MUST NOT contain leading zeroes.
   X is the major version, Y is the minor version, and Z is the patch version. Each element MUST increase numerically.
   For instance: 1.9.0 -> 1.10.0 -> 1.11.0.
2. Once a versioned document has been released, the contents of that version MUST NOT be modified.
   Any modifications MUST be released as a new version.
3. Major version zero (0.y.z) is for initial development before the `initial_release_date`.
   The document status MUST be `draft`. Anything MAY change at any time.
   The document SHOULD NOT be considered stable. Changes which would increment the major version according to rule 7 are
   tracked in this stage with (0.y.z) by incrementing the minor version y instead.
   Changes that would increment the minor or patch version according to rule 6 or 5 are both tracked in this stage with
   (0.y.z) by incrementing the patch version z instead.
4. Version 1.0.0 defines the initial public release.
   The way in which the version number is incremented after this release is dependent on the content and structure of
   the document and how it changes.
5. Patch version Z (x.y.Z | x > 0) MUST be incremented if only backwards compatible bug fixes are introduced.
   A bug fix is defined as an internal change that fixes incorrect behavior.

   > In the context of the document this is the case e.g. for spelling mistakes.

6. Minor version Y (x.Y.z | x > 0) MUST be incremented if the content of an existing element changes except for
   those which are covert through rule 7. It MUST be incremented if substantial new information are introduced or new elements are provided.
   It MAY include patch level changes. Patch version MUST be reset to 0 when minor version is incremented.
7. Major version X (X.y.z | X > 0) MUST be incremented if a new comparison with the end user's asset database is required.
   This includes:

   * changes (adding, removing elements or modifying content) in `/product_tree` or elements which contain `/product_tree` in their path
   * adding or removing items of `/vulnerabilities`
   * adding or removing elements in:
     * `/vulnerabilities[]/product_status/first_affected`
     * `/vulnerabilities[]/product_status/known_affected`
     * `/vulnerabilities[]/product_status/last_affected`
   * removing elements from:
     * `/vulnerabilities[]/product_status/first_fixed`
     * `/vulnerabilities[]/product_status/fixed`
     * `/vulnerabilities[]/product_status/known_not_affected`

   It MAY also include minor and patch level changes.
   Patch and minor version MUST be reset to 0 when major version is incremented.
8. A pre-release version (document status `draft`) MAY be denoted by appending a hyphen and a series of dot separated identifiers immediately
   following the patch version. Identifiers MUST comprise only ASCII alphanumerics and hyphens [0-9A-Za-z-].
   Identifiers MUST NOT be empty. Numeric identifiers MUST NOT include leading zeroes.
   Pre-release versions have a lower precedence than the associated normal version.
   A pre-release version indicates that the version is unstable and might not satisfy the intended compatibility requirements as
   denoted by its associated normal version.

   *Examples 1:*<a id='version-type-semantic-versioning-eg-1'></a><a id='sec-3-1-11-2-eg-1'></a><a id='example-24'></a>

   ```
   1.0.0-0.3.7
   1.0.0-alpha
   1.0.0-alpha.1
   1.0.0-x-y-z.–
   1.0.0-x.7.z.92
   ```

9. Pre-release MUST NOT be included if `/document/tracking/status` is `final`.
10. Build metadata MAY be denoted by appending a plus sign and a series of dot separated identifiers immediately following
    the patch or pre-release version. Identifiers MUST comprise only ASCII alphanumerics and hyphens [0-9A-Za-z-].
    Identifiers MUST NOT be empty. Build metadata MUST be ignored when determining version precedence.
    Thus two versions that differ only in the build metadata, have the same precedence.

    *Examples 2:*<a id='version-type-semantic-versioning-eg-2'></a><a id='sec-3-1-11-2-eg-2'></a><a id='example-25'></a>

    ```
    1.0.0+20130313144700
    1.0.0+21AF26D3—-117B344092BD
    1.0.0-alpha+001
    1.0.0-beta+exp.sha.5114f85
    ```

11. Precedence refers to how versions are compared to each other when ordered.

    1. Precedence MUST be calculated by separating the version into major, minor,
       patch and pre-release identifiers in that order (Build metadata does not figure into precedence).
    2. Precedence is determined by the first difference when comparing each of these identifiers from left to right as follows:
       Major, minor, and patch versions are always compared numerically.

       *Example 3:*<a id='version-type-semantic-versioning-eg-3'></a><a id='sec-3-1-11-2-eg-3'></a><a id='example-26'></a>

       ```
       1.0.0 < 2.0.0 < 2.1.0 < 2.1.1
       ```

    3. When major, minor, and patch are equal, a pre-release version has lower precedence than a normal version:

       *Example 4:*<a id='version-type-semantic-versioning-eg-4'></a><a id='sec-3-1-11-2-eg-4'></a><a id='example-27'></a>

       ```
       1.0.0-alpha < 1.0.0
       ```

    4. Precedence for two pre-release versions with the same major, minor,
       and patch version MUST be determined by comparing each dot separated identifier from left to right until a difference is found as follows:

       1. Identifiers consisting of only digits are compared numerically.
       2. Identifiers with letters or hyphens are compared lexically in ASCII sort order.
       3. Numeric identifiers always have lower precedence than non-numeric identifiers.
       4. A larger set of pre-release fields has a higher precedence than a smaller set, if all of the preceding identifiers are equal.

       *Example 5:*<a id='version-type-semantic-versioning-eg-5'></a><a id='sec-3-1-11-2-eg-5'></a><a id='example-28'></a>

       ```
       1.0.0-alpha < 1.0.0-alpha.1 < 1.0.0-alpha.beta < 1.0.0-beta < 1.0.0-beta.2 < 1.0.0-beta.11 < 1.0.0-rc.1 < 1.0.0
       ```

## 3.2 Properties <a id='properties'></a>

These final three subsections document the three properties of a CSAF document.
The single mandatory property `document`, as well as the optional properties `product_tree` and `vulnerabilities` in that order.

### 3.2.1 Document Property <a id='document-property'></a>

Document level meta-data (`document`) of value type `object` with the 5 mandatory properties Category (`category`),
CSAF Version (`csaf_version`), Publisher (`publisher`), Title (`title`),
and  Tracking (`tracking`) captures the meta-data about this document describing a particular set of security advisories.
In addition, the `document` object MAY provide the 7 optional properties Acknowledgments (`acknowledgments`),
Aggregate Severity (`aggregate_severity`), Distribution (`distribution`), Language (`lang`), Notes (`notes`),
References (`references`), and Source Language (`source_lang`).

```
    "document": {
      // ...
      "properties": {
        "acknowledgments": {
          // ...
        },
        "aggregate_severity" : {
          // ...
        },
        "category": {
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
        "notes": {
          // ...
        },
        "publisher": {
          // ...
        },
        "references": {
          // ...
        },
        "source_lang": {
          // ...
        },
        "title": {
          // ...
        },
        "tracking": {
          // ...
        }
      }
    },
```

#### 3.2.1.1 Document Property - Acknowledgments <a id='document-property-acknowledgments'></a>

Document acknowledgments (`acknowledgments`) of value type Acknowledgments Type (`acknowledgments_t`) contains
a list of acknowledgment elements associated with the whole document.

```
    "acknowledgments": {
      // ...
    },
```

#### 3.2.1.2 Document Property - Aggregate Severity <a id='document-property-aggregate-severity'></a>

Aggregate severity (`aggregate_severity`) of value type `object` with the mandatory property `text` and
the optional property `namespace` is a vehicle that is provided by the document producer to convey the urgency and
criticality with which the one or more vulnerabilities reported should be addressed.
It is a document-level metric and applied to the document as a whole — not any specific vulnerability.
The range of values in this field is defined according to the document producer's policies and procedures.

```
    "aggregate_severity": {
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
```

The Namespace of aggregate severity (`namespace`) of value type `string` with format `uri` points to the namespace so referenced.

The Text of aggregate severity (`text`) of value type `string` with 1 or more characters provides a severity which is
independent of - and in addition to - any other standard metric for determining the impact or severity of a given vulnerability (such as CVSS).

*Examples 1:*<a id='document-property-aggregate-severity-eg-1'></a><a id='sec-3-2-1-2-eg-1'></a><a id='example-29'></a>

```
    Critical
    Important
    Moderate
```

#### 3.2.1.3 Document Property - Category <a id='document-property-category'></a>

Document category (`category`) with value type `string` of 1 or more characters with `pattern` (regular expression):

```
    ^[^\\s\\-_\\.](.*[^\\s\\-_\\.])?$
```

Document category defines a short canonical name, chosen by the document producer, which will inform the end user as to the category of document.

> It is directly related to the profiles defined in section [4](#profiles).

```
    "category": {
      // ...
    }
```

*Examples 1:*<a id='document-property-category-eg-1'></a><a id='sec-3-2-1-3-eg-1'></a><a id='example-30'></a>

```
    csaf_base
    csaf_security_advisory
    csaf_vex
    Example Company Security Notice
```

#### 3.2.1.4 Document Property - CSAF Version <a id='document-property-csaf-version'></a>

CSAF version (`csaf_version`) of value type `string` and `enum` gives the version of the CSAF specification which the document was generated for.
The single valid value for this `enum` is:

```
    2.0
```

#### 3.2.1.5 Document Property - Distribution <a id='document-property-distribution'></a>

Rules for sharing document (`distribution`) of value type `object` with at least 1 of the 2 properties Text (`text`) and
Traffic Light Protocol (TLP) (`tlp`) describes any constraints on how this document might be shared.

```
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
```

If both values are present, the TLP information SHOULD be preferred as this aids in automation.

##### 3.2.1.5.1 Document Property - Distribution - Text <a id='document-property-distribution-text'></a>

The Textual description (`text`) of value type `string` with 1 or more characters provides a textual description of additional constraints.

*Examples 1:*<a id='document-property-distribution-text-eg-1'></a><a id='sec-3-2-1-5-1-eg-1'></a><a id='example-31'></a>

```
    Copyright 2021, Example Company, All Rights Reserved.
    Distribute freely.
    Share only on a need-to-know-basis only.
```

##### 3.2.1.5.2 Document Property - Distribution - TLP <a id='document-property-distribution-tlp'></a>

Traffic Light Protocol (TLP) (`tlp`) of value type `object` with the mandatory property Label (`label`) and
the optional property URL (`url`) provides details about the TLP classification of the document.

```
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
```

The Label of TLP (`label`) with value type `string` and `enum` provides the TLP label of the document.
Valid values of the `enum` are:

```
    AMBER
    GREEN
    RED
    WHITE
```

The URL of TLP version (`url`) with value type `string` with format `uri` provides a URL where to find
the textual description of the TLP version which is used in this document.
The default value is the URL to the definition by FIRST:

```
    https://www.first.org/tlp/
```

*Examples 1:*<a id='document-property-distribution-tlp-eg-1'></a><a id='sec-3-2-1-5-2-eg-1'></a><a id='example-32'></a>

```
    https://www.us-cert.gov/tlp
    https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Kritis/Merkblatt_TLP.pdf
```

#### 3.2.1.6 Document Property - Language <a id='document-property-language'></a>

Document language (`lang`) of value type Language Type (`lang_t`) identifies the language used by this document,
corresponding to IETF BCP 47 / RFC 5646.

#### 3.2.1.7 Document Property - Notes <a id='document-property-notes'></a>

Document notes (`notes`) of value type Notes Type (`notes_t`) holds notes associated with the whole document.

```
    "notes": {
      // ...
    },
```

#### 3.2.1.8 Document Property - Publisher <a id='document-property-publisher'></a>

Publisher (`publisher`) has value type `object` with the mandatory properties Category (`category`), Name (`name`) and
Namespace (`namespace`) and provides information on the publishing entity.
The 2 other optional properties are: `contact_details` and `issuing_authority`.

```
    "publisher": {
      // ...
      "properties": {
        "category": {
          // ...
        },
        "contact_details": {
          // ...
        },
        "issuing_authority": {
          // ...
        },
        "name": {
          // ...
        }
        "namespace": {
          // ...
        }
      }
    },
```

##### 3.2.1.8.1 Document Property - Publisher - Category <a id='document-property-publisher-category'></a>

The Category of publisher (`category`) of value type `string` and `enum` provides information about the category of
publisher releasing the document.
The valid values are:

```
    coordinator
    discoverer
    other
    translator
    user
    vendor
```

The value `coordinator` indicates individuals or organizations that
manage a single vendor’s response or multiple vendors’ responses to a vulnerability, a security flaw, or an incident.
This includes all Computer Emergency/Incident Response Teams (CERTs/CIRTs) or agents acting on the behalf of a researcher.

The value `discoverer` indicates individuals or organizations that find vulnerabilities or security weaknesses.
This includes all manner of researchers.

The value `translator` indicates individuals or organizations that translate CSAF documents.
This includes all manner of language translators, also those who work for the party issuing the original advisory.

The value `other` indicates a catchall for everyone else. Currently this includes editors, reviewers, forwarders, republishers,
and miscellaneous contributors.

The value `user` indicates anyone using a vendor’s product.

The value `vendor` indicates developers or maintainers of information system products or services.
This includes all authoritative product vendors, Product Security Incident Response Teams (PSIRTs), and
product resellers and distributors, including authoritative vendor partners.

##### 3.2.1.8.2 Document Property - Publisher - Contact Details <a id='document-property-publisher-contact-details'></a>

Contact details (`contact_details`) of value type `string` with 1 or more characters provides information on how to contact the publisher,
possibly including details such as web sites, email addresses, phone numbers, and postal mail addresses.

*Example 1:*<a id='document-property-publisher-contact-details-eg-1'></a><a id='sec-3-2-1-8-2-eg-1'></a><a id='example-33'></a>

```
    Example Company can be reached at contact_us@example.com, or via our website at https://www.example.com/contact.
```

##### 3.2.1.8.3 Document Property - Publisher - Issuing Authority <a id='document-property-publisher-issuing-authority'></a>

Issuing authority (`issuing_authority`) of value type `string` with 1 or more characters Provides information about
the authority of the issuing party to release the document, in particular, the party's constituency and responsibilities or other obligations.

##### 3.2.1.8.4 Document Property - Publisher - Name <a id='document-property-publisher-name'></a>

The Name of publisher (`name`) of value type `string` with 1 or more characters contains the name of the issuing party.

*Example 1:*<a id='document-property-publisher-name-eg-1'></a><a id='sec-3-2-1-8-4-eg-1'></a><a id='example-34'></a>

```
     BSI
     Cisco PSIRT
     Siemens ProductCERT
```

##### 3.2.1.8.5 Document Property - Publisher - Namespace <a id='document-property-publisher-namespace'></a>

The Namespace of publisher (`namespace`) of value type `string` with format `uri` contains a URL which
is under control of the issuing party and can be used as a globally unique identifier for that issuing party.
The URL SHALL be normalized.

An issuing party can choose any URL which fulfills the requirements state above.
The URL MAY be dereferenceable. If an issuing party has chosen a URL, it SHOULD NOT change.
Tools can make use of the combination of `/document/publisher/namespace` and `/document/tracking/id` as it
identifies a CSAF document globally unique.

If an issuing party decides to change its Namespace it SHOULD reissue all CSAF documents with
an incremented (patch) version which has no other changes than:

* the new publisher information
* the updated revision history
* the updated item in `/document/references[]` which points to the new version of the CSAF document
* an added item in `/document/references[]` which points to the previous version of the CSAF document (if the URL changed)

*Examples 1:*<a id='document-property-publisher-namespace-eg-1'></a><a id='sec-3-2-1-8-5-eg-1'></a><a id='example-35'></a>

```
    https://csaf.io
    https://www.example.com
```

#### 3.2.1.9 Document Property - References <a id='document-property-references'></a>

Document references (`references`) of value type References Type (`references_t`) holds a list of references associated with the whole document.

```
    "references": {
      // ...
    },
```

#### 3.2.1.10 Document Property - Source Language <a id='document-property-source-language'></a>

Source language (`source_lang`) of value type Language Type (`lang_t`) identifies if this copy of the document is
a translation then the value of this property describes from which language this document was translated.

The property MUST be present and set for any CSAF document with the value `translator` in `/document/publisher/category`.
The property SHALL NOT be present if the document was not translated.

> If an issuing party publishes a CSAF document with the same content in more than one language,
> one of these documents SHOULD be deemed the "original", the other ones SHOULD be considered translations from the "original".
> The issuing party can retain its original publisher information including the `category`.
> However, other rules defined in the conformance clause "CSAF translator" SHOULD be applied.

#### 3.2.1.11 Document Property - Title <a id='document-property-title'></a>

Title of this document (`title`) of value type `string` with 1 or more characters SHOULD be a canonical name for the document,
and sufficiently unique to distinguish it from similar documents.

*Examples 1:*<a id='document-property-title-eg-1'></a><a id='sec-3-2-1-11-eg-1'></a><a id='example-36'></a>

```
    Cisco IPv6 Crafted Packet Denial of Service Vulnerability
    Example Company Cross-Site-Scripting Vulnerability in Example Generator
```

#### 3.2.1.12 Document Property - Tracking <a id='document-property-tracking'></a>

Tracking (`tracking`) of value type `object` with the six mandatory properties: Current Release Date (`current_release_date`),
Identifier (`id`), Initial Release Date (`initial_release_date`), Revision History (`revision_history`), Status (`status`),
and Version (`version`) is a container designated to hold all management attributes necessary to track a CSAF document as a whole.
The two optional additional properties are Aliases (`aliases`) and Generator (`generator`).

```
    "tracking": {
      // ...
      "properties": {
        "aliases": {
          // ...
        },
        "current_release_date": {
          // ...
        },
        "generator": {
          // ...
        },
        "id": {
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
```

##### 3.2.1.12.1 Document Property - Tracking - Aliases <a id='document-property-tracking-aliases'></a>

Aliases (`aliases`) of value type `array` with 1 or more unique items (a `set`) representing Alternate Names contains a
list of alternate names for the same document.

```
    "aliases": {
      // ...
      "items": {
        // ...
      }
    },
```

Every such Alternate Name of value type `string` with 1 or more characters specifies a non-empty string that represents a
distinct optional alternative ID used to refer to the document.

*Example 1:*<a id='document-property-tracking-aliases-eg-1'></a><a id='sec-3-2-1-12-1-eg-1'></a><a id='example-37'></a>

```
    CVE-2019-12345
```

##### 3.2.1.12.2 Document Property - Tracking - Current Release Date <a id='document-property-tracking-current-release-date'></a>

Current release date (`current_release_date`) with value type `string` with format `date-time` holds the date when
the current revision of this document was released.

##### 3.2.1.12.3 Document Property - Tracking - Generator <a id='document-property-tracking-generator'></a>

Document Generator (`generator`) of value type `object` with mandatory property Engine (`engine`) and
optional property Date (`date`) is a container to hold all elements related to the generation of the document.
These items will reference when the document was actually created, including the date it was generated and the entity that generated it.

```
        "generator": {
          // ...
          "properties": {
            "date": {
              // ...
            },
            "engine": {
              // ...
            }
          }
        },
```

Date of document generation (`date`) of value type `string` with format `date-time` SHOULD be the current date that the document was generated.
Because documents are often generated internally by a document producer and exist for a nonzero amount of time before being released,
this field MAY be different from the Initial Release Date and Current Release Date.

Engine of document generation (`engine`) of value type `object` with mandatory property Engine name (`name`) and
optional property Engine version (`version`) contains information about the engine that generated the CSAF document.

```
        "engine": {
          // ...
          "properties": {
            "name": {
              // ...
            },
            "version": {
              // ...
            }
          }
        },
```

Engine name (`name`) of value type `string` with 1 or more characters represents the name of the engine that generated the CSAF document.

*Examples 1:*<a id='document-property-tracking-generator-eg-1'></a><a id='sec-3-2-1-12-3-eg-1'></a><a id='example-38'></a>

```
    Red Hat rhsa-to-cvrf
    Secvisogram
    TVCE
```

Engine version (`version`) of value type `string` with 1 or more characters contains the version of the engine that generated the CSAF document.

> Although it is not formally required, the TC suggests to use a versioning which is compatible with Semantic Versioning as described in
> the external specification [SemVer]. This could help the end user to identify when CSAF consumers have to be updated.

*Examples 2:*<a id='document-property-tracking-generator-eg-2'></a><a id='sec-3-2-1-12-3-eg-2'></a><a id='example-39'></a>

```
    0.6.0
    1.0.0-beta+exp.sha.a1c44f85
    2
```

##### 3.2.1.12.4 Document Property - Tracking - ID <a id='document-property-tracking-id'></a>

Unique identifier for the document (`id`) of value type `string` with 1 or more characters with `pattern` (regular expression):

```
    ^[\\S](.*[\\S])?$
```

Unique identifier for the document holds the Identifier.

> It SHALL NOT start or end with a white space and SHALL NOT contain a line break.

The ID is a simple label that provides for a wide range of numbering values, types, and schemes.
Its value SHOULD be assigned and maintained by the original document issuing authority. It MUST be unique for that organization.

*Examples 1:*<a id='document-property-tracking-id-eg-1'></a><a id='sec-3-2-1-12-4-eg-1'></a><a id='example-40'></a>

```
    Example Company - 2019-YH3234
    RHBA-2019:0024
    cisco-sa-20190513-secureboot
```

> The combination of `/document/publisher/namespace` and `/document/tracking/id` identifies a CSAF document globally unique.

This value is also used to determine the filename for the CSAF document (cf. section [5.1](#filename)).

##### 3.2.1.12.5 Document Property - Tracking - Initial Release Date <a id='document-property-tracking-initial-release-date'></a>

Initial release date (`initial_release_date`) with value type `string` with format `date-time` holds the date when this document was first published.

##### 3.2.1.12.6 Document Property - Tracking - Revision History <a id='document-property-tracking-revision-history'></a>

The Revision History (`revision_history`) with value type `array` of 1 or more Revision History Entries holds one revision item for each version of
the CSAF document, including the initial one.

```
        "revision_history": {
          // ...
          "items": {
            // ...
          }
        },
```

Each Revision contains all the information elements required to track the evolution of a CSAF document.
Revision History Entry items are of value type `object` with the three mandatory properties: Date (`date`), Number (`number`),
and Summary (`summary`).
In addition, a Revision MAY expose the optional property `legacy_version`.

```
        "properties": {
          "date": {
            // ...
          },
          "legacy_version": {
            // ...
          },
          "number": {
            // ...
          },
          "summary": {
            // ...
          }
        }
```

The Date of the revision (`date`) of value type `string` with format `date-time` states the date of the revision entry.

Legacy version of the revision (`legacy_version`) of value type `string` with 1 or more characters contains the version string used
in an existing document with the same content.

> This SHOULD be used to aid in the mapping between existing (human-readable) documents which might use a different version scheme and
> CSAF documents with the same content.
> It is recommended, to use the CSAF revision number to describe the revision history for any new human-readable equivalent.

The Number (`number`) has value type Version (`version_t`).

The Summary of the revision (`summary`) of value type `string` with 1 or more characters holds a single non-empty string representing
a short description of the changes.

Each Revision item which has a `number` of `0` or `0.y.z` MUST be removed from the document if the document status is `final`.
Versions of the document which are pre-release SHALL NOT have its own revision item.
All changes MUST be tracked in the item for the next release version.
Build metadata SHOULD NOT be included in the `number` of any revision item.

##### 3.2.1.12.7 Document Property - Tracking - Status <a id='document-property-tracking-status'></a>

Document status (`status`) of value type `string` and `enum` defines the draft status of the document.
The value MUST be one of the following:

```
    draft
    final
    interim
```

The value `draft` indicates, that this is a pre-release, intended for issuing party's internal use only,
or possibly used externally when the party is seeking feedback or indicating its intentions regarding a specific issue.

The value `final` indicates, that the issuing party asserts the content is unlikely to change.
“Final” status is an indication only, and does not preclude updates.
This SHOULD be used if the issuing party expects no, slow or few changes.

The value `interim` indicates, that the issuing party expects rapid updates.
This SHOULD be used if the expected rate of release for this document is significant higher than for other documents.
Once the rate slows down it MUST be changed to `final`. This MAY be done in a patch version.

> This is extremely useful for downstream vendors to constantly inform the end users about ongoing investigation.
> It can be used as an indication to pull the CSAF document more frequently.

##### 3.2.1.12.8 Document Property - Tracking - Version <a id='document-property-tracking-version'></a>

Version has the value type Version (`version_t`).

### 3.2.2 Product Tree Property <a id='product-tree-property'></a>

Product Tree (`product_tree`) has value type `object` with 1 or more properties is a container for all fully qualified product names that
can be referenced elsewhere in the document.
The properties are Branches (`branches`), Full Product Names (`full_product_names`), Product Groups (`product_groups`),
and Relationships (`relationships`).

```
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
      }
    },
```

#### 3.2.2.1 Product Tree Property - Branches <a id='product-tree-property-branches'></a>

List of branches (`branches`) has the value type `branches_t`.

#### 3.2.2.2 Product Tree Property - Full Product Names <a id='product-tree-property-full-product-names'></a>

List of full product names (`full_product_names`) of value type `array` with 1 or more items of type `full_product_name_t` contains a
list of full product names.

#### 3.2.2.3 Product Tree Property - Product Groups <a id='product-tree-property-product-groups'></a>

List of product groups (`product_groups`) of value type `array` with 1 or more items of value type `object` contains a list of product groups.

```
    "product_groups": {
      // ...
      "items": {
        // ...
      }
    },
```

The product group items are of value type `object` with the 2 mandatory properties Group ID (`group_id`) and Product IDs (`product_ids`) and
the optional Summary (`summary`) property.

```
    "properties": {
      "group_id": {
        // ...
      },
      "product_ids": {
        // ...
      },
      "summary": {
        // ...
      }
    }
```

The summary of the product group (`summary`) of value type `string` with 1 or more characters gives a short, optional description of the group.

*Examples 1:*<a id='product-tree-property-product-groups-eg-1'></a><a id='sec-3-2-2-3-eg-1'></a><a id='example-41'></a>

```
    Products supporting Modbus.
    The x64 versions of the operating system.
```

Group ID (`group_id`) has value type Product Group ID (`product_group_id_t`).

List of Product IDs (`product_ids`) of value type `array` with 2 or more unique items of value type Product ID (`product_id_t`) lists
the product_ids of those products which known as one group in the document.

#### 3.2.2.4 Product Tree Property - Relationships <a id='product-tree-property-relationships'></a>

List of relationships (`relationships`) of value type `array` with 1 or more items contains a list of relationships.

```
    "relationships": {
      // ...
      "items": {
        // ...
      }
    }
```

The Relationship item is of value type `object` and has four mandatory properties: Relationship category (`category`),
Full Product Name (`full_product_name`), Product Reference (`product_reference`), and Relates to Product Reference (`relates_to_product_reference`).
The Relationship item establishes a link between two existing `full_product_name_t` elements,
allowing the document producer to define a combination of two products that form a new `full_product_name` entry.

```
    "properties": {
      "category": {
        // ...
      },
      "full_product_name": {
        // ...
      },
      "product_reference": {
        // ...
      },
      "relates_to_product_reference": {
        // ...
      }
    }
```

> The situation where a need for declaring a Relationship arises,
> is given when a product is e.g. vulnerable only when installed together with another, or to describe operating system components.

Relationship category (`category`) of value type `string` and `enum` defines the category of relationship for the referenced component.
The valid values are:

```
    default_component_of
    external_component_of
    installed_on
    installed_with
    optional_component_of
```

The value `default_component_of` indicates that the entity labeled with one Product ID (e.g. CSAFPID-0001) is a default component of
an entity with another Product ID (e.g. CSAFPID-0002).
These Product IDs SHOULD NOT be identical to provide minimal redundancy.

The value `external_component_of` indicates that the entity labeled with one Product ID (e.g. CSAFPID-0001) is an external component of
an entity with another Product ID (e.g. CSAFPID-0002).
These Product IDs SHOULD NOT be identical to provide minimal redundancy.

The value `installed_on` indicates that the entity labeled with one Product ID (e.g. CSAFPID-0001) is installed on a platform entity with
another Product ID (e.g. CSAFPID-0002).
These Product IDs SHOULD NOT be identical to provide minimal redundancy.

The value `installed_with` indicates that the entity labeled with one Product ID (e.g. CSAFPID-0001) is installed alongside
an entity with another Product ID (e.g. CSAFPID-0002).
These Product IDs SHOULD NOT be identical to provide minimal redundancy.

The value `optional_component_of` indicates that the entity labeled with one Product ID (e.g. CSAFPID-0001) is an optional component of
an entity with another Product ID (e.g. CSAFPID-0002).
These Product IDs SHOULD NOT be identical to provide minimal redundancy.

Full Product Name (`full_product_name`) of value type Full Product Name Type (`full_product_name_t`).

Product Reference (`product_reference`) of value type Product ID (`product_id_t`) holds a Product ID that refers to the Full Product Name element,
which is referenced as the first element of the relationship.

Relates to Product Reference (`relates_to_product_reference`) of value type Product ID (`product_id_t`) holds a Product ID that refers to
the Full Product Name element, which is referenced as the second element of the relationship.

*Examples 1:*<a id='product-tree-property-relationships-eg-1'></a><a id='sec-3-2-2-4-eg-1'></a><a id='example-42'></a>

```
  "product_tree": {
    "full_product_names": [
      {
        "product_id": "CSAFPID-908070601",
        "name": "Cisco AnyConnect Secure Mobility Client 4.9.04053"
      },
      {
        "product_id": "CSAFPID-908070602",
        "name": "Microsoft Windows"
      }
    ],
    "relationships": [
      {
        "product_reference": "CSAFPID-908070601",
        "category": "installed_on",
        "relates_to_product_reference": "CSAFPID-908070602",
        "full_product_name": {
          "product_id": "CSAFPID-908070603",
          "name": "Cisco AnyConnect Secure Mobility Client 2.3.185 installed on Microsoft Windows"
        }
      }
    ]
  }
```

> The product `Cisco AnyConnect Secure Mobility Client 4.9.04053"` (Product ID: `CSAFPID-908070601`) and the product `Microsoft Windows`
> (Product ID: `CSAFPID-908070602`) form together a new product with the separate Product ID `CSAFPID-908070603`.
> The latter one can be used to refer to that combination in other parts of the CSAF document.
> In example 34, it might be the case that `Cisco AnyConnect Secure Mobility Client 4.9.04053"` is only
> vulnerable when installed on `Microsoft Windows`.

### 3.2.3 Vulnerabilities Property <a id='vulnerabilities-property'></a>

Vulnerabilities (`vulnerabilities`) of value type `array` with 1 or more objects representing vulnerabilities and providing 1 or more
properties represents a list of all relevant vulnerability information items.

```
    "vulnerabilities": {
      // ...
      "items": {
        // ...
      }
    }
```

The Vulnerability item of value type `object` with 1 or more properties is a container for the aggregation of all fields that are related to
a single vulnerability in the document.
Any vulnerability MAY provide the optional properties Acknowledgments (`acknowledgments`), Common Vulnerabilities and Exposures (CVE) (`cve`),
Common Weakness Enumeration (CWE) (`cwe`), Discovery Date (`discovery_date`), Flags (`flags`), IDs (`ids`), Involvements (`involvements`),
Notes (`notes`), Product Status (`product_status`), References (`references`), Release Date (`release_date`), Remediations (`remediations`),
Scores (`scores`), Threats (`threats`), and Title (`title`).

```
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
      "discovery_date": {
        // ...
      },
      "flags": {
        // ...
      },
      "ids": {
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
      "scores": {
        // ...
      },
      "threats": {
        // ...
      },
      "title": {
        // ...
      }
    }
```

#### 3.2.3.1 Vulnerabilities Property - Acknowledgments <a id='vulnerabilities-property-acknowledgments'></a>

Vulnerability acknowledgments (`acknowledgments`) of value type Acknowledgments Type (`acknowledgments_t`) contains a list of
acknowledgment elements associated with this vulnerability item.

```
    "acknowledgments": {
      // ...
    },
```

#### 3.2.3.2 Vulnerabilities Property - CVE <a id='vulnerabilities-property-cve'></a>

CVE (`cve`) of value type `string` with `pattern` (regular expression):

```
    ^CVE-[0-9]{4}-[0-9]{4,}$
```

holds the MITRE standard Common Vulnerabilities and Exposures (CVE) tracking number for the vulnerability.

#### 3.2.3.3 Vulnerabilities Property - CWE <a id='vulnerabilities-property-cwe'></a>

CWE (`cwe`) of value type `object` with the 2 mandatory properties Weakness ID (`id`) and Weakness Name (`name`) holds the
MITRE standard Common Weakness Enumeration (CWE) for the weakness associated. For more information cf. \[[CWE](#CWE)\].

```
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
```

The Weakness ID (`id`) has value type `string` with `pattern` (regular expression):

```
    ^CWE-[1-9]\\d{0,5}$
```

and holds the ID for the weakness associated.

*Examples 1:*<a id='vulnerabilities-property-cwe-eg-1'></a><a id='sec-3-2-3-3-eg-1'></a><a id='example-43'></a>

```
    CWE-22
    CWE-352
    CWE-79
```

The Weakness name (`name`) has value type `string` with 1 or more characters and holds the full name of the weakness as given
in the CWE specification.

*Examples 2:*<a id='vulnerabilities-property-cwe-eg-2'></a><a id='sec-3-2-3-3-eg-2'></a><a id='example-44'></a>

```
    Cross-Site Request Forgery (CSRF)
    Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')
    Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')
```

#### 3.2.3.4 Vulnerabilities Property - Discovery Date <a id='vulnerabilities-property-discovery-date'></a>

Discovery date (`discovery_date`) of value type `string` with format `date-time` holds the date and time the vulnerability was originally discovered.

#### 3.2.3.5 Vulnerabilities Property - Flags <a id='vulnerabilities-property-flags'></a>

List of flags (`flags`) of value type `array` with 1 or more unique items (a set) of value type `object` contains a list of machine readable flags.

```
    "flags": {
      // ...
      "items": {
        // ...
      }
    },
```

Every Flag item of value type `object` with the mandatory property Label (`label`) contains product specific information in regard to
this vulnerability as a single machine readable flag.
For example, this could be a machine readable justification code why a product is not affected.
At least one of the optional elements Group IDs (`group_ids`) and Product IDs (`product_ids`) MUST be present to state for which products or
product groups this flag is applicable.

> These flags enable the receiving party to automate the selection of actions to take.

In addition, any Flag item MAY provide the three optional properties Date (`date`), Group IDs (`group_ids`) and Product IDs (`product_ids`).

```
    "properties": {
      "date": {
        // ...
      },
      "group_ids": {
        // ...
      },
      "label": {
        // ...
      },
      "product_ids": {
        // ...
      }
    }
```

Date of the flag (`date`) of value type `string` with format `date-time` contains the date when assessment was done or the flag was assigned.

Group IDs (`group_ids`) are of value type Product Groups (`product_groups_t`) and contain a list of Product Groups the current flag item applies to.

Label of the flag (`label`) of value type `string` and `enum` specifies the machine readable label. Valid `enum` values are:

```
    component_not_present
    inline_mitigations_already_exist
    vulnerable_code_cannot_be_controlled_by_adversary
    vulnerable_code_not_in_execute_path
    vulnerable_code_not_present
```

The given values reflect the VEX not affected justifications. See [VEX-Justification] for more details. The values MUST be used as follows:

* `component_not_present`: The software is not affected because the vulnerable component is not in the product.
* `vulnerable_code_not_present`: The product is not affected because the code underlying the vulnerability is not present in the product.
  > Unlike `component_not_present`, the component in question is present, but for whatever reason (e.g. compiler options)
  > the specific code causing the vulnerability is not present in the component.
* `vulnerable_code_cannot_be_controlled_by_adversary`: The vulnerable component is present, and the component contains the vulnerable code.
  However, vulnerable code is used in such a way that an attacker cannot mount any anticipated attack.
* `vulnerable_code_not_in_execute_path`: The affected code is not reachable through the execution of the code,
  including non-anticipated states of the product.
  > Components that are neither used nor executed by the product.
* `inline_mitigations_already_exist`: Built-in inline controls or mitigations prevent an adversary from leveraging the vulnerability.

Product IDs (`product_ids`) are of value type Products (`products_t`) and contain a list of Products the current flag item applies to.

#### 3.2.3.6 Vulnerabilities Property - IDs <a id='vulnerabilities-property-ids'></a>

List of IDs (`ids`) of value type `array` with one or more unique ID items of value type `object` represents a list of unique labels or
tracking IDs for the vulnerability (if such information exists).

```
    "ids": {
      // ...
      "items": {
        // ...
      }
    },
```

Every ID item of value type `object` with the two mandatory properties System Name (`system_name`) and Text (`text`) contains a single unique label or
tracking ID for the vulnerability.

```
      "properties": {
        "system_name": {
          // ...
        },
        "text": {
          // ...
        }
      }
```

System name (`system_name`) of value type `string` with 1 or more characters indicates the name of the vulnerability tracking or numbering system.

*Examples 1:*<a id='vulnerabilities-property-ids-eg-1'></a><a id='sec-3-2-3-6-eg-1'></a><a id='example-45'></a>

```
    Cisco Bug ID
    GitHub Issue
```

Text (`text`) of value type `string` with 1 or more characters is unique label or tracking ID for the vulnerability (if such information exists).

*Examples 2:*<a id='vulnerabilities-property-ids-eg-2'></a><a id='sec-3-2-3-6-eg-2'></a><a id='example-46'></a>

```
    CSCso66472
    oasis-tcs/csaf#210
```

> General examples may include an identifier from a vulnerability tracking system that is available to customers, such as:
>
> * a Cisco bug ID,
> * a GitHub Issue number,
> * an ID from a Bugzilla system, or
> * an ID from a public vulnerability database such as the X-Force Database.
>
> The ID MAY be a vendor-specific value but is not to be used to publish the CVE tracking numbers
> (MITRE standard Common Vulnerabilities and Exposures), as these are specified inside the dedicated CVE element.

#### 3.2.3.7 Vulnerabilities Property - Involvements <a id='vulnerabilities-property-involvements'></a>

List of involvements (`involvements`) of value type `array` with 1 or more items of value type `object` contains a list of involvements.

```
    "involvements": {
      // ...
      "items": {
        // ...
      }
    },
```

Every Involvement item of value type `object` with the 2 mandatory properties Party (`party`), Status (`status`) and
the 2 optional properties Date of involvement (`date`) and Summary (`summary`) is a container that allows the document producers to
comment on the level of involvement (or engagement) of themselves (or third parties) in the vulnerability identification, scoping,
and remediation process.
It can also be used to convey the disclosure timeline.
The ordered tuple of the values of `party` and `date` (if present) SHALL be unique within `involvements`.

```
        "properties": {
          "date": {
            // ...
          },
          "party": {
            // ...
          },
          "status": {
            // ...
          },
          "summary": {
            // ...
          },
        }
```

Date of involvement (`date`) of value type `string` with format `date-time` holds the date and time of the involvement entry.

Party category (`party`) of value type `string` and `enum` defines the category of the involved party.
Valid values are:

```
    coordinator
    discoverer
    other
    user
    vendor
```

These values follow the same definitions as given for the publisher category (cf. section [3.2.1.8.1](#document-property-publisher-category)).

Party status (`status`) of value type `string` and `enum` defines contact status of the involved party.
Valid values are:

```
    completed
    contact_attempted
    disputed
    in_progress
    not_contacted
    open
```

Each status is mutually exclusive - only one status is valid for a particular vulnerability at a particular time. As the vulnerability ages,
a party's involvement could move from state to state.
However, in many cases, a document producer may choose not to issue CSAF documents at each state, or simply omit this element altogether.
It is recommended, however, that vendors that issue CSAF documents indicating an open or in-progress involvement SHOULD eventually expect to issue
a document containing one of the statuses `disputed` or `completed` as the latest one.

> The two vulnerability involvement status states, `contact_attempted` and `not_contacted` are intended for use by document producers other than
> vendors (such as research or coordinating entities).

The value `completed` indicates that the party asserts that investigation of the vulnerability is complete.
No additional information, fixes, or documentation from the party about the vulnerability should be expected to be released.

The value `contact_attempted` indicates that the document producer attempted to contact the party.

The value `disputed` indicates that the party disputes the vulnerability report in its entirety.
This status SHOULD be used when the party believes that a vulnerability report regarding a product is completely inaccurate
(that there is no real underlying security vulnerability) or that the technical issue being reported has no security implications.

The value `in_progress` indicates that some hotfixes, permanent fixes, mitigations, workarounds,
or patches may have been made available by the party, but more information or fixes may be released in the future.
The use of this status by a vendor indicates that future information from the vendor about the vulnerability is to be expected.

The value `not_contacted` indicates that the document producer has not attempted to make contact with the party.

The value `open` is the default status.
It doesn’t indicate anything about the vulnerability remediation effort other than the fact that the party has acknowledged awareness of
the vulnerability report.
The use of this status by a vendor indicates that future updates from the vendor about the vulnerability are to be expected.

Summary of involvement (`summary`) of value type `string` with 1 or more characters contains additional context regarding what is going on.

#### 3.2.3.8 Vulnerabilities Property - Notes <a id='vulnerabilities-property-notes'></a>

Vulnerability notes (`notes`) of value type Notes Type (`notes_t`) holds notes associated with this vulnerability item.

```
    "notes": {
      // ...
    },
```

#### 3.2.3.9 Vulnerabilities Property - Product Status <a id='vulnerabilities-property-product-status'></a>

Product status (`product_status`) of value type `object` with 1 or more properties contains different lists of `product_ids` which
provide details on the status of the referenced product related to the current vulnerability.
The eight defined properties are First affected (`first_affected`), First fixed (`first_fixed`), Fixed (`fixed`), Known affected (`known_affected`),
Known not affected (`known_not_affected`), Last affected (`last_affected`), Recommended (`recommended`),
and Under investigation (`under_investigation`) are all of value type Products (`products_t`).

```
    "product_status": {
      // ...
      "properties": {
        "first_affected": {
          // ...
        },
        "first_fixed": {
          // ...
        },
        "fixed": {
          // ...
        },
        "known_affected": {
          // ...
        },
        "known_not_affected": {
          // ...
        },
        "last_affected": {
          // ...
        },
        "recommended": {
          // ...
        },
        "under_investigation": {
          // ..
        }
      }
    },
```

First affected (`first_affected`) of value type Products (`products_t`) represents that these are the first versions of the releases known to be
affected by the vulnerability.

First fixed (`first_fixed`) of value type Products (`products_t`) represents that these versions contain the first fix for the vulnerability but
may not be the recommended fixed versions.

Fixed (`fixed`) of value type Products (`products_t`) represents that these versions contain a fix for the vulnerability but
may not be the recommended fixed versions.

Known affected (`known_affected`) of value type Products (`products_t`) represents that these versions are known to be affected by the vulnerability.
Actions are recommended to remediate or address this vulnerability.

> This could include for instance learning more about the vulnerability and context,
> and/or making a risk-based decision to patch or apply defense-in-depth measures.
> See `/vulnerabilities[]/remediations`, `/vulnerabilities[]/notes` and `/vulnerabilities[]/threats` for more details.

Known not affected (`known_not_affected`) of value type Products (`products_t`) represents that these versions are known not to be affected by
the vulnerability.
No remediation is required regarding this vulnerability.

> This could for instance be because the code referenced in the vulnerability is not present, not exposed, compensating controls exist,
> or other factors.
See `/vulnerabilities[]/threats` in category `impact` for more details.

Last affected (`last_affected`) of value type Products (`products_t`) represents that these are the last versions in a release train known to be
affected by the vulnerability. Subsequently released versions would contain a fix for the vulnerability.

Recommended (`recommended`) of value type Products (`products_t`) represents that these versions have a fix for the vulnerability and are
the vendor-recommended versions for fixing the vulnerability.

Under investigation (`under_investigation`) of value type Products (`products_t`) represents that it is not known yet whether these versions are or
are not affected by the vulnerability.
However, it is still under investigation - the result will be provided in a later release of the document.

#### 3.2.3.10 Vulnerabilities Property - References <a id='vulnerabilities-property-references'></a>

Vulnerability references (`references`) of value type References Type (`references_t`) holds a
list of references associated with this vulnerability item.

```
    "references": {
      // ...
    },
```

#### 3.2.3.11 Vulnerabilities Property - Release Date <a id='vulnerabilities-property-release-date'></a>

Release date (`release_date`) with value type `string` of format `date-time` holds the date and time
the vulnerability was originally released into the wild.

#### 3.2.3.12 Vulnerabilities Property - Remediations <a id='vulnerabilities-property-remediations'></a>

List of remediations (`remediations`) of value type `array` with 1 or more Remediation items of value type `object` contains a list of remediations.

```
    "remediations": {
      // ...
      "items": {
        // ...
      }
    },
```

Every Remediation item of value type `object` with the 2 mandatory properties Category (`category`) and
Details (`details`) specifies details on how to handle (and presumably, fix) a vulnerability.
At least one of the optional elements Group IDs (`group_ids`) and Product IDs (`product_ids`) MUST be present to state for which
products or product groups this remediation is applicable.

In addition, any Remediation MAY expose the six optional properties Date (`date`), Entitlements (`entitlements`), Group IDs (`group_ids`),
Product IDs (`product_ids`), Restart required (`restart_required`), and URL (`url`).

```
      "properties": {
        "category": {
          // ...
        },
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
        },
        "url": {
          // ...
        }
      }
```

##### 3.2.3.12.1 Vulnerabilities Property - Remediations - Category <a id='vulnerabilities-property-remediations-category'></a>

Category of the remediation (`category`) of value type `string` and `enum` specifies the category which this remediation belongs to.
Valid values are:

```
    mitigation
    no_fix_planned
    none_available
    vendor_fix
    workaround
```

The value `workaround` indicates that the remediation contains information about a configuration or specific deployment scenario that
can be used to avoid exposure to the vulnerability. There MAY be none, one, or more workarounds available.
This is typically the “first line of defense” against a new vulnerability before a mitigation or vendor fix has been issued or even discovered.

The value `mitigation` indicates that the remediation contains information about a configuration or deployment scenario that
helps to reduce the risk of the vulnerability but that does not resolve the vulnerability on the affected product.
Mitigations MAY include using devices or access controls external to the affected product.
Mitigations MAY or MAY NOT be issued by the original author of the affected product,
and they MAY or MAY NOT be officially sanctioned by the document producer.

The value `vendor_fix` indicates that the remediation contains information about an official fix that
is issued by the original author of the affected product.
Unless otherwise noted, it is assumed that this fix fully resolves the vulnerability.
This value contradicts with the categories `none_available` and `no_fix_planned` for the same product.
Therefore, such a combination can't be used in the list of remediations.

The value `none_available` indicates that there is currently no fix or other remediation available.
The text in field `details` SHOULD contain details about why there is no fix or other remediation.
The values `none_available` and `vendor_fix` are mutually exclusive per product.

> An issuing party might choose to use this category to announce that a fix is currently developed.
It is recommended that this also includes a date when a customer can expect the fix to be ready and distributed.  

The value `no_fix_planned` indicates that there is no fix for the vulnerability and it is not planned to provide one at any time.
This is often the case when a product has been orphaned, declared end-of-life, or otherwise deprecated.
The text in field `details` SHOULD contain details about why there will be no fix issued.
The values `no_fix_planned` and `vendor_fix` are mutually exclusive per product.

##### 3.2.3.12.2 Vulnerabilities Property - Remediations - Date <a id='vulnerabilities-property-remediations-date'></a>

Date of the remediation (`date`) of value type `string` with format `date-time` contains the date from which the remediation is available.

##### 3.2.3.12.3 Vulnerabilities Property - Remediations - Details <a id='vulnerabilities-property-remediations-details'></a>

Details of the remediation (`details`) of value type `string` with 1 or more characters contains a thorough human-readable discussion of the remediation.

##### 3.2.3.12.4 Vulnerabilities Property - Remediations - Entitlements <a id='vulnerabilities-property-remediations-entitlements'></a>

List of entitlements (`entitlements`) of value type `array` with 1 or more items of type Entitlement of the remediation as `string` with
1 or more characters contains a list of entitlements.

```
                "entitlements": {
                  // ....
                  "items": {
                    // ...
                  }
                },
```

Every Entitlement of the remediation contains any possible vendor-defined constraints for obtaining fixed software or hardware that
fully resolves the vulnerability.

##### 3.2.3.12.5 Vulnerabilities Property - Remediations - Group IDs <a id='vulnerabilities-property-remediations-group-ids'></a>

Group IDs (`group_ids`) are of value type Product Groups (`product_groups_t`) and contain a list of
Product Groups the current remediation item applies to.

##### 3.2.3.12.6 Vulnerabilities Property - Remediations - Product IDs <a id='vulnerabilities-property-remediations-product-ids'></a>

Product IDs (`product_ids`) are of value type Products (`products_t`) and contain a list of Products the current remediation item applies to.

##### 3.2.3.12.7 Vulnerabilities Property - Remediations - Restart Required <a id='vulnerabilities-property-remediations-restart-required'></a>

Restart required by remediation (`restart_required`) of value type `object` with the 1 mandatory property Category (`category`) and
the optional property Details (`details`) provides information on category of restart is required by this remediation to become effective.

```
      "restart_required": {
        // ...
        "properties": {
          "category": {
            // ...
          }
          "details": {
            // ...
          }
        }
      },
```

Category of restart (`category`) of value type `string` and `enum` specifies what category of restart is required by
this remediation to become effective.
Valid values are:

```
    connected
    dependencies
    machine
    none
    parent
    service
    system
    vulnerable_component
    zone
```

The values MUST be used as follows:

* `none`: No restart required.
* `vulnerable_component`: Only the vulnerable component (as given by the elements of `product_ids` or `group_ids` in the current remediation item)
   needs to be restarted.
* `service`: The vulnerable component and the background service used by the vulnerable component need to be restarted.
* `parent`: The vulnerable component and its parent process need to be restarted. This could be the case if the parent process has no build-in way
  to restart the vulnerable component or process values / context is only given at the start of the parent process.
* `dependencies`: The vulnerable component and all components which require the vulnerable component to work need to be restarted.
  This could be the case e.g. for a core service of a software.
* `connected`: The vulnerable component and all components connected (via network or any type of inter-process communication)
  to the vulnerable component need to be restarted.
* `machine`: The machine on which the vulnerable component is installed on needs to be restarted.
  This is the value which SHOULD be used if an OS needs to be restarted.
  It is typically the case for OS upgrades.
* `zone`: The security zone in which the machine resides on which the vulnerable component is installed needs to be restarted.
  This value might be useful for a remediation if no patch is available.
  If the malware can be wiped out by restarting the infected machines but the infection spreads fast the controlled shutdown of all machines at
  the same time and restart afterwards can leave one with a clean system.
* `system`: The whole system which the machine resides on which the vulnerable component is installed needs to be restarted.
  This MAY include multiple security zones. This could be the case for a major system upgrade in an ICS system or a protocol change.

Additional restart information (`details`) of value type `string` with 1 or more characters provides additional information for the restart.
This can include details on procedures, scope or impact.

##### 3.2.3.12.8 Vulnerabilities Property - Remediations - URL <a id='vulnerabilities-property-remediations-url'></a>

URL (`url`) of value type `string` with format `uri` contains the URL where to obtain the remediation.

#### 3.2.3.13 Vulnerabilities Property - Scores <a id='vulnerabilities-property-scores'></a>

List of scores (`scores`) of value type `array` with 1 or more items of type score holds a list of score objects for the current vulnerability.

```
    "scores": {
      // ...
      "items": {
        // ...
      }
    },
```

Value type of every such Score item is `object` with the mandatory property `products` and the optional properties `cvss_v2` and
`cvss_v3` specifies information about (at least one) score of the vulnerability and for which products the given value applies.
Each Score item has at least 2 properties.

```
        "properties": {
          "cvss_v2": {
            // ...
          },
          "cvss_v3": {
            "oneOf": [
              // ...
            ]
          }
          "products": {
            // ...
          }
        }
```

The property CVSS v2 (`cvss_v2`) holding a CVSS v2.0 value abiding by the schema at
[https://www.first.org/cvss/cvss-v2.0.json](https://www.first.org/cvss/cvss-v2.0.json).

The property CVSS v3 (`cvss_v3`) holding a CVSS v3.x value abiding by one of the schemas at
[https://www.first.org/cvss/cvss-v3.0.json](https://www.first.org/cvss/cvss-v3.0.json) or
[https://www.first.org/cvss/cvss-v3.1.json](https://www.first.org/cvss/cvss-v3.1.json).

Product IDs (`products`) of value type `products_t` with 1 or more items indicates for which products the given scores apply.
A score object SHOULD reflect the associated product's status (for example,
a fixed product no longer contains a vulnerability and should have a CVSS score of 0, or simply no score listed;
the known affected versions of that product can list the vulnerability score as it applies to them).

#### 3.2.3.14 Vulnerabilities Property - Threats <a id='vulnerabilities-property-threats'></a>

List of threats (`threats`) of value type `array` with 1 or more items of value type `object` contains
information about a vulnerability that can change with time.

```
    "threats": {
      // ...
      "items": {
        // ...
      }
    },
```

Every Threat item of value type `object` with the two mandatory properties Category (`category`) and Details (`details`) contains
the vulnerability kinetic information.
This information can change as the vulnerability ages and new information becomes available.
In addition, any Threat item MAY expose the three optional properties Date (`date`), Group IDs (`group_ids`), and Product IDs (`product_ids`).

```
    "properties": {
      "category": {
        // ...
      }
      "date": {
        // ...
      },
      "details": {
        // ...
      },
      "group_ids": {
        // ...
      },
      "product_ids": {
        // ...
      }
    }
```

Category of the threat (`category`) of value type `string` and `enum` categorizes the threat according to the rules of the specification.
Valid values are:

```
    exploit_status
    impact
    target_set
```

The value `exploit_status` indicates that the `details` field contains a description of the degree to which an exploit for the vulnerability is known.
This knowledge can range from information privately held among a very small group to an issue that has been described to the public at
a major conference or is being widely exploited globally.
For consistency and simplicity, this section can be a mirror image of the CVSS "Exploitability" metric.
However, it can also contain a more contextual status, such as "Weaponized" or "Functioning Code".

The value `impact` indicates that the `details` field contains an assessment of the impact on the user or the target set if
the vulnerability is successfully exploited or a description why it cannot be exploited.
If applicable, for consistency and simplicity, this section can be a textual summary of the three CVSS impact metrics.
These metrics measure how a vulnerability detracts from the three core security properties of an information system:
Confidentiality, Integrity, and Availability.

The value `target_set` indicates that the `details` field contains a description of
the currently known victim population in whatever terms are appropriate.
Such terms MAY include: operating system platform, types of products, user segments, and geographic distribution.

Date of the threat (`date`) of value type `string` with format `date-time` contains the date when the assessment was done or the threat appeared.

Details of the threat (`details`) of value type `string` with 1 or more characters represents a thorough human-readable discussion of the threat.

Group IDs (`group_ids`) are of value type Product Groups (`product_groups_t`) and contain a list of Product Groups the current threat item applies to.

Product IDs (`product_ids`) are of value type Products (`products_t`) and contain a list of Products the current threat item applies to.

#### 3.2.3.15 Vulnerabilities Property - Title <a id='vulnerabilities-property-title'></a>

Title (`title`) has value type `string` with 1 or more characters and gives the document producer the ability to apply a canonical name or
title to the vulnerability.

-------

# 4. Profiles <a id='profiles'></a>

CSAF documents do not have many required fields as they can be used for different purposes.
To ensure a common understanding of which fields are required in a given use case the standard defines profiles.
Each subsection describes such a profile by describing necessary content for that specific use case and providing insights into its purpose.
The value of `/document/category` is used to identify a CSAF document's profile. The following rules apply:

1. Each CSAF document MUST conform the **CSAF Base** profile.
2. Each profile extends the base profile "CSAF Base" - directly or indirect through another profile from the standard - by making additional
   fields from the standard mandatory.
   A profile can always add, but never subtract nor overwrite requirements defined in the profile it extends.
3. Any optional field from the standard can also be added to a CSAF document which conforms with a profile without breaking conformance with
   the profile.
   One and only exempt is when the profile requires not to have a certain set of fields.
4. Values of `/document/category` starting with `csaf_` are reserved for existing, upcoming and future profiles defined in the CSAF standard.
5. Values of `/document/category` that do not match any of the values defined in section [4](#profiles) of this standard SHALL be validated against
   the "CSAF Base" profile.
6. Local or private profiles MAY exist and tools MAY choose to support them.
7. If an official profile and a private profile exists, tools MUST validate against the official one from the standard.

## 4.1 Profile 1: CSAF Base <a id='profile-1-csaf-base'></a>

This profile defines the default required fields for any CSAF document.
Therefore, it is a "catch all" for CSAF documents that do not satisfy any other profile.
Furthermore, it is the foundation all other profiles are build on.

A CSAF document SHALL fulfill the following requirements to satisfy the profile "CSAF Base":

* The following elements MUST exist and be valid:
  * `/document/category`
  * `/document/csaf_version`
  * `/document/publisher/category`
  * `/document/publisher/name`
  * `/document/publisher/namespace`
  * `/document/title`
  * `/document/tracking/current_release_date`
  * `/document/tracking/id`
  * `/document/tracking/initial_release_date`
  * `/document/tracking/revision_history[]/date`
  * `/document/tracking/revision_history[]/number`
  * `/document/tracking/revision_history[]/summary`
  * `/document/tracking/status`
  * `/document/tracking/version`
* The value of `/document/category` SHALL NOT be equal to any value that is intended to only be used by another profile nor to the
  (case insensitive) name of any other profile from the standard.
  This does not differentiate between underscore, dash or whitespace.
  To explicitly select the use of this profile the value `csaf_base` SHOULD be used.

> Neither `CSAF Security Advisory` nor `csaf security advisory` are valid values for `/document/category`.

An issuing party might choose to set `/document/publisher/name` in front of a value that is intended to only be used by another
profile to state that the CSAF document does not use the profile associated with this value.
In this case, the (case insensitive) string "CSAF" MUST be removed from the value.
This SHOULD be done if the issuing party is unable or unwilling to use the value `csaf_base`, e.g. due to legal or cooperate identity reasons.

> Both values `Example Company Security Advisory` and `Example Company security_advisory` in `/document/category` use the profile "CSAF Base".
> This is important to prepare forward compatibility as later versions of CSAF might add new profiles.
> Therefore, the values which can be used for the profile "CSAF Base" might change.

## 4.2 Profile 2: Security incident response <a id='profile-2-security-incident-response'></a>

This profile SHOULD be used to provide a response to a security breach or incident.
This MAY also be used to convey information about an incident that is unrelated to the issuing party's own products or infrastructure.

> Example Company might use a CSAF document satisfying this profile to respond to a security incident at ACME Inc. and
the implications on its own products and infrastructure.

A CSAF document SHALL fulfill the following requirements to satisfy the profile "Security incident response":

* The following elements MUST exist and be valid:
  * all elements required by the profile "CSAF Base".
  * `/document/notes` with at least one item which has a `category` of `description`, `details`, `general` or `summary`
    > Reasoning: Without at least one note item which contains information about response to the event referred to this doesn't provide
    > any useful information.
  * `/document/references` with at least one item which has a `category` of `external`
    > The intended use for this field is to refer to one or more documents or websites which provides more details about the incident.
* The value of `/document/category` SHALL be `csaf_security_incident_response`.

## 4.3 Profile 3: Informational Advisory <a id='profile-3-informational-advisory'></a>

This profile SHOULD be used to provide information which are **not related to a vulnerability** but e.g. a misconfiguration.

A CSAF document SHALL fulfill the following requirements to satisfy the profile "Informational Advisory":

* The following elements MUST exist and be valid:
  * all elements required by the profile "CSAF Base".
  * `/document/notes` with at least one item which has a `category` of `description`, `details`, `general` or `summary`
    > Reasoning: Without at least one note item which contains information about the "issue" which is the topic of the advisory it is useless.
  * `/document/references` with at least one item which has a `category` of `external`
    > The intended use for this field is to refer to one or more documents or websites which provide more details about
    > the issue or its remediation (if possible).
    > This could be a hardening guide, a manual, best practices or any other helpful information.
* The value of `/document/category` SHALL be `csaf_informational_advisory`.
* The element `/vulnerabilities` SHALL NOT exist.
  If there is any information that would reside in the element `/vulnerabilities` the CSAF document SHOULD use another profile,
  e.g. "Security Advisory".

If the element `/product_tree` exists, a user MUST assume that all products mentioned are affected.

## 4.4 Profile 4: Security Advisory <a id='profile-4-security-advisory'></a>

This profile SHOULD be used to provide information which is related to vulnerabilities and corresponding remediations.

A CSAF document SHALL fulfill the following requirements to satisfy the profile "Security Advisory":

* The following elements MUST exist and be valid:
  * all elements required by the profile "CSAF Base".
  * `/product_tree` which lists all products referenced later on in the CSAF document regardless of their state.
  * `/vulnerabilities` which lists all vulnerabilities.
  * `/vulnerabilities[]/notes`
    > Provides details about the vulnerability.
  * `/vulnerabilities[]/product_status`
    > Lists each product's status in regard to the vulnerability.
* The value of `/document/category` SHALL be `csaf_security_advisory`.

## 4.5 Profile 5: VEX <a id='profile-5-vex'></a>

This profile SHOULD be used to provide information of the "Vulnerability Exploitability eXchange".
The main purpose of the VEX format is to state that and why a certain product is, or is not, affected by a vulnerability.
See \[[VEX](#VEX)\] for details.

A CSAF document SHALL fulfill the following requirements to satisfy the profile "VEX":

* The following elements MUST exist and be valid:
  * all elements required by the profile "CSAF Base".
  * `/product_tree` which lists all products referenced later on in the CSAF document regardless of their state.
  * `/vulnerabilities` which lists all vulnerabilities.
  * at least one of
    * `/vulnerabilities[]/product_status/fixed`
    * `/vulnerabilities[]/product_status/known_affected`
    * `/vulnerabilities[]/product_status/known_not_affected`
    * `/vulnerabilities[]/product_status/under_investigation`
  * at least one of
    * `/vulnerabilities[]/cve`
    * `/vulnerabilities[]/ids`
  * `/vulnerabilities[]/notes`
    > Provides details about the vulnerability.
* For each item in
  * `/vulnerabilities[]/product_status/known_not_affected` an impact statement SHALL exist as machine readable flag
    in `/vulnerabilities[]/flags` or as human readable justification in `/vulnerabilities[]/threats`.
    For the latter one, the `category` value for such a statement MUST be `impact` and the `details` field SHALL contain
    a description why the vulnerability cannot be exploited.
  * `/vulnerabilities[]/product_status/known_affected` additional product specific information SHALL be provided
    in `/vulnerabilities[]/remediations` as an action statement.
    Optional, additional information MAY also be provide through `/vulnerabilities[]/notes` and `/vulnerabilities[]/threats`.
    > The use of the categories `no_fix_planned` and `none_available` for an action statement is permitted.
  > Even though Product status lists Product IDs, Product Group IDs can be used in the `remediations` and `threats` object.
  > However, it MUST be ensured that for each Product ID the required information according to its product status as stated
  > in the two points above is available. This implies that all products with the status `known_not_affected` MUST have an
  > impact statement and all products with the status `known_affected` MUST have additional product specific information
  > regardless of whether that is referenced through the Product ID or a Product Group ID.
* The value of `/document/category` SHALL be `csaf_vex`.

-------

# 5. Additional Conventions <a id='additional-conventions'></a>

This section provides additional rules for handling CSAF documents.

## 5.1 Filename <a id='filename'></a>

The following rules MUST be applied to determine the filename for the CSAF document:

1. The value `/document/tracking/id` is converted into lower case.
2. Any character sequence which is not part of one of the following groups MUST be replaced by a single underscore (`_`):
   * Lower case ASCII letters (0x61 - 0x7A)
   * digits (0x30 - 0x39)
   * special characters: `+` (0x2B), `-` (0x2D)
   > The regex `[^+\-a-z0-9]+` can be used to find a character sequence which has to be replaced by an underscore.
   > However, it SHALL NOT be applied before completing the first step.
   >
   > Even though the underscore `_` (0x5F) is a valid character in the filename it is replaced to avoid situations
   > where the conversion rule might lead to multiple consecutive underscores.
   > As a result, a `/document/tracking/id` with the value `2022_#01-A` is converted into `2022_01-a` instead of `2022__01-a`.
3. The file extension `.json` MUST be appended.

*Examples 1:*<a id='filename-eg-1'></a><a id='sec-5-1-eg-1'></a><a id='example-47'></a>

```
  cisco-sa-20190513-secureboot.json
  example_company_-_2019-yh3234.json
  rhba-2019_0024.json
```

> It is currently considered best practice to indicate that a CSAF document is invalid by
> inserting `_invalid` into the filename in front of the file extension.

*Examples 2:*<a id='filename-eg-2'></a><a id='sec-5-1-eg-2'></a><a id='example-48'></a>

```
  cisco-sa-20190513-secureboot_invalid.json
  example_company_-_2019-yh3234_invalid.json
  rhba-2019_0024_invalid.json
```

## 5.2 Separation in Data Stream <a id='separation-in-data-stream'></a>

If multiple CSAF documents are transported via a data stream in a sequence without requests inbetween,
they MUST be separated by the Record Separator in accordance with \[[RFC7464](#RFC7464)\].

## 5.3 Sorting <a id='additional-conventions--sorting'></a>

The keys within a CSAF document SHOULD be sorted alphabetically.

-------

# 6. Tests <a id='tests'></a>

The following three subsections list a number of tests which all will have a short description and an excerpt of an example which fails the test.

## 6.1 Mandatory Tests <a id='mandatory-tests'></a>

Mandatory tests MUST NOT fail at a valid CSAF document.
A program MUST handle a test failure as an error.

### 6.1.1 Missing Definition of Product ID <a id='missing-definition-of-product-id'></a>

For each element of type `/$defs/product_id_t` which is not inside a Full Product Name (type: `full_product_name_t`) and
therefore reference an element within the `product_tree` it MUST be tested that the Full Product Name element with the matching `product_id` exists.
The same applies for all items of elements of type `/$defs/products_t`.

The relevant paths for this test are:

```
  /product_tree/product_groups[]/product_ids[]
  /product_tree/relationships[]/product_reference
  /product_tree/relationships[]/relates_to_product_reference
  /vulnerabilities[]/product_status/first_affected[]
  /vulnerabilities[]/product_status/first_fixed[]
  /vulnerabilities[]/product_status/fixed[]
  /vulnerabilities[]/product_status/known_affected[]
  /vulnerabilities[]/product_status/known_not_affected[]
  /vulnerabilities[]/product_status/last_affected[]
  /vulnerabilities[]/product_status/recommended[]
  /vulnerabilities[]/product_status/under_investigation[]
  /vulnerabilities[]/remediations[]/product_ids[]
  /vulnerabilities[]/scores[]/products[]
  /vulnerabilities[]/threats[]/product_ids[]
```

*Example 1 (which fails the test):*<a id='missing-definition-of-product-id-eg-1'></a><a id='sec-6-1-1-eg-1'></a><a id='example-49'></a>

```
  "product_tree": {
    "product_groups": [
      {
        "group_id": "CSAFGID-1020300",
        "product_ids": [
          "CSAFPID-9080700",
          "CSAFPID-9080701"
        ]
      }
    ]
  }
```

> Neither `CSAFPID-9080700` nor `CSAFPID-9080701` were defined in the `product_tree`.

### 6.1.2 Multiple Definition of Product ID <a id='multiple-definition-of-product-id'></a>

For each Product ID (type `/$defs/product_id_t`) in Full Product Name elements (type: `/$defs/full_product_name_t`) it
MUST be tested that the `product_id` was not already defined within the same document.

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/product/product_id
  /product_tree/full_product_names[]/product_id
  /product_tree/relationships[]/full_product_name/product_id
```

*Example 1 (which fails the test):*<a id='multiple-definition-of-product-id-eg-1'></a><a id='sec-6-1-2-eg-1'></a><a id='example-50'></a>

```
  "product_tree": {
    "full_product_names": [
      {
        "product_id": "CSAFPID-9080700",
        "name": "Product A"
      },
      {
        "product_id": "CSAFPID-9080700",
        "name": "Product B"
      }
    ]
  }
```

> `CSAFPID-9080700` was defined twice.

### 6.1.3 Circular Definition of Product ID <a id='circular-definition-of-product-id'></a>

For each new defined Product ID (type `/$defs/product_id_t`) in items of relationships (`/product_tree/relationships`) it
MUST be tested that the `product_id` does not end up in a circle.

The relevant path for this test is:

```
  /product_tree/relationships[]/full_product_name/product_id
```

> As this can be quite complex a program for large CSAF documents, a program could check first whether
> a Product ID defined in a relationship item is used as `product_reference` or `relates_to_product_reference`.
> Only for those which fulfill this condition it is necessary to run the full check following the references.

*Example 1 (which fails the test):*<a id='circular-definition-of-product-id-eg-1'></a><a id='sec-6-1-3-eg-1'></a><a id='example-51'></a>

```
  "product_tree": {
    "full_product_names": [
      {
        "product_id": "CSAFPID-9080700",
        "name": "Product A"
      }
    ],
    "relationships": [
      {
        "category": "installed_on",
        "full_product_name": {
          "name": "Product B",
          "product_id": "CSAFPID-9080701"
        },
        "product_reference": "CSAFPID-9080700",
        "relates_to_product_reference": "CSAFPID-9080701"
      }
    ]
  }
```

> `CSAFPID-9080701` refers to itself - this is a circular definition.

### 6.1.4 Missing Definition of Product Group ID <a id='missing-definition-of-product-group-id'></a>

For each element of type `/$defs/product_group_id_t` which is not inside a Product Group (`/product_tree/product_groups[]`) and
therefore reference an element within the `product_tree` it MUST be tested that the Product Group element with the matching `group_id` exists.
The same applies for all items of elements of type `/$defs/product_groups_t`.

The relevant paths for this test are:

```
  /vulnerabilities[]/remediations[]/group_ids
  /vulnerabilities[]/threats[]/group_ids
```

*Example 1 (which fails the test):*<a id='missing-definition-of-product-group-id-eg-1'></a><a id='sec-6-1-4-eg-1'></a><a id='example-52'></a>

```
  "product_tree": {
    "full_product_names": [
      {
        "product_id": "CSAFPID-9080700",
        "name": "Product A"
      }
    ]
  },
  "vulnerabilities": [
    {
      "threats": [
        {
          "category": "exploit_status",
          "details": "Reliable exploits integrated in Metasploit.",
          "group_ids": [
            "CSAFGID-1020301"
          ]
        }
      ]
    }
  ]
```

> `CSAFGID-1020301` was not defined in the Product Tree.

### 6.1.5 Multiple Definition of Product Group ID <a id='multiple-definition-of-product-group-id'></a>

For each Product Group ID (type `/$defs/product_group_id_t`) Product Group elements (`/product_tree/product_groups[]`) it
MUST be tested that the `group_id` was not already defined within the same document.

The relevant path for this test is:

```
    /product_tree/product_groups[]/group_id
```

*Example 1 (which fails the test):*<a id='multiple-definition-of-product-group-id-eg-1'></a><a id='sec-6-1-5-eg-1'></a><a id='example-53'></a>

```
  "product_tree": {
    "full_product_names": [
      {
        "product_id": "CSAFPID-9080700",
        "name": "Product A"
      },
      {
        "product_id": "CSAFPID-9080701",
        "name": "Product B"
      },
      {
        "product_id": "CSAFPID-9080702",
        "name": "Product C"
      }
    ],
    "product_groups": [
      {
        "group_id": "CSAFGID-1020300",
        "product_ids": [
          "CSAFPID-9080700",
          "CSAFPID-9080701"
        ]
      },
      {
        "group_id": "CSAFGID-1020300",
        "product_ids": [
          "CSAFPID-9080700",
          "CSAFPID-9080702"
        ]
      }
    ]
  }
```

> `CSAFGID-1020300` was defined twice.

### 6.1.6 Contradicting Product Status <a id='contradicting-product-status'></a>

For each item in `/vulnerabilities` it MUST be tested that the same Product ID is not member of contradicting product status groups.
The sets formed by the contradicting groups within one vulnerability item MUST be pairwise disjoint.

Contradiction groups are:

* Affected:

   ```
   /vulnerabilities[]/product_status/first_affected[]  
   /vulnerabilities[]/product_status/known_affected[]
   /vulnerabilities[]/product_status/last_affected[]
   ```

* Not affected:

  ```
  /vulnerabilities[]/product_status/known_not_affected[]
  ```

* Fixed:

  ```
  /vulnerabilities[]/product_status/first_fixed[]
  /vulnerabilities[]/product_status/fixed[]
  ```

* Under investigation:

  ```
  /vulnerabilities[]/product_status/under_investigation[]
  ```

> Note: An issuer might recommend (`/vulnerabilities[]/product_status/recommended`) a product version from any group - also from the affected group,
> i.e. if it was discovered that fixed versions introduce a more severe vulnerability.

*Example 1 (which fails the test):*<a id='contradicting-product-status-eg-1'></a><a id='sec-6-1-6-eg-1'></a><a id='example-54'></a>

```
  "product_tree": {
    "full_product_names": [
      {
        "product_id": "CSAFPID-9080700",
        "name": "Product A"
      }
    ]
  },
  "vulnerabilities": [
    {
      "product_status": {
        "known_affected": [
          "CSAFPID-9080700"
        ],
        "known_not_affected": [
          "CSAFPID-9080700"
        ]
      }
    }
  ]
```

> `CSAFPID-9080700` is a member of the two contradicting groups "Affected" and "Not affected".

### 6.1.7 Multiple Scores with same Version per Product <a id='multiple-scores-with-same-version-per-product'></a>

For each item in `/vulnerabilities` it MUST be tested that the same Product ID is not member of more than one CVSS-Vectors with the same version.

The relevant path for this test is:

```
    /vulnerabilities[]/scores[]
```

*Example 1 (which fails the test):*<a id='multiple-scores-with-same-version-per-product-eg-1'></a><a id='sec-6-1-7-eg-1'></a><a id='example-55'></a>

```
  "product_tree": {
    "full_product_names": [
      {
        "product_id": "CSAFPID-9080700",
        "name": "Product A"
      }
    ]
  },
  "vulnerabilities": [
    {
      "scores": [
        {
          "products": [
            "CSAFPID-9080700"
          ],
          "cvss_v3": {
            "version": "3.1",
            "vectorString": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H",
            "baseScore": 10,
            "baseSeverity": "CRITICAL"
          }
        },
        {
          "products": [
            "CSAFPID-9080700"
          ],
          "cvss_v3": {
            "version": "3.1",
            "vectorString": "CVSS:3.1/AV:L/AC:L/PR:H/UI:R/S:U/C:H/I:H/A:H",
            "baseScore": 6.5,
            "baseSeverity": "MEDIUM"
          }
        }
      ]
    }
  ]
```

> Two CVSS v3.1 scores are given for `CSAFPID-9080700`.

### 6.1.8 Invalid CVSS <a id='invalid-cvss'></a>

It MUST be tested that the given CVSS object is valid according to the referenced schema.

The relevant paths for this test are:

```
  /vulnerabilities[]/scores[]/cvss_v2
  /vulnerabilities[]/scores[]/cvss_v3
```

*Example 1 (which fails the test):*<a id='invalid-cvss-eg-1'></a><a id='sec-6-1-8-eg-1'></a><a id='example-56'></a>

```
  "cvss_v3": {
    "version": "3.1",
    "vectorString": "CVSS:3.1/AV:L/AC:L/PR:H/UI:R/S:U/C:H/I:H/A:H",
    "baseScore": 6.5
  }
```

> The required element `baseSeverity` is missing.

> A tool MAY add one or more of the missing properties `version`, `baseScore` and `baseSeverity` based on
> the values given in `vectorString` as quick fix.

### 6.1.9 Invalid CVSS computation <a id='invalid-cvss-computation'></a>

It MUST be tested that the given CVSS object has the values computed correctly according to the definition.

> The `vectorString` SHOULD take precedence.

The relevant paths for this test are:

```
  /vulnerabilities[]/scores[]/cvss_v2/baseScore
  /vulnerabilities[]/scores[]/cvss_v2/temporalScore
  /vulnerabilities[]/scores[]/cvss_v2/environmentalScore
  /vulnerabilities[]/scores[]/cvss_v3/baseScore
  /vulnerabilities[]/scores[]/cvss_v3/baseSeverity
  /vulnerabilities[]/scores[]/cvss_v3/temporalScore
  /vulnerabilities[]/scores[]/cvss_v3/temporalSeverity
  /vulnerabilities[]/scores[]/cvss_v3/environmentalScore
  /vulnerabilities[]/scores[]/cvss_v3/environmentalSeverity
```

*Example 1 (which fails the test):*<a id='invalid-cvss-computation-eg-1'></a><a id='sec-6-1-9-eg-1'></a><a id='example-57'></a>

```
  "cvss_v3": {
    "version": "3.1",
    "vectorString": "CVSS:3.1/AV:L/AC:L/PR:H/UI:R/S:U/C:H/I:H/A:H",
    "baseScore": 10.0,
    "baseSeverity": "LOW"
  }
```

> Neither `baseScore` nor `baseSeverity` has the correct value according to the specification.

> A tool MAY set the correct values as computed according to the specification as quick fix.

### 6.1.10 Inconsistent CVSS <a id='inconsistent-cvss'></a>

It MUST be tested that the given CVSS properties do not contradict the CVSS vector.

The relevant paths for this test are:

```
  /vulnerabilities[]/scores[]/cvss_v2
  /vulnerabilities[]/scores[]/cvss_v3
```

*Example 1 (which fails the test):*<a id='inconsistent-cvss-eg-1'></a><a id='sec-6-1-10-eg-1'></a><a id='example-58'></a>

```
  "cvss_v3": {
    "version": "3.1",
    "vectorString": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",
    "baseScore": 9.8,
    "baseSeverity": "CRITICAL",
    "attackVector": "LOCAL",
    "attackComplexity": "LOW",
    "privilegesRequired": "NONE",
    "userInteraction": "NONE",
    "scope": "CHANGED",
    "confidentialityImpact": "HIGH",
    "integrityImpact": "HIGH",
    "availabilityImpact": "LOW"
  }
```

> The values in CVSS vector differs from values of the properties `attackVector`, `scope` and `availabilityImpact`.

> A tool MAY overwrite contradicting values according to the `vectorString` as quick fix.

### 6.1.11 CWE <a id='cwe'></a>

It MUST be tested that given CWE exists and is valid.

The relevant path for this test is:

```
    /vulnerabilities[]/cwe
```

*Example 1 (which fails the test):*<a id='cwe-eg-1'></a><a id='sec-6-1-11-eg-1'></a><a id='example-59'></a>

```
  "cwe": {
    "id": "CWE-79",
    "name": "Improper Input Validation"
  }
```

> The `CWE-79` exists. However, its name is `Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')`.

### 6.1.12 Language <a id='language'></a>

For each element of type `/$defs/language_t` it MUST be tested that the language code is valid and exists.

The relevant paths for this test are:

```
  /document/lang
  /document/source_lang
```

*Example 1 (which fails the test):*<a id='language-eg-1'></a><a id='sec-6-1-12-eg-1'></a><a id='example-60'></a>

```
  "lang": "EZ"
```

> `EZ` is not a valid language. It is the subtag for the region "Eurozone".

> For any deprecated subtag, a tool MAY replace it with its preferred value as a quick fix.

### 6.1.13 PURL <a id='purl'></a>

It MUST be tested that given PURL is valid.

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/product/product_identification_helper/purl
  /product_tree/full_product_names[]/product_identification_helper/purl
  /product_tree/relationships[]/full_product_name/product_identification_helper/purl
```

*Example 1 (which fails the test):*<a id='purl-eg-1'></a><a id='sec-6-1-13-eg-1'></a><a id='example-61'></a>

```
  "product_tree": {
    "full_product_names": [
      {
        "name": "Product A",
        "product_id": "CSAFPID-9080700",
        "product_identification_helper": {
          "purl": "pkg:maven/@1.3.4"
        }
      }
    ]
  }
```

> Any valid purl has a name component.

### 6.1.14 Sorted Revision History <a id='sorted-revision-history'></a>

It MUST be tested that the value of `number` of items of the revision history are sorted ascending when the items are sorted ascending by `date`.

The relevant path for this test is:

```
    /document/tracking/revision_history
```

*Example 1 (which fails the test):*<a id='sorted-revision-history-eg-1'></a><a id='sec-6-1-14-eg-1'></a><a id='example-62'></a>

```
  "revision_history": [
    {
      "date": "2021-07-22T10:00:00.000Z",
      "number": "2",
      "summary": "Second version."
    },
    {
      "date": "2021-07-23T10:00:00.000Z",
      "number": "1",
      "summary": "Initial version."
    }
  ]
```

> The first item has a higher version number than the second.

### 6.1.15 Translator <a id='translator'></a>

It MUST be tested that `/document/source_lang` is present and set if the value `translator` is used for `/document/publisher/category`.

The relevant path for this test is:

```
    /document/source_lang
```

*Example 1 (which fails the test):*<a id='translator-eg-1'></a><a id='sec-6-1-15-eg-1'></a><a id='example-63'></a>

```
  "document": {
    // ...
    "publisher": {
      "category": "translator",
      "name": "CSAF TC Translator",
      "namespace": "https://csaf.io/translator"
    },
    "title": "Mandatory test: Translator (failing example 1)",
    // ...
  }
```

> The required element `source_lang` is missing.

### 6.1.16 Latest Document Version <a id='latest-document-version'></a>

It MUST be tested that document version has the same value as the `number` in the last item of Revision History when
it is sorted ascending by `date`. Build metadata is ignored in the comparison.
Any pre-release part is also ignored if the document status is `draft`.

The relevant path for this test is:

```
    /document/tracking/version
```

*Example 1 (which fails the test):*<a id='latest-document-version-eg-1'></a><a id='sec-6-1-16-eg-1'></a><a id='example-64'></a>

```
  "tracking": {
    // ...
    "revision_history": [
      {
        "date": "2021-07-21T09:00:00.000Z",
        "number": "1",
        "summary": "Initial version."
      },
      {
        "date": "2021-07-21T10:00:00.000Z",
        "number": "2",
        "summary": "Second version."
      }
    ],
    // ...
    "version": "1"
  }
```

> The value of `number` of the last item after sorting is `2`. However, the document version is `1`.

### 6.1.17 Document Status Draft <a id='document-status-draft'></a>

It MUST be tested that document status is `draft` if the document version is `0` or `0.y.z` or contains the pre-release part.

The relevant path for this test is:

```
    /document/tracking/status
```

*Example 1 (which fails the test):*<a id='document-status-draft-eg-1'></a><a id='sec-6-1-17-eg-1'></a><a id='example-65'></a>

```
    "tracking": {
      // ...
      "status": "final",
      "version": "0.9.5"
    }
```

> The `/document/tracking/version` is `0.9.5` but the document status is `final`.

### 6.1.18 Released Revision History <a id='released-revision-history'></a>

It MUST be tested that no item of the revision history has a `number` of `0` or `0.y.z` when the document status is `final` or `interim`.

The relevant path for this test is:

```
    /document/tracking/revision_history[]/number
```

*Example 1 (which fails the test):*<a id='released-revision-history-eg-1'></a><a id='sec-6-1-18-eg-1'></a><a id='example-66'></a>

```
    "tracking": {
      // ...
      "revision_history": [
        {
          "date": "2021-05-17T10:00:00.000Z",
          "number": "0",
          "summary": "First draft"
        },
        {
          "date": "2021-07-21T10:00:00.000Z",
          "number": "1",
          "summary": "Initial version."
        }
      ],
      "status": "final",
      "version": "1"
    }
```

> The document status is `final` but the revision history includes an item which has `0` as value for `number`.

### 6.1.19 Revision History Entries for Pre-release Versions <a id='revision-history-entries-for-pre-release-versions'></a>

It MUST be tested that no item of the revision history has a `number` which includes pre-release information.

The relevant path for this test is:

```
    /document/tracking/revision_history[]/number
```

*Example 1 (which fails the test):*<a id='revision-history-entries-for-pre-release-versions-eg-1'></a><a id='sec-6-1-19-eg-1'></a><a id='example-67'></a>

```
    "revision_history": [
      {
        "date": "2021-04-22T10:00:00.000Z",
        "number": "1.0.0-rc",
        "summary": "Release Candidate for initial version."
      },
      {
        "date": "2021-04-23T10:00:00.000Z",
        "number": "1.0.0",
        "summary": "Initial version."
      }
    ]
```

> The revision history contains an item which has a `number` that indicates that this is pre-release.

### 6.1.20 Non-draft Document Version <a id='non-draft-document-version'></a>

It MUST be tested that document version does not contain a pre-release part if the document status is `final` or `interim`.

The relevant path for this test is:

```
    /document/tracking/version
```

*Example 1 (which fails the test):*<a id='non-draft-document-version-eg-1'></a><a id='sec-6-1-20-eg-1'></a><a id='example-68'></a>

```
    "tracking": {
      // ...
      "status": "interim",
      "version": "1.0.0-alpha"
    }
```

> The document status is `interim` but the document version contains the pre-release part `-alpha`.

### 6.1.21 Missing Item in Revision History <a id='missing-item-in-revision-history'></a>

It MUST be tested that items of the revision history do not omit a version number when the items are sorted ascending by `date`.
In the case of semantic versioning, this applies only to the Major version.
It MUST also be tested that the first item in such a sorted list has either the version number 0 or 1 in the case of integer versioning or
a Major version of 0 or 1 in the case of semantic versioning.

The relevant path for this test is:

```
    /document/tracking/revision_history
```

*Example 1 (which fails the test):*<a id='missing-item-in-revision-history-eg-1'></a><a id='sec-6-1-21-eg-1'></a><a id='example-69'></a>

```
    "revision_history": [
      {
        "date": "2021-04-22T10:00:00.000Z",
        "number": "1",
        "summary": "Initial version."
      },
      {
        "date": "2021-07-21T10:00:00.000Z",
        "number": "3",
        "summary": "Some other changes."
      }
    ]
```

> The item for version `2` is missing.

### 6.1.22 Multiple Definition in Revision History <a id='multiple-definition-in-revision-history'></a>

It MUST be tested that items of the revision history do not contain the same version number.

The relevant path for this test is:

```
    /document/tracking/revision_history
```

*Example 1 (which fails the test):*<a id='multiple-definition-in-revision-history-eg-1'></a><a id='sec-6-1-22-eg-1'></a><a id='example-70'></a>

```
   "revision_history": [
      {
        "date": "2021-07-20T10:00:00.000Z",
        "number": "1",
        "summary": "Initial version."
      },
      {
        "date": "2021-07-21T10:00:00.000Z",
        "number": "1",
        "summary": "Some other changes."
      }
    ]
```

> The revision history contains two items with the version number `1`.

### 6.1.23 Multiple Use of Same CVE <a id='multiple-use-of-same-cve'></a>

It MUST be tested that a CVE is not used in multiple vulnerability items.

The relevant path for this test is:

```
    /vulnerabilities[]/cve
```

*Example 1 (which fails the test):*<a id='multiple-use-of-same-cve-eg-1'></a><a id='sec-6-1-23-eg-1'></a><a id='example-71'></a>

```
  "vulnerabilities": [
    {
      "cve": "CVE-2017-0145"
    },
    {
      "cve": "CVE-2017-0145"
    }
  ]
```

> The vulnerabilities array contains two items with the same CVE identifier `CVE-2017-0145`.

### 6.1.24 Multiple Definition in Involvements <a id='multiple-definition-in-involvements'></a>

It MUST be tested that items of the list of involvements do not contain the same `party` regardless of its `status` more than once at any `date`.

The relevant path for this test is:

```
    /vulnerabilities[]/involvements
```

*Example 1 (which fails the test):*<a id='multiple-definition-in-involvements-eg-1'></a><a id='sec-6-1-24-eg-1'></a><a id='example-72'></a>

```
  "vulnerabilities": [
    {
      "involvements": [
        {
          "date": "2021-04-23T10:00:00.000Z",
          "party": "vendor",
          "status": "completed"
        },
        {
          "date": "2021-04-23T10:00:00.000Z",
          "party": "vendor",
          "status": "in_progress",
          "summary": "The vendor has released a mitigation and is working to fully resolve the issue."
        }
      ]
    }
  ]
```

> The list of involvements contains two items with the same tuple `party` and `date`.

### 6.1.25 Multiple Use of Same Hash Algorithm <a id='multiple-use-of-same-hash-algorithm'></a>

It MUST be tested that the same hash algorithm is not used multiple times in one item of hashes.

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/product/product_identification_helper/hashes[]/file_hashes
  /product_tree/full_product_names[]/product_identification_helper/hashes[]/file_hashes
  /product_tree/relationships[]/full_product_name/product_identification_helper/hashes[]/file_hashes
```

*Example 1 (which fails the test):*<a id='multiple-use-of-same-hash-algorithm-eg-1'></a><a id='sec-6-1-25-eg-1'></a><a id='example-73'></a>

```
  "product_tree": {
    "full_product_names": [
      {
        "name": "Product A",
        "product_id": "CSAFPID-9080700",
        "product_identification_helper": {
          "hashes": [
            {
              "file_hashes": [
                {
                  "algorithm": "sha256",
                  "value": "026a37919b182ef7c63791e82c9645e2f897a3f0b73c7a6028c7febf62e93838"
                },
                {
                  "algorithm": "sha256",
                  "value": "0a853ce2337f0608489ac596a308dc5b7b19d35a52b10bf31261586ac368b175"
                }
              ],
              "filename": "product_a.so"
            }
          ]
         }
      }
    ]
  }
```

> The hash algorithm `sha256` is used two times in one item of hashes.

### 6.1.26 Prohibited Document Category Name <a id='prohibited-document-category-name'></a>

It MUST be tested that the document category is not equal to the (case insensitive) name (without the prefix `csaf_`) or
value of any other profile than "CSAF Base". Any occurrences of dash, whitespace,
and underscore characters are removed from the values on both sides before the match.
Also the value MUST NOT start with the reserved prefix `csaf_` except if the value is `csaf_base`.

This test does only apply for CSAF documents with the profile "CSAF Base".
Therefore, it MUST be skipped if the document category matches one of the values defined for the profile other than "CSAF Base".

> For CSAF 2.0, the test must be skipped for the following values in `/document/category`:
>
> ```
>   csaf_base
>   csaf_security_incident_response
>   csaf_informational_advisory
>   csaf_security_advisory
>   csaf_vex
> ```

This is the only mandatory test related to the profile "CSAF Base" as the required fields SHALL be checked by validating the JSON schema.

The relevant path for this test is:

```
  /document/category
```

*Examples 1 (for currently prohibited values):*<a id='prohibited-document-category-name-eg-1'></a><a id='sec-6-1-26-eg-1'></a><a id='example-74'></a>

```
  Csaf_a
  Informational Advisory
  security-incident-response
  Security      Advisory
  veX
  V_eX
```

*Example 2 (which fails the test):*<a id='prohibited-document-category-name-eg-2'></a><a id='sec-6-1-26-eg-2'></a><a id='example-75'></a>

```
  "category": "Security_Incident_Response"
```

> The value `Security_Incident_Response` is the name of a profile where the space was replaced with underscores.

### 6.1.27 Profile Tests <a id='profile-tests'></a>

This subsubsection structures the tests for the profiles. Not all tests apply for all profiles.
Tests SHOULD be skipped if the document category does not match the one given in the test.
Each of the following tests SHOULD be treated as they where listed similar to the other tests.

> An application MAY group these tests by profiles when providing the additional function to only run one or more selected tests.
> This results in one virtual test per profile.

#### 6.1.27.1 Document Notes <a id='document-notes'></a>

It MUST be tested that at least one item in `/document/notes` exists which has a `category` of `description`, `details`, `general` or `summary`.

The relevant values for `/document/category` are:

```
  csaf_informational_advisory
  csaf_security_incident_response
```

The relevant path for this test is:

```
  /document/notes
```

*Example 1 (which fails the test):*<a id='document-notes-eg-1'></a><a id='sec-6-1-27-1-eg-1'></a><a id='example-76'></a>

```
  "notes": [
    {
      "category": "legal_disclaimer",
      "text": "The CSAF document is provided to You \"AS IS\" and \"AS AVAILABLE\" and with all faults and defects without warranty of any kind.",
      "title": "Terms of Use"
    }
  ]
```

> The document notes do not contain an item which has a `category` of `description`, `details`, `general` or `summary`.

#### 6.1.27.2 Document References <a id='document-references'></a>

It MUST be tested that at least one item in `/document/references` exists that has links to an `external` source.

The relevant values for `/document/category` are:

```
  csaf_informational_advisory
  csaf_security_incident_response
```

The relevant path for this test is:

```
  /document/references
```

*Example 1 (which fails the test):*<a id='document-references-eg-1'></a><a id='sec-6-1-27-2-eg-1'></a><a id='example-77'></a>

```
  "references": [
    {
      "category": "self",
      "summary": "The canonical URL.",
      "url": "https://example.com/security/data/csaf/2021/OASIS_CSAF_TC-CSAF_2_0-2021-6-1-27-02-01.json"
    }
  ]
```

> The document references do not contain any item which has the category `external`.

#### 6.1.27.3 Vulnerabilities <a id='vulnerabilities-for-informational-advisory'></a>

It MUST be tested that the element `/vulnerabilities` does not exist.

The relevant value for `/document/category` is:

```
  csaf_informational_advisory
```

The relevant path for this test is:

```
  /vulnerabilities
```

*Example 1 (which fails the test):*<a id='vulnerabilities-for-informational-advisory-eg-1'></a><a id='sec-6-1-27-3-eg-1'></a><a id='example-78'></a>

```
  "vulnerabilities": [
    {
      "title": "A vulnerability item that SHALL NOT exist"
    }
  ]
```

> The element `/vulnerabilities` exists.

> A tool MAY change the `/document/category` to `csaf_base` as a quick fix.

#### 6.1.27.4 Product Tree <a id='product-tree'></a>

It MUST be tested that the element `/product_tree` exists.

The relevant values for `/document/category` are:

```
  csaf_security_advisory
  csaf_vex
```

The relevant path for this test is:

```
  /product_tree
```

*Example 1 (which fails the test):*<a id='product-tree-eg-1'></a><a id='sec-6-1-27-4-eg-1'></a><a id='example-79'></a>

```
  {
    "document": {
      // ...
    },
    "vulnerabilities": [
      // ...
    ]
  }
```

> The element `/product_tree` does not exist.

#### 6.1.27.5 Vulnerability Notes <a id='vulnerability-notes'></a>

For each item in `/vulnerabilities` it MUST be tested that the element `notes` exists.

The relevant values for `/document/category` are:

```
  csaf_security_advisory
  csaf_vex
```

The relevant path for this test is:

```
  /vulnerabilities[]/notes
```

*Example 1 (which fails the test):*<a id='vulnerability-notes-eg-1'></a><a id='sec-6-1-27-5-eg-1'></a><a id='example-80'></a>

```
  "vulnerabilities": [
    {
      "title": "A vulnerability item without a note"
    }
  ]
```

> The vulnerability item has no `notes` element.

#### 6.1.27.6 Product Status <a id='product-status'></a>

For each item in `/vulnerabilities` it MUST be tested that the element `product_status` exists.

The relevant value for `/document/category` is:

```
  csaf_security_advisory
```

The relevant path for this test is:

```
  /vulnerabilities[]/product_status
```

*Example 1 (which fails the test):*<a id='product-status-eg-1'></a><a id='sec-6-1-27-6-eg-1'></a><a id='example-81'></a>

```
  "vulnerabilities": [
    {
      "title": "A vulnerability item without a product status"
    }
  ]
```

> The vulnerability item has no `product_status` element.

#### 6.1.27.7 VEX Product Status <a id='vex-product-status'></a>

For each item in `/vulnerabilities` it MUST be tested that at least one of the elements `fixed`, `known_affected`, `known_not_affected`,
or `under_investigation` is present in `product_status`.

The relevant value for `/document/category` is:

```
  csaf_vex
```

The relevant paths for this test are:

```
  /vulnerabilities[]/product_status/fixed
  /vulnerabilities[]/product_status/known_affected
  /vulnerabilities[]/product_status/known_not_affected
  /vulnerabilities[]/product_status/under_investigation
```

*Example 1 (which fails the test):*<a id='vex-product-status-eg-1'></a><a id='sec-6-1-27-7-eg-1'></a><a id='example-82'></a>

```
  "product_status": {
    "first_fixed": [
      // ...
    ],
    "recommended": [
      // ...
    ]
  }
```

> None of the elements `fixed`, `known_affected`, `known_not_affected`, or `under_investigation` is present in `product_status`.

#### 6.1.27.8 Vulnerability ID <a id='vulnerability-id'></a>

For each item in `/vulnerabilities` it MUST be tested that at least one of the elements `cve` or `ids` is present.

The relevant value for `/document/category` is:

```
  csaf_vex
```

The relevant paths for this test are:

```
  /vulnerabilities[]/cve
  /vulnerabilities[]/ids
```

*Example 1 (which fails the test):*<a id='vulnerability-id-eg-1'></a><a id='sec-6-1-27-8-eg-1'></a><a id='example-83'></a>

```
  "vulnerabilities": [
    {
      "title": "A vulnerability item without a CVE or ID"
    }
  ]
```

> None of the elements `cve` or `ids` is present.

#### 6.1.27.9 Impact Statement <a id='impact-statement'></a>

For each item in `/vulnerabilities[]/product_status/known_not_affected` it MUST be tested that
a corresponding impact statement exist in `/vulnerabilities[]/flags` or `/vulnerabilities[]/threats`.
For the latter one, the `category` value for such a statement MUST be `impact`.

The relevant value for `/document/category` is:

```
  csaf_vex
```

The relevant path for this test is:

```
  /vulnerabilities[]/flags
  /vulnerabilities[]/threats
```

*Example 1 (which fails the test):*<a id='impact-statement-eg-1'></a><a id='sec-6-1-27-9-eg-1'></a><a id='example-84'></a>

```
  "product_tree": {
    "full_product_names": [
      {
        "product_id": "CSAFPID-9080700",
        "name": "Product A"
      },
      {
        "product_id": "CSAFPID-9080701",
        "name": "Product B"
      },
      {
        "product_id": "CSAFPID-9080702",
        "name": "Product C"
      }
    ],
    "product_groups": [
      {
        "group_id": "CSAFGID-0001",
        "product_ids": [
          "CSAFPID-9080700",
          "CSAFPID-9080701"
        ]
      }
    ]
  },
  "vulnerabilities": [
    {
      // ...
      "product_status": {
        "known_not_affected": [
          "CSAFPID-9080700",
          "CSAFPID-9080701",
          "CSAFPID-9080702"
        ]
      },
      "threats": [
        {
          "category": "impact",
          "details": "The vulnerable code is not present in these products.",
          "group_ids": [
            "CSAFGID-0001"
          ]
        }
      ]
    }
  ]
```

> There is no impact statement for `CSAFPID-9080702`.
>
> Note: The impact statement for `CSAFPID-9080700` and `CSAFPID-9080701` is given through `CSAFGID-0001`.

#### 6.1.27.10 Action Statement <a id='action-statement'></a>

For each item in `/vulnerabilities[]/product_status/known_affected` it MUST be tested that
a corresponding action statement exist in `/vulnerabilities[]/remediations`.

The relevant value for `/document/category` is:

```
  csaf_vex
```

The relevant path for this test is:

```
  /vulnerabilities[]/remediations
```

*Example 1 (which fails the test):*<a id='action-statement-eg-1'></a><a id='sec-6-1-27-10-eg-1'></a><a id='example-85'></a>

```
  "product_tree": {
    "full_product_names": [
      {
        "product_id": "CSAFPID-9080700",
        "name": "Product A"
      },
      {
        "product_id": "CSAFPID-9080701",
        "name": "Product B"
      },
      {
        "product_id": "CSAFPID-9080702",
        "name": "Product C"
      }
    ],
    "product_groups": [
      {
        "group_id": "CSAFGID-0001",
        "product_ids": [
          "CSAFPID-9080700",
          "CSAFPID-9080701"
        ],
        "summary": "EOL products"
      }
    ]
  },
  "vulnerabilities": [
    {
      // ...
      "product_status": {
        "known_affected": [
          "CSAFPID-9080700",
          "CSAFPID-9080701",
          "CSAFPID-9080702"
        ]
      },
      "remediations": [
        {
          "category": "no_fix_planned",
          "details": "These products are end-of-life. Therefore, no fix will be provided.",
          "group_ids": [
            "CSAFGID-0001"
          ]
        }
      ]
    }
  ]
```

> There is no action statement for `CSAFPID-9080702`.
>
> Note: The action statement for `CSAFPID-9080700` and `CSAFPID-9080701` is given through `CSAFGID-0001`.

#### 6.1.27.11 Vulnerabilities <a id='vulnerabilities-for-security-advisory-or-vex'></a>

It MUST be tested that the element `/vulnerabilities` exists.

The relevant values for `/document/category` are:

```
  csaf_security_advisory
  csaf_vex
```

The relevant path for this test is:

```
  /vulnerabilities
```

*Example 1 (which fails the test):*<a id='vulnerabilities-for-security-advisory-or-vex-eg-1'></a><a id='sec-6-1-27-11-eg-1'></a><a id='example-86'></a>

```
  {
    "document": {
      // ...
    },
    "product_tree": [
      // ...
    ]
  }
```

> The element `/vulnerabilities` does not exist.

### 6.1.28 Translation <a id='translation'></a>

It MUST be tested that the given source language and document language are not the same.

The relevant path for this test is:

```
  /document/lang
  /document/source_lang
```

*Example 1 (which fails the test):*<a id='translation-eg-1'></a><a id='sec-6-1-28-eg-1'></a><a id='example-87'></a>

```
  "document": {
    // ...
    "lang": "en-US",
    // ...
    "source_lang": "en-US",
    // ...
  }
```

> The document language and the source language have the same value `en-US`.
>
> Note: A translation from `en-US` to `en-GB` would pass the test.

> A tool MAY remove the source language as quick fix.

### 6.1.29 Remediation without Product Reference <a id='remediation-without-product-reference'></a>

For each item in `/vulnerabilities[]/remediations` it MUST be tested that it includes at least one of the elements `group_ids` or `product_ids`.

The relevant path for this test is:

```
  /vulnerabilities[]/remediations[]
```

*Example 1 (which fails the test):*<a id='remediation-without-product-reference-eg-1'></a><a id='sec-6-1-29-eg-1'></a><a id='example-88'></a>

```
      "remediations": [
        {
          "category": "no_fix_planned",
          "details": "These products are end-of-life. Therefore, no fix will be provided."
        }
      ]
```

> The given remediation does not specify to which products it should be applied.

> A tool MAY add all products of the affected group of this vulnerability to the remediation as quick fix.

### 6.1.30 Mixed Integer and Semantic Versioning <a id='mixed-integer-and-semantic-versioning'></a>

It MUST be tested that all elements of type `/$defs/version_t` follow either integer versioning or
semantic versioning homogeneously within the same document.

The relevant paths for this test are:

```
  /document/tracking/revision_history[]/number
  /document/tracking/version
```

*Example 1 (which fails the test):*<a id='mixed-integer-and-semantic-versioning-eg-1'></a><a id='sec-6-1-30-eg-1'></a><a id='example-89'></a>

```
    "tracking": {
      // ...
      "revision_history": [
        {
          "date": "2021-07-21T09:00:00.000Z",
          "number": "1.0.0",
          "summary": "Initial version."
        },
        {
          "date": "2021-07-21T10:00:00.000Z",
          "number": "2",
          "summary": "Second version."
        }
      ],
      // ...
      "version": "2"
    }
```

> The document started with semantic versioning (`1.0.0`) and switched to integer versioning (`2`).

> A tool MAY assign all items their corresponding value according to integer versioning as a quick fix.
> In such case, the old `number` SHOULD be stored in `legacy_version`.

### 6.1.31 Version Range in Product Version <a id='version-range-in-product-version'></a>

For each element of type `/$defs/branches_t` with `category` of `product_version` it MUST be tested that
the value of `name` does not contain a version range.

> To implement this test it is deemed sufficient that, when converted to lower case,
> the value of `name` does not contain any of the following strings:
>
> ```
>   <
>   <=
>   >
>   >=
>   after
>   all
>   before
>   earlier
>   later
>   prior
>   versions
> ```

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/name
```

*Example 1 (which fails the test):*<a id='version-range-in-product-version-eg-1'></a><a id='sec-6-1-31-eg-1'></a><a id='example-90'></a>

```
            "branches": [
              {
                "category": "product_version",
                "name": "prior to 4.2",
                // ...
              }
            ]
```

> The version range `prior to 4.2` is given for the branch category `product_version`.

### 6.1.32 Flag without Product Reference <a id='flag-without-product-reference'></a>

For each item in `/vulnerabilities[]/flags` it MUST be tested that it includes at least one of the elements `group_ids` or `product_ids`.

The relevant path for this test is:

```
  /vulnerabilities[]/flags[]
```

*Example 1 (which fails the test):*<a id='flag-without-product-reference-eg-1'></a><a id='sec-6-1-32-eg-1'></a><a id='example-91'></a>

```
      "flags": [
        {
          "label": "component_not_present"
        }
      ]
```

> The given flag does not specify to which products it should be applied.

### 6.1.33 Multiple Flags with VEX Justification Codes per Product <a id='multiple-flags-with-vex-justification-codes-per-product'></a>

For each item in `/vulnerabilities[]` it MUST be tested that a Product is not member of more than one Flag item with
a VEX justification code (see section [3.2.3.5](#vulnerabilities-property-flags)).
This takes indirect relations through Product Groups into account.

> Additional flags with a different purpose might be provided in later versions of CSAF.
> Through the explicit reference of VEX justification codes the test is specified to be forward-compatible.

The relevant path for this test is:

```
  /vulnerabilities[]/flags
```

*Example 1 (which fails the test):*<a id='multiple-flags-with-vex-justification-codes-per-product-eg-1'></a><a id='sec-6-1-33-eg-1'></a><a id='example-92'></a>

```
  "product_tree": {
    "full_product_names": [
      {
        "product_id": "CSAFPID-9080700",
        "name": "Product A"
      },
      {
        "product_id": "CSAFPID-9080701",
        "name": "Product B"
      }
    ],
    "product_groups": [
      {
        "group_id": "CSAFGID-0001",
        "product_ids": [
          "CSAFPID-9080700",
          "CSAFPID-9080701"
        ]
      }
    ]
  },
  "vulnerabilities": [
    {
      // ...
      "flags": [
        {
          "label": "component_not_present",
          "group_ids": [
            "CSAFGID-0001"
          ]
        },
        {
          "label": "vulnerable_code_cannot_be_controlled_by_adversary",
          "product_ids": [
            "CSAFPID-9080700"
          ]
        }
      ],
      // ...
      "product_status": {
        "known_not_affected": [
          "CSAFPID-9080700",
          "CSAFPID-9080701"
        ]
      }
    }
  ]
```

> There are two flags given for `CSAFPID-9080700` - one indirect through `CSAFGID-0001` and one direct.

## 6.2 Optional Tests <a id='optional-tests'></a>

Optional tests SHOULD NOT fail at a valid CSAF document without a good reason. Failing such a test does not make the CSAF document invalid.
These tests may include information about features which are still supported but expected to be deprecated in a future version of CSAF.
A program MUST handle a test failure as a warning.

### 6.2.1 Unused Definition of Product ID <a id='unused-definition-of-product-id'></a>

For each Product ID (type `/$defs/product_id_t`) in Full Product Name elements (type: `/$defs/full_product_name_t`) it MUST be tested that
the `product_id` is referenced somewhere within the same document.

This test SHALL be skipped for CSAF documents conforming the profile "Informational Advisory".

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/product/product_id
  /product_tree/full_product_names[]/product_id
  /product_tree/relationships[]/full_product_name/product_id
```

*Example 1 (which fails the test):*<a id='unused-definition-of-product-id-eg-1'></a><a id='sec-6-2-1-eg-1'></a><a id='example-93'></a>

```
  "product_tree": {
    "full_product_names": [
      {
        "product_id": "CSAFPID-9080700",
        "name": "Product A"
      }
    ]
  }
```

> `CSAFPID-9080700` was defined but never used.

> A tool MAY remove the unused definition as quick fix. However, such quick fix shall not be applied if the test was skipped.

### 6.2.2 Missing Remediation <a id='missing-remediation'></a>

For each Product ID (type `/$defs/product_id_t`) in the Product Status groups Affected and Under investigation it MUST be tested that
a remediation exists.

> The remediation might be of the category `none_available` or `no_fix_planned`.

The relevant paths for this test are:

```
  /vulnerabilities[]/product_status/first_affected[]  
  /vulnerabilities[]/product_status/known_affected[]
  /vulnerabilities[]/product_status/last_affected[]
  /vulnerabilities[]/product_status/under_investigation[]
```

*Example 1 (which fails the test):*<a id='missing-remediation-eg-1'></a><a id='sec-6-2-2-eg-1'></a><a id='example-94'></a>

```
  "product_tree": {
    "full_product_names": [
      {
        "product_id": "CSAFPID-9080700",
        "name": "Product A"
      }
    ]
  },
  "vulnerabilities": [
    {
      "product_status": {
        "last_affected": [
          "CSAFPID-9080700"
        ]
      }
    }
  ]
```

> `CSAFPID-9080700` has in Product Status `last_affected` but there is no remediation object for this Product ID.

### 6.2.3 Missing Score <a id='missing-score'></a>

For each Product ID (type `/$defs/product_id_t`) in the Product Status groups Affected it MUST be tested that
a score object exists which covers this product.

The relevant paths for this test are:

```
  /vulnerabilities[]/product_status/first_affected[]  
  /vulnerabilities[]/product_status/known_affected[]
  /vulnerabilities[]/product_status/last_affected[]
```

*Example 1 (which fails the test):*<a id='missing-score-eg-1'></a><a id='sec-6-2-3-eg-1'></a><a id='example-95'></a>

```
  "product_tree": {
    "full_product_names": [
      {
        "product_id": "CSAFPID-9080700",
        "name": "Product A"
      }
    ]
  },
  "vulnerabilities": [
    {
      "product_status": {
        "first_affected": [
          "CSAFPID-9080700"
        ]
      }
    }
  ]
```

> `CSAFPID-9080700` has in Product Status `first_affected` but there is no score object which covers this Product ID.

### 6.2.4 Build Metadata in Revision History <a id='build-metadata-in-revision-history'></a>

For each item in revision history it MUST be tested that `number` does not include build metadata.

The relevant path for this test is:

```
    /document/tracking/revision_history[]/number
```

*Example 1 (which fails the test):*<a id='build-metadata-in-revision-history-eg-1'></a><a id='sec-6-2-4-eg-1'></a><a id='example-96'></a>

```
    "revision_history": [
      {
        "date": "2021-04-23T10:00:00.000Z",
        "number": "1.0.0+exp.sha.ac00785",
        "summary": "Initial version."
      }
    ]
```

> The revision history contains an item which has a `number` that includes the build metadata `+exp.sha.ac00785`.

### 6.2.5 Older Initial Release Date than Revision History <a id='older-initial-release-date-than-revision-history'></a>

It MUST be tested that the Initial Release Date is not older than the `date` of the oldest item in Revision History.

The relevant path for this test is:

```
    /document/tracking/initial_release_date
```

*Example 1 (which fails the test):*<a id='older-initial-release-date-than-revision-history-eg-1'></a><a id='sec-6-2-5-eg-1'></a><a id='example-97'></a>

```
    "tracking": {
      // ...
      "initial_release_date": "2021-04-22T10:00:00.000Z",
      "revision_history": [
        {
          "date": "2021-05-06T10:00:00.000Z",
          "number": "1",
          "summary": "Initial version."
        },
        {
          "date": "2021-07-21T11:00:00.000Z",
          "number": "2",
          "summary": "Second version."
        }
      ],
      // ...
    }
```

> The initial release date `2021-04-22T10:00:00.000Z` is older than `2021-05-06T10:00:00.000Z` which is the `date` of
> the oldest item in Revision History.

### 6.2.6 Older Current Release Date than Revision History <a id='older-current-release-date-than-revision-history'></a>

It MUST be tested that the Current Release Date is not older than the `date` of the newest item in Revision History.

The relevant path for this test is:

```
    /document/tracking/current_release_date
```

*Example 1 (which fails the test):*<a id='older-current-release-date-than-revision-history-eg-1'></a><a id='sec-6-2-6-eg-1'></a><a id='example-98'></a>

```
    "tracking": {
      "current_release_date": "2021-05-06T10:00:00.000Z",
      // ...
      "revision_history": [
        {
          "date": "2021-05-06T10:00:00.000Z",
          "number": "1",
          "summary": "Initial version."
        },
        {
          "date": "2021-07-21T11:00:00.000Z",
          "number": "2",
          "summary": "Second version."
        }
      ],
      // ...
    }
```

> The current release date `2021-05-06T10:00:00.000Z` is older than `2021-05-23T1100:00.000Z` which is the `date` of
> the newest item in Revision History.

### 6.2.7 Missing Date in Involvements <a id='missing-date-in-involvements'></a>

For each item in the list of involvements it MUST be tested that it includes the property `date`.

The relevant path for this test is:

```
    /vulnerabilities[]/involvements
```

*Example 1 (which fails the test):*<a id='missing-date-in-involvements-eg-1'></a><a id='sec-6-2-7-eg-1'></a><a id='example-99'></a>

```
  "vulnerabilities": [
    {
      "involvements": [
        {
          "party": "vendor",
          "status": "in_progress"
        }
      ]
    }
  ]
```

> The list of involvements contains an item which does not contain the property `date`.

### 6.2.8 Use of MD5 as the only Hash Algorithm <a id='use-of-md5-as-the-only-hash-algorithm'></a>

It MUST be tested that the hash algorithm `md5` is not the only one present.

> Since collision attacks exist for MD5 such value should be accompanied by a second cryptographically stronger hash.
> This will allow users to double check the results.

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/product/product_identification_helper/hashes[]/file_hashes
  /product_tree/full_product_names[]/product_identification_helper/hashes[]/file_hashes
  /product_tree/relationships[]/full_product_name/product_identification_helper/hashes[]/file_hashes
```

*Example 1 (which fails the test):*<a id='use-of-md5-as-the-only-hash-algorithm-eg-1'></a><a id='sec-6-2-8-eg-1'></a><a id='example-100'></a>

```
  "product_tree": {
    "full_product_names": [
      {
        "name": "Product A",
        "product_id": "CSAFPID-9080700",
        "product_identification_helper": {
          "hashes": [
            {
              "file_hashes": [
                {
                  "algorithm": "md5",
                  "value": "6ae24620ea9656230f49234efd078935"
                }
              ],
              "filename": "product_a.so"
            }
          ]
        }
      }
    ]
  }
```

> The hash algorithm `md5` is used in one item of hashes without being accompanied by a second hash algorithm.

### 6.2.9 Use of SHA-1 as the only Hash Algorithm <a id='use-of-sha-1-as-the-only-hash-algorithm'></a>

It MUST be tested that the hash algorithm `sha1` is not the only one present.

> Since collision attacks exist for SHA-1 such value should be accompanied by a second cryptographically stronger hash.
> This will allow users to double check the results.

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/product/product_identification_helper/hashes[]/file_hashes
  /product_tree/full_product_names[]/product_identification_helper/hashes[]/file_hashes
  /product_tree/relationships[]/full_product_name/product_identification_helper/hashes[]/file_hashes
```

*Example 1 (which fails the test):*<a id='use-of-sha-1-as-the-only-hash-algorithm-eg-1'></a><a id='sec-6-2-9-eg-1'></a><a id='example-101'></a>

```
  "product_tree": {
    "full_product_names": [
      {
        "name": "Product A",
        "product_id": "CSAFPID-9080700",
        "product_identification_helper": {
          "hashes": [
            {
              "file_hashes": [
                {
                  "algorithm": "sha1",
                  "value": "e067035314dd8673fe1c9fc6b01414fe0950fdc4"
                }
              ],
              "filename": "product_a.so"
            }
          ]
        }
      }
    ]
  }
```

> The hash algorithm `sha1` is used in one item of hashes without being accompanied by a second hash algorithm.

### 6.2.10 Missing TLP label <a id='missing-tlp-label'></a>

It MUST be tested that `/document/distribution/tlp/label` is present and valid.

> TLP labels support the machine-readability and automated distribution.

The relevant path for this test is:

```
  /document/distribution/tlp/label
```

*Example 1 (which fails the test):*<a id='missing-tlp-label-eg-1'></a><a id='sec-6-2-10-eg-1'></a><a id='example-102'></a>

```
    "distribution": {
      "text": "Distribute freely."
    }
```

> The CSAF document has no TLP label.

### 6.2.11 Missing Canonical URL <a id='missing-canonical-url'></a>

It MUST be tested that the CSAF document has a canonical URL.

> To implement this test it is deemed sufficient that one item in `/document/references` fulfills all of the following:
>
> * It has the category `self`.
> * The `url` starts with `https://`.
> * The `url` ends with the valid filename for the CSAF document according to the rules in section [5.1](#filename).

The relevant path for this test is:

```
  /document/references
```

*Example 1 (which fails the test):*<a id='missing-canonical-url-eg-1'></a><a id='sec-6-2-11-eg-1'></a><a id='example-103'></a>

```
  "document": {
    // ...
    "references": [
      {
        "category": "self",
        "summary": "A non-canonical URL.",
        "url": "https://example.com/security/data/csaf/2021/OASIS_CSAF_TC-CSAF_2.0-2021-6-2-11-01_1.json"
      }
    ],
    // ...
    "tracking": {
      // ...
      "id": "OASIS_CSAF_TC-CSAF_2.0-2021-6-2-11-01",
      // ...
      "version": "1"
    },
    // ...
  }
```

> The only element where the `category` is `self` has a URL that does not fulfill the requirement of a valid filename for a CSAF document.

### 6.2.12 Missing Document Language <a id='missing-document-language'></a>

It MUST be tested that the document language is present and set.

The relevant path for this test is:

```
  /document/lang
```

*Example 1 (which fails the test):*<a id='missing-document-language-eg-1'></a><a id='sec-6-2-12-eg-1'></a><a id='example-104'></a>

```
  "document": {
    "category": "csaf_base",
    "csaf_version": "2.0",
    "publisher": {
      // ...
    },
    // ...
  }
```

> The document language is not defined.

### 6.2.13 Sorting <a id='optional-tests--sorting'></a>

It MUST be tested that all keys in a CSAF document are sorted alphabetically.

The relevant path for this test is:

```
  /
```

*Example 1 (which fails the test):*<a id='optional-tests--sorting-eg-1'></a><a id='sec-6-2-13-eg-1'></a><a id='example-105'></a>

```
  "document": {
    "csaf_version": "2.0",
    "category": "csaf_base",
    // ...
  }
```

> The key `csaf_version` is not at the right place.

> A tool MAY sort the keys as a quick fix.

### 6.2.14 Use of Private Language <a id='use-of-private-language'></a>

For each element of type `/$defs/language_t` it MUST be tested that the language code does not contain subtags reserved for private use.

The relevant paths for this test are:

```
  /document/lang
  /document/source_lang
```

*Example 1 (which fails the test):*<a id='use-of-private-language-eg-1'></a><a id='sec-6-2-14-eg-1'></a><a id='example-106'></a>

```
  "lang": "qtx"
```

> The language code `qtx` is reserved for private use.

> A tool MAY remove such subtag as a quick fix.

### 6.2.15 Use of Default Language <a id='use-of-default-language'></a>

For each element of type `/$defs/language_t` it MUST be tested that the language code is not `i-default`.

The relevant paths for this test are:

```
  /document/lang
  /document/source_lang
```

*Example 1 (which fails the test):*<a id='use-of-default-language-eg-1'></a><a id='sec-6-2-15-eg-1'></a><a id='example-107'></a>

```
  "lang": "i-default"
```

> The language code `i-default` is used.

> A tool MAY remove such element as a quick fix.

### 6.2.16 Missing Product Identification Helper <a id='missing-product-identification-helper'></a>

For each element of type `/$defs/full_product_name_t` it MUST be tested that it includes the property `product_identification_helper`.

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/product
  /product_tree/full_product_names[]
  /product_tree/relationships[]/full_product_name
```

*Example 1 (which fails the test):*<a id='missing-product-identification-helper-eg-1'></a><a id='sec-6-2-16-eg-1'></a><a id='example-108'></a>

```
    "full_product_names": [
      {
        "product_id": "CSAFPID-9080700",
        "name": "Product A"
      }
    ]
```

> The product `CSAFPID-9080700` does not provide any Product Identification Helper at all.

### 6.2.17 CVE in field IDs <a id='cve-in-field-ids'></a>

For each item in `/vulnerabilities[]/ids` it MUST be tested that it is not a CVE ID.

> It is sufficient to check, whether the property `text` matches the regex `^CVE-[0-9]{4}-[0-9]{4,}$`.

The relevant paths for this test are:

```
  /vulnerabilities[]/ids[]
```

*Example 1 (which fails the test):*<a id='cve-in-field-ids-eg-1'></a><a id='sec-6-2-17-eg-1'></a><a id='example-109'></a>

```
      "ids": [
        {
          "system_name": "CVE Project",
          "text": "CVE-2021-44228"
        }
      ]
```

> The `CVE-2021-44228` is listed in an item of the `ids` array instead under `cve`.

> A tool MAY set such element as value for the `cve` property as a quick fix, if that didn't exist before.
> Alternatively, it MAY remove such element as a quick fix.

### 6.2.18 Product Version Range without vers <a id='product-version-range-without-vers'></a>

For each element of type `/$defs/branches_t` with `category` of `product_version_range` it MUST be tested that
the value of `name` conforms the vers specification.

> To implement this test it is deemed sufficient that the value of `name` matches the following regex:
>
> ```
>   ^vers:[a-z\\.\\-\\+][a-z0-9\\.\\-\\+]*/.+
> ```

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/name
```

*Example 1 (which fails the test):*<a id='product-version-range-without-vers-eg-1'></a><a id='sec-6-2-18-eg-1'></a><a id='example-110'></a>

```
            "branches": [
              {
                "category": "product_version_range",
                "name": ">4.2",
                // ...
              }
            ]
```

> The version range `>4.2` is a valid vsl but not valid according to the vers specification.

### 6.2.19 CVSS for Fixed Products <a id='cvss-for-fixed-products'></a>

For each item the fixed products group (`first_fixed` and `fixed`) it MUST be tested that
a CVSS applying to this product has an environmental score of `0`.
The test SHALL pass if none of the Product IDs listed within product status `fixed` or
`first_fixed` is found in `products` of any item of the `scores` element.

The relevant path for this test is:

```
  /vulnerabilities[]/product_status/first_fixed[]
  /vulnerabilities[]/product_status/fixed[]
```

*Example 1 (which fails the test):*<a id='cvss-for-fixed-products-eg-1'></a><a id='sec-6-2-19-eg-1'></a><a id='example-111'></a>

```
  "product_tree": {
    "full_product_names": [
      {
        "product_id": "CSAFPID-9080700",
        "name": "Product A"
      }
    ]
  },
  "vulnerabilities": [
    {
      "product_status": {
        "fixed": [
          "CSAFPID-9080700"
        ]
      },
      "scores": [
        {
          "cvss_v3": {
            "baseScore": 6.5,
            "baseSeverity": "MEDIUM",
            "vectorString": "CVSS:3.1/AV:L/AC:L/PR:H/UI:R/S:U/C:H/I:H/A:H",
            "version": "3.1"
          },
          "products": [
            "CSAFPID-9080700"
          ]
        }
      ]
    }
  ]
```

> Neither the `environmentalScore` nor the properties `modifiedIntegrityImpact`, `modifiedAvailabilityImpact`, `modifiedConfidentialityImpact` nor
> the corresponding attributes in the `vectorString` have been set.

> A tool MAY set the properties `modifiedIntegrityImpact`, `modifiedAvailabilityImpact`, `modifiedConfidentialityImpact` accordingly and
> compute the `environmentalScore` as quick fix.

### 6.2.20 Additional Properties <a id='additional-properties'></a>

It MUST be tested that there is no additional property in the CSAF document that was not defined in the CSAF JSON schema.

The relevant path for this test is:

```
  /
```

> To implement this test it is deemed sufficient to validate the CSAF document against a "strict" version schema that
> sets `additionalProperties` to `false` for every key of type `object`.

*Example 1 (which fails the test):*<a id='additional-properties-eg-1'></a><a id='sec-6-2-20-eg-1'></a><a id='example-112'></a>

```
  "document": {
    "category": "csaf_base",
    "csaf_version": "2.0",
    "custom_property": "any",
    // ...
  }
```

> The key `custom_property` is not defined in the JSON schema.

> A tool MAY remove such keys as a quick fix.

## 6.3 Informative Test <a id='informative-test'></a>

Informative tests provide insights in common mistakes and bad practices.
They MAY fail at a valid CSAF document.
It is up to the issuing party to decide whether this was an intended behavior and can be ignore or should be treated.
These tests MAY include information about recommended usage.
A program MUST handle a test failure as a information.

### 6.3.1 Use of CVSS v2 as the only Scoring System <a id='use-of-cvss-v2-as-the-only-scoring-system'></a>

For each item in the list of scores which contains the `cvss_v2` object it MUST be tested that is not the only scoring item present.
The test SHALL pass if a second scoring object is available.

The relevant path for this test is:

```
    /vulnerabilities[]/scores
```

*Example 1 (which fails the test):*<a id='use-of-cvss-v2-as-the-only-scoring-system-eg-1'></a><a id='sec-6-3-1-eg-1'></a><a id='example-113'></a>

```
  "product_tree": {
    "full_product_names": [
      {
        "product_id": "CSAFPID-9080700",
        "name": "Product A"
      }
    ]
  },
  "vulnerabilities": [
    {
      "scores": [
        {
          "products": [
            "CSAFPID-9080700"
          ],
          "cvss_v2": {
            "version": "2.0",
            "vectorString": "AV:N/AC:L/Au:N/C:C/I:C/A:C",
            "baseScore": 10
          }
        }
      ]
    }
  ]
```

> There is only a CVSS v2 score given for `CSAFPID-9080700`.

Recommendation:

It is recommended to (also) use the CVSS v3.1.

### 6.3.2 Use of CVSS v3.0 <a id='use-of-cvss-v3-0'></a>

For each item in the list of scores which contains the `cvss_v3` object it MUST be tested that CVSS v3.0 is not used.

The relevant paths for this test are:

```
  /vulnerabilities[]/scores[]/cvss_v3/version
  /vulnerabilities[]/scores[]/cvss_v3/vectorString
```

*Example 1 (which fails the test):*<a id='use-of-cvss-v3-0-eg-1'></a><a id='sec-6-3-2-eg-1'></a><a id='example-114'></a>

```
  "cvss_v3": {
    "version": "3.0",
    "vectorString": "CVSS:3.0/AV:L/AC:L/PR:H/UI:R/S:U/C:H/I:H/A:H",
    "baseScore": 6.5,
    "baseSeverity": "MEDIUM"
  }
```

> The CVSS v3.0 is used.

Recommendation:

It is recommended to upgrade to CVSS v3.1.

> A tool MAY upgrade to CVSS v3.1 as quick fix.
> However, if such quick fix is supported the tool SHALL also recompute the `baseScore` and `baseSeverity`.
> The same applies for `temporalScore` and `temporalSeverity` respectively `environmentalScore` and `environmentalSeverity` if
> the necessary fields for computing their value are present and set.

### 6.3.3 Missing CVE <a id='missing-cve'></a>

It MUST be tested that the CVE number is given.

The relevant path for this test is:

```
  /vulnerabilities[]/cve
```

*Example 1 (which fails the test):*<a id='missing-cve-eg-1'></a><a id='sec-6-3-3-eg-1'></a><a id='example-115'></a>

```
  "vulnerabilities": [
    {
      "title": "BlueKeep"
    }
  ]
```

> The CVE number is not given.

Recommendation:

It is recommended to provide a CVE number to support the users efforts to find more details about a vulnerability and
potentially track it through multiple advisories.
If no CVE exists for that vulnerability, it is recommended to get one assigned.

### 6.3.4 Missing CWE <a id='missing-cwe'></a>

It MUST be tested that the CWE is given.

The relevant path for this test is:

```
  /vulnerabilities[]/cwe
```

*Example 1 (which fails the test):*<a id='missing-cwe-eg-1'></a><a id='sec-6-3-4-eg-1'></a><a id='example-116'></a>

```
  "vulnerabilities": [
    {
      "cve": "CVE-2019-0708",
      "title": "BlueKeep"
    }
  ]
```

> The CWE number is not given.

### 6.3.5 Use of Short Hash <a id='use-of-short-hash'></a>

It MUST be tested that the length of the hash value is not shorter than 64 characters.

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/product/product_identification_helper/hashes[]/file_hashes[]/value
  /product_tree/full_product_names[]/product_identification_helper/hashes[]/file_hashes[]/value
  /product_tree/relationships[]/full_product_name/product_identification_helper/hashes[]/file_hashes[]/value
```

*Example 1 (which fails the test):*<a id='use-of-short-hash-eg-1'></a><a id='sec-6-3-5-eg-1'></a><a id='example-117'></a>

```
  "product_tree": {
    "full_product_names": [
      {
        "name": "Product A",
        "product_id": "CSAFPID-9080700",
        "product_identification_helper": {
          "hashes": [
            {
              "file_hashes": [
                {
                  "algorithm": "md4",
                  "value": "3202b50e2e5b2fcd75e284c3d9d5f8d6"
                }
              ],
              "filename": "product_a.so"
            }
          ]
        }
      }
    ]
  }
```

> The length of the hash value is only 32 characters long.

### 6.3.6 Use of non-self referencing URLs Failing to Resolve <a id='use-of-non-self-referencing-urls-failing-to-resolve'></a>

For each URL which is not in the category `self` it MUST be tested that it resolves with a HTTP status code from
the 2xx (Successful) or 3xx (Redirection) class.

> This test does not apply for any item in an array of type `references_t` with the category `self`.
> For details about the HTTP status code classes see \[[RFC7231](#RFC7231)\].

The relevant paths for this test are:

```
  /document/acknowledgments[]/urls[]
  /document/aggregate_severity/namespace
  /document/distribution/tlp/url
  /document/references[]/url
  /document/publisher/namespace
  /product_tree/branches[]/product/product_identification_helper/sbom_urls[]
  /product_tree/branches[]/product/product_identification_helper/x_generic_uris[]/namespace
  /product_tree/branches[]/product/product_identification_helper/x_generic_uris[]/uri
  /product_tree/branches[](/branches[])*/product/product_identification_helper/sbom_urls[]
  /product_tree/branches[](/branches[])*/product/product_identification_helper/x_generic_uris[]/namespace
  /product_tree/branches[](/branches[])*/product/product_identification_helper/x_generic_uris[]/uri
  /product_tree/full_product_names[]/product_identification_helper/sbom_urls[]
  /product_tree/full_product_names[]/product_identification_helper/x_generic_uris[]/namespace
  /product_tree/full_product_names[]/product_identification_helper/x_generic_uris[]/uri
  /product_tree/relationships[]/full_product_name/product_identification_helper/sbom_urls[]
  /product_tree/relationships[]/full_product_name/product_identification_helper/x_generic_uris[]/namespace
  /product_tree/relationships[]/full_product_name/product_identification_helper/x_generic_uris[]/uri
  /vulnerabilities[]/acknowledgments[]/urls[]
  /vulnerabilities[]/references[]/url
  /vulnerabilities[]/remediations[]/url
```

*Example 1 (which fails the test):*<a id='use-of-non-self-referencing-urls-failing-to-resolve-eg-1'></a><a id='sec-6-3-6-eg-1'></a><a id='example-118'></a>

```
    "references": [
      {
        "summary": "A URL that does not resolve with HTTP status code in the interval between (including) 200 and (excluding) 400.",
        "url": "https://example.invalid"
      }
    ]
```

> The `category` is not set and therefore treated as its default value `external`.
> A request to that URL does not resolve with a status code from the 2xx (Successful) or 3xx (Redirection) class.

### 6.3.7 Use of self referencing URLs Failing to Resolve <a id='use-of-self-referencing-urls-failing-to-resolve'></a>

For each item in an array of type `references_t` with the category `self` it MUST be tested that
the URL referenced resolves with a HTTP status code less than 400.

> This test will most likely fail if the CSAF document is in a status before the initial release.
> For details about the HTTP status code classes see \[[RFC7231](#RFC7231)\].

The relevant paths for this test are:

```
  /document/references[]/url
  /vulnerabilities[]/references[]/url
```

*Example 1 (which fails the test):*<a id='use-of-self-referencing-urls-failing-to-resolve-eg-1'></a><a id='sec-6-3-7-eg-1'></a><a id='example-119'></a>

```
    "references": [
      {
        "category": "self",
        "summary": "A URL that does not resolve with HTTP status code in the interval between (including) 200 and (excluding) 400.",
        "url": "https://example.invalid"
      }
    ]
```

> The `category` is `self` and a request to that URL does not resolve with a status code from the 2xx (Successful) or 3xx (Redirection) class.

### 6.3.8 Spell check <a id='spell-check'></a>

If the document language is given it MUST be tested that a spell check for the given language does not find any mistakes.
The test SHALL be skipped if not document language is set. It SHALL fail it the given language is not supported.
The value of `/document/category` SHOULD NOT be tested if the CSAF document does not use the profile "CSAF Base".

The relevant paths for this test are:

```
  /document/acknowledgments[]/names[]
  /document/acknowledgments[]/organization
  /document/acknowledgments[]/summary
  /document/aggregate_severity/text
  /document/category
  /document/distribution/text
  /document/notes[]/audience
  /document/notes[]/text
  /document/notes[]/title
  /document/publisher/issuing_authority
  /document/publisher/name
  /document/references[]/summary
  /document/title
  /document/tracking/aliases[]
  /document/tracking/generator/engine/name
  /document/tracking/revision_history[]/summary
  /product_tree/branches[](/branches[])*/name
  /product_tree/branches[](/branches[])*/product/name
  /product_tree/branches[]/name
  /product_tree/branches[]/product/name
  /product_tree/full_product_names[]/name
  /product_tree/product_groups[]/summary
  /product_tree/relationships[]/full_product_name/name
  /vulnerabilities[]/acknowledgments[]/names[]
  /vulnerabilities[]/acknowledgments[]/organization
  /vulnerabilities[]/acknowledgments[]/summary
  /vulnerabilities[]/involvements[]/summary
  /vulnerabilities[]/notes[]/audience
  /vulnerabilities[]/notes[]/text
  /vulnerabilities[]/notes[]/title
  /vulnerabilities[]/references[]/summary
  /vulnerabilities[]/remediations[]/details
  /vulnerabilities[]/remediations[]/entitlements[]
  /vulnerabilities[]/remediations[]/restart_required/details
  /vulnerabilities[]/threats[]/details
  /vulnerabilities[]/title
```

*Example 1 (which fails the test):*<a id='spell-check-eg-1'></a><a id='sec-6-3-8-eg-1'></a><a id='example-120'></a>

```
  "document": {
    // ...
    "lang": "en",
    "notes": [
      {
        "category": "summary",
        "text": "Secruity researchers found multiple vulnerabilities in XYZ."
      }
    ],
    // ...
  }
```

> There is a spelling mistake in `Secruity`.

### 6.3.9 Branch Categories <a id='branch-categories'></a>

For each element of type `/$defs/full_product_name_t` in `/product_tree/branches` it MUST be tested that
ancestor nodes along the path exist which use the following branch categories `vendor` -> `product_name` -> `product_version` in that
order starting with the Product tree node.

> Other branch categories can be used before, after or between the aforementioned branch categories without making the test invalid.

The relevant paths for this test are:

```
  /product_tree/branches
```

*Example 1 (which fails the test):*<a id='branch-categories-eg-1'></a><a id='sec-6-3-9-eg-1'></a><a id='example-121'></a>

```
    "branches": [
      {
        "category": "vendor",
        "name": "Example Company",
        "branches": [
          {
            "category": "product_name",
            "name": "Product A",
            "branches": [
              {
                "category": "patch_level",
                "name": "91",
                "product": {
                  "product_id": "CSAFPID-0002",
                  "name": "Example Company Product A Update 91"
                }
              }
            ]
          }
        ]
      }
    ]
```

> The product `CSAFPID-9080700` does not have any ancestor with the branch category `product_version`.

### 6.3.10 Usage of Product Version Range <a id='usage-of-product-version-range'></a>

For each element of type `/$defs/branches_t` it MUST be tested that the `category` is not `product_version_range`.

> It is usually hard decide for machines whether a product version matches a product version ranges.
> Therefore, it is recommended to avoid version ranges and enumerate versions wherever possible.

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/category
```

*Example 1 (which fails the test):*<a id='usage-of-product-version-range-eg-1'></a><a id='sec-6-3-10-eg-1'></a><a id='example-122'></a>

```
                "category": "product_version_range",
```

> The category `product_version_range` was used.

### 6.3.11 Usage of V as Version Indicator <a id='usage-of-v-as-version-indicator'></a>

For each element of type `/$defs/branches_t` with `category` of `product_version` it MUST be tested that
the value of `name` does not start with `v` or `V` before the version.

> To implement this test it is deemed sufficient that the value of `name` does not match the following regex:
>
> ```
>   ^[vV][0-9].*$
> ```

The relevant paths for this test are:

```
  /product_tree/branches[](/branches[])*/name
```

*Example 1 (which fails the test):*<a id='usage-of-v-as-version-indicator-eg-1'></a><a id='sec-6-3-11-eg-1'></a><a id='example-123'></a>

```
            "branches": [
              {
                "category": "product_version",
                "name": "v4.2",
                // ...
              }
            ]
```

> The product version starts with a `v`.

-------

# 7. Distributing CSAF documents <a id='distributing-csaf-documents'></a>

This section lists requirements and roles defined for distributing CSAF documents.
The first subsection provides all requirements - the second one the roles.
It is mandatory to fulfill the basic role "CSAF publisher". The last section provides specific rules for the process of retrieving CSAF documents.

## 7.1 Requirements <a id='requirements'></a>

The requirements in this subsection are consecutively numbered to be able to refer to them directly.
The order does not give any hint about the importance.
Not all requirements have to be fulfilled to conform to this specification - the sets of
requirements per conformance clause are defined in section [7.2](#roles).

### 7.1.1 Requirement 1: Valid CSAF document <a id='requirement-1-valid-csaf-document'></a>

The document is a valid CSAF document (cf. Conformance clause 1).

### 7.1.2 Requirement 2: Filename <a id='requirement-2-filename'></a>

The CSAF document has a filename according to the rules in section [5.1](#filename).

### 7.1.3 Requirement 3: TLS <a id='requirement-3-tls'></a>

The CSAF document is per default retrievable from a website which uses TLS for encryption and server authenticity.
The CSAF document MUST NOT be downloadable from a location which does not encrypt the transport when crossing organizational
boundaries to maintain the chain of custody.

### 7.1.4 Requirement 4: TLP:WHITE <a id='requirement-4-tlp-white'></a>

If the CSAF document is labeled TLP:WHITE, it MUST be freely accessible.

This does not exclude that such a document is also available in an access protected customer portal.
However, there MUST be one copy of the document available for people without access to the portal.

> Reasoning: If an advisory is already in the media, an end user should not be forced to collect the pieces of information from a
> press release but be able to retrieve the CSAF document.

### 7.1.5 Requirement 5: TLP:AMBER and TLP:RED <a id='requirement-5-tlp-amber-and-tlp-red'></a>

CSAF documents labeled TLP:AMBER or TLP:RED MUST be access protected.
If they are provided via a web server this SHALL be done under a different path than for TLP:WHITE,
TLP:GREEN and unlabeled CSAF documents. TLS client authentication, access tokens or any other automatable authentication method SHALL be used.

An issuing party MAY agree with the recipients to use any kind of secured drop at the recipients' side to avoid putting them on their own website.
However, it MUST be ensured that the documents are still access protected.

### 7.1.6 Requirement 6: No Redirects <a id='requirement-6-no-redirects'></a>

Redirects SHOULD NOT be used. If they are inevitable only HTTP Header redirects are allowed.

> Reasoning: Clients should not parse the payload for navigation and some, as e.g. `curl`, do not follow any other kind of redirects.

### 7.1.7 Requirement 7: provider-metadata.json <a id='requirement-7-provider-metadata-json'></a>

The party MUST provide a valid `provider-metadata.json` according to the schema
[CSAF provider metadata](https://docs.oasis-open.org/csaf/csaf/v2.0/provider_json_schema.json) for its own metadata.
The `publisher` object SHOULD match the one used in the CSAF documents of the issuing party but can be set to whatever value a
CSAF aggregator SHOULD display over any individual `publisher` values in the CSAF documents themselves.

> This information is used to collect the data for CSAF aggregators, listers and end users.
> The CSAF provider metadata schema ensures the consistency of the metadata for a CSAF provider across the ecosystem.
> Other approaches, like extracting the `publisher` object from CSAF documents, are likely to fail if the object differs between CSAF documents.
>
> It is suggested to put the file `provider-metadata.json` adjacent to the ROLIE feed documents (requirement 15)
> or in the main directory adjacent to the year folders (requirement 14), `changes.csv` (requirement 13) and the `index.txt` (requirement 12).
> Suggested locations to store the `provider-metadata.json` are:
>
> * https://www.example.com/.well-known/csaf/provider-metadata.json
> * https://domain.tld/security/data/csaf/provider-metadata.json
> * https://psirt.domain.tld/advisories/csaf/provider-metadata.json
> * https://domain.tld/security/csaf/provider-metadata.json

*Example 1 (minimal with ROLIE document):*<a id='requirement-7-provider-metadata-json-eg-1'></a><a id='sec-7-1-7-eg-1'></a><a id='example-124'></a>

```
  {
    "canonical_url": "https://www.example.com/.well-known/csaf/provider-metadata.json",
    "distributions": [
      {
        "rolie":{
          "feeds": [
            {
              "summary":"All TLP:WHITE advisories of Example Company.",
              "tlp_label": "WHITE",
              "url": "https://www.example.com/.well-known/csaf/feed-tlp-white.json"
            }
          ]
        }
      }
    ],
    "last_updated": "2021-07-12T20:20:56.169Z",
    "list_on_CSAF_aggregators": true,
    "metadata_version": "2.0",
    "mirror_on_CSAF_aggregators": true,
    "public_openpgp_keys": [
      {
        "fingerprint": "8F5F267907B2C4559DB360DB2294BA7D2B2298B1",
        "url": "https://keys.example.net/vks/v1/by-fingerprint/8F5F267907B2C4559DB360DB2294BA7D2B2298B1"
      }
    ],
    "publisher": {
      "category": "vendor",
      "name": "Example Company ProductCERT",
      "namespace":"https://psirt.example.com"
    },
    "role": "csaf_trusted_provider"
  }
```

If a CSAF publisher (cf. section [7.2.1](#role-csaf-publisher)) does not provide the `provider-metadata.json`,
an aggregator SHOULD contact the CSAF publisher in question to determine the values for `list_on_CSAF_aggregators` and `mirror_on_CSAF_aggregators`.
If that is impossible or if the CSAF publisher is unresponsive the following values MUST be used:

```
    "list_on_CSAF_aggregators": true,
    "mirror_on_CSAF_aggregators": false
```

> This prevents that CSAF documents of a CSAF publisher which have been collected by one CSAF aggregator A are mirrored again on a
> second CSAF aggregator B. Such cascades are prone to outdated information.
> If the first aggregator A collects the CSAF documents on best effort and B copies the files from A and announces that this is done weekly,
> one might assume that B's CSAF documents are more recent.
> However, that is not the case as B's information depends on A.

### 7.1.8 Requirement 8: security.txt <a id='requirement-8-security-txt'></a>

In the security.txt there MUST be at least one field `CSAF` which points to the `provider-metadata.json` (requirement 7).
If this field indicates a web URI, then it MUST begin with "https://" (as per section 2.7.2 of \[[RFC7230](#RFC7230)\]).
See \[[SECURITY-TXT](#SECURITY-TXT)\] for more details.

> The security.txt was published as \[[RFC9116](#RFC9116)\] in April 2022. At the time of this writing,
> the `CSAF` field is in the process of being officially added.

*Examples 1:*<a id='requirement-8-security-txt-eg-1'></a><a id='sec-7-1-8-eg-1'></a><a id='example-125'></a>

```
CSAF: https://domain.tld/security/data/csaf/provider-metadata.json
CSAF: https://psirt.domain.tld/advisories/csaf/provider-metadata.json
CSAF: https://domain.tld/security/csaf/provider-metadata.json
CSAF: https://www.example.com/.well-known/csaf/provider-metadata.json
```

It is possible to advertise more than one `provider-metadata.json` by adding multiple `CSAF` fields,
e.g. in case of changes to the organizational structure through merges or acquisitions.
However, this SHOULD NOT be done and removed as soon as possible.
If one of the URLs fulfills requirement 9, this MUST be used as the first CSAF entry in the security.txt.

### 7.1.9 Requirement 9: Well-known URL for provider-metadata.json <a id='requirement-9-well-known-url-for-provider-metadata-json'></a>

The URL path `/.well-known/csaf/provider-metadata.json` under the main domain of the issuing authority serves directly
the `provider-metadata.json` according to requirement 7.
The use of the scheme "HTTPS" is required. See \[[RFC8615](#RFC8615)\] for more details.

*Example 1:*<a id='requirement-9-well-known-url-for-provider-metadata-json-eg-1'></a><a id='sec-7-1-9-eg-1'></a><a id='example-126'></a>

```
  https://www.example.com/.well-known/csaf/provider-metadata.json
```

### 7.1.10 Requirement 10: DNS path <a id='requirement-10-dns-path'></a>

The DNS record `csaf.data.security.domain.tld` SHALL resolve as a web server which serves directly
the `provider-metadata.json` according to requirement 7.
The use of the scheme "HTTPS" is required.

### 7.1.11 Requirement 11: One folder per year <a id='requirement-11-one-folder-per-year'></a>

The CSAF documents MUST be located within folders named `<YYYY>` where `<YYYY>` is the year given in the
value of `/document/tracking/initial_release_date`.

*Examples 1:*<a id='requirement-11-one-folder-per-year-eg-1'></a><a id='sec-7-1-11-eg-1'></a><a id='example-127'></a>

```
2021
2020
```

### 7.1.12 Requirement 12: index.txt <a id='requirement-12-index-txt'></a>

The index.txt file within MUST provide a list of all filenames of CSAF documents which are located in the sub-directories with their filenames.

*Example 1:*<a id='requirement-12-index-txt-eg-1'></a><a id='sec-7-1-12-eg-1'></a><a id='example-128'></a>

```
2020/example_company_-_2020-yh4711.json
2019/example_company_-_2019-yh3234.json
2018/example_company_-_2018-yh2312.json
```

> This can be used to download all CSAF documents.

### 7.1.13 Requirement 13: changes.csv <a id='requirement-13-changes-csv'></a>

The file changes.csv MUST contain the filename as well as the value of `/document/tracking/current_release_date` for each
CSAF document in the sub-directories without a heading; lines MUST be sorted by the `current_release_date` timestamp with the latest one first.

*Example 1:*<a id='requirement-13-changes-csv-eg-1'></a><a id='sec-7-1-13-eg-1'></a><a id='example-129'></a>

```
"2020/example_company_-_2020-yh4711.json","2020-07-01T10:09:07Z"
"2018/example_company_-_2018-yh2312.json","2020-07-01T10:09:01Z"
"2019/example_company_-_2019-yh3234.json","2019-04-17T15:08:41Z"
"2018/example_company_-_2018-yh2312.json","2019-03-01T06:01:00Z"
```

### 7.1.14 Requirement 14: Directory listings <a id='requirement-14-directory-listings'></a>

Directory listing SHALL be enabled to support manual navigation.

### 7.1.15 Requirement 15: ROLIE feed <a id='requirement-15-rolie-feed'></a>

Resource-Oriented Lightweight Information Exchange (ROLIE) is a standard to ease discovery of security content.
ROLIE is built on top of the Atom Publishing Format and Protocol, with specific requirements that support publishing security content.
All CSAF documents with the same TLP level MUST be listed in a single ROLIE feed.
At least one of the feeds

* TLP:WHITE
* TLP:GREEN
* unlabeled

MUST exist.
Each ROLIE feed document MUST be a JSON file that conforms with \[[RFC8322](#RFC8322)\].

*Example 1:*<a id='requirement-15-rolie-feed-eg-1'></a><a id='sec-7-1-15-eg-1'></a><a id='example-130'></a>

```
  {
    "feed": {
      "id": "example-csaf-feed-tlp-white",
      "title": "Example CSAF feed (TLP:WHITE)",
      "link": [
        {
          "rel": "self",
          "href": "https://psirt.domain.tld/advisories/csaf/feed-tlp-white.json"
        }
      ],
      "category": [ 
        {
          "scheme": "urn:ietf:params:rolie:category:information-type",
          "term": "csaf"
        }
      ],
      "updated": "2021-01-01T12:00:00.000Z",
      "entry": [
        {
          "id": "2020-ESA-001",
          "title": "Example Security Advisory 001",
          "link": [
            {
              "rel": "self",
              "href": "https://psirt.domain.tld/advisories/csaf/2020/2020-ESA-001.json"
            },
            {
              "rel": "hash",
              "href": "https://psirt.domain.tld/advisories/csaf/2020/2020-ESA-001.json.sha512"
            },
            {
              "rel": "signature",
              "href": "https://psirt.domain.tld/advisories/csaf/2020/2020-ESA-001.json.asc"
            }
          ],
          "published": "2021-01-01T11:00:00.000Z",
          "updated": "2021-01-01T12:00:00.000Z",
          "summary": {
            "content": "Vulnerabilities fixed in ABC 0.0.1"
          },
          "content": {
            "type": "application/json",
            "src": "https://psirt.domain.tld/advisories/csaf/2020/2020-ESA-001.json"
          },
          "format": {
            "schema": "https://docs.oasis-open.org/csaf/csaf/v2.0/csaf_json_schema.json",
            "version": "2.0"
          }
        }
      ]
    }
  }
```

Any existing hash file (requirement 18) MUST be listed in the corresponding entry of the ROLIE feed as an item of
the array `link` having the `rel` value of `hash`.
Any existing signature file (requirement 19) MUST be listed in the corresponding entry of the ROLIE feed as an item of the array `link`
having the `rel` value of `signature`.

### 7.1.16 Requirement 16: ROLIE service document <a id='requirement-16-rolie-service-document'></a>

The use and therefore the existence of ROLIE service document is optional.
If it is used, each ROLIE service document MUST be a JSON file that conforms with \[[RFC8322](#RFC8322)\] and lists the ROLIE feed documents.

*Example 1:*<a id='requirement-16-rolie-service-document-eg-1'></a><a id='sec-7-1-16-eg-1'></a><a id='example-131'></a>

```
  {
    "service": {
      "workspace": [
        {
          "title": "Public CSAF feed",
          "collection": [
            {
              "title": "Example CSAF feed (TLP:WHITE)",
              "href": "https://psirt.domain.tld/advisories/csaf/feed-tlp-white.json",
              "categories": {
                "category": [
                  {
                    "scheme": "urn:ietf:params:rolie:category:information-type",
                    "term": "csaf"
                  }
                ]
              }
            }
          ]
        }
      ]
    }
  }
```

### 7.1.17 Requirement 17: ROLIE category document <a id='requirement-17-rolie-category-document'></a>

The use and therefore the existence of ROLIE category document is optional.
If it is used, each ROLIE category document MUST be a JSON file that conforms with \[[RFC8322](#RFC8322)\].
ROLIE categories SHOULD be used for to further dissect CSAF documents by one or more of the following criteria:

* document category
* document language
* values of the branch category within the Product Tree including but not limited to
  * `vendor`
  * `product_family`
  * `product_name`
  * `product_version`
* type of product

  *Examples 1:*<a id='requirement-17-rolie-category-document-eg-1'></a><a id='sec-7-1-17-eg-1'></a><a id='example-132'></a>

  ```
    CPU
    Firewall
    Monitor
    PLC
    Printer
    Router
    Sensor
    Server
  ```

* areas or sectors, the products are used in

  *Examples 2:*<a id='requirement-17-rolie-category-document-eg-2'></a><a id='sec-7-1-17-eg-2'></a><a id='example-133'></a>

  ```
    Chemical
    Commercial
    Communication
    Critical Manufacturing
    Dams
    Energy
    Healthcare
    Water
  ```

* any other categorization useful to the consumers

*Example 3:*<a id='requirement-17-rolie-category-document-eg-3'></a><a id='sec-7-1-17-eg-3'></a><a id='example-134'></a>

```
  {
    "categories": {
      "category": [
        {
            "term": "Example Company Product A"
        },
        {
            "term": "Example Company Product B"
        }
      ]
    }
  }
```

### 7.1.18 Requirement 18: Integrity <a id='requirement-18-integrity'></a>

All CSAF documents SHALL have at least one hash file computed with a secure cryptographic hash algorithm (e.g. SHA-512 or SHA-3)
to ensure their integrity. The filename is constructed by appending the file extension which is given by the algorithm.

MD5 and SHA1 SHOULD NOT be used.

*Example 1:*<a id='requirement-18-integrity-eg-1'></a><a id='sec-7-1-18-eg-1'></a><a id='example-135'></a>

```
File name of CSAF document: example_company_-_2019-yh3234.json
File name of SHA-256 hash file: example_company_-_2019-yh3234.json.sha256
File name of SHA-512 hash file: example_company_-_2019-yh3234.json.sha512
```

The file content SHALL start with the first byte of the hexadecimal hash value.
Any subsequent data (like a filename) which is optional SHALL be separated by at least one space.

*Example 2:*<a id='requirement-18-integrity-eg-2'></a><a id='sec-7-1-18-eg-2'></a><a id='example-136'></a>

```
ea6a209dba30a958a78d82309d6cdcc6929fcb81673b3dc4d6b16fac18b6ff38  example_company_-_2019-yh3234.json
```

If a ROLIE feed exists, each hash file MUST be listed in it as described in requirement 15.

### 7.1.19 Requirement 19: Signatures <a id='requirement-19-signatures'></a>

All CSAF documents SHALL have at least one OpenPGP signature file which is provided under the same filename which is
extended by the appropriate extension. See \[[RFC4880](#RFC4880)\] for more details.

*Example 1:*<a id='requirement-19-signatures-eg-1'></a><a id='sec-7-1-19-eg-1'></a><a id='example-137'></a>

```
File name of CSAF document: example_company_-_2019-yh3234.json
File name of signature file: example_company_-_2019-yh3234.json.asc
```

If a ROLIE feed exists, each signature file MUST be listed in it as described in requirement 15.

### 7.1.20 Requirement 20: Public OpenPGP Key <a id='requirement-20-public-openpgp-key'></a>

The public part of the OpenPGP key used to sign the CSAF documents MUST be available.
It SHOULD also be available at a public key server.

> For example, the public part of the OpenPGP key could be placed in a directory `openpgp` adjacent to the `provider-metadata.json`.

The OpenPGP key SHOULD have a strength that is considered secure.

> Guidance on OpenPGP key strength can be retrieved from technical guidelines of competent authorities.

### 7.1.21 Requirement 21: List of CSAF providers <a id='requirement-21-list-of-csaf-providers'></a>

The file `aggregator.json` MUST be present and valid according to the
JSON schema [CSAF aggregator](https://docs.oasis-open.org/csaf/csaf/v2.0/aggregator_json_schema.json).
It MUST NOT be stored adjacent to a `provider-metadata.json`.

> Suggested locations to store the `aggregator.json` are:
>
> * https://www.example.com/.well-known/csaf-aggregator/aggregator.json
> * https://domain.tld/security/data/aggregator/csaf/aggregator.json
> * https://psirt.domain.tld/advisories/aggregator/csaf/aggregator.json
> * https://domain.tld/security/aggregator/csaf/aggregator.json

The file `aggregator.json` SHOULD only list the latest version of the metadata of a CSAF provider.

*Example 1:*<a id='requirement-21-list-of-csaf-providers-eg-1'></a><a id='sec-7-1-21-eg-1'></a><a id='example-138'></a>

```
  {
    "aggregator": {
      "category": "lister",
      "contact_details": "Example CSAF Lister can be reached at contact_us@lister.example, or via our website at https://lister.example/security/csaf/aggregator/contact.",
      "issuing_authority": "This service is provided as it is. It is free for everybody.",
      "name": "Example CSAF Lister",
      "namespace": "https://lister.example"
    },
    "aggregator_version": "2.0",
    "canonical_url": "https://aggregator.example/.well-known/csaf-aggregator/aggregator.json",
    "csaf_providers": [
      {
        "metadata": {
          "last_updated": "2021-07-12T20:20:56.169Z",
          "publisher": {
            "category": "vendor",
            "name": "Example Company ProductCERT",
            "namespace": "https://psirt.example.com"
          },
          "url": "https://www.example.com/.well-known/csaf/provider-metadata.json"
        }
      },
      {
        "metadata": {
          "last_updated": "2021-07-12T21:35:38.000Z",
          "publisher": {
            "category": "coordinator",
            "name": "Example Coordinator CERT",
            "namespace": "https://cert.example"
          },
          "url": "https://cert.example/advisories/csaf/provider-metadata.json"
        }
      }
    ],
    "last_updated":"2021-07-12T22:35:38.978Z"
  }
```

### 7.1.22 Requirement 22: Two disjoint issuing parties <a id='requirement-22-two-disjoint-issuing-parties'></a>

The file `aggregator.json` (requirement 21) lists at least two disjoint CSAF providers (including CSAF trusted providers)
or one CSAF publisher and one CSAF provider (including CSAF trusted provider).

### 7.1.23 Requirement 23: Mirror <a id='requirement-23-mirror'></a>

The CSAF documents for each issuing party that is mirrored MUST be in a different folder.
The folder name SHOULD be retrieved from the name of the issuing authority.
This folders MUST be adjacent to the `aggregator.json` (requirement 21).
Each such folder MUST at least:

* provide a `provider-metadata.json` for the current issuing party.
* provide the ROLIE feed document according to requirement 15 which links to the local copy of the CSAF document.

*Example 1:*<a id='requirement-23-mirror-eg-1'></a><a id='sec-7-1-23-eg-1'></a><a id='example-139'></a>

```
  {
    "aggregator": {
      "category": "aggregator",
      "contact_details": "Example Aggregator can be reached at contact_us@aggregator.example, or via our website at https://aggregator.example/security/csaf/aggregator/contact.",
      "issuing_authority": "This service is provided as it is. It is free for everybody.",
      "name": "Example Aggregator",
      "namespace": "https://aggregator.example"
    },
    "aggregator_version": "2.0",
    "canonical_url": "https://aggregator.example/.well-known/csaf-aggregator/aggregator.json",
    "csaf_providers": [
      {
        "metadata": {
          "last_updated": "2021-07-12T20:20:56.169Z",
          "publisher": {
            "category": "vendor",
            "name": "Example Company ProductCERT",
            "namespace": "https://psirt.example.com"
          },
          "url": "https://www.example.com/.well-known/csaf/provider-metadata.json"
        },
        "mirrors": [
          "https://aggregator.example/.well-known/csaf-aggregator/Example_Company_ProductCERT/provider-metadata.json"
        ]
      },
      {
        "metadata": {
          "last_updated": "2021-07-12T21:35:38.000Z",
          "publisher": {
            "category": "coordinator",
            "name": "Example Coordinator CERT",
            "namespace": "https://cert.example"
          },
          "url": "https://cert.example/advisories/csaf/provider-metadata.json"
        },
        "mirrors": [
          "https://aggregator.example/.well-known/csaf-aggregator/Example_Coordinator_CERT/provider-metadata.json"
        ]
      }
    ],
    "last_updated":"2021-07-12T22:35:38.978Z"
  }
```

## 7.2 Roles <a id='roles'></a>

This subsection groups the requirements from the previous subsection into named sets which target the roles with the same name.
This allows end users to request their suppliers to fulfill a certain set of requirements.
A supplier can use roles for advertising and marketing.

The roles "CSAF publisher", "CSAF provider", and "CSAF trusted provider" are intended directly for issuing parties and form the first group.
The second group consists of the roles "CSAF lister" and "CSAF aggregator".
They collect data from the aforementioned issuing parties of the first group and provide them in a single place to aid in automation.
Parties of the second group can also issue their own advisories.
However, they MUST follow the rules for the first group for that.

Both, a CSAF lister and a CSAF aggregator, decide based on their own rules which issuing parties to list respectively to mirror.
However, an issuing party MAY apply to be listed or mirrored.

Issuing parties MUST indicate through the value `false` in `list_on_CSAF_aggregators` if they do not want to be listed.
Issuing parties MUST indicate through the value `false` in `mirror_on_CSAF_aggregators` if they do not want to be mirrored.

The values are independent.
The combination of the value `false` in `list_on_CSAF_aggregators` and `true` in `mirror_on_CSAF_aggregators` implies that
the issuing party does not want to be listed without having the CSAF documents mirrored.
Therefore, a CSAF aggregator can list that issuing party if it mirrors the files.

### 7.2.1 Role: CSAF publisher <a id='role-csaf-publisher'></a>

A distributing party satisfies the "CSAF publisher" role if the party:

* satisfies the requirements 1 to 4 in section [7.1](#requirements).
* distributes only CSAF documents on behalf of its own.

### 7.2.2 Role: CSAF provider <a id='role-csaf-provider'></a>

A CSAF publisher satisfies the "CSAF provider" role if the party fulfills the following three groups of requirements:

Firstly, the party:

* satisfies the "CSAF publisher" role profile.
* additionally satisfies the requirements 5 to 7 in section [7.1](#requirements).

Secondly, the party:

* satisfies at least one of the requirements 8 to 10 in section [7.1](#requirements).

Thirdly, the party:

* satisfies the requirements 11 to 14 in section [7.1](#requirements) or requirements 15 to 17 in section [7.1](#requirements).

> If the party uses the ROLIE-based distribution, it MUST also satisfy requirements 15 to 17.
> If it uses the directory-based distribution, it MUST also satisfy requirements 11 to 14.

### 7.2.3 Role: CSAF trusted provider <a id='role-csaf-trusted-provider'></a>

A CSAF provider satisfies the "CSAF trusted provider" role if the party:

* satisfies the "CSAF provider" role profile.
* additionally satisfies the requirements 18 to 20 in section [7.1](#requirements).

### 7.2.4 Role: CSAF lister <a id='role-csaf-lister'></a>

A distributing party satisfies the "CSAF lister" role if the party:

* satisfies the requirements 6, 21 and 22 in section [7.1](#requirements).
* uses the value `lister` for `/aggregator/category`.
* does not list any mirror pointing to a domain under its own control.

> The purpose of this role is to provide a list of URLs where to find CSAF documents.
> It is not assumed that the list will be complete.

### 7.2.5 Role: CSAF aggregator <a id='role-csaf-aggregator'></a>

A distributing party satisfies the "CSAF aggregator" role if the party:

* satisfies the requirements 1 to 6 and 21 to 23 in section [7.1](#requirements).
* uses the value `aggregator` for `/aggregator/category`.
* lists a mirror for at least two disjoint issuing parties pointing to a domain under its own control.
* links the public part of the OpenPGP key used to sign CSAF documents for each mirrored issuing party in
  the corresponding `provider-metadata.json`.
* provides for each CSAF document that is mirrored a signature (requirement 19) and a hash (requirement 18).
  Both SHALL be listed in the ROLIE feed. If the issuing party provides those files for a CSAF document, they SHOULD be copied as well.
  If the issuing party does not provide those files, they SHALL be created by the CSAF aggregator.
  Such a signature does not imply any liability of CSAF aggregator for the content of the corresponding CSAF document.
  It just confirms that the CSAF document provided has not been modified after being downloaded from the issuing party.
  A CSAF aggregator MAY add additional signatures and hashes for a CSAF document.

Additionally, a CSAF aggregator MAY list one or more issuing parties that it does not mirror.

> The purpose of this role is to provide a single point where CSAF documents can be retrieved.
> Multiple CSAF aggregators are expected to exist around the world. None of them is required to mirror all CSAF documents of all issuing parties.
> CSAF aggregators can be provided for free or as a paid service.
>
> To aid in automation, CSAF aggregators MAY mirror CSAF documents from CSAF publishers.
> Regarding the terms of use they SHOULD consult with the issuing party.
> The purpose of this option is that a consumer can retrieve CSAF documents from a CSAF publisher as if this issuing party would be a
> CSAF trusted provider. To reach that goal, a CSAF aggregator collects the CSAF documents from the CSAF publisher and mirrors it.
> The collection process MAY be automated or manual. CSAF aggregators announce the collection interval through the field `update_interval` in
> the corresponding item of the CSAF publishers list (`csaf_publishers`) in their `aggregator.json`.
> To minimize the implementation efforts and process overhead, a CSAF aggregator MAY upload the CSAF documents of a CSAF publisher into
> an internal instance of a CSAF provider software.
> Such construct is called "CSAF proxy provider" as it can be mirrored by the CSAF aggregator software.
> However, such a CSAF proxy provider MUST NOT be accessible from anyone else than the CSAF aggregator itself.
> Otherwise, that would violate the second rule of section [7.2.1](#role-csaf-publisher).
> Therefore, it is recommended to expose the CSAF proxy provider only on localhost and allow the access only from the CSAF aggregator software.

## 7.3 Retrieving rules <a id='retrieving-rules'></a>

The retrieving process executes in two phases: Finding the `provider-metadata.json` (requirement 7 in section [7.1](#requirements)) and
retrieving CSAF documents.

> A retrieving party SHOULD do the first phase every time.
> Based on the setup and use case of the retrieving party it MAY choose to do it less often,
> e.g. only when adding new or updating distributing parties.
> In that case, it SHOULD to check regularly whether new information is available.

### 7.3.1 Finding provider-metadata.json <a id='finding-provider-metadata-json'></a>

**Direct locating**: The following process SHOULD be used to determine the location of a `provider-metadata.json`
(requirement 7 in section [7.1](#requirements)) based on the main domain of the issuing party:

1. Checking the Well-known URL (requirement 9 in section [7.1](#requirements))
2. Checking the security.txt (requirement 8 in section [7.1](#requirements))
3. Checking the DNS path (requirement 10 in section [7.1](#requirements))
4. Select one or more `provider-metadata.json` to use.

> The term "checking" used in the listing above SHOULD be understood as follows:
> Try to access the resource and test whether the response provides an expected result as defined in the requirement in section 7.1.
> If that is the case, the step was successful - otherwise not.

The first two steps SHOULD be performed in all cases as the security.txt MAY advertise additional `provider-metadata.json`.
The third step SHOULD only be performed if the first two did not result in the location of at least one `provider-metadata.json`.

**Indirect locating**: A retrieving party MAY choose to determine the location of a `provider-metadata.json` by retrieving
its location from an `aggregator.json` (requirement 21 in section [7.1](#requirements)) of a CSAF lister or CSAF aggregator.

### 7.3.2 Retrieving CSAF documents <a id='retrieving-csaf-documents'></a>

Given a `provider-metadata.json`, the following process SHOULD be used to retrieve CSAF documents:

1. Parse the `provider-metadata.json` to determine whether the directory-based (requirements 11 to 14 in section [7.1](#requirements))
   or ROLIE-based distribution (requirements 15 to 17 in section [7.1](#requirements)) is used.
   If both are present, the ROLIE information SHOULD be preferred.
2. For any CSAF trusted provider, the hash and signature files (requirements 18 to 19 in section [7.1](#requirements)) SHOULD be retrieved together
   with the CSAF document.
   They MUST be checked before further processing the CSAF document.
3. Test the CSAF document against the schema.
4. Execute mandatory tests on the CSAF document.

-------

# 8. Safety, Security, and Data Protection Considerations <a id='safety-security-and-data-protection-considerations'></a>

CSAF documents are based on JSON, thus the security considerations of \[[RFC8259](#RFC8259)\] apply and are repeated here as service for the reader:
> Generally, there are security issues with scripting languages.  JSON is a subset of JavaScript but excludes assignment and invocation.
>
> Since JSON's syntax is borrowed from JavaScript, it is possible to use that language's `eval()` function to parse most JSON texts
> (but not all; certain characters such as `U+2028 LINE SEPARATOR` and `U+2029 PARAGRAPH SEPARATOR` are legal in JSON but not JavaScript).
> This generally constitutes an unacceptable security risk, since the text could contain executable code along with data declarations.
> The same consideration applies to the use of eval()-like functions in any other programming language in which JSON texts conform to
> that language's syntax.

In addition, CSAF documents may be rendered by consumers in various human-readable formats like HTML or PDF.
Thus, for security reasons, CSAF producers and consumers SHALL adhere to the following:

* CSAF producers SHOULD NOT emit messages that contain HTML, even though all variants of Markdown permit it.
  To include HTML, source code, or any other content that may be interpreted or executed by a CSAF consumer,
  e.g. to provide a proof-of-concept, the issuing party SHALL use Markdown's fenced code blocks or inline code option.
* Deeply nested markup can cause a stack overflow in the Markdown processor \[[GFMENG](#GFMENG)\].
  To reduce this risk, CSAF consumers SHALL use a Markdown processor that is hardened against such attacks.
  **Note**: One example is the GitHub fork of the `cmark` Markdown processor \[[GFMCMARK](#GFMCMARK)\].
* To reduce the risk posed by possibly malicious CSAF files that do contain arbitrary HTML (including, for example, javascript: links),
  CSAF consumers SHALL either disable HTML processing (for example, by using an option such as the --safe option in the cmark Markdown processor)
  or run the resulting HTML through an HTML sanitizer.
CSAF consumers that are not prepared to deal with the security implications of formatted messages SHALL NOT attempt to
render them and SHALL instead fall back to the corresponding plain text messages. As also any other programming code can
be contained within a CSAF document, CSAF consumers SHALL ensure that none of the values of a CSAF document is run as code.
Moreover, it SHALL be treated as unsafe (user) input.
  > Additional, supporting mitigation measures like retrieving only CSAF documents from trusted sources and check their integrity and
  > signature before parsing the document SHOULD be in place to reduce the risk further.

-------

# 9. Conformance <a id='conformance'></a>

In the only subsection of this section, the conformance targets and clauses are listed.
The clauses, matching the targets one to one, are listed in separate sub-subsections of the targets listing subsection.

Informative Comments:

> The order in which targets, and their corresponding clauses appear is somewhat arbitrary as there is
> no natural order on such diverse roles participating in the document exchanging ecosystem.
>
> Except for the target **CSAF document**, all other 16 targets span a taxonomy of the complex CSAF ecosystems existing
> in and between diverse security advisory generating, sharing, and consuming communities.
>
> In any case, there are no capabilities organized in increasing quality levels for targets because
> the security advisory sharing communities follow the chain link model.
> Instead, a single minimum capability level for every target is given to maintain important goals of providing
> a common framework for security advisories:
>
> * Fast production, sharing, and actionable consumption of security advisories
> * Consistent end to end automation through collaborating actors
> * Clear baseline across the communities per this specification
> * Additional per-community cooperative extensions which may flow back into future updates of this specification

## 9.1 Conformance Targets <a id='conformance-targets'></a>

This document defines requirements for the CSAF file format and for certain software components that interact with it.
The entities ("conformance targets") for which this document defines requirements are:

* **CSAF document**: A security advisory text document in the format defined by this document.
* **CSAF producer**: A program which emits output in the CSAF format.
* **CSAF direct producer**: An analysis tool which acts as a CSAF producer.
* **CSAF converter**: A CSAF producer that transforms the output of an analysis tool from its native output format into the CSAF format.
* **CVRF CSAF converter**: A CSAF producer which takes a CVRF document as input and converts it into a valid CSAF document.
* **CSAF content management system**: A program that is able to create,
  review and manage CSAF documents and is able to preview their details as required by CSAF viewer.
* **CSAF post-processor**: A CSAF producer that transforms an existing CSAF document into a new CSAF document,
  for example, by removing or redacting elements according to sharing policies.
* **CSAF modifier**: A CSAF post-processor which takes a CSAF document as input and modifies the structure or values of properties.
  The output is a valid CSAF document.
* **CSAF translator**: A CSAF post-processor which takes a CSAF document as input and translates values of properties into another language.
  The output is a valid CSAF document.
* **CSAF consumer**: A program that reads and interprets a CSAF document.
* **CSAF viewer**: A CSAF consumer that reads a CSAF document, displays a list of the results it contains,
  and allows an end user to view each result in the context of the artifact in which it occurs.
* **CSAF management system**: A program that is able to manage CSAF documents and is able to display their details as required by CSAF viewer.
* **CSAF asset matching system**: A program that connects to or is an asset database and is able to manage CSAF documents as required
  by CSAF management system as well as matching them to assets of the asset database.
* **CSAF basic validator**: A program that reads a document and checks it against the JSON schema and performs mandatory tests.
* **CSAF extended validator**: A CSAF basic validator that additionally performs optional tests.
* **CSAF full validator**: A CSAF extended validator that additionally performs informative tests.
* **CSAF SBOM matching system**: A program that connects to or is an SBOM database and is able to manage CSAF documents as required
  by CSAF management system as well as matching them to SBOM components of the SBOM database.

### 9.1.1 Conformance Clause 1: CSAF document <a id='conformance-clause-1-csaf-document'></a>

A text file or data stream satisfies the "CSAF document" conformance profile if it:

* conforms to the syntax and semantics defined in section [3](#schema-elements).
* satisfies at least one profile defined in section [4](#profiles).
* does not fail any mandatory test defined in section [6.1](#mandatory-tests).

### 9.1.2 Conformance Clause 2: CSAF producer <a id='conformance-clause-2-csaf-producer'></a>

A program satisfies the "CSAF producer" conformance profile if the program:

* produces output in the CSAF format, according to the conformance profile "CSAF document" .
* satisfies those normative requirements in section [3](#schema-elements) and [8](#safety-security-and-data-protection-considerations) that
  are designated as applying to CSAF producers.

### 9.1.3 Conformance Clause 3: CSAF direct producer <a id='conformance-clause-3-csaf-direct-producer'></a>

An analysis tool satisfies the "CSAF direct producer" conformance profile if the analysis tool:

* satisfies the "CSAF producer" conformance profile.
* additionally satisfies those normative requirements in section [3](#schema-elements) that are designated as applying to "direct producers" or
  to "analysis tools".
* does not emit any objects, properties, or values which, according to section [3](#schema-elements),
  are intended to be produced only by converters.

### 9.1.4 Conformance Clause 4: CSAF converter <a id='conformance-clause-4-csaf-converter'></a>

A converter satisfies the “CSAF converter” conformance profile if the converter:

* satisfies the "CSAF producer" conformance profile.
* additionally satisfies those normative requirements in section [3](#schema-elements) that are designated as applying to converters.
* does not emit any objects, properties, or values which, according to section [3](#schema-elements),
  are intended to be produced only by direct producers.

### 9.1.5 Conformance Clause 5: CVRF CSAF converter <a id='conformance-clause-5-cvrf-csaf-converter'></a>

A program satisfies the "CVRF CSAF converter" conformance profile if the program fulfills the following two groups of requirements:

Firstly, the program:

* satisfies the "CSAF producer" conformance profile.
* takes only CVRF documents as input.
* additionally satisfies the normative requirements given below.

Secondly, the program fulfills the following for all items of:

* type `/$defs/branches_t`: If any `prod:Branch` instance has the type `Realm` or `Resource`,
  the CVRF CSAF converter replaces those with the category `product_name`.
  In addition, the converter outputs a warning that those types do not exist in CSAF and have been replaced with the category `product_name`.
* type `/$defs/version_t`: If any element doesn't match the semantic versioning,
  replace the all elements of type `/$defs/version_t` with the corresponding integer version.
  For that, CVRF CSAF converter sorts the items of `/document/tracking/revision_history` by `number` ascending according to the rules of CVRF.
  Then, it replaces the value of `number` with the index number in the array (starting with 1).
  The value of `/document/tracking/version` is replaced by value of `number` of the corresponding revision item.
  The match MUST be calculated by the original values used in the CVRF document.
  If this conversion was applied, for each Revision the original value of `cvrf:Number` MUST be set as `legacy_version` in the converted document.
* `/document/acknowledgments[]/organization` and `/vulnerabilities[]/acknowledgments[]/organization`:
  If more than one `cvrf:Organization` instance is given, the CVRF CSAF converter converts the first one into the `organization`.
  In addition, the converter outputs a warning that information might be lost during conversion of document or vulnerability acknowledgment.
* `/document/lang`: If one or more CVRF element containing an `xml:lang` attribute exist and contain the exact same value,
  the CVRF CSAF converter converts this value into `lang`.
  If the values of `xml:lang` attributes are not equal, the CVRF CSAF converter outputs a warning that the language could not be
  determined and possibly a document with multiple languages was produced.
  In addition, it SHOULD also present all values of `xml:lang` attributes as a set in the warning.
* `/document/publisher/name` and `/document/publisher/namespace`:
  Sets the value as given in the configuration of the program or the corresponding argument the program was invoked with.
  If values from both sources are present, the program SHOULD prefer the latter one.
  The program SHALL NOT use hard-coded values.
* `/document/tracking/id`: If the element `cvrf:ID` contains any line breaks or leading or trailing white space,
  the CVRF CSAF converter removes those characters.
  In addition, the converter outputs a warning that the ID was changed.
* `/product_tree/relationships[]`: If more than one `prod:FullProductName` instance is given,
  the CVRF CSAF converter converts the first one into the `full_product_name`.
  In addition, the converter outputs a warning that information might be lost during conversion of product relationships.
* `/vulnerabilities[]/cwe`: If more than one `vuln:CWE` instance is given,
  the CVRF CSAF converter converts the first one into `cwe`.
  In addition, the converter outputs a warning that information might be lost during conversion of the CWE.
* `/vulnerabilities[]/ids`: If a `vuln:ID` element is given, the CVRF CSAF converter converts it into the first item of the `ids` array.
* `/vulnerabilities[]/remediation[]`: If no `product_ids` or `group_ids` is given,
  the CVRF CSAF converter appends all Product IDs which are listed under `../product_status` in the arrays `known_affected`,
  `first_affected` and `last_affected` into `product_ids`.
  If none of these arrays exist, the CVRF CSAF converter outputs an error that no matching Product ID was found for this remediation element.
* `/vulnerabilities[]/scores[]`:
  * For any CVSS v3 element, the CVRF CSAF converter MUST compute the `baseSeverity` from the `baseScore` according to
    the rules of the applicable CVSS standard.
  * If no `product_id` is given, the CVRF CSAF converter appends all Product IDs which are listed under `../product_status` in
    the arrays `known_affected`, `first_affected` and `last_affected`.
    If none of these arrays exist, the CVRF CSAF converter outputs an error that no matching Product ID was found for this score element.
  * If a `vectorString` is missing, the CVRF CSAF converter outputs an error that the CVSS element could not be converted as
    the CVSS vector was missing.
    A CVRF CSAF converter MAY offer a configuration option to delete such elements.
  * If there are CVSS v3.0 and CVSS v3.1 Vectors available for the same product, the CVRF CSAF converter discards
    the CVSS v3.0 information and provide in CSAF only the CVSS v3.1 information.
  * To determine, which minor version of CVSS v3 is used, the CVRF CSAF converter uses the following steps:
    1. Retrieve the CVSS version from the CVSS vector, if present.

        *Example 1:*<a id='conformance-clause-5-cvrf-csaf-converter-eg-1'></a><a id='sec-9-1-5-eg-1'></a><a id='example-140'></a>

        ```
          CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H => 3.1
        ```

    2. Retrieve the CVSS version from the CVSS element's namespace, if present.
       The CVRF CSAF converter outputs a warning that this value was guessed from the element's namespace.

        *Example 2:*<a id='conformance-clause-5-cvrf-csaf-converter-eg-2'></a><a id='sec-9-1-5-eg-2'></a><a id='example-141'></a>

        ```
          xmlns:cvssv31="https://www.first.org/cvss/cvss-v3.1.xsd"
          <!-- -->
          <cvssv31:ScoreSetV3>
        ```

        is handled the same as

        *Example 3:*<a id='conformance-clause-5-cvrf-csaf-converter-eg-3'></a><a id='sec-9-1-5-eg-3'></a><a id='example-142'></a>

        ```
          <ScoreSetV3 xmlns="https://www.first.org/cvss/cvss-v3.1.xsd">
        ```

    3. Retrieve the CVSS version from the CVSS namespace given in the root element, if present.
       The CVRF CSAF converter outputs a warning that this value was guessed from the global namespace.
       If more than one CVSS namespace is present and the element is not clearly defined via the namespace,
       this step MUST be skipped without a decision.

        *Example 4:*<a id='conformance-clause-5-cvrf-csaf-converter-eg-4'></a><a id='sec-9-1-5-eg-4'></a><a id='example-143'></a>

        ```
          xmlns:cvssv3="https://www.first.org/cvss/cvss-v3.0.xsd" => 3.0
        ```

    4. Retrieve the CVSS version from a config value, which defaults to `3.0`.
       (As CSAF CVRF v1.2 predates CVSS v3.1.) The CVRF CSAF converter outputs a warning that this value was taken from the config.

### 9.1.6 Conformance Clause 6: CSAF content management system <a id='conformance-clause-6-csaf-content-management-system'></a>

A CSAF content management system satisfies the "CSAF content management system" conformance profile if the content management system:

* satisfies the "CSAF producer" conformance profile.
* satisfies the "CSAF viewer" conformance profile.
* provides at least the following management functions:

  * create new CSAF documents
  * prefill CSAF documents based on values given in the configuration (see below)
  * create a new version of an existing CSAF document
  * checkout old versions of a CSAF document
  * show all differences between versions of a CSAF document
  * list all CSAF documents within the system
  * delete CSAF documents from the system
  * review CSAF documents in the system
  * approve CSAF documents
  * search for CSAF documents by values of required fields at `document`-level or their children within the system
  * search for CSAF documents by values of `cve` within the system
  * search for CSAF documents based on properties of `product_tree`
  * filter on all properties which it is required to search for
  * export of CSAF documents
  * show an audit log for each CSAF document
  * identify the latest version of CSAF documents with the same `/document/tracking/id`
  * suggest a `/document/tracking/id` based on the given configuration.
  * track of the version of CSAF documents automatically and increment according to the versioning scheme
    (see also subsections of [3.1.11](#version-type)) selected in the configuration.
  * check that the document version is set correctly based on the changes in comparison to the previous version
    (see also subsections of [3.1.11](#version-type)).
  * suggest to use the document status `interim` if a CSAF document is updated more frequent than the given threshold in
    the configuration (default: 3 weeks)
  * suggest to publish a new version of the CSAF document with the document status `final` if the document status was
    `interim` and no new release has be done during the given threshold in the configuration (default: 6 weeks)
  * support the following workflows:

    * "New Advisory": create a new advisory, request a review, provide review comments or approve it, resolve review comments;
      if the review approved it, the approval for publication can be requested;
      if granted the document status changes to `final` (or `ìnterim` based on the selection in approval or configuration)
      and the advisory is provided for publication (manual or time-based)
    * "Update Advisory": open an existing advisory, create new revision & change content, request a review,
      provide review comments or approve it, resolve review comments;
      if the review approved it, the approval for publication can be requested;
      if granted the document status changes to `final` (or `ìnterim` based on the selection in approval or configuration)
      and the advisory is provided for publication (manual or time-based)

* offers both: publication immediately or at a given date/time.
* automates handling of date/time and version.
* provides an API to retrieve all CSAF documents which are currently in the status published.
* optionally provides an API to import or create new advisories from outside systems (e.g. bug tracker, CVD platform,...).
* provides a user management and support at least the following roles:

  * _Registered_: Able to see all published CSAF documents (but only in the published version).
  * _Author_: inherits _Registered_ permissions and also can Create and Edit Own (mostly used for automated creation, see above)
  * _Editor_: inherits _Author_ permissions and can Edit (mostly used in PSIRT)
  * _Publisher_: inherits _Editor_ permissions and can Change state and Review any (mostly used as HEAD of PSIRT or team lead)
  * _Reviewer_: inherits _Registered_ permissions and can Review advisories assigned to him (might be a subject matter expert or management)
  * _Manager_: inherits _Publisher_ permissions and can Delete; User management up to _Publisher_
  * _Administrator_: inherits _Manager_ permissions and can Change the configuration

* may use groups to support client separation (multitenancy) and therefore restrict the roles to actions within their group.
  In this case, there MUST be a _Group configurator_ which is able to change the values which are used to prefill fields in
  new advisories for that group. He might also do the user management for the group up to a configured level.
* prefills the following fields in new CSAF documents with the values given below or based on the templates from configuration:

  * `/document/csaf_version` with the value `2.0`
  * `/document/language`
  * `/document/notes`
    * `legal_disclaimer` (Terms of use from the configuration)
    * `general` (General Security recommendations from the configuration)
  * `/document/tracking/current_release_date` with the current date
  * `/document/tracking/generator` and children
  * `/document/tracking/initial_release_date` with the current date
  * `/document/tracking/revision_history`
    * `date` with the current date
    * `number` (based on the templates according to the versioning scheme configured)
    * `summary` (based on the templates from configuration; default: "Initial version.")
  * `/document/tracking/status` with `draft`
  * `/document/tracking/version` with the value of `number` the latest `/document/tracking/revision_history[]` element
  * `/document/publisher` and children
  * `/document/category` (based on the templates from configuration)

* When updating an existing CSAF document:
  
  * prefills all fields which have be present in the existing CSAF document
  * adds a new item in `/document/tracking/revision_history[]`
  * updates the following fields with the values given below or based on the templates from configuration:
    * `/document/csaf_version` with the value `2.0`
    * `/document/language`
    * `/document/notes`
      * `legal_disclaimer` (Terms of use from the configuration)
      * `general` (General Security recommendations from the configuration)
    * `/document/tracking/current_release_date` with the current date
    * `/document/tracking/generator` and children
    * the new item in `/document/tracking/revision_history[]`
      * `date` with the current date
      * `number` (based on the templates according to the versioning scheme configured)
    * `/document/tracking/status` with `draft`
    * `/document/tracking/version` with the value of `number` the latest `/document/tracking/revision_history[]` element
    * `/document/publisher` and children

### 9.1.7 Conformance Clause 7: CSAF post-processor <a id='conformance-clause-7-csaf-post-processor'></a>

A CSAF post-processor satisfies the "CSAF post-processor" conformance profile if the post-processor:

* satisfies the "CSAF consumer" conformance profile.
* satisfies the "CSAF producer" conformance profile.
* additionally satisfies those normative requirements in section [3](#schema-elements) that are designated as applying to post-processors.

### 9.1.8 Conformance Clause 8: CSAF modifier <a id='conformance-clause-8-csaf-modifier'></a>

A program satisfies the "CSAF modifier" conformance profile if the program fulfills the two following groups of requirements:

The program:

* satisfies the "CSAF post-processor" conformance profile.
* adds, deletes or modifies at least one property, array, object or value of a property or item of an array.
* does not emit any objects, properties, or values which, according to section [9](#conformance),
  are intended to be produced only by CSAF translators.
* satisfies the normative requirements given below.

The resulting modified document:

* does not have the same `/document/tracking/id` as the original document.
  The modified document can use a completely new `/document/tracking/id` or compute one by appending the original `/document/tracking/id` as
  a suffix after an ID from the naming scheme of the issuer of the modified version.
  It SHOULD NOT use the original `/document/tracking/id` as a prefix.
* includes a reference to the original advisory as first element of the array `/document/references[]`.

### 9.1.9 Conformance Clause 9: CSAF translator <a id='conformance-clause-9-csaf-translator'></a>

A program satisfies the "CSAF translator" conformance profile if the program fulfills the two following groups of requirements:

The program:

* satisfies the "CSAF post-processor" conformance profile.
* translates at least one value.
* preserves the same semantics and form across translations.
* satisfies the normative requirements given below and does not add or remove other elements than required below.

The resulting translated document:

* does not use the same `/document/tracking/id` as the original document.
  The translated document can use a completely new `/document/tracking/id` or compute one by using the original `/document/tracking/id` as
  a prefix and adding an ID from the naming scheme of the issuer of the translated version.
  It SHOULD NOT use the original `/document/tracking/id` as a suffix.
  If an issuer uses a CSAF translator to publish his advisories in multiple languages they MAY use the combination of
  the original `/document/tracking/id` and translated `/document/lang` as a `/document/tracking/id` for the translated document.
* provides the `/document/lang` property with a value matching the language of the translation.
* provides the `/document/source_lang` to contain the language of the original document (and SHOULD only be set by CSAF translators).
* has the value `translator` set in `/document/publisher/category`
* includes a reference to the original advisory as first element of the array `/document/references[]`.
* MAY contain translations for elements in arrays of `references_t` after the first element.
  However, it MUST keep the original URLs as references at the end.

### 9.1.10 Conformance Clause 10: CSAF consumer <a id='conformance-clause-10-csaf-consumer'></a>

A processor satisfies the "CSAF consumer" conformance profile if the processor:

* reads CSAF documents and interprets them according to the semantics defined in section [3](#schema-elements).
* satisfies those normative requirements in section [3](#schema-elements) and [8](#safety-security-and-data-protection-considerations) that
  are designated as applying to CSAF consumers.

### 9.1.11 Conformance Clause 11: CSAF viewer <a id='conformance-clause-11-csaf-viewer'></a>

A viewer satisfies the "CSAF viewer" conformance profile if the viewer fulfills the two following groups of requirements:

The viewer:

* satisfies the "CSAF consumer" conformance profile.
* satisfies the normative requirements given below.

For each CVSS-Score in `/vulnerabilities[]/scores[]` the viewer:

* preferably shows the `vector` if there is an inconsistency between the `vector` and any other sibling attribute.
* SHOULD prefer the item of `scores[]` for each `product_id` which has the highest CVSS Base Score and newest CVSS version
  (in that order) if a `product_id` is listed in more than one item of `scores[]`.

### 9.1.12 Conformance Clause 12: CSAF management system <a id='conformance-clause-12-csaf-management-system'></a>

A CSAF management system satisfies the "CSAF management system" conformance profile if the management system:

* satisfies the "CSAF viewer" conformance profile.
* provides at least the following management functions:
  * add new CSAF documents (e.g. from file system or URL) to the system
  * list all CSAF documents within the system
  * delete CSAF documents from the system
  * comment on CSAF documents in the system
  * mark CSAF documents as read in the system
  * search for CSAF documents by values of required fields at `document`-level or their children within the system
  * search for CSAF documents by values of `cve` within the system
  * search for CSAF documents based on properties of `/product_tree`
  * filter on all properties which it is required to search for
  * sort on all properties which it is required to search for
  * sort on CVSS scores and `/document/aggregate_severity/text`
* identifies the latest version of CSAF documents with the same `/document/tracking/id`.
* is able to show the difference between 2 versions of a CSAF document with the same `/document/tracking/id`.

### 9.1.13 Conformance Clause 13: CSAF asset matching system <a id='conformance-clause-13-csaf-asset-matching-system'></a>

A CSAF asset matching system satisfies the "CSAF asset matching system" conformance profile if the asset matching system:

* satisfies the "CSAF management system" conformance profile.
* is an asset database or connects to one.
* matches the CSAF documents within the system to the respective assets.
  This might be done with a probability which gives the end user the chance to broaden or narrow the results.
  The process of matching is also referred to as "run of the asset matching module".
* provides for each product of the asset database a list of matched advisories.
* provides for each asset of the asset database a list of matched advisories.
* provides for each CSAF document a list of matched product of the asset database.
* provides for each CSAF document a list of matched asset of the asset database.
* provides for each vulnerability within a CSAF document the option to mark a matched asset in the asset database as "not remediated",
  "remediation in progress", or "remediation done". A switch to mark all assets at once MAY be implemented.
* does not bring up a newer revision of a CSAF document as a new match if the remediation for the matched product or asset has not changed.
* detects the usage semantic version (as described in section [3.1.11.2](#version-type-semantic-versioning)).
* is able to trigger a run of the asset matching module:
  * manually:
    * per CSAF document
    * per list of CSAF documents
    * per asset
    * per list of assets
  * automatically:
    * when a new CSAF document is inserted (for this CSAF document)
    * when a new asset is inserted (for this asset)
    * when the Major version in a CSAF document with semantic versioning changes (for this CSAF document)
    > These also apply if more than one CSAF document or asset was added.
    > To reduce the computational efforts the runs can be pooled into one run which fulfills all the tasks at once (batch mode).
  * Manually and automatically triggered runs SHOULD NOT be pooled.
* provides at least the following statistics for the count of assets:
  * matching that CSAF document at all
  * marked with a given status

### 9.1.14 Conformance Clause 14: CSAF basic validator <a id='conformance-clause-14-csaf-basic-validator'></a>

A program satisfies the "CSAF basic validator" conformance profile if the program:

* reads documents and performs a check against the JSON schema.
* performs all mandatory tests as given in section [6.1](#mandatory-tests).
* does not change the CSAF documents.

A CSAF basic validator MAY provide one or more additional functions:

* Only run one or more selected mandatory tests.
* Apply quick fixes as specified in the standard.
* Apply additional quick fixes as implemented by the vendor.

### 9.1.15 Conformance Clause 15: CSAF extended validator <a id='conformance-clause-15-csaf-extended-validator'></a>

A CSAF basic validator satisfies the "CSAF extended validator" conformance profile if the CSAF basic validator:

* satisfies the "CSAF basic validator" conformance profile.
* additionally performs all optional tests as given in section [6.2](#optional-tests).

A CSAF extended validator MAY provide an additional function to only run one or more selected optional tests.

### 9.1.16 Conformance Clause 16: CSAF full validator <a id='conformance-clause-16-csaf-full-validator'></a>

A CSAF extended validator satisfies the "CSAF full validator" conformance profile if the CSAF extended validator:

* satisfies the "CSAF extended validator" conformance profile.
* additionally performs all informative tests as given in section [6.3](#informative-test).

A CSAF full validator MAY provide an additional function to only run one or more selected informative tests.

### 9.1.17 Conformance Clause 17: CSAF SBOM matching system <a id='conformance-clause-17-csaf-sbom-matching-system'></a>

A CSAF SBOM matching system satisfies the "CSAF SBOM matching system" conformance profile if the SBOM matching system:

* satisfies the "CSAF management system" conformance profile.
* is an SBOM database or connects to one.
  > A repository or any other location that can be queried for SBOMs and their content is also considered an SBOM database.
* matches the CSAF documents within the system to the respective SBOM components.
  This might be done with a probability which gives the user the chance to broaden or narrow the results.
  The process of matching is also referred to as "run of the SBOM matching module".
* provides for each SBOM of the SBOM database a list of matched advisories.
* provides for each SBOM component of the SBOM database a list of matched advisories.
* provides for each CSAF document a list of matched SBOMs of the SBOM database.
* provides for each CSAF document a list of matched SBOM components of the SBOM database.
* provides for each vulnerability within a CSAF document the option to mark a matched SBOM component in the SBOM database as "not remediated",
  "remediation in progress", or "remediation done".
  A switch to mark all SBOM component at once MAY be implemented.
* does not bring up a newer revision of a CSAF document as a new match if the remediation for the matched SBOM or SBOM component has not changed.
* detects the usage semantic version (as described in section [3.1.11.2](#version-type-semantic-versioning)).
* is able to trigger a run of the asset matching module:
  * manually:
    * per CSAF document
    * per list of CSAF documents
    * per SBOM component
    * per list of SBOM components
  * automatically:
    * when a new CSAF document is inserted (for this CSAF document)
    * when a new SBOM component is inserted (for this SBOM component)
    * when the Major version in a CSAF document with semantic versioning changes (for this CSAF document)
    > These also apply if more than one CSAF document or SBOM component was added.
    > To reduce the computational efforts the runs can be pooled into one run which fulfills all the tasks at once (batch mode).
  > Manually and automatically triggered runs should not be pooled.
* provides at least the following statistics for the count of SBOM component:
  * matching that CSAF document at all
  * marked with a given status

-------

# Appendix A. Acknowledgments <a id='acknowledgments'></a>

The following individuals were members of the OASIS CSAF Technical Committee during the creation of this specification and their contributions are gratefully acknowledged:

**CSAF TC Members:**

| First Name | Last Name        | Company                                               |
|:-----------|:-----------------|:------------------------------------------------------|
| Alexandre  | Dulaunoy         | CIRCL                                                 |
| Anthony    | Berglas          | Cryptsoft Pty Ltd.                                    |
| Art        | Manion           | Carnegie Mellon University                            |
| Aukjan     | van Belkum       | EclecticIQ                                            |
| Ben        | Sooter           | Electric Power Research Institute (EPRI)              |
| Bernd      | Grobauer         | Siemens AG                                            |
| Bruce      | Rich             | Cryptsoft Pty Ltd.                                    |
| Chok       | Poh              | Oracle                                                |
| Dan        | West             | Microsoft                                             |
| David      | Waltermire       | NIST                                                  |
| Denny      | Page             | TIBCO Software Inc.                                   |
| Duncan     | Sparrell         | sFractal Consulting LLC                               |
| Eric       | Johnson          | TIBCO Software Inc.                                   |
| Ethan      | Rahn             | Arista Networks                                       |
| Feng       | Cao              | Oracle                                                |
| Greg       | Scott            | Cryptsoft Pty Ltd.                                    |
| Harold     | Booth            | NIST                                                  |
| Jason      | Masters          | TELUS                                                 |
| Jennifer   | Victor           | Dell                                                  |
| Jessica    | Fitzgerald-McKay | National Security Agency                              |
| Jonathan   | Bitle            | Kaiser Permanente                                     |
| Justin     | Corlett          | Cryptsoft Pty Ltd.                                    |
| Kazuo      | Noguchi          | Hitachi, Ltd.                                         |
| Kent       | Landfield        | McAfee                                                |
| Langley    | Rock             | Red Hat                                               |
| Martin     | Prpic            | Red Hat                                               |
| Masato     | Terada           | Hitachi, Ltd.                                         |
| Mike       | Gorski           | Cisco Systems                                         |
| Nicole     | Parrish          | Mitre Corporation                                     |
| Omar       | Santos           | Cisco Systems                                         |
| Patrick    | Maroney          | AT&T                                                  |
| Rhonda     | Levy             | Cisco Systems                                         |
| Richard    | Struse           | Mitre Corporation                                     |
| Ritwik     | Ghoshal          | Oracle                                                |
| Robert     | Coderre          | Accenture                                             |
| Robert     | Keith            | Accenture                                             |
| Stefan     | Hagen            | Individual                                            |
| Tania      | Ward             | Dell                                                  |
| Ted        | Bedwell          | Cisco Systems                                         |
| Thomas     | Proell           | Siemens AG                                            |
| Thomas     | Schmidt          | Federal Office for Information Security (BSI) Germany |
| Tim        | Hudson           | Cryptsoft Pty Ltd.                                    |
| Tobias     | Limmer           | Siemens AG                                            |
| Tony       | Cox              | Cryptsoft Pty Ltd.                                    |
| Vincent    | Danen            | Red Hat                                               |
| Will       | Rideout          | Arista Networks                                       |
| Xiaoyu     | Ge               | Huawei Technologies Co., Ltd.                         |

The following individuals were members of the OASIS CSAF Technical Committee during the creation of the previous version (CVRF v1.2) of this specification and their contributions are gratefully acknowledged:

**CSAF TC Members:**

| First Name | Last Name        | Company                                               |
|:-----------|:-----------------|:------------------------------------------------------|
| Adam       | Montville        | CIS                                                   |
| Allan      | Thomson          | LookingGlass                                          |
| Anthony    | Berglas          | Cryptsoft Pty Ltd.                                    |
| Art        | Manion           | Carnegie Mellon University                            |
| Aukjan     | van Belkum       | EclecticIQ                                            |
| Ben        | Sooter           | Electric Power Research Institute                     |
| Bernd      | Grobauer         | Siemens AG                                            |
| Beth       | Pumo             | Kaiser Permanente                                     |
| Bret       | Jordan           | Symantec Corp.                                        |
| Bruce      | Rich             | Cryptsoft Pty Ltd.                                    |
| Chet       | Ensign           | OASIS                                                 |
| Chok       | Poh              | Oracle                                                |
| Chris      | Rouland          | Individual                                            |
| David      | Waltermire       | NIST                                                  |
| Denny      | Page             | TIBCO Software Inc.                                   |
| Doron      | Shiloach         | IBM                                                   |
| Duncan     | Sparrell         | sFractal Consulting LLC                               |
| Eric       | Johnson          | TIBCO Software Inc.                                   |
| Feng       | Cao              | Oracle                                                |
| Greg       | Reaume           | TELUS                                                 |
| Greg       | Scott            | Cryptsoft Pty Ltd.                                    |
| Harold     | Booth            | NIST                                                  |
| Jamison    | Day              | LookingGlass                                          |
| Jared      | Semrau           | "FireEye, Inc."                                       |
| Jason      | Masters          | TELUS                                                 |
| Jerome     | Athias           | Individual                                            |
| Jessica    | Fitzgerald-McKay | National Security Agency                              |
| Jonathan   | Bitle            | Kaiser Permanente                                     |
| Justin     | Corlett          | Cryptsoft Pty Ltd.                                    |
| Karen      | Scarfone         | Individual                                            |
| Kazuo      | Noguchi          | "Hitachi, Ltd."                                       |
| Kent       | Landfield        | McAfee                                                |
| Lothar     | Braun            | Siemens AG                                            |
| Louis      | Ronnau           | Cisco Systems                                         |
| Mark       | Davidson         | NC4                                                   |
| Mark-David | McLaughlin       | Cisco Systems                                         |
| Masato     | Terada           | "Hitachi, Ltd."                                       |
| Masood     | Nasir            | TELUS                                                 |
| Nicole     | Gong             | Mitre Corporation                                     |
| Omar       | Santos           | Cisco Systems                                         |
| Patrick    | Maroney          | Wapack Labs LLC                                       |
| Paul       | Patrick          | "FireEye, Inc."                                       |
| Peter      | Allor            | IBM                                                   |
| Phillip    | Boles            | "FireEye, Inc."                                       |
| Ravi       | Balupari         | Netskope                                              |
| Rich       | Reybok           | ServiceNow                                            |
| Richard    | Struse           | DHS Office of Cybersecurity and Communications (CS&C) |
| Ritwik     | Ghoshal          | Oracle                                                |
| Robert     | Coderre          | VeriSign                                              |
| Robin      | Cover            | OASIS                                                 |
| Rupert     | Wimmer           | Siemens AG                                            |
| Sanjiv     | Kalkar           | Individual                                            |
| Sean       | Barnum           | Mitre Corporation                                     |
| Stefan     | Hagen            | Individual                                            |
| Ted        | Bedwell          | Cisco Systems                                         |
| Thomas     | Schreck          | Siemens AG                                            |
| Tim        | Hudson           | Cryptsoft Pty Ltd.                                    |
| Tony       | Cox              | Cryptsoft Pty Ltd.                                    |
| Trey       | Darley           | "Kingfisher Operations, sprl"                         |
| Vincent    | Danen            | Red Hat                                               |
| Zach       | Turk             | Microsoft                                             |

-------

# Appendix B. Revision History <a id='revision-history'></a>

| Revision                 | Date       | Editor                          | Changes Made                                                                          |
|:-------------------------|:-----------|:--------------------------------|:--------------------------------------------------------------------------------------|
| csaf-v2.0-wd20210927-dev | 2021-09-27 | Stefan Hagen and Thomas Schmidt | Preparing next Editor revision for TC review and submittal as CS for public review    |
| csaf-v2.0-wd20220329-dev | 2022-03-29 | Stefan Hagen and Thomas Schmidt | Preparing next Editor revision for TC review and submittal as CSD02 for public review |
| csaf-v2.0-wd20220514-dev | 2022-05-14 | Stefan Hagen and Thomas Schmidt | Preparing next Editor revision for TC review and submittal as CS                      |
| csaf-v2.0-wd20220715-dev | 2022-07-15 | Stefan Hagen and Thomas Schmidt | Preparing next Editor revision for TC review and submittal as CS                      |
| csaf-v2.0-wd20220720-dev | 2022-07-20 | Stefan Hagen and Thomas Schmidt | Preparing next Editor revision for TC review and submittal as CS                      |

-------

# Appendix C. Guidance on the Size of CSAF Documents <a id='guidance-on-the-size-of-csaf-documents'></a>

This appendix provides informative guidance on the size of CSAF documents.

The TC carefully considered all known aspects to provide size limits for CSAF documents for this version of the specification with
the result that hard limits SHOULD NOT be enforced.
However, since there is the need for guidance to ensure interoperability in the ecosystem, the TC provides a set of soft limits.
A CSAF document which exceeds those, can still be valid but it might not be processable for some parties.

All _CSAF consumers_ SHOULD be able to process CSAF documents which comply with the limits below.
All _CSAF producers_ SHOULD NOT produce CSAF documents which exceed those limits.

> If you come across a case where these limits are exceeded, please provide feedback to the TC.

## C.1 File size <a id='file-size'></a>

A CSAF document in the specified JSON format encoded in UTF-8 SHOULD conform to known size limits of current technologies parsing JSON content,
e.g.: 15 MB.

> At least one database technology in wide use for storing CSAF documents rejects insert attempts when
> the transformed BSON size exceeds 16 megabytes.
> The BSON format optimizes for accessibility and not size.
> So, small integers and small strings may incur more overhead in the BSON format than in JSON.
> In addition, the BSON format adds length information for the entries inside the document,
> which adds to the size when storing CSAF document content in a BSON format.

## C.2 Array length <a id='array-length'></a>

An array SHOULD NOT have more than:

* 10 000 items for
  * `/document/acknowledgments`
  * `/document/acknowledgments[]/names`
  * `/document/acknowledgments[]/urls`
  * `/document/tracking/aliases`
  * `/product_tree/branches[]/product/product_identification_helper/hashes`
  * `/product_tree/branches[]/product/product_identification_helper/hashes[]/file_hashes`
  * `/product_tree/branches[]/product/product_identification_helper/sbom_urls`
  * `/product_tree/branches[]/product/product_identification_helper/x_generic_uris`
  * `/product_tree/branches[](/branches[])*/product/product_identification_helper/hashes`
  * `/product_tree/branches[](/branches[])*/product/product_identification_helper/hashes[]/file_hashes`
  * `/product_tree/branches[](/branches[])*/product/product_identification_helper/sbom_urls`
  * `/product_tree/branches[](/branches[])*/product/product_identification_helper/x_generic_uris`
  * `/product_tree/full_product_names[]/product_identification_helper/hashes`
  * `/product_tree/full_product_names[]/product_identification_helper/hashes[]/file_hashes`
  * `/product_tree/full_product_names[]/product_identification_helper/sbom_urls`
  * `/product_tree/full_product_names[]/product_identification_helper/x_generic_uris`
  * `/product_tree/relationships[]/full_product_name/product_identification_helper/hashes`
  * `/product_tree/relationships[]/full_product_name/product_identification_helper/hashes[]/file_hashes`
  * `/product_tree/relationships[]/full_product_name/product_identification_helper/sbom_urls`
  * `/product_tree/relationships[]/full_product_name/product_identification_helper/x_generic_uris`
  * `/vulnerabilities[]/acknowledgments`
  * `/vulnerabilities[]/acknowledgments[]/names`
  * `/vulnerabilities[]/acknowledgments[]/urls`
  * `/vulnerabilities[]/ids`
  * `/vulnerabilities[]/remediations[]/entitlements`

* 40 000 items for
  * `/document/notes`
  * `/document/references`
  * `/vulnerabilities[]/involvements`
  * `/vulnerabilities[]/notes`
  * `/vulnerabilities[]/references`

* 100 000 for
  * `/document/tracking/revision_history`
  * `/product_tree/branches`
  * `/product_tree(/branches[])*/branches`
  * `/product_tree/branches[]/product/product_identification_helper/model_numbers`
  * `/product_tree/branches[]/product/product_identification_helper/serial_numbers`
  * `/product_tree/branches[]/product/product_identification_helper/skus`
  * `/product_tree/branches[](/branches[])*/product/product_identification_helper/model_numbers`
  * `/product_tree/branches[](/branches[])*/product/product_identification_helper/serial_numbers`
  * `/product_tree/branches[](/branches[])*/product/product_identification_helper/skus`
  * `/product_tree/full_product_names`
  * `/product_tree/full_product_names[]/product_identification_helper/model_numbers`
  * `/product_tree/full_product_names[]/product_identification_helper/serial_numbers`
  * `/product_tree/full_product_names[]/product_identification_helper/skus`
  * `/product_tree/product_groups[]/product_ids`
  * `/product_tree/relationships[]/full_product_name/product_identification_helper/model_numbers`
  * `/product_tree/relationships[]/full_product_name/product_identification_helper/serial_numbers`
  * `/product_tree/relationships[]/full_product_name/product_identification_helper/skus`
  * `/vulnerabilities`

* 10 000 000 for
  * `/product_tree/relationships`
  * `/product_tree/product_groups`
  * `/vulnerabilities[]/remediations[]/group_ids`

* 100 000 000 for
  * `/vulnerabilities[]/flags`
  * `/vulnerabilities[]/flags[]/group_ids`
  * `/vulnerabilities[]/flags[]/product_ids`
  * `/vulnerabilities[]/product_status/first_affected`
  * `/vulnerabilities[]/product_status/first_fixed`
  * `/vulnerabilities[]/product_status/fixed`
  * `/vulnerabilities[]/product_status/known_affected`
  * `/vulnerabilities[]/product_status/known_not_affected`
  * `/vulnerabilities[]/product_status/last_affected`
  * `/vulnerabilities[]/product_status/recommended`
  * `/vulnerabilities[]/product_status/under_investigation`
  * `/vulnerabilities[]/remediations`
  * `/vulnerabilities[]/remediations[]/product_ids`
  * `/vulnerabilities[]/scores`
  * `/vulnerabilities[]/scores[]/products`
  * `/vulnerabilities[]/threats`
  * `/vulnerabilities[]/threats[]/group_ids`
  * `/vulnerabilities[]/threats[]/product_ids`

## C.3 String length <a id='string-length'></a>

A string SHOULD NOT have a length greater than:

* 1000 for
  * `/document/acknowledgments[]/names[]`
  * `/document/acknowledgments[]/organization`
  * `/document/aggregate_severity/text`
  * `/document/category`
  * `/document/lang`
  * `/document/notes[]/audience`
  * `/document/notes[]/title`
  * `/document/publisher/name`
  * `/document/source_lang`
  * `/document/title`
  * `/document/tracking/aliases[]`
  * `/document/tracking/generator/engine/name`
  * `/document/tracking/generator/engine/version`
  * `/document/tracking/id`
  * `/document/tracking/revision_history[]/legacy_version`
  * `/document/tracking/revision_history[]/number`
  * `/document/tracking/version`
  * `/product_tree/branches[]/name`
  * `/product_tree/branches[]/product/name`
  * `/product_tree/branches[]/product/product_id`
  * `/product_tree/branches[]/product/product_identification_helper/hashes[]/file_hashes[]/algorithm`
  * `/product_tree/branches[]/product/product_identification_helper/hashes[]/file_hashes[]/value`
  * `/product_tree/branches[]/product/product_identification_helper/hashes[]/filename`
  * `/product_tree/branches[]/product/product_identification_helper/model_numbers[]`
  * `/product_tree/branches[]/product/product_identification_helper/serial_numbers[]`
  * `/product_tree/branches[]/product/product_identification_helper/skus[]`
  * `/product_tree/branches[](/branches[])*/name`
  * `/product_tree/branches[](/branches[])*/product/name`
  * `/product_tree/branches[](/branches[])*/product/product_id`
  * `/product_tree/branches[](/branches[])*/product/product_identification_helper/hashes[]/file_hashes[]/algorithm`
  * `/product_tree/branches[](/branches[])*/product/product_identification_helper/hashes[]/file_hashes[]/value`
  * `/product_tree/branches[](/branches[])*/product/product_identification_helper/hashes[]/filename`
  * `/product_tree/branches[](/branches[])*/product/product_identification_helper/model_numbers[]`
  * `/product_tree/branches[](/branches[])*/product/product_identification_helper/serial_numbers[]`
  * `/product_tree/branches[](/branches[])*/product/product_identification_helper/skus[]`
  * `/product_tree/full_product_names[]/name`
  * `/product_tree/full_product_names[]/product_id`
  * `/product_tree/full_product_names[]/product_identification_helper/hashes[]/file_hashes[]/algorithm`
  * `/product_tree/full_product_names[]/product_identification_helper/hashes[]/file_hashes[]/value`
  * `/product_tree/full_product_names[]/product_identification_helper/hashes[]/filename`
  * `/product_tree/full_product_names[]/product_identification_helper/model_numbers[]`
  * `/product_tree/full_product_names[]/product_identification_helper/serial_numbers[]`
  * `/product_tree/full_product_names[]/product_identification_helper/skus[]`
  * `/product_tree/product_groups[]/group_id`
  * `/product_tree/product_groups[]/product_ids[]`
  * `/product_tree/relationships[]/full_product_name/name`
  * `/product_tree/relationships[]/full_product_name/product_id`
  * `/product_tree/relationships[]/full_product_name/product_identification_helper/hashes[]/file_hashes[]/algorithm`
  * `/product_tree/relationships[]/full_product_name/product_identification_helper/hashes[]/file_hashes[]/value`
  * `/product_tree/relationships[]/full_product_name/product_identification_helper/hashes[]/filename`
  * `/product_tree/relationships[]/full_product_name/product_identification_helper/model_numbers[]`
  * `/product_tree/relationships[]/full_product_name/product_identification_helper/serial_numbers[]`
  * `/product_tree/relationships[]/full_product_name/product_identification_helper/skus[]`
  * `/product_tree/relationships[]/product_reference`
  * `/product_tree/relationships[]/relates_to_product_reference`
  * `/vulnerabilities[]/acknowledgments[]/names[]`
  * `/vulnerabilities[]/acknowledgments[]/organization`
  * `/vulnerabilities[]/cve`
  * `/vulnerabilities[]/cwe/id`
  * `/vulnerabilities[]/cwe/name`
  * `/vulnerabilities[]/flags[]/group_ids[]`
  * `/vulnerabilities[]/flags[]/product_ids[]`
  * `/vulnerabilities[]/ids[]/system_name`
  * `/vulnerabilities[]/ids[]/text`
  * `/vulnerabilities[]/notes[]/audience`
  * `/vulnerabilities[]/notes[]/title`
  * `/vulnerabilities[]/product_status/first_affected[]`
  * `/vulnerabilities[]/product_status/first_fixed[]`
  * `/vulnerabilities[]/product_status/fixed[]`
  * `/vulnerabilities[]/product_status/known_affected[]`
  * `/vulnerabilities[]/product_status/known_not_affected[]`
  * `/vulnerabilities[]/product_status/last_affected[]`
  * `/vulnerabilities[]/product_status/recommended[]`
  * `/vulnerabilities[]/product_status/under_investigation[]`
  * `/vulnerabilities[]/remediations[]/group_ids[]`
  * `/vulnerabilities[]/remediations[]/product_ids[]`
  * `/vulnerabilities[]/scores[]/cvss_v2/vectorString`
  * `/vulnerabilities[]/scores[]/cvss_v3/vectorString`
  * `/vulnerabilities[]/scores[]/products[]`
  * `/vulnerabilities[]/threats[]/group_ids[]`
  * `/vulnerabilities[]/threats[]/product_ids[]`
  * `/vulnerabilities[]/title`

* 10 000 for
  * `/document/acknowledgments[]/summary`
  * `/document/distribution/text`
  * `/document/publisher/contact_details`
  * `/document/publisher/issuing_authority`
  * `/document/references[]/summary`
  * `/document/tracking/revision_history[]/summary`
  * `/product_tree/branches[]/product/product_identification_helper/cpe`
  * `/product_tree/branches[]/product/product_identification_helper/purl`
  * `/product_tree/branches[](/branches[])*/product/product_identification_helper/cpe`
  * `/product_tree/branches[](/branches[])*/product/product_identification_helper/purl`
  * `/product_tree/full_product_names[]/product_identification_helper/cpe`
  * `/product_tree/full_product_names[]/product_identification_helper/purl`
  * `/product_tree/product_groups[]/summary`
  * `/product_tree/relationships[]/full_product_name/product_identification_helper/cpe`
  * `/product_tree/relationships[]/full_product_name/product_identification_helper/purl`
  * `/vulnerabilities[]/acknowledgments[]/summary`
  * `/vulnerabilities[]/involvements[]/summary`
  * `/vulnerabilities[]/references[]/summary`
  * `/vulnerabilities[]/remediations[]/entitlements[]`

* 30 000 for
  * `/document/notes[]/text`
  * `/vulnerabilities[]/notes[]/text`

* 250 000 for
  * `/vulnerabilities[]/remediations[]/details`
  * `/vulnerabilities[]/remediations[]/restart_required/details`
  * `/vulnerabilities[]/threats[]/details`

## C.4 URI length <a id='uri-length'></a>

A string with format `uri` SHOULD NOT have a length greater than 20000. This applies to:

* `/document/acknowledgments[]/urls[]`
* `/document/aggregate_severity/namespace`
* `/document/distribution/tlp/url`
* `/document/references[]/url`
* `/document/publisher/namespace`
* `/product_tree/branches[]/product/product_identification_helper/sbom_urls[]`
* `/product_tree/branches[]/product/product_identification_helper/x_generic_uris[]/namespace`
* `/product_tree/branches[]/product/product_identification_helper/x_generic_uris[]/uri`
* `/product_tree/branches[](/branches[])*/product/product_identification_helper/sbom_urls[]`
* `/product_tree/branches[](/branches[])*/product/product_identification_helper/x_generic_uris[]/namespace`
* `/product_tree/branches[](/branches[])*/product/product_identification_helper/x_generic_uris[]/uri`
* `/product_tree/full_product_names[]/product_identification_helper/sbom_urls[]`
* `/product_tree/full_product_names[]/product_identification_helper/x_generic_uris[]/namespace`
* `/product_tree/full_product_names[]/product_identification_helper/x_generic_uris[]/uri`
* `/product_tree/relationships[]/full_product_name/product_identification_helper/sbom_urls[]`
* `/product_tree/relationships[]/full_product_name/product_identification_helper/x_generic_uris[]/namespace`
* `/product_tree/relationships[]/full_product_name/product_identification_helper/x_generic_uris[]/uri`
* `/vulnerabilities[]/acknowledgments[]/urls[]`
* `/vulnerabilities[]/references[]/url`
* `/vulnerabilities[]/remediations[]/url`

## C.5 Enum <a id='enum'></a>

A string which is an enum has a fixed maximum length given by its longest value.

> Later versions of CSAF might add, modify or delete possible value which could change the longest value.
> Therefore, this sizes should not be implemented as fixed limits if forward compatibility is desired.

It seems to be safe to assume that the length of each value is not greater than 50. This applies to:

* `/document/csaf_version` (3)
* `/document/distribution/tlp/label` (5)
* `/document/notes[]/category` (16)
* `/document/publisher/category` (11)
* `/document/references[]/category` (8)
* `/document/tracking/status` (7)
* `/product_tree/branches[]/category` (15)
* `/product_tree/branches[](/branches[])*/category` (15)
* `/product_tree/relationships[]/category` (21)
* `/vulnerabilities[]/flags[]/label` (49)
* `/vulnerabilities[]/involvements[]/party` (11)
* `/vulnerabilities[]/involvements[]/status` (17)
* `/vulnerabilities[]/notes[]/category` (16)
* `/vulnerabilities[]/references[]/category` (8)
* `/vulnerabilities[]/remediations[]/category` (14)
* `/vulnerabilities[]/remediations[]/restart_required/category` (20)
* `/vulnerabilities[]/scores[]/cvss_v2/version` (3)
* `/vulnerabilities[]/scores[]/cvss_v2/accessVector` (16)
* `/vulnerabilities[]/scores[]/cvss_v2/accessComplexity` (6)
* `/vulnerabilities[]/scores[]/cvss_v2/authentication` (8)
* `/vulnerabilities[]/scores[]/cvss_v2/confidentialityImpact` (8)
* `/vulnerabilities[]/scores[]/cvss_v2/integrityImpact` (8)
* `/vulnerabilities[]/scores[]/cvss_v2/availabilityImpact` (8)
* `/vulnerabilities[]/scores[]/cvss_v2/exploitability` (16)
* `/vulnerabilities[]/scores[]/cvss_v2/remediationLevel` (13)
* `/vulnerabilities[]/scores[]/cvss_v2/reportConfidence` (14)
* `/vulnerabilities[]/scores[]/cvss_v2/collateralDamagePotential` (11)
* `/vulnerabilities[]/scores[]/cvss_v2/targetDistribution` (11)
* `/vulnerabilities[]/scores[]/cvss_v2/confidentialityRequirement` (11)
* `/vulnerabilities[]/scores[]/cvss_v2/integrityRequirement` (11)
* `/vulnerabilities[]/scores[]/cvss_v2/availabilityRequirement` (11)
* `/vulnerabilities[]/scores[]/cvss_v3/version` (3)
* `/vulnerabilities[]/scores[]/cvss_v3/attackVector` (16)
* `/vulnerabilities[]/scores[]/cvss_v3/attackComplexity` (4)
* `/vulnerabilities[]/scores[]/cvss_v3/privilegesRequired` (4)
* `/vulnerabilities[]/scores[]/cvss_v3/userInteraction` (8)
* `/vulnerabilities[]/scores[]/cvss_v3/scope` (9)
* `/vulnerabilities[]/scores[]/cvss_v3/confidentialityImpact` (4)
* `/vulnerabilities[]/scores[]/cvss_v3/integrityImpact` (4)
* `/vulnerabilities[]/scores[]/cvss_v3/availabilityImpact` (4)
* `/vulnerabilities[]/scores[]/cvss_v3/baseSeverity` (8)
* `/vulnerabilities[]/scores[]/cvss_v3/exploitCodeMaturity` (16)
* `/vulnerabilities[]/scores[]/cvss_v3/remediationLevel` (13)
* `/vulnerabilities[]/scores[]/cvss_v3/reportConfidence` (11)
* `/vulnerabilities[]/scores[]/cvss_v3/temporalSeverity` (8)
* `/vulnerabilities[]/scores[]/cvss_v3/confidentialityRequirement` (11)
* `/vulnerabilities[]/scores[]/cvss_v3/integrityRequirement` (11)
* `/vulnerabilities[]/scores[]/cvss_v3/availabilityRequirement` (11)
* `/vulnerabilities[]/scores[]/cvss_v3/modifiedAttackVector` (16)
* `/vulnerabilities[]/scores[]/cvss_v3/modifiedAttackComplexity` (11)
* `/vulnerabilities[]/scores[]/cvss_v3/modifiedPrivilegesRequired` (11)
* `/vulnerabilities[]/scores[]/cvss_v3/modifiedUserInteraction` (11)
* `/vulnerabilities[]/scores[]/cvss_v3/modifiedScope` (11)
* `/vulnerabilities[]/scores[]/cvss_v3/modifiedConfidentialityImpact` (11)
* `/vulnerabilities[]/scores[]/cvss_v3/modifiedIntegrityImpact` (11)
* `/vulnerabilities[]/scores[]/cvss_v3/modifiedAvailabilityImpact` (11)
* `/vulnerabilities[]/scores[]/cvss_v3/environmentalSeverity` (8)
* `/vulnerabilities[]/threats[]/category` (14)

## C.6 Date <a id='date'></a>

The maximum length of strings representing a temporal value is given by the format specifier. This applies to:

* `/document/tracking/current_release_date`
* `/document/tracking/generator/date`
* `/document/tracking/initial_release_date`
* `/document/tracking/revision_history[]/date`
* `/vulnerabilities[]/discovery_date`
* `/vulnerabilities[]/flags[]/date`
* `/vulnerabilities[]/release_date`
* `/vulnerabilities[]/involvements[]/date`
* `/vulnerabilities[]/remediations[]/date`
* `/vulnerabilities[]/threats[]/date`
