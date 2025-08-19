## Presets

A test preset is a predefined set of tests that was given a name.
It MAY contain any number of tests.
Two presets MAY overlap.
The content of a preset MAY vary in different CSAF versions.
A CSAF validator MUST support every official preset that solely include tests that are implemented by the CSAF validator.
A CSAF validator MAY provide or support additional presets.
A CSAF validator MUST implement all tests for any supported preset.
Names of presets not defined in this CSAF standard SHALL have the following prefix before their name:

- `x_`: for any CSAF validator specific preset.
  > Multiple CSAF validators might use the same preset name for different sets of tests.
  > Users are advised to carefully check the documentation of the tools to avoid incorrect assumptions.
- `org_` followed by an organization identifier and an underscore (`_`): for any preset specified by an organization as a part of a public definition
  that can be implemented by different CSAF validators.
  The organization identifier MUST only use the characters identified by the pattern `[0-9a-zA-Z-]`.
  The organization identifier MUST be registered with the OASIS CSAF TC.
- `csaf_`: for any preset defined later on by the OASIS CSAF TC.

Official presets are defined in different parts of the standard.

### Presets Defined through Test Subsections

The following presets are defined through subsections of the test section:

- `mandatory`: all tests given in section [sec](#mandatory-tests)
- `recommended`: all tests given in section [sec](#recommended-tests)
- `informative`: all tests given in section [sec](#informative-tests)

### Presets Defined through Conformance Targets

The following presets are defined through conformance targets:

- `schema`: Check against the JSON schema (see section [sec](#conformance-clause-14-csaf-basic-validator))
- `basic`: `schema` + `mandatory` (see section [sec](#conformance-clause-14-csaf-basic-validator))
- `extended`: `basic` + `recommended` (see section [sec](#conformance-clause-15-csaf-extended-validator))
- `full`: `extended` + `informative` (see section [sec](#conformance-clause-16-csaf-full-validator))

As presets are sets, the operator `+` MUST be interpreted as the union operation.

### Additional Presets

Additional presets are defined as follows:

- `external-request-free`:
  - Description: Any test that can be executed without a request into the Internet or a different network.
    > This is intended to be used for browser-based tools as external requests may result in CORS issues.
    > Request over network to a tool that is delivered with or an install requirement for a CSAF validator are not considered external.
  - Set: `full` excluding tests [sec](#use-of-non-self-referencing-urls-failing-to-resolve)
    and [sec](#use-of-self-referencing-urls-failing-to-resolve)
- `consistent-revision-history`:
  - Description: Any test that is related to the revision history and ensures consistence within it.
  - Set:
    - [sec](#sorted-revision-history)
    - [sec](#released-revision-history)
    - [sec](#revision-history-entries-for-pre-release-versions)
    - [sec](#missing-item-in-revision-history)
    - [sec](#multiple-definition-in-revision-history)
    - [sec](#mandatory-tests--date-and-time)
    - [sec](#build-metadata-in-revision-history)
    - [sec](#older-initial-release-date-than-revision-history)
    - [sec](#older-current-release-date-than-revision-history)
    - [sec](#same-timestamps-in-revision-history)
    - [sec](#disclosure-date-newer-than-revision-history)
- `consistent-date-times`:
  - Description: Any test that is related to timestamps in CSAF and avoids invalid situations.
  - Set:
    - [sec](#mandatory-tests--date-and-time)
    - [sec](#inconsistent-disclosure-date)
    - [sec](#inconsistent-ssvc-timestamp)
    - [sec](#inconsistent-epss-timestamp)
    - [sec](#inconsistent-first-known-exploitation-dates)
    - [sec](#inconsistent-exploitation-date)
