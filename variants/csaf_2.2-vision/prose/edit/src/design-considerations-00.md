# Design Considerations

The Common Security Advisory Framework (CSAF) is a language to exchange Security Advisories formulated in JSON.

The term Security Advisory as used in this document describes any notification of security issues in products of and by providers.
Anyone providing a product is considered in this document as a vendor, i.e. developers or maintainers of information system products or services.
This includes all authoritative product vendors, Product Security Incident Response Teams (PSIRTs), and product resellers and distributors,
including authoritative vendor partners.
A security issue is not necessarily constrained to a problem statement, the focus of the term is on the security aspect impacting
(or not impacting) specific product-platform-version combinations.
Information on presence or absence of workarounds is also considered part of the security issue.
This document is the definitive reference for the language elements of CSAF version 2.1.
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
