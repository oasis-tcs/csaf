<link rel="stylesheet" href="https://docs.oasis-open.org/templates/css/markdown-styles-v1.7.3a.css" />

![OASIS Logo](https://docs.oasis-open.org/templates/OASISLogo-v3.0.png)

-------

# Common Security Advisory Framework Version 2.0 Errata 01

## Committee Specification Draft 01

## 06 December 2023

#### This stage:
https://docs.oasis-open.org/csaf/csaf/v2.0/errata01/csd01/csaf-v2.0-errata01-csd01.md (Authoritative) \
https://docs.oasis-open.org/csaf/csaf/v2.0/errata01/csd01/csaf-v2.0-errata01-csd01.html \
https://docs.oasis-open.org/csaf/csaf/v2.0/errata01/csd01/csaf-v2.0-errata01-csd01.pdf

#### Previous stage:
N/A

#### Latest stage:
https://docs.oasis-open.org/csaf/csaf/v2.0/errata01/csaf-v2.0-errata01.md (Authoritative) \
https://docs.oasis-open.org/csaf/csaf/v2.0/errata01/csaf-v2.0-errata01.html \
https://docs.oasis-open.org/csaf/csaf/v2.0/errata01/csaf-v2.0-errata01.pdf

#### Technical Committee:
[OASIS Common Security Advisory Framework (CSAF) TC](https://www.oasis-open.org/committees/csaf/)

#### Chair:
Omar Santos (osantos@cisco.com), [Cisco Systems](https://cisco.com/)

#### Editors:
Langley Rock (lrock@redhat.com), [Red Hat](https://redhat.com/) \
Stefan Hagen (stefan@hagen.link), [Individual](https://stefan-hagen.website/) \
Thomas Schmidt (thomas.schmidt@bsi.bund.de), [Federal Office for Information Security (BSI) Germany](https://www.bsi.bund.de/)

#### Additional artifacts:
This document is one component of a Work Product that also includes:

* Aggregator JSON schema: https://docs.oasis-open.org/csaf/csaf/v2.0/errata01/csd01/schemas/aggregator_json_schema.json.
* CSAF JSON schema: https://docs.oasis-open.org/csaf/csaf/v2.0/errata01/csd01/schemas/csaf_json_schema.json.
* Provider JSON schema: https://docs.oasis-open.org/csaf/csaf/v2.0/errata01/csd01/schemas/provider_json_schema.json.

#### Declared JSON namespaces:

* [https://docs.oasis-open.org/csaf/csaf/v2.0/aggregator_json_schema.json](https://docs.oasis-open.org/csaf/csaf/v2.0/aggregator_json_schema.json)
* [https://docs.oasis-open.org/csaf/csaf/v2.0/csaf_json_schema.json](https://docs.oasis-open.org/csaf/csaf/v2.0/csaf_json_schema.json)
* [https://docs.oasis-open.org/csaf/csaf/v2.0/provider_json_schema.json](https://docs.oasis-open.org/csaf/csaf/v2.0/provider_json_schema.json)

#### Abstract:
This document provides Errata for the OASIS Standard _Common Security Advisory Framework Version 2.0_.
There are no changes to the published CSAF document. Changes have been made only to the included Aggregator JSON schema: https://docs.oasis-open.org/csaf/csaf/v2.0/errata01/csd01/schemas/aggregator_json_schema.json. No changes have been made to the other two included JSON schemas.

#### Status:
This document was last revised or approved by the OASIS Common Security Advisory Framework (CSAF) TC on the above date. The level of approval is also listed above. Check the "Latest stage" location noted above for possible later revisions of this document. Any other numbered Versions and other technical work produced by the Technical Committee (TC) are listed at https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=csaf#technical.

TC members should send comments on this specification to the TC's email list. Others should send comments to the TC's public comment list, after subscribing to it by following the instructions at the "Send A Comment" button on the TC's web page at https://www.oasis-open.org/committees/csaf/.

This specification is provided under the [Non-Assertion](https://www.oasis-open.org/policies-guidelines/ipr/#Non-Assertion-Mode) Mode of the [OASIS IPR Policy](https://www.oasis-open.org/policies-guidelines/ipr/), the mode chosen when the Technical Committee was established. For information on whether any patents have been disclosed that may be essential to implementing this specification, and any offers of patent licensing terms, please refer to the Intellectual Property Rights section of the TC's web page (https://www.oasis-open.org/committees/csaf/ipr.php).

Note that any machine-readable content ([Computer Language Definitions](https://www.oasis-open.org/policies-guidelines/tc-process-2017-05-26/#wpComponentsCompLang)) declared Normative for this Work Product is provided in separate plain text files. In the event of a discrepancy between any such plain text file and display content in the Work Product's prose narrative document(s), the content in the separate plain text file prevails.

#### Citation format:
When referencing this specification the following citation format should be used:

**[csaf-v2.0-errata01]**

_Common Security Advisory Framework Version 2.0 Errata 01_. Edited by Langley Rock, Stefan Hagen, and Thomas Schmidt. 06 December 2023. OASIS Committee Specification Draft 01. https://docs.oasis-open.org/csaf/csaf/v2.0/errata01/csd01/csaf-v2.0-errata01-csd01.html. Latest stage: https://docs.oasis-open.org/csaf/csaf/v2.0/errata01/csaf-v2.0-errata01.html.

#### Notices
Copyright &copy; OASIS Open 2023. All Rights Reserved.

Distributed under the terms of the OASIS [IPR Policy](https://www.oasis-open.org/policies-guidelines/ipr/).

The name "OASIS" is a trademark of [OASIS](https://www.oasis-open.org/), the owner and developer of this specification, and should be used only to refer to the organization and its official outputs.

For complete copyright information please see the full Notices section in Appendix C below.


-------

# Table of Contents

[[TOC will be inserted here]]

-------

# 1 Introduction

This document lists the draft changes to the OASIS Standard _Common Security Advisory Framework Version 2.0_, consisting of the following components:
* _Common Security Advisory Framework Version 2.0_ (prose document)
* Aggregator JSON schema
* CSAF JSON schema
* Provider JSON schema

There are no changes to the published CSAF document. Changes have been made only to the included Aggregator JSON schema. No changes have been made to the other two included JSON schemas.

## 1.1 Description of changes

In the aggregator schema, a typo has been corrected that blocked creation of any valid JSON aggregator document instance.

In line 178 of the `aggregator_json_schema.json`, the entry `mirror` as `required` field has been corrected to be `mirrors` to match the existing property definition in line 187 of the same schema file. There is no field `mirror`.

## 1.2 Scope of changes

The only draft change is to the Aggregator JSON schema file, "aggregator_json_schema.json".
The corrected file is linked in the section [Additional artifacts](#additional-artifacts) on the title page.

-------

# 2 Conformance

The conformance requirements stated in the OASIS Standard _Common Security Advisory Framework Version 2.0_ [[csaf-v2.0-os](#csaf-v20-os)] are not changed in any way by the publication of this Errata document.

-------

# Appendix A. Normative References

The following documents are referenced in such a way that some or all of their content constitutes requirements of this document.

###### [csaf-v2.0-os]

_Common Security Advisory Framework Version 2.0_. Edited by Langley Rock, Stefan Hagen, and Thomas Schmidt. 18 November 2022. OASIS Standard. https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html. This specification includes the following components:
* Aggregator JSON schema: https://docs.oasis-open.org/csaf/csaf/v2.0/os/schemas/aggregator_json_schema.json.
* CSAF JSON schema: https://docs.oasis-open.org/csaf/csaf/v2.0/os/schemas/csaf_json_schema.json.
* Provider JSON schema: https://docs.oasis-open.org/csaf/csaf/v2.0/os/schemas/provider_json_schema.json.

-------

# Appendix B. Acknowledgments

The following individuals were members of the OASIS CSAF Technical Committee during the creation of this specification and their contributions are gratefully acknowledged:

**CSAF TC Members:**

| First Name | Last Name | Company |
| :--- | :--- | :--- |
|Alexandre | Dulaunoy | CIRCL|
|Anthony | Berglas | Cryptsoft Pty Ltd.|
|Art | Manion | Carnegie Mellon University|
|Aukjan | van Belkum | EclecticIQ|
|Ben | Sooter | Electric Power Research Institute (EPRI)|
|Bernd | Grobauer | Siemens AG|
|Bruce | Rich | Cryptsoft Pty Ltd.|
|Chok | Poh | Oracle|
|Dan | West | Microsoft|
|David | Waltermire | NIST|
|Denny | Page | TIBCO Software Inc.|
|Duncan | Sparrell | sFractal Consulting LLC|
|Eric | Johnson | TIBCO Software Inc.|
|Ethan | Rahn | Arista Networks|
|Feng | Cao | Oracle|
|Greg | Scott | Cryptsoft Pty Ltd.|
|Harold | Booth | NIST|
|Jason | Masters | TELUS|
|Jennifer | Victor | Dell|
|Jessica | Fitzgerald-McKay | National Security Agency|
|Jonathan | Bitle | Kaiser Permanente|
|Justin | Corlett | Cryptsoft Pty Ltd.|
|Kazuo | Noguchi | Hitachi, Ltd.|
|Kent | Landfield | McAfee|
|Langley | Rock | Red Hat|
|Martin | Prpic | Red Hat|
|Masato | Terada | Hitachi, Ltd.|
|Mike | Gorski | Cisco Systems|
|Nicole | Parrish | Mitre Corporation|
|Omar | Santos | Cisco Systems|
|Patrick | Maroney | AT&T|
|Rhonda | Levy | Cisco Systems|
|Richard | Struse | Mitre Corporation|
|Ritwik | Ghoshal | Oracle|
|Robert | Coderre | Accenture|
|Robert | Keith | Accenture|
|Stefan | Hagen | Individual|
|Tania | Ward | Dell|
|Ted | Bedwell | Cisco Systems|
|Thomas | Proell | Siemens AG|
|Thomas | Schmidt | Federal Office for Information Security (BSI) Germany|
|Tim | Hudson | Cryptsoft Pty Ltd.|
|Tobias | Limmer | Siemens AG|
|Tony | Cox | Cryptsoft Pty Ltd.|
|Vincent | Danen | Red Hat|
|Will | Rideout | Arista Networks|
|Xiaoyu | Ge | Huawei Technologies Co., Ltd.|

-------

# Appendix C. Notices

Copyright © OASIS Open 2023. All Rights Reserved.

All capitalized terms in the following text have the meanings assigned to them in the OASIS Intellectual Property Rights Policy (the "OASIS IPR Policy"). The full [Policy](https://www.oasis-open.org/policies-guidelines/ipr/) may be found at the OASIS website.

This document and translations of it may be copied and furnished to others, and derivative works that comment on or otherwise explain it or assist in its implementation may be prepared, copied, published, and distributed, in whole or in part, without restriction of any kind, provided that the above copyright notice and this section are included on all such copies and derivative works. However, this document itself may not be modified in any way, including by removing the copyright notice or references to OASIS, except as needed for the purpose of developing any document or deliverable produced by an OASIS Technical Committee (in which case the rules applicable to copyrights, as set forth in the OASIS IPR Policy, must be followed) or as required to translate it into languages other than English.

The limited permissions granted above are perpetual and will not be revoked by OASIS or its successors or assigns.

This document and the information contained herein is provided on an "AS IS" basis and OASIS DISCLAIMS ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO ANY WARRANTY THAT THE USE OF THE INFORMATION HEREIN WILL NOT INFRINGE ANY OWNERSHIP RIGHTS OR ANY IMPLIED WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.

As stated in the OASIS IPR Policy, the following three paragraphs in brackets apply to OASIS Standards Final Deliverable documents (Committee Specification, Candidate OASIS Standard, OASIS Standard, or Approved Errata).

[OASIS requests that any OASIS Party or any other party that believes it has patent claims that would necessarily be infringed by implementations of this OASIS Standards Final Deliverable, to notify OASIS TC Administrator and provide an indication of its willingness to grant patent licenses to such patent claims in a manner consistent with the IPR Mode of the OASIS Technical Committee that produced this deliverable.]

[OASIS invites any party to contact the OASIS TC Administrator if it is aware of a claim of ownership of any patent claims that would necessarily be infringed by implementations of this OASIS Standards Final Deliverable by a patent holder that is not willing to provide a license to such patent claims in a manner consistent with the IPR Mode of the OASIS Technical Committee that produced this OASIS Standards Final Deliverable. OASIS may include such claims on its website, but disclaims any obligation to do so.]

[OASIS takes no position regarding the validity or scope of any intellectual property or other rights that might be claimed to pertain to the implementation or use of the technology described in this OASIS Standards Final Deliverable or the extent to which any license under such rights might or might not be available; neither does it represent that it has made any effort to identify any such rights. Information on OASIS' procedures with respect to rights in any document or deliverable produced by an OASIS Technical Committee can be found on the OASIS website. Copies of claims of rights made available for publication and any assurances of licenses to be made available, or the result of an attempt made to obtain a general license or permission for the use of such proprietary rights by implementers or users of this OASIS Standards Final Deliverable, can be obtained from the OASIS TC Administrator. OASIS makes no representation that any information or list of intellectual property rights will at any time be complete, or that any claims in such list are, in fact, Essential Claims.]

The name "OASIS" is a trademark of [OASIS](https://www.oasis-open.org/), the owner and developer of this specification, and should be used only to refer to the organization and its official outputs. OASIS welcomes reference to, and implementation and use of, specifications, while reserving the right to enforce its marks against misleading uses. Please see https://www.oasis-open.org/policies-guidelines/trademark/ for above guidance.

