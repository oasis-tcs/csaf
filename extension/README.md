# Governance of CSAF Extensions for CSAF

## Overview

The Common Security Advisory Framework (CSAF) standard provides a broad schema for security advisories. However, no single standard can address every use case or anticipate every emerging requirement. CSAF Extensions let the community extend the core specification in controlled, governed ways while preserving interoperability and data quality.

Extensions allow implementers to add domain-specific or organization-specific data fields to CSAF documents. The mechanism is deliberately flexible yet disciplined: extensions are expected to remain focused, well-documented, and aligned with the core principles of CSAF, so that adding data in one place does not undermine the predictability of the format elsewhere. To prevent issuing parties from inventing new attributes at will, which would defeat the purpose of a single standardized format, the safeguards described in this document apply to every extension.

The OASIS Open CSAF Technical Committee (hereafter: TC) oversees and governs the CSAF Extensions.

## Conventions

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 [[RFC 2119](https://www.rfc-editor.org/rfc/rfc2119)] [[RFC 8174](https://www.rfc-editor.org/rfc/rfc8174)] when, and only when, they appear in all capitals, as shown here.

## Extension Classes

CSAF defines three classes of extensions. They differ in how widely they are shared, whether they are reviewed, and where they are hosted:

| Class | Registration / review | Listed in registry | Hosting | Typical use |
| --- | --- | --- | --- | --- | 
| Official | Registered, plus additional testing and TC review | Yes | `extensions.csaf.dev` | Mature, validated extensions RECOMMENDED for broad adoption |
| Registered | Reviewed and approved by the OASIS CSAF Technical Committee | Yes | Publicly accessible at location of implementer's choice | Extensions with demonstrated community need, available for any implementer to use |
| Private | None required | No | Implementer's choice | Internal and experimental use within a single organization or closed community; not intended for production |

**Official extensions** are the subset of extensions registered that have reached the highest level of maturity and validation. They are hosted at `extensions.csaf.dev`, undergo additional implementation testing and TC review, and are RECOMMENDED for broad adoption. Official extensions classified as critical additionally require the second vote described under [Review and Approval](#review-and-approval)..

**Registered extensions** are reviewed and approved by the OASIS CSAF Technical Committee (TC) and then listed publicly in the CSAF Extension Registry. They MUST meet all governance requirements described below, are available for any implementer to use, and are expected to demonstrate genuine community need alongside a baseline of quality. Registered extensions classified as critical additionally require the second vote described under [Review and Approval](#review-and-approval)..

**Private extensions** are used within a single organization or closed community. They require no registration or review and are not discoverable through the CSAF registry. They are intended for internal and experimental use rather than production; documents meant for production or for exchange beyond a closed community SHOULD rely on CSAF Core or on registered and official extensions.

## Versioning and Schema

Every extension MUST be versioned and MUST publish a schema that consumers can use to validate documents that employ the extension. The schema MUST be publicly available for registered and official extensions. Authors MUST version their extensions using semantic versioning and MUST document the changes between versions; a major-version increment signals a breaking change to the extension's schema or semantics.

## Processing Model: Critical and Non-Critical Extensions

Because a consuming tool cannot be expected to understand every extension, each extension is either critical or non-critical, and tools handle the two differently.

An extension MUST be marked as critical when using it would cause any mandatory CSAF test to fail. All other extensions are non-critical.

Tools MUST honor this marking when processing a CSAF document:

- A tool that encounters an **non-critical** extension it does not understand MAY ignore that extension's data and continue processing.

  > Note: The value of `critical` is solely relevant for processing, the extension's content and its impact of the understanding of the document is provided via the Extension Category (`category`; see also https://docs.oasis-open.org/csaf/csaf/v2.1/csaf-v2.1.html#content-schema-property---category).

- A tool that encounters a **critical** extension it does not understand MUST fail processing of the CSAF document, unless the user explicitly forces it to continue.

## Governance Requirements

Every extension MUST meet the requirements below to ensure quality, utility, and alignment with CSAF principles. Extensions that violate these requirements MAY be deny-listed by the TC at any point in time.
Requirements that do not need to be fulfilled by private extensions are clearly marked.
Nevertheless, it is RECOMMENDED that also private extensions fulfill them.

### Core Principles

**Complement, do not duplicate.** An extension MUST NOT convey data that CSAF Core already intends to convey. Implementers MUST fully use the relevant CSAF Core fields before turning to an extension. Extensions exist to fill genuine gaps in the standard, not to work around limited adoption of existing fields. Once CSAF Core or an official extension conveys information previously carried by an extension, the official field MUST be used, and the TC MAY deny-list the superseded extension to preserve interoperability.

**Align with the purpose of CSAF.** An extension MUST NOT contradict the purpose or intent of CSAF. It MUST support the creation, exchange, and consumption of security advisory information, and any domain-specific data it introduces MUST serve a vulnerability or product context, the description or assessment of a vulnerability, the technical identification, lifecycle or vulnerability applicability of a product, remediation or mitigation, identification or configuration of a product, or the relationships between vulnerabilities and products. Extensions addressing unrelated concerns, such as organizational processes or internal workflows not tied to advisory content, are out of scope and will not be considered for registration. 

**Limit scope to a single location.** An extension is limited to one specific location in the CSAF schema. This constraint keeps extensions predictable and straightforward to implement. Extensions that can apply to a single vulnerability or the whole CSAF document are allowed to appear in both locations.

### Documentation and Implementation

**Open source.** The CSAF Extension Package [https://github.com/oasis-tcs/csaf/blob/master/csaf_2.1/prose/share/csaf-v2.1-draft.md#conformance-clause-35-csaf-extension-package], extension schema, specification, tests, and all supporting documentation MUST be open source, and the source repositories MUST be publicly accessible. The chosen license MUST be compatible with the OASIS IPR Policy so that the material can be incorporated into CSAF. Documentation MUST be sufficient for an independent party to implement the extension without access to the authors. Private extensions are exempted from the requirement to make the Extension Package open source and publicly accessible while this is still RECOMMENDED.

**Reference implementation.** A reference implementation MUST be available as open source and MUST be written in a memory-safe programming language. It demonstrates feasibility and surfaces implementation challenges before formal adoption. For official extensions, the reference implementation SHOULD be complete before the final TC vote. Private extensions are exempted from the requirement to make the reference implementation open source and publicly accessible while this is still RECOMMENDED.

**Documentation standards.** Extensions MUST be reasonably documented, with a clear statement of purpose and usage guidance. Documentation MUST include schema definitions, use cases, examples, and integration guidance, and MUST be clear enough for independent developers to implement the extension correctly.

### Review and Approval

**Technical Committee vote.** Accepting an extension as a registered or official extension requires a vote in the OASIS CSAF TC. A documented review of all governance requirements MUST precede the vote, and a community discussion period precedes formal voting.

**Critical extension assessment.** Criticality is determined by the rules in the processing model above. When an extension proposed for registration is critical, a second vote is required that explicitly weighs whether its risks outweigh its benefits. Proposers SHOULD self-assess criticality at submission, and the TC assesses the classification during review.

**Pre-release implementation testing.** For official extensions, the reference implementation SHOULD be complete and tested before the final vote. Real-world implementation reveals bugs, ambiguities, and integration issues, and feedback from that work informs the TC's decision.

### Intellectual Property

Extension authors MUST grant OASIS a license to include the extension, with or without modifications, in any future version of CSAF. Granting this license does not guarantee inclusion; the TC retains final decision authority. The requirement protects the future evolution of CSAF and prevents licensing obstacles to standardization.

## Extension Status and TC-Maintained Lists

The TC maintains four authoritative lists that govern which extensions may be used and how:

- **Official extensions.** The list of extensions maintained by the TC and hosted at `extensions.csaf.dev`.
- **Registered extensions.** The list of registered extensions.
- **Deprecated extensions.** Extensions that MAY still be used, but whose support is scheduled for removal in the near future. Authors SHOULD migrate away from a deprecated extension to CSAF Core or to a current extension.
- **Deny-listed extensions.** Extensions that MUST NOT be used, for example because an official property now conveys the same information.

All lists are hosted at `extensions.csaf.dev`. The TC is free to place any extension, including experimental or non-conforming ones, on lists 3 and 4.

An extension change controller MAY request to put its extension at any point on list 3 or 4.
An extension change controller MAY submit its extension for registration.
For lists 1 and 2, the process is described in [Review and Approval)[#Review-and-Approval).

## Extension Registry

The CSAF Extension Registry is a public catalog of registered and official extensions. It lets implementers discover available extensions, review their specifications, and reach their documentation and reference implementations. Private extensions are not listed.

## Getting Started

To propose a new extension:

1. Engage the OASIS CSAF Technical Committee early through its public discussions or issue tracker to validate the need and the intended schema location.
2. Develop the CSAF Extension Package, extension schema, specification, and an open-source reference implementation in a memory-safe language.
3. Confirm that all governance requirements above are met, and assemble the submission package (CSAF Extension Package, versioned schema, specification, tests, documentation, reference implementation, and IPR license grant).
4. Submit the extension for TC review and community feedback.
5. The TC votes on the extension and if applicable on the criticality assessment.
6. On approval, the extension is registered and documented in the registry.
7. Optionally, pursue official status by completing the additional implementation testing and TC review required for official extensions. Not every registered extension needs to become official.

For questions or guidance, reach the OASIS CSAF Technical Committee through the project's public channels (issue tracker and TC mailing list).

