## Conformance Roles{#conformance-roles}

Every conformance target that is a program takes one or more of the following roles, either directly or through the conformance profiles it satisfies. A role states what the tests of each level mean for a target in that role. The conformance clause of a target names its roles below its heading.

### Conformance Role: Producer{#conformance-role-producer}

Creates or changes CSAF Documents: writes them by hand or tool, converts from other formats, translates, withdraws or supersedes them.

The tests mean for a target in this role:

- mandatory tests: A producer MUST NOT emit a document that fails one of these tests.
- recommended tests: A producer SHOULD NOT emit a document that fails one of these tests.

Conformance targets taking this role:

- [sec](#conformance-clause-2-csaf-producer)
- [sec](#conformance-clause-3-csaf-direct-producer)
- [sec](#conformance-clause-4-csaf-converter)
- [sec](#conformance-clause-5-cvrf-csaf-converter)
- [sec](#conformance-clause-6-csaf-content-management-system)
- [sec](#conformance-clause-7-csaf-post-processor)
- [sec](#conformance-clause-8-csaf-modifier)
- [sec](#conformance-clause-9-csaf-translator)
- [sec](#conformance-clause-18-csaf-2-0-to-csaf-2-1-converter)
- [sec](#conformance-clause-19-csaf-library)
- [sec](#conformance-clause-20-csaf-library-with-basic-validation)
- [sec](#conformance-clause-21-csaf-library-with-extended-validation)
- [sec](#conformance-clause-22-csaf-library-with-full-validation)
- [sec](#conformance-clause-24-csaf-withdrawer)
- [sec](#conformance-clause-25-csaf-superseder)
- [sec](#conformance-clause-26-csaf-rvisc-id-updater)

Roles in the distribution of CSAF Documents covered by this role:

- [sec](#role-csaf-publisher)

### Conformance Role: Intermediary{#conformance-role-intermediary}

Moves CSAF Documents between producers and consumers without changing them: publishes, mirrors, lists, aggregates, downloads; may filter and index.

The tests mean for a target in this role:

- mandatory tests: An intermediary MUST NOT offer a document failing one of these tests as valid; it MAY offer it flagged as invalid.

Conformance targets taking this role:

- [sec](#conformance-clause-23-csaf-downloader)

Roles in the distribution of CSAF Documents covered by this role:

- [sec](#role-csaf-provider)
- [sec](#role-csaf-trusted-provider)
- [sec](#role-csaf-lister)
- [sec](#role-csaf-aggregator)

### Conformance Role: Consumer{#conformance-role-consumer}

Reads CSAF Documents and acts on them: displays them, matches them against assets or SBOMs, and derives (automated) decisions from them.

The tests mean for a target in this role:

- mandatory tests: A consumer MAY rely on these tests holding for a valid document; it MUST NOT derive an automated action from a part of a document that fails one of them.

Conformance targets taking this role:

- [sec](#conformance-clause-6-csaf-content-management-system)
- [sec](#conformance-clause-7-csaf-post-processor)
- [sec](#conformance-clause-8-csaf-modifier)
- [sec](#conformance-clause-9-csaf-translator)
- [sec](#conformance-clause-10-csaf-consumer)
- [sec](#conformance-clause-11-csaf-viewer)
- [sec](#conformance-clause-12-csaf-management-system)
- [sec](#conformance-clause-13-csaf-asset-matching-system)
- [sec](#conformance-clause-17-csaf-sbom-matching-system)
- [sec](#conformance-clause-19-csaf-library)
- [sec](#conformance-clause-20-csaf-library-with-basic-validation)
- [sec](#conformance-clause-21-csaf-library-with-extended-validation)
- [sec](#conformance-clause-22-csaf-library-with-full-validation)
- [sec](#conformance-clause-24-csaf-withdrawer)
- [sec](#conformance-clause-25-csaf-superseder)
- [sec](#conformance-clause-26-csaf-rvisc-id-updater)

### Conformance Role: Validator{#conformance-role-validator}

Runs the tests and reports results; selects them through presets; may apply quick fixes when explicitly asked.

The tests mean for a target in this role:

- mandatory tests: A validator MUST run these tests (preset `mandatory`, basic validator and up) and report a failure as error.
- recommended tests: A validator MUST run these tests in preset `recommended` (extended validator and up) and report a failure as warning.
- informative tests: A validator MUST run these tests in preset `informative` (full validator) and report a failure as information.

Conformance targets taking this role:

- [sec](#conformance-clause-14-csaf-basic-validator)
- [sec](#conformance-clause-15-csaf-extended-validator)
- [sec](#conformance-clause-16-csaf-full-validator)
- [sec](#conformance-clause-20-csaf-library-with-basic-validation)
- [sec](#conformance-clause-21-csaf-library-with-extended-validation)
- [sec](#conformance-clause-22-csaf-library-with-full-validation)

Capabilities, as the presets of tests the target runs:

- [sec](#conformance-clause-14-csaf-basic-validator): `basic`
- [sec](#conformance-clause-15-csaf-extended-validator): `extended`
- [sec](#conformance-clause-16-csaf-full-validator): `full`
- [sec](#conformance-clause-20-csaf-library-with-basic-validation): `basic`
- [sec](#conformance-clause-21-csaf-library-with-extended-validation): `extended`
- [sec](#conformance-clause-22-csaf-library-with-full-validation): `full`
