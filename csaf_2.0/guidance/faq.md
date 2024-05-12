# FAQ

This document provides answers regarding frequently asked questions about CSAF 2.0. The TC will update the list if necessary. Questions can be suggested via [GitHub issues](https://github.com/oasis-tcs/csaf/issues) or via email on the [TC's comment mailing list](https://lists.oasis-open.org/archives/csaf-comment/).

## General

### What is the Common Security Advisory Framework (CSAF)?

The Common Security Advisory Framework (CSAF) is the definitive reference for the language which supports creation, update, and interoperable exchange of security advisories as structured information on products, vulnerabilities and the status of impact and remediation among interested parties. You can [access the CSAF 2.0 standard here](https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html).

### What problems are addressed by CSAF?

CSAF enables individuals and organizations to successfully disclose and consume security advisories in machine readable format. It also specifies the distribution and discovery of CSAF documents.

## Relation to other standard and specifications

### Is CSAF a replacement for CVE?

**No.** CSAF is not a replacement for CVE. A CSAF document may include one or many security vulnerabilities that have been assigned a CVE. Not all vulnerabilities are assigned a CVE. CSAF also allows for any organization to be able to disclose or consume security vulnerabilities or responses that do not have an assigned CVE.

### Is CSAF the replacement for CVRF?

Yes. CSAF is the replacement for the [Common Vulnerability Reporting Framework (CVRF)](https://docs.oasis-open.org/csaf/csaf-cvrf/v1.2/csaf-cvrf-v1.2.html). It enhances the capabilities of CVRF including different profiles (e.g., CSAF Base, Informational Advisory, Incident Response, VEX, etc.). Each profile extends the base profile "CSAF Base" - directly or indirect through another profile from the standard - by making additional fields from the standard mandatory. A profile can always add, but never subtract nor overwrite requirements defined in the profile it extends. CSAF also provides several additional enhancements that were not supported in CVRF. In addition, CSAF uses JSON while CVRF used XML.

### What is VEX and how is it supported in CSAF?

The Vulnerability Exploitability eXchange (VEX) allows a software supplier or other parties to assert the status of specific vulnerabilities in a particular product. CSAF supports VEX to allow suppliers and other parties to provide the status of the vulnerabilities that may affect a product. As stated in [CISA's VEX Use Case documentation](https://www.cisa.gov/sites/default/files/publications/VEX_Use_Cases_Aprill2022.pdf), VEX is a form of a security advisory, similar to those already issued by mature product security teams today. There are a few important improvements for the VEX model over ‘traditional’ security advisories. First, VEX documents are machine readable, built to support integration into existing and novel security management tools, as well as broader vulnerability tracking platforms. Second, VEX data can support more effective use of [Software Bills of Materials (SBOM)](https://www.cisa.gov/sbom) data.

### Why is CSAF 2.0 still using TLP v1?

When the CSAF Committee Specification, which was later promoted to OASIS standard, was published the new [TLP v2](https://www.first.org/tlp/) was not available. Therefore, CSAF 2.0 only supports [TLP v1](https://www.first.org/tlp/v1/). Nevertheless, as TLP v2 is backwards compatible the following mapping table can be used to display the new TLP v2 terms in a human-readable advisory:

| TLP v2 | TLP v1 |
|--------|--------|
| `TLP:CLEAR` | `TLP:WHITE` |
| `TLP:GREEN` | `TLP:GREEN` |
| `TLP:AMBER` | `TLP:AMBER` |
| `TLP:AMBER+STRICT` | *not present* |
| `TLP:RED` | `TLP:RED` |

*Note:* There is no equivalent for the TLP v2 `TLP:AMBER+STRICT` in TLP v1. For situations, where the label `TLP:AMBER+STRICT` would be needed it is recommended to use the label `TLP:RED` in CSAF and explain the laxer requirement through `/document/distribution/text`.

Starting with version CSAF 2.1, [CSAF will support TLP v2](https://github.com/oasis-tcs/csaf/issues/591).

## CSAF Distribution

### How can my organization be added to a CSAF lister or CSAF aggregator?

CSAF lister and CSAF aggregator choose on their own which producing parties they add to their lists. Please reach out to the CSAF lister or CSAF aggregator in question. Their contact details are available in the metadata of the list.

### How long should signatures of CSAF documents be valid?

At all times, signatures MUST remain valid for a minimum of 30 days and ideally for at least 90 days. When executing CSAF document signatures, the signing party SHOULD adhere to or surpass the prevailing best practices and recommendations regarding key length.
Tools SHOULD treat the violation of the rules given in the first sentence as:

* warning if the signature is only valid for 90 days or less at the time of the verification,
* error, which MAY be ignored by the user per option, if the signature is only valid for 30 days or less at the time of the verification and
* error if the signature is expired at the time of the verification.

### I want to use a Content Delivery Network (CDN) to distribute CSAF files. What do I need to consider?

Please see our advise on [CDNs](./cdn.md).

### Where can I find a list of all parties that produce CSAF?

Currently, there is no such list available. However, [BSI hosts a list with metadata of known parties](https://wid.cert-bund.de/.well-known/csaf-aggregator/aggregator.json) that produce CSAF files and distribute them in a way that they are automatically retrievable. This list is called a CSAF lister.
