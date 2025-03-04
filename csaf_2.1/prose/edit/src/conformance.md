# Conformance

In the only subsection of this section, the conformance targets and clauses are listed.
The clauses, matching the targets one to one, are listed in separate sub-subsections of the targets listing subsection.

Informative Comments:

> The order in which targets, and their corresponding clauses appear is somewhat arbitrary as there is
> no natural order on such diverse roles participating in the document exchanging ecosystem.
>
> Except for the target **CSAF document**, all other 22 targets span a taxonomy of the complex CSAF ecosystems existing
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

## Conformance Targets

This document defines requirements for the CSAF file format and for certain software components that interact with it.
The entities ("conformance targets") for which this document defines requirements are:

* **CSAF document**: A security advisory text document in the format defined by this document.
* **CSAF downloader**: A program that retrieves CSAF documents in an automated fashion.
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
* **CSAF 2.0 to CSAF 2.1 converter**: A CSAF producer which takes a CSAF 2.0 document as input and converts it into a valid CSAF 2.1 document.
* **CSAF library**: A library that implements CSAF data capabilities.
* **CSAF library with basic validation**: A CSAF library that also satisfies the conformance target "CSAF basic validator".
* **CSAF library with extended validation**: A CSAF library that also satisfies the conformance target "CSAF extended validator".
* **CSAF library with full validation**: A CSAF library that also satisfies the conformance target "CSAF full validator".

### Conformance Clause 1: CSAF document

A text file or data stream satisfies the "CSAF document" conformance profile if it:

* conforms to the syntax and semantics defined in section [sec](#date-and-time).
* conforms to the syntax and semantics defined in section [sec](#schema-elements).
* satisfies at least one profile defined in section [sec](#profiles).
* conforms to the syntax and semantics defined in section [sec](#additional-conventions).
* does not fail any mandatory test defined in section [sec](#mandatory-tests).

### Conformance Clause 2: CSAF producer

A program satisfies the "CSAF producer" conformance profile if the program:

* produces output in the CSAF format, according to the conformance profile "CSAF document".
* satisfies those normative requirements in section [sec](#schema-elements) and [sec](#safety-security-and-data-protection-considerations) that
  are designated as applying to CSAF producers.

### Conformance Clause 3: CSAF direct producer

An analysis tool satisfies the "CSAF direct producer" conformance profile if the analysis tool:

* satisfies the "CSAF producer" conformance profile.
* additionally satisfies those normative requirements in section [sec](#schema-elements) that are designated as applying to "direct producers" or
  to "analysis tools".
* does not emit any objects, properties, or values which, according to section [sec](#schema-elements),
  are intended to be produced only by converters.

### Conformance Clause 4: CSAF converter

A converter satisfies the “CSAF converter” conformance profile if the converter:

* satisfies the "CSAF producer" conformance profile.
* additionally satisfies those normative requirements in section [sec](#schema-elements) that are designated as applying to converters.
* does not emit any objects, properties, or values which, according to section [sec](#schema-elements),
  are intended to be produced only by direct producers.

### Conformance Clause 5: CVRF CSAF converter

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
* `/vulnerabilities[]/cwes[]`:
  * The CVRF CSAF converter MUST determine the CWE specification version the given CWE was selected from by
    using the latest version that matches the `id` and `name` exactly and was published prior to the value of
    `/document/tracking/current_release_date` of the source document.
    If no such version exist, the first matching version published after the value of `/document/tracking/current_release_date`
    of the source document SHOULD be used.
    > This is done to create a deterministic conversion.

    If the CWE does not match at all, the CVRF CSAF converter MUST omit this CWE and output a warning that an invalid CWE was found and has
    been removed.
  * If a `vuln:CWE` instance refers to a CWE category or view, the CVRF CSAF converter MUST omit this instance and output a
    warning that this CWE has been removed as its usage is not allowed in vulnerability mappings.
* `/vulnerabilities[]/disclosure_date`: If a `vuln:ReleaseDate` was given, the CVRF CSAF converter MUST convert its value into the `disclosure_date` element.
* `/vulnerabilities[]/ids`: If a `vuln:ID` element is given, the CVRF CSAF converter converts it into the first item of the `ids` array.
* `/vulnerabilities[]/remediations[]`:
  * If neither `product_ids` nor `group_ids` are given, the CVRF CSAF converter appends all Product IDs which are listed under
    `../product_status` in the arrays `known_affected`, `first_affected` and `last_affected` into `product_ids`.
    If none of these arrays exist, the CVRF CSAF converter outputs an error that no matching Product ID was found for this remediation element.
  * The CVRF CSAF converter MUST convert any remediation with the type `Vendor Fix` into the category `optional_patch` if the product in
    question is in one of the product status groups "Not Affected" or "Fixed" for this vulnerability.
    Otherwise, the category `vendor_fix` MUST be set.
    If multiple products are associated with the remediation - either directly or through a product group - and the products belong to
    different product status groups, the CVRF CSAF converter MUST duplicate the remediation, change the category in one instance
    to `optional_patch` and distribute the products accordingly as stated by the conversion rule.
  * The CVRF CSAF converter MUST convert any remediation with the type `None Available` into the category `fix_planned`
    if the product in question is also listed in a remediation of the type `Vendor Fix` with a `Date` in the future or no `Date` at all.
    Consequently, the product MUST be removed from the remediation of the category `vendor_fix`.
    If it was the last product in that remediation, the remediation MUST be removed.
  * The CVRF CSAF converter MUST remove any product from a remediation with the type `None Available`
    if the product in question is also listed in a remediation of the type `Vendor Fix` with a `Date` in the past or to the exact same time.
    If it was the last product in that remediation, the remediation MUST be removed.
  * In any other case, the CVRF CSAF converter MUST preserve the product in the remediation of the category `none_available`.
  * The CVRF CSAF converter MUST output a warning if a remediation was added, deleted or the value of the category was changed,
    including the products it was changed for.
* `/vulnerabilities[]/metrics[]`:
  * For any CVSS v4 element, the CVRF CSAF converter MUST compute the `baseSeverity` from the `baseScore` according to
    the rules of the applicable CVSS standard. (CSAF CVRF v1.2 predates CVSS v4.0.)
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
  * To determine, which minor version of CVSS v3 is used and to evaluate a CVSS v4 that was wrongly inserted in a CVSS v3 element,
    the CVRF CSAF converter uses the following steps:
    1. Retrieve the CVSS version from the CVSS vector, if present.

        *Example 1:*

        ```
          CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H => 3.1
        ```

    2. Retrieve the CVSS version from the CVSS element's namespace, if present.
       The CVRF CSAF converter outputs a warning that this value was guessed from the element's namespace.

        *Example 2:*

        ```
          xmlns:cvssv31="https://www.first.org/cvss/cvss-v3.1.xsd"
          <!-- -->
          <cvssv31:ScoreSetV3>
        ```

        is handled the same as

        *Example 3:*

        ```
          <ScoreSetV3 xmlns="https://www.first.org/cvss/cvss-v3.1.xsd">
        ```

    3. Retrieve the CVSS version from the CVSS namespace given in the root element, if present.
       The CVRF CSAF converter outputs a warning that this value was guessed from the global namespace.
       If more than one CVSS namespace is present and the element is not clearly defined via the namespace,
       this step MUST be skipped without a decision.

        *Example 4:*

        ```
          xmlns:cvssv3="https://www.first.org/cvss/cvss-v3.0.xsd" => 3.0
        ```

    4. Retrieve the CVSS version from a config value, which defaults to `3.0`.
       (As CSAF CVRF v1.2 predates CVSS v3.1.) The CVRF CSAF converter outputs a warning that this value was taken from the config.

### Conformance Clause 6: CSAF content management system

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
    (see also subsections of [sec](#version-type)) selected in the configuration.
  * check that the document version is set correctly based on the changes in comparison to the previous version
    (see also subsections of [sec](#version-type)).
  * suggest to use the document status `interim` if a CSAF document is updated more frequent than the given threshold in
    the configuration (default: 3 weeks)
  * suggest to publish a new version of the CSAF document with the document status `final` if the document status was
    `interim` and no new release has be done during the given threshold in the configuration (default: 6 weeks)
    > Note that the terms "publish", "publication" and their derived forms are used in this conformance profile independent of
      whether the specified target group is the public or a closed group.
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

  * `/$schema` with the value prescribed by the schema
  * `/document/csaf_version` with the value prescribed by the schema
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
    * `/$schema` with the value prescribed by the schema
    * `/document/csaf_version` with the value prescribed by the schema
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

### Conformance Clause 7: CSAF post-processor

A CSAF post-processor satisfies the "CSAF post-processor" conformance profile if the post-processor:

* satisfies the "CSAF consumer" conformance profile.
* satisfies the "CSAF producer" conformance profile.
* additionally satisfies those normative requirements in section [sec](#schema-elements) that are designated as applying to post-processors.

### Conformance Clause 8: CSAF modifier

A program satisfies the "CSAF modifier" conformance profile if the program fulfills the two following groups of requirements:

The program:

* satisfies the "CSAF post-processor" conformance profile.
* adds, deletes or modifies at least one property, array, object or value of a property or item of an array.
* does not emit any objects, properties, or values which, according to section [sec](#conformance),
  are intended to be produced only by CSAF translators.
* satisfies the normative requirements given below.

The resulting modified document:

* does not have the same `/document/tracking/id` as the original document.
  The modified document can use a completely new `/document/tracking/id` or compute one by appending the original `/document/tracking/id` as
  a suffix after an ID from the naming scheme of the issuer of the modified version.
  It SHOULD NOT use the original `/document/tracking/id` as a prefix.
* includes a reference to the original advisory as first element of the array `/document/references[]`.

### Conformance Clause 9: CSAF translator

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
  > Note that the term "publish" is used in this conformance profile independent of whether the specified target group is the public
    or a closed group.
* provides the `/document/lang` property with a value matching the language of the translation.
* provides the `/document/source_lang` to contain the language of the original document (and SHOULD only be set by CSAF translators).
* has the value `translator` set in `/document/publisher/category`
* includes a reference to the original advisory as first element of the array `/document/references[]`.
* MAY contain translations for elements in arrays of `references_t` after the first element.
  However, it MUST keep the original URLs as references at the end.

### Conformance Clause 10: CSAF consumer

A processor satisfies the "CSAF consumer" conformance profile if the processor:

* reads CSAF documents and interprets them according to the semantics defined in section [sec](#schema-elements) and [sec](#additional-conventions).
* satisfies those normative requirements in section [sec](#schema-elements), [sec](#additional-conventions) and
  [sec](#safety-security-and-data-protection-considerations) that are designated as applying to CSAF consumers.

### Conformance Clause 11: CSAF viewer

A viewer satisfies the "CSAF viewer" conformance profile if the viewer fulfills the two following groups of requirements:

The viewer:

* satisfies the "CSAF consumer" conformance profile.
* satisfies the normative requirements given below.

For each CVSS-Score in `/vulnerabilities[]/metrics[]` the viewer:

* preferably shows the `vector` if there is an inconsistency between the `vector` and any other sibling attribute.
* SHOULD prefer the item of `metrics[]` for each `product_id` which originates from the document author (and therefore has no property `source`)
  and has the highest CVSS Base Score and newest CVSS version (in that order) if a `product_id` is listed in more than one item of `metrics[]`.

### Conformance Clause 12: CSAF management system

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

### Conformance Clause 13: CSAF asset matching system

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
* detects the usage semantic version (as described in section [sec](#version-type-semantic-versioning)).
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

### Conformance Clause 14: CSAF basic validator

A program satisfies the "CSAF basic validator" conformance profile if the program:

* reads documents and performs a check against the JSON schema.
* performs all mandatory tests as given in section [sec](#mandatory-tests).
* does not change the CSAF documents.

A CSAF basic validator MAY provide one or more additional functions:

* Only run one or more selected mandatory tests.
* Apply quick fixes as specified in the standard.
* Apply additional quick fixes as implemented by the vendor.

### Conformance Clause 15: CSAF extended validator

A CSAF basic validator satisfies the "CSAF extended validator" conformance profile if the CSAF basic validator:

* satisfies the "CSAF basic validator" conformance profile.
* additionally performs all optional tests as given in section [sec](#optional-tests).

A CSAF extended validator MAY provide an additional function to only run one or more selected optional tests.

### Conformance Clause 16: CSAF full validator

A CSAF extended validator satisfies the "CSAF full validator" conformance profile if the CSAF extended validator:

* satisfies the "CSAF extended validator" conformance profile.
* additionally performs all informative tests as given in section [sec](#informative-test).

A CSAF full validator MAY provide an additional function to only run one or more selected informative tests.

### Conformance Clause 17: CSAF SBOM matching system

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
* detects the usage semantic version (as described in section [sec](#version-type-semantic-versioning)).
* is able to trigger a run of the SBOM matching module:
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

### Conformance Clause 18: CSAF 2.0 to CSAF 2.1 converter

A program satisfies the "CSAF 2.0 to CSAF 2.1 converter" conformance profile if the program fulfills the following two groups of requirements:

Firstly, the program:

* satisfies the "CSAF producer" conformance profile.
* takes only CSAF 2.0 documents as input.
* additionally satisfies the normative requirements given below.

Secondly, the program fulfills the following for all items of:

* type `/$defs/full_product_name_t/product_identification_helper/cpe`: If a CPE is invalid, the CSAF 2.0 to CSAF 2.1 converter SHOULD removed the
  invalid value and output a warning that an invalid CPE was detected and removed. Such a warning MUST include the invalid CPE.
* type `/$defs/full_product_name_t/model_number`:
  * If a model number is given that does not end on a star, the CSAF 2.0 to CSAF 2.1 converter SHOULD add a `*` to the end and output a
    warning that a partial model number was detected and a star has been added.
    Such a warning MUST include the model number.
  * If the model number contains a `\`, the CSAF 2.0 to CSAF 2.1 converter MUST escape it by inserting an additional `\` before the character.
  * If the model number contains multiple unescaped `*` after the conversion, the CSAF 2.0 to CSAF 2.1 converter MUST remove the entry and
    output a warning that a model number with multiple stars was detected and removed.
    Such a warning MUST include the model number.

  > A tool MAY provide a non-default option to interpret all model numbers as complete and therefore does not add any stars.

  > A tool MAY provide a non-default option to interpret the `?` in all model numbers as part of the model number itself and therefore escape it.

  > A tool MAY provide a non-default option to interpret the `*` in all model numbers as part of the model number itself and therefore escape it.

* type `/$defs/full_product_name_t/product_identification_helper/purls`: If a `/$defs/full_product_name_t/product_identification_helper/purl` is given,
  the CSAF 2.0 to CSAF 2.1 converter MUST convert it into the first item of the corresponding `purls` array.
* type `/$defs/full_product_name_t/serial_number`:
  * If a serial number is given that does not end on a star, the CSAF 2.0 to CSAF 2.1 converter SHOULD add a `*` to the end and output a
    warning that a partial serial number was detected and a star has been added.
    Such a warning MUST include the serial number.
  * If the serial number contains a `\`, the CSAF 2.0 to CSAF 2.1 converter MUST escape it by inserting an additional `\` before the character.
  * If the serial number contains multiple unescaped `*` after the conversion, the CSAF 2.0 to CSAF 2.1 converter MUST remove the entry and
    output a warning that a serial number with multiple stars was detected and removed.
    Such a warning MUST include the serial number.

  > A tool MAY provide a non-default option to interpret all serial numbers as complete and therefore does not add any stars.

  > A tool MAY provide a non-default option to interpret the `?` in all serial numbers as part of the serial number itself and therefore escape it.

  > A tool MAY provide a non-default option to interpret the `*` in all serial numbers as part of the serial number itself and therefore escape it.

* `/$schema`: The CSAF 2.0 to CSAF 2.1 converter MUST set property with the value prescribed by the schema.
* `/document/csaf_version`: The CSAF 2.0 to CSAF 2.1 converter MUST update the value to `2.1`.
* `/document/distribution/tlp/label`: If a TLP label is given, the CSAF 2.0 to CSAF 2.1 converter MUST convert it according to the table below:
  
  | CSAF 2.0 (using TLP v1.0) | CSAF 2.1 (using TLP v2.0) |
  |---------------------------|---------------------------|
  | `TLP:WHITE`               | `TLP:CLEAR`               |
  | `TLP:GREEN`               | `TLP:GREEN`               |
  | `TLP:AMBER`               | `TLP:AMBER`               |
  | `TLP:RED`                 | `TLP:RED`                 |

  If `/document/distribution/text` contains the string `TLP v2.0: TLP:<ValidTLPLabel>`, the CSAF 2.0 to CSAF 2.1 converter SHOULD provide an
  option to use this label instead. If the TLP label changes through such conversion in a way that is not reflected in the table above, the
  the CSAF 2.0 to CSAF 2.1 converter MUST output a warning that the TLP label was taken from the distribution text. Such a warning MUST include
  both values: the converted one based on the table and the one from the distribution text.
  > This is a common case for CSAF 2.0 documents labeled as `TLP:RED` but actually intended to be `TLP:AMBER+STRICT`.

  If no TLP label was given, the CSAF 2.0 to CSAF 2.1 converter SHOULD assign `TLP:CLEAR` and output a warning that the default TLP has been set.
* `/document/publisher/category`: If the value is `other`, the CSAF 2.0 to CSAF 2.1 converter SHOULD output a warning that some parties have
  been regrouped into the new value `multiplier`. An option to suppress this warning MUST exist. In addition, an option SHOULD be provided to
  set the value to `multiplier`.
* `/document/title`: If the value contains the `/document/tracking/id`, the CSAF 2.0 to CSAF 2.1 converter MUST remove the `/document/tracking/id`
  from the `/document/title`. In addition, separating characters including but not limited to whitespace, colon, dash and brackets MUST be removed.
* `/vulnerabilities[]/cwes[]`: The CSAF 2.0 to CSAF 2.1 converter MUST determine the CWE specification version the given CWE was selected from by
  using the latest version that matches the `id` and `name` exactly and was published prior to the value of `/document/tracking/current_release_date`
  of the source document. If no such version exist, the first matching version published after the value of `/document/tracking/current_release_date`
  of the source document SHOULD be used.
  > This is done to create a deterministic conversion.

  The tool SHOULD implement an option to use the latest available CWE version at the time of the conversion that still matches.

* `/vulnerabilities[]/disclosure_date`: If a `release_date` was given, the CSAF 2.0 to CSAF 2.1 converter MUST convert the key as `disclosure_date`.
* `/vulnerabilities[]/metrics/ssvc_v1`: If a SSVC vector or decision points of an SSVC vector are given in an item of `notes` of the current
  vulnerability using the `title` `SSVC` and the `category` `other`, the CSAF 2.0 to CSAF 2.1 converter MUST convert that data into the `ssvc_v1`
  object within the current vulnerability.
  If the CSAF 2.0 to CSAF 2.1 converter is able to construct a valid object without loosing any information, the corresponding `notes` item SHALL
  be removed.
  If the CSAF 2.0 to CSAF 2.1 converter is unable to construct a valid object with the information given, the CSAF 2.0 to CSAF 2.1 converter SHALL
  remove the invalid `ssvc_v1` object, keep the original item of `notes` and output a warning that the automatic conversion of the SSVC data failed.
  If the CSAF 2.0 to CSAF 2.1 converter would loose information during the conversion, the CSAF 2.0 to CSAF 2.1 converter SHALL remove the `ssvc_v1`
  object, keep the original item of `notes` and output a warning that the automatic conversion of the SSVC data would lead to loosing information.
* `/vulnerabilities[]/remediations[]`:
  * The CSAF 2.0 to CSAF 2.1 converter MUST convert any remediation with the category `vendor_fix` into the category `optional_patch`
    if the product in question is in one of the product status groups "Not Affected" or "Fixed" for this vulnerability.
    Otherwise, the category `vendor_fix` MUST stay the same.
    If multiple products are associated with the remediation - either directly or through a product group - and the products belong to different
    product status groups, the CSAF 2.0 to CSAF 2.1 converter MUST duplicate the remediation, change the category in one instance to `optional_patch`
    and distribute the products accordingly as stated by the conversion rule.
  * The CSAF 2.0 to CSAF 2.1 converter MUST convert any remediation with the category `none_available` into the category `fix_planned`
    if the product in question is also listed in a remediation of the category `vendor_fix` with a `date` in the future or no `date` at all.
    Consequently, the product MUST be removed from the remediation of the category `vendor_fix`.
    If it was the last product in that remediation, the remediation MUST be removed.
  * The CSAF 2.0 to CSAF 2.1 converter MUST remove any product from a remediation with the category `none_available`
    if the product in question is also listed in a remediation of the category `vendor_fix` with a `date` in the past or to the exact same time.
    If it was the last product in that remediation, the remediation MUST be removed.
  * In any other case, the CSAF 2.0 to CSAF 2.1 converter MUST preserve the product in the remediation of the category `none_available`.
  * The CSAF 2.0 to CSAF 2.1 converter MUST output a warning if a remediation was added, deleted or the value of the category was changed,
    including the products it was changed for.
* The CSAF 2.0 to CSAF 2.1 converter SHALL provide the JSON path where the warning occurred together with the warning.

> A tool MAY implement options to convert other Markdown formats to GitHub-flavored Markdown.

> A tool MAY implement an additional, non-default option to output an invalid document that can be fixed afterwards. Solely in this case, any
> of the rules above MAY be ignored to avoid data loss.

### Conformance Clause 19: CSAF library

A library satisfies the "CSAF library" conformance profile if the library:

* implements all elements as data structures conforming to the syntax and semantics defined in section [sec](#schema-elements).
* checks all elements according to the patterns provided in the JSON schema.
* has a function that checks version ranges.
* has a function that helps to create version ranges.
* provides for each element functions that allow to create, add, modify and delete that element.
* has a function that reads a CSAF document into the data structure from a
  * file system.
  * URL.
  * data stream.
* provides function for sorting the keys and sorts the keys automatically on output.
* has a function that outputs the data structure as CSAF document
  * on the file system.
  * as string.
  * into a data stream.
* has a function to determine the filename according to [sec](#filename) and sets the filename per default when saving a CSAF document.
* generates a new `product_id` for each new element of type `full_product_name_t` unless an ID is given during the creation.
* generates a new `group_id` for each new element of type `product_group_id_t` unless an ID is given during the creation.
* provides a function to retrieve all elements of type `product_id_t` with its corresponding `full_product_name_t/name` and
  `full_product_name_t/product_identification_helper`.
* provides a function to retrieve all `product_identification_helper` and their mapping to elements of type `product_id_t`.
* provides a function to retrieve a VEX status mapping for all data, which includes the combination of vulnerability, product, product status
  and, where necessary according to the profile, the impact statement respectively the action statement.
* provides a function to generate a `full_product_name_t/name` with in `branches` through concatenating the `name` values separated by whitespace
  of the elements along the path towards this leaf.
* calculates the CVSS scores and severities for existing data for all CVSS versions.
* validates the CVSS scores and severities for existing data for all CVSS versions.

> The library MAY implement an option to retrieve the keys unsorted.

### Conformance Clause 20: CSAF library with basic validation

A CSAF library satisfies the "CSAF library with basic validation" conformance profile if the CSAF library:

* satisfies the "CSAF library" conformance profile.
* satisfies the "CSAF basic validator" conformance profile.
* validates the CSAF document before output according to the "CSAF basic validator" and presents the validation result accordingly.
* provide a function to validate the data structure in its current state according to the "CSAF basic validator" and presents the validation
  result accordingly.

A CSAF library does not satisfies the "CSAF library with basic validation" conformance profile if the CSAF library uses an external library or
program for the "CSAF basic validator" part and does not enforce its presence.

### Conformance Clause 21: CSAF library with extended validation

A CSAF library satisfies the "CSAF library with extended validation" conformance profile if the CSAF library:

* satisfies the "CSAF library" conformance profile.
* satisfies the "CSAF extended validator" conformance profile.
* validates the CSAF document before output according to the "CSAF extended validator" and presents the validation result accordingly.
* provide a function to validate the data structure in its current state according to the "CSAF extended validator" and presents the validation
  result accordingly.

A CSAF library does not satisfies the "CSAF library with extended validation" conformance profile if the CSAF library uses an external library or
program for the "CSAF extended validator" part and does not enforce its presence.

### Conformance Clause 22: CSAF library with full validation

A CSAF library satisfies the "CSAF library with extended validation" conformance profile if the CSAF library:

* satisfies the "CSAF library" conformance profile.
* satisfies the "CSAF full validator" conformance profile.
* validates the CSAF document before output according to the "CSAF full validator" and presents the validation result accordingly.
* provide a function to validate the data structure in its current state according to the "CSAF full validator" and presents the validation
  result accordingly.

A CSAF library does not satisfies the "CSAF library with full validation" conformance profile if the CSAF library uses an external library or
program for the "CSAF full validator" part and does not enforce its presence.

### Conformance Clause 23: CSAF downloader

A program satisfies the "CSAF downloader" conformance profile if the program:

* conforms to the process defined in section [sec](#retrieving-rules) by executing all parts that are applicable to the given role.
* supports directory-based and ROLIE-based retrieval.
* is able to execute both steps from section [sec](#retrieving-rules) separately.
* uses a program-specific HTTP User Agent, e.g. consisting of the name and version of the program.

> A tool MAY implement an option to store CSAF documents that fail any of the steps in section [sec](#retrieving-csaf-documents).

-------
