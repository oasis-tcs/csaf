# Conformance

In the only subsection of this section, the conformance targets and clauses are listed.
The clauses, matching the targets one to one, are listed in separate sub-subsections of the targets listing subsection.

> The order in which targets, and their corresponding clauses appear is somewhat arbitrary as there is
> no natural order on such diverse roles participating in the document exchanging ecosystem.
>
> Except for the target **CSAF Document**, all other 24 targets span a taxonomy of the complex CSAF ecosystems existing
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

This document defines requirements for the file format and for certain software components that interact with it.
The entities ("conformance targets") for which this document defines requirements are:

* **CSAF Document**: A security advisory text document in the format defined by this document.
* **CSAF Producer**: A program which emits output in the CSAF format.
* **CSAF Direct Producer**: An analysis tool which acts as a CSAF Producer.
* **CSAF Converter**: A CSAF Producer that transforms the output of an analysis tool from its native output format into the CSAF format.
* **CVRF CSAF Converter**: A CSAF Producer which takes a CVRF document as input and converts it into a valid CSAF Document.
* **CSAF Content Management System**: A program that is able to create,
  review and manage CSAF Documents and is able to preview their details as required by CSAF Viewer.
* **CSAF Post-Processor**: A CSAF Producer that transforms an existing CSAF Document into a new CSAF Document,
  for example, by removing or redacting elements according to sharing policies.
* **CSAF Modifier**: A CSAF Post-Processor which takes a CSAF Document as input and modifies the structure or values of properties.
  The output is a valid CSAF Document.
* **CSAF Translator**: A CSAF Post-Processor which takes a CSAF Document as input and translates values of properties into another language.
  The output is a valid CSAF Document.
* **CSAF Consumer**: A program that reads and interprets a CSAF Document.
* **CSAF Viewer**: A CSAF Consumer that reads a CSAF Document, displays a list of the results it contains,
  and allows an end user to view each result in the context of the artifact in which it occurs.
* **CSAF Management System**: A program that is able to manage CSAF Documents and is able to display their details as required by CSAF Viewer.
* **CSAF Asset Matching System**: A program that connects to or is an asset database and is able to manage CSAF Documents as required
  by CSAF Management System as well as matching them to assets of the asset database.
* **CSAF Basic Validator**: A program that reads a document and checks it against the JSON schema and performs mandatory tests.
* **CSAF Extended Validator**: A CSAF Basic Validator that additionally performs recommended tests.
* **CSAF Full Validator**: A CSAF Extended Validator that additionally performs informative tests.
* **CSAF SBOM Matching System**: A program that connects to or is an SBOM database and is able to manage CSAF Documents as required
  by CSAF Management System as well as matching them to SBOM components of the SBOM database.
* **CSAF 2.0 to CSAF 2.1 Converter**: A CSAF Producer which takes a CSAF 2.0 Document as input and converts it into a valid CSAF 2.1 Document.
* **CSAF Library**: A library that implements CSAF data capabilities.
* **CSAF Library with Basic Validation**: A CSAF Library that also satisfies the conformance target "CSAF Basic Validator".
* **CSAF Library with Extended Validation**: A CSAF Library that also satisfies the conformance target "CSAF Extended Validator".
* **CSAF Library with Full Validation**: A CSAF Library that also satisfies the conformance target "CSAF Full Validator".
* **CSAF Downloader**: A program that retrieves CSAF Documents in an automated fashion.
* **CSAF Withdrawer**: A CSAF Post-Processor that transforms a given CSAF into a Withdrawn one.
* **CSAF Superseder**: A CSAF Post-Processor that transforms a given CSAF into a Superseded one.

### Conformance Clause 1: CSAF Document

A text file or data stream satisfies the "CSAF Document" conformance profile if it:

* conforms to the syntax and semantics defined in section [sec](#format-validation).
* conforms to the syntax and semantics defined in section [sec](#date-and-time).
* conforms to the syntax and semantics defined in section [sec](#schema-elements).
* satisfies at least one profile defined in section [sec](#profiles).
* conforms to the syntax and semantics defined in section [sec](#additional-conventions).
* does not fail any mandatory test defined in section [sec](#mandatory-tests).

### Conformance Clause 2: CSAF Producer

A program satisfies the "CSAF Producer" conformance profile if the program:

* produces output in the CSAF format, according to the conformance profile "CSAF Document".
* satisfies those normative requirements in section [sec](#schema-elements) and [sec](#safety-security-and-data-protection-considerations) that
  are designated as applying to CSAF Producers.

### Conformance Clause 3: CSAF Direct Producer

An analysis tool satisfies the "CSAF Direct Producer" conformance profile if the analysis tool:

* satisfies the "CSAF Producer" conformance profile.
* additionally satisfies those normative requirements in section [sec](#schema-elements) that are designated as applying to "direct producers" or
  to "analysis tools".
* does not emit any objects, properties, or values which, according to section [sec](#schema-elements),
  are intended to be produced only by converters.

### Conformance Clause 4: CSAF Converter

A converter satisfies the “CSAF Converter” conformance profile if the converter:

* satisfies the "CSAF Producer" conformance profile.
* additionally satisfies those normative requirements in section [sec](#schema-elements) that are designated as applying to converters.
* does not emit any objects, properties, or values which, according to section [sec](#schema-elements),
  are intended to be produced only by direct producers.

### Conformance Clause 5: CVRF CSAF Converter

A program satisfies the "CVRF CSAF Converter" conformance profile if the program fulfills the following two groups of requirements:

Firstly, the program:

* satisfies the "CSAF Producer" conformance profile.
* takes only CVRF documents as input.
* outputs a warning that an additional property was detected and not converted if it detects an additional property in the input.
  The CVRF CSAF Converter SHALL ignore that additional property during the conversion.
* additionally satisfies the normative requirements given below.

Secondly, the program fulfills the following for all items of:

* value type `string` with format `date-time`: If the value contains a `60` in the seconds place, the CVRF CSAF Converter MUST replace the seconds
  and their fractions with `59.999999`.
  In addition, the converter outputs a warning that leap seconds are now prohibited in CSAF and the value has been replaced.
  The CVRF CSAF Converter SHOULD indicate in such warning message whether the value was a valid leap second or not.
* type `/$defs/branches_t`:
  * If any `prod:Branch` instance has the type `Legacy`, `Realm`, or `Resource`,
    the CVRF CSAF Converter MUST replace those with the category `product_name`.
    In addition, the converter outputs a warning that those types do not exist in CSAF 2.1 and have been replaced with the category `product_name`.

    > There is a chance, that this replacement is incorrect or another category is a better fit.
    > Users of the converter are advised to check the content of such documents to make sure the conversion is correct or at least not misleading.

  * If any `Branch Type` appears multiple times along a path under `/prod:ProductTree/prod:Branch` and the `Branch Type` does not map to
    an excepted category according to test [sec](#stacked-branch-categories), the CVRF CSAF Converter MUST try to convert the data into
    a valid product tree by applying the following steps to the path:
    1. If the stacked `Branch Type` is `Vendor`, the vendor items named `Open Source`, `NOASSERTION` `undefined` and `unknown`
       (white space, dash, hyphen, minus, underscore and case insensitive) MUST be removed.
    2. If the stacked `Branch Type` is `Product Version` and the item directly before the first `Product Version` is a `Product Name`:
       * the category of the original `Product Name` item MUST be changed to `product_family` and
       * the category of the first `Product Version` item MUST be changed to `product_name` and
       * the value of the newly created `product_family` item MUST be prepended at the value of the newly created `product_name` item.

    If the CVRF CSAF Converter is able to create a valid product tree,
    it MUST output a warning that an invalid product tree with stacked branch types was detected and resolved.
    Such a warning MUST include the invalid path as well as the branch types that were present multiple times.

    > A tool MAY provide a non-default option to suppress this conversion step.

    If the CVRF CSAF Converter is unable to create a valid product tree,
    it MUST output an error that an invalid product tree with stacked branch types was detected and could not be resolved.
    Such a error MUST include the invalid path as well as the branch types that were present multiple times.

    > A tool MAY provide a non-default option to output the invalid document.

* type `/$defs/version_t`: If any element doesn't match the semantic versioning,
  replace the all elements of type `/$defs/version_t` with the corresponding integer version.
  For that, CVRF CSAF Converter sorts the items of `/document/tracking/revision_history` by `number` ascending according to the rules of CVRF.
  Then, it replaces the value of `number` with the index number in the array (starting with 1).
  The value of `/document/tracking/version` is replaced by value of `number` of the corresponding revision item.
  The match MUST be calculated by the original values used in the CVRF document.
  If this conversion was applied, for each Revision the original value of `cvrf:Number` MUST be set as `legacy_version` in the converted document.
* `/document/acknowledgments[]/organization` and `/vulnerabilities[]/acknowledgments[]/organization`:
  If more than one `cvrf:Organization` instance is given, the CVRF CSAF Converter converts the first one into the `organization`.
  In addition, the converter outputs a warning that information might be lost during conversion of document or vulnerability acknowledgment.
* `/document/category`:
  * If the `cvrf:DocumentType` is Security Advisory (case-insensitive), the CVRF CSAF Converter MUST try to convert the data
    into a valid CSAF Document in this profile according to CSAF 2.1.

    > A tool MAY offer rules to create the missing fixed products from version ranges, if applicable.

    If the CVRF CSAF Converter is unable to create a valid CSAF 2.1 Document according to the profile, it SHALL set the `category` value to
    `csaf_deprecated_security_advisory`.
  * If one or more CVRF elements containing an `xml:lang` attribute exist and their value is English or
    the document language of the CVRF document is unspecified,
    the following rules apply:
    * If the `cvrf:DocumentTitle` starts with the string `Superseded` or the `cvrf:DocumentType` starts with `Superseded` (case-insensitive),
      the CVRF CSAF Converter MUST try to convert all data into a valid CSAF Document in the profile "Superseded" according to CSAF 2.1.
    * If the `cvrf:DocumentTitle` starts with the string `Withdrawn` or the `cvrf:DocumentType` starts with `Withdrawn` (case-insensitive),
      the CVRF CSAF Converter MUST try to convert all data into a valid CSAF Document in the profile "Withdrawn" according to CSAF 2.1.

    > A tool MAY provide a non-default option to remove or transform certain or all elements the hinder the creation of a valid CSAF Document according
    > to the profile.

    > A tool MAY support this detection for other languages.

    If the CVRF CSAF Converter is unable to create a valid CSAF 2.1 Document according to the profile, it SHALL set the `category`
    according to the conversion rules and output a warning a potentially withdrawn CSAF Document was created which would result in an invalid CSAF.
* `/document/lang`: If one or more CVRF elements containing an `xml:lang` attribute exist and contain the exact same value,
  the CVRF CSAF Converter converts this value into `lang`.
  If the values of `xml:lang` attributes are not equal, the CVRF CSAF Converter outputs a warning that the language could not be
  determined and possibly a document with multiple languages was produced.
  In addition, it SHOULD also present all values of `xml:lang` attributes as a set in the warning.
* `/document/license_expression`: If any `cvrf:Note` item with `Type` `Legal Disclaimer` contains a valid SPDX license expression,
  the CVRF CSAF Converter SHALL convert this value into `license_expression`.
  In addition, the converter outputs an information that license expression was found and set as document license expression.
* `/document/notes`: If any `cvrf:Note` item contains one of the `category` and `title` combinations specified in [sec](#document-property-notes),
  where the `title` is extended, the CVRF CSAF Converter SHALL try to identify whether that extension is a specific product name, version or family.
  In such case, the CVRF CSAF Converter SHALL try to add the corresponding products to the note item and output a warning that a potential product
  specific note has been discovered and products have been assigned to it.
  Such warning MUST also include the note and the assigned products.
  If the CVRF CSAF Converter is unable to create a valid object, it MUST remove the reference to the products and output a warning that a potential
  product specific note has been discovered and no products could been assigned to it.
* `/document/publisher/name` and `/document/publisher/namespace`:
  Sets the value as given in the configuration of the program or the corresponding argument the program was invoked with.
  If values from both sources are present, the program SHOULD prefer the latter one.
  The program SHALL NOT use hard-coded values.
* `/document/tracking/id`: If the element `cvrf:ID` contains any newline sequence or leading or trailing white space,
  the CVRF CSAF Converter removes those characters.
  In addition, the converter outputs a warning that the ID was changed.
* `/product_tree/relationships[]`: If more than one `prod:FullProductName` instance is given,
  the CVRF CSAF Converter converts the first one into the `full_product_name`.
  In addition, the converter outputs a warning that information might be lost during conversion of product relationships.
* `/vulnerabilities[]/cwes[]`:
  * The CVRF CSAF Converter MUST remove all preceding and trailing white space from the `name`.
  * The CVRF CSAF Converter MUST determine the CWE specification version the given CWE was selected from by
    using the latest version that matches the `id` and `name` exactly and was published prior to the value of
    `/document/tracking/current_release_date` of the source document.
    If no such version exist, the first matching version published after the value of `/document/tracking/current_release_date`
    of the source document SHOULD be used.

    > This is done to create a deterministic conversion.

    If the CWE does not match at all, the CVRF CSAF Converter MUST omit this CWE and output a warning that an invalid CWE was found and has
    been removed.
  * If a `vuln:CWE` instance refers to a CWE category or view, the CVRF CSAF Converter MUST omit this instance and output a
    warning that this CWE has been removed as its usage is not allowed in vulnerability mappings.
* `/vulnerabilities[]/disclosure_date`: If a `vuln:ReleaseDate` was given, the CVRF CSAF Converter MUST convert its value into the `disclosure_date` element.
* `/vulnerabilities[]/ids`: If a `vuln:ID` element is given, the CVRF CSAF Converter converts it into the first item of the `ids` array.
* `/vulnerabilities[]/metrics[]`:
  * For any CVSS v4 element, the CVRF CSAF Converter MUST compute the `baseSeverity` from the `baseScore` according to
    the rules of the applicable CVSS standard. (CSAF CVRF v1.2 predates CVSS v4.0.)
  * For any CVSS v3 element, the CVRF CSAF Converter MUST compute the `baseSeverity` from the `baseScore` according to
    the rules of the applicable CVSS standard.
  * If no `product_id` is given, the CVRF CSAF Converter appends all Product IDs which are listed under `../product_status` in
    the arrays `known_affected`, `first_affected` and `last_affected`.
    If none of these arrays exist, the CVRF CSAF Converter outputs an error that no matching Product ID was found for this score element.
  * If a `vectorString` is missing, the CVRF CSAF Converter outputs an error that the CVSS element could not be converted as
    the CVSS vector was missing.
    A CVRF CSAF Converter MAY offer a configuration option to delete such elements.
  * If there are CVSS v3.0 and CVSS v3.1 Vectors available for the same product, the CVRF CSAF Converter discards
    the CVSS v3.0 information and provide in CSAF only the CVSS v3.1 information.
  * To determine, which minor version of CVSS v3 is used and to evaluate a CVSS v4 that was wrongly inserted in a CVSS v3 element,
    the CVRF CSAF Converter uses the following steps:
    1. Retrieve the CVSS version from the CVSS vector, if present.

        *Example 1:*

        ```
          CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H => 3.1
        ```

    2. Retrieve the CVSS version from the CVSS element's namespace, if present.
       The CVRF CSAF Converter outputs a warning that this value was guessed from the element's namespace.

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
       The CVRF CSAF Converter outputs a warning that this value was guessed from the global namespace.
       If more than one CVSS namespace is present and the element is not clearly defined via the namespace,
       this step MUST be skipped without a decision.

        *Example 4:*

        ```
          xmlns:cvssv3="https://www.first.org/cvss/cvss-v3.0.xsd" => 3.0
        ```

    4. Retrieve the CVSS version from a config value, which defaults to `3.0`.
       (As CSAF CVRF v1.2 predates CVSS v3.1.) The CVRF CSAF Converter outputs a warning that this value was taken from the config.
* `/vulnerabilities[]/metrics[]/content/cvss_v4`: If an external reference in the vulnerability linking to the official FIRST.org CVSS v4.0 calculator exists,
  the CVRF CSAF Converter MUST convert the vector given in the fragment into a `cvss_v4` object linked to all affected products of the vulnerability.

  > A tool MAY implement an option to suppress this conversion.

  If the CVRF CSAF Converter is unable to construct a valid object with the information given, the CVRF CSAF Converter SHALL
  remove the invalid `cvss_v4` object and output a warning that the automatic conversion of the CVSS v4.0 reference failed.
  Such warning SHOULD include the specific error that occurred.
* `/vulnerabilities[]/notes`: If any `vuln:Note` item contains one of the `category` and `title` combinations specified in
  [sec](#vulnerabilities-property-notes), where the `title` is extended, the CVRF CSAF Converter SHALL try to identify whether that extension is
  a specific product name, version or family.
  In such case, the CVRF CSAF Converter SHALL try to add the corresponding products to the note item and output a warning that a potential product
  specific note has been discovered and products have been assigned to it.
  Such warning MUST also include the note and the assigned products.
  If the CVRF CSAF Converter is unable to create a valid object, it MUST remove the reference to the products and output a warning that a potential
  product specific note has been discovered and no products could been assigned to it.
* `/vulnerabilities[]/remediations[]`:
  * If neither `product_ids` nor `group_ids` are given, the CVRF CSAF Converter appends all Product IDs which are listed under
    `../product_status` in the arrays `known_affected`, `first_affected` and `last_affected` into `product_ids`.
    If none of these arrays exist, the CVRF CSAF Converter outputs an error that no matching Product ID was found for this remediation element.
  * The CVRF CSAF Converter MUST convert any remediation with the type `Vendor Fix` into the category `optional_patch` if the product in
    question is in one of the product status groups "Not Affected" or "Fixed" for this vulnerability.
    Otherwise, the category `vendor_fix` MUST be set.
    If multiple products are associated with the remediation - either directly or through a product group - and the products belong to
    different product status groups, the CVRF CSAF Converter MUST duplicate the remediation, change the category in one instance
    to `optional_patch` and distribute the products accordingly as stated by the conversion rule.
  * The CVRF CSAF Converter MUST convert any remediation with the type `None Available` into the category `fix_planned`
    if the product in question is also listed in a remediation of the type `Vendor Fix` with a `Date` in the future or no `Date` at all.
    Consequently, the product MUST be removed from the remediation of the category `vendor_fix`.
    If it was the last product in that remediation, the remediation MUST be removed.
  * The CVRF CSAF Converter MUST remove any product from a remediation with the type `None Available`
    if the product in question is also listed in a remediation of the type `Vendor Fix` with a `Date` in the past or to the exact same time.
    If it was the last product in that remediation, the remediation MUST be removed.
  * In any other case, the CVRF CSAF Converter MUST preserve the product in the remediation of the category `none_available`.
  * The CVRF CSAF Converter MUST output a warning if a remediation was added, deleted or the value of the category was changed,
    including the products it was changed for.
* The CVRF CSAF Converter SHALL provide the JSON path where the warning occurred together with the warning.

### Conformance Clause 6: CSAF Content Management System

A CSAF Content Management System satisfies the "CSAF Content Management System" conformance profile if the content management system:

* satisfies the "CSAF Producer" conformance profile.
* satisfies the "CSAF Viewer" conformance profile.
* provides at least the following management functions:

  * create new CSAF Documents
  * prefill CSAF Documents based on values given in the configuration (see below)
  * create a new version of an existing CSAF Document
  * checkout old versions of a CSAF Document
  * show all differences between versions of a CSAF Document
  * list all CSAF Documents within the system
  * delete CSAF Documents from the system
  * review CSAF Documents in the system
  * approve CSAF Documents
  * search for CSAF Documents by values of required fields at `document`-level or their children within the system
  * search for CSAF Documents by values of `cve` within the system
  * search for CSAF Documents based on properties of `product_tree`
  * filter on all properties which it is required to search for
  * export of CSAF Documents
  * show an audit log for each CSAF Document
  * identify the latest version of CSAF Documents with the same `/document/tracking/id`
  * suggest a `/document/tracking/id` based on the given configuration.
  * track of the version of CSAF Documents automatically and increment according to the versioning scheme
    (see also subsections of [sec](#version-type)) selected in the configuration.
  * check that the document version is set correctly based on the changes in comparison to the previous version
    (see also subsections of [sec](#version-type)).
  * suggest to use the document status `interim` if a CSAF Document is updated more frequent than the given threshold in
    the configuration (default: `3` weeks)
  * suggest to publish a new version of the CSAF Document with the document status `final` if the document status was
    `interim` and no new release has be done during the given threshold in the configuration (default: `6` weeks)

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
* provides an API to retrieve all CSAF Documents which are currently in the status published.
* optionally provides an API to import or create new advisories from outside systems (e.g. bug tracker, CVD platform,...).
* provides a user management and support at least the following roles:

  * _Registered_: Able to see all published CSAF Documents (but only in the published version).
  * _Author_: inherits _Registered_ permissions and also can Create and Edit Own (mostly used for automated creation, see above)
  * _Editor_: inherits _Author_ permissions and can Edit (mostly used in PSIRT)
  * _Publisher_: inherits _Editor_ permissions and can Change state and Review any (mostly used as HEAD of PSIRT or team lead)
  * _Reviewer_: inherits _Registered_ permissions and can Review advisories assigned to him (might be a subject matter expert or management)
  * _Manager_: inherits _Publisher_ permissions and can Delete; User management up to _Publisher_
  * _Administrator_: inherits _Manager_ permissions and can Change the configuration

* may use groups to support client separation (multitenancy) and therefore restrict the roles to actions within their group.
  In this case, there MUST be a _Group configurator_ which is able to change the values which are used to prefill fields in
  new advisories for that group. He might also do the user management for the group up to a configured level.
* prefills the following fields in new CSAF Documents with the values given below or based on the templates from configuration:

  * `/$schema` with the value prescribed by the schema
  * `/document/csaf_version` with the value prescribed by the schema
  * `/document/lang`
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

* When updating an existing CSAF Document:
  
  * prefills all fields which have be present in the existing CSAF Document
  * adds a new item in `/document/tracking/revision_history[]`
  * updates the following fields with the values given below or based on the templates from configuration:
    * `/$schema` with the value prescribed by the schema
    * `/document/csaf_version` with the value prescribed by the schema
    * `/document/lang`
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

### Conformance Clause 7: CSAF Post-Processor

A CSAF Post-Processor satisfies the "CSAF Post-Processor" conformance profile if the post-processor:

* satisfies the "CSAF Consumer" conformance profile.
* satisfies the "CSAF Producer" conformance profile.
* additionally satisfies those normative requirements in section [sec](#schema-elements) that are designated as applying to post-processors.

### Conformance Clause 8: CSAF Modifier

A program satisfies the "CSAF Modifier" conformance profile if the program fulfills the two following groups of requirements:

The program:

* satisfies the "CSAF Post-Processor" conformance profile.
* adds, deletes or modifies at least one property, array, object or value of a property or item of an array.
* does not emit any objects, properties, or values which, according to section [sec](#conformance),
  are intended to be produced only by CSAF Translators.
* satisfies the normative requirements given below.

The resulting modified document:

* does not have the same `/document/tracking/id` as the original document.
  The modified document can use a completely new `/document/tracking/id` or compute one by appending the original `/document/tracking/id` as
  a suffix after an ID from the naming scheme of the issuer of the modified version.
  It SHOULD NOT use the original `/document/tracking/id` as a prefix.
* includes a reference to the original advisory as first element of the array `/document/references[]`.

### Conformance Clause 9: CSAF Translator

A program satisfies the "CSAF Translator" conformance profile if the program fulfills the two following groups of requirements:

The program:

* satisfies the "CSAF Post-Processor" conformance profile.
* translates at least one value.
* preserves the same semantics and form across translations.
* satisfies the normative requirements given below and does not add or remove other elements than required below.

The resulting translated document:

* does not use the same `/document/tracking/id` as the original document.
  The translated document can use a completely new `/document/tracking/id` or compute one by using the original `/document/tracking/id` as
  a prefix and adding an ID from the naming scheme of the issuer of the translated version.
  It SHOULD NOT use the original `/document/tracking/id` as a suffix.
  If an issuer uses a CSAF Translator to publish his advisories in multiple languages they MAY use the combination of
  the original `/document/tracking/id` and translated `/document/lang` as a `/document/tracking/id` for the translated document.

  > Note that the term "publish" is used in this conformance profile independent of whether the specified target group is the public
    or a closed group.

* provides the `/document/lang` property with a value matching the language of the translation.
* provides the `/document/source_lang` to contain the language of the original document (and SHOULD only be set by CSAF Translators).
* has the value `translator` set in `/document/publisher/category`
* includes a reference to the original advisory as first element of the array `/document/references[]`.
* MAY contain translations for elements in arrays of `references_t` after the first element.
  However, it MUST keep the original URLs as references at the end.

### Conformance Clause 10: CSAF Consumer

A processor satisfies the "CSAF Consumer" conformance profile if the processor:

* reads CSAF Documents and interprets them according to the semantics defined in section [sec](#schema-elements) and [sec](#additional-conventions).
* satisfies those normative requirements in section [sec](#schema-elements), [sec](#additional-conventions) and
  [sec](#safety-security-and-data-protection-considerations) that are designated as applying to CSAF Consumers.

### Conformance Clause 11: CSAF Viewer

A viewer satisfies the "CSAF Viewer" conformance profile if the viewer fulfills the two following groups of requirements:

The viewer:

* satisfies the "CSAF Consumer" conformance profile.
* satisfies those normative requirements in section [sec](#schema-elements), [sec](#additional-conventions) and
  [sec](#safety-security-and-data-protection-considerations) that are designated as applying to CSAF Viewers.
* satisfies the normative requirements given below.

For each CVSS-Score in `/vulnerabilities[]/metrics[]` the viewer:

* preferably shows the `vector` if there is an inconsistency between the `vector` and any other sibling attribute.
* SHOULD prefer the item of `metrics[]` for each `product_id` which originates from the document author (and therefore has no property `source`)
  and has the highest CVSS Base Score and newest CVSS version (in that order) if a `product_id` is listed in more than one item of `metrics[]`.

### Conformance Clause 12: CSAF Management System

A CSAF Management System satisfies the "CSAF Management System" conformance profile if the management system:

* satisfies the "CSAF Viewer" conformance profile.
* provides at least the following management functions:
  * add new CSAF Documents (e.g. from file system or URL) to the system
  * list all CSAF Documents within the system
  * delete CSAF Documents from the system
  * comment on CSAF Documents in the system
  * mark CSAF Documents as read in the system
  * search for CSAF Documents by values of required fields at `document`-level or their children within the system
  * search for CSAF Documents by values of `cve` within the system
  * search for CSAF Documents based on properties of `/product_tree`
  * filter on all properties which it is required to search for
  * sort on all properties which it is required to search for
  * sort on CVSS scores and `/document/aggregate_severity/text`
* identifies the latest version of CSAF Documents with the same `/document/tracking/id`.
* is able to show the difference between `2` versions of a CSAF Document with the same `/document/tracking/id`.

### Conformance Clause 13: CSAF Asset Matching System

A CSAF Asset Matching System satisfies the "CSAF Asset Matching System" conformance profile if the asset matching system:

* satisfies the "CSAF Management System" conformance profile.
* is an asset database or connects to one.
* matches the CSAF Documents within the system to the respective assets.
  This might be done with a probability which gives the end user the chance to broaden or narrow the results.
  The process of matching is also referred to as "run of the asset matching module".
* provides for each product of the asset database a list of matched advisories.
* provides for each asset of the asset database a list of matched advisories.
* provides for each CSAF Document a list of matched product of the asset database.
* provides for each CSAF Document a list of matched asset of the asset database.
* provides for each vulnerability within a CSAF Document the option to mark a matched asset in the asset database as "not remediated",
  "remediation in progress", or "remediation done". A switch to mark all assets at once MAY be implemented.
* does not bring up a newer revision of a CSAF Document as a new match if the remediation for the matched product or asset has not changed.
* detects the usage semantic version (as described in section [sec](#version-type-semantic-versioning)).
* is able to trigger a run of the asset matching module:
  * manually:
    * per CSAF Document
    * per list of CSAF Documents
    * per asset
    * per list of assets
  * automatically:
    * when a new CSAF Document is inserted (for this CSAF Document)
    * when a new asset is inserted (for this asset)
    * when the Major version in a CSAF Document with semantic versioning changes (for this CSAF Document)

    > These also apply if more than one CSAF Document or asset was added.
    > To reduce the computational efforts the runs can be pooled into one run which fulfills all the tasks at once (batch mode).

  * Manually and automatically triggered runs SHOULD NOT be pooled.
* provides at least the following statistics for the count of assets:
  * matching that CSAF Document at all
  * marked with a given status

### Conformance Clause 14: CSAF Basic Validator

A program satisfies the "CSAF Basic Validator" conformance profile if the program:

* reads documents and performs a check against the JSON schema,
  including also the format validation (cf. section [sec](#format-validation)).
* performs all tests of the preset `mandatory` as given in section [sec](#presets-defined-through-test-subsections).
* does not change the CSAF Documents.
* satisfies those normative requirements in section [sec](#presets) that are designated as applying to CSAF Validators.

A CSAF Basic Validator MAY provide one or more additional functions:

* Only run one or more selected mandatory tests.
* Apply quick fixes as specified in the standard.
* Apply additional quick fixes as implemented by the vendor.

### Conformance Clause 15: CSAF Extended Validator

A CSAF Basic Validator satisfies the "CSAF Extended Validator" conformance profile if the CSAF Basic Validator:

* satisfies the "CSAF Basic Validator" conformance profile.
* additionally performs all tests of the preset `recommended` as given in section [sec](#presets-defined-through-test-subsections).

A CSAF Extended Validator MAY provide an additional function to only run one or more selected recommended tests.

### Conformance Clause 16: CSAF Full Validator

A CSAF Extended Validator satisfies the "CSAF Full Validator" conformance profile if the CSAF Extended Validator:

* satisfies the "CSAF Extended Validator" conformance profile.
* additionally performs all tests of the preset `informative` as given in section [sec](#presets-defined-through-test-subsections).
* provides an option to additionally use a custom dictionary for test [sec](#spell-check).

A CSAF Full Validator MAY provide an additional function to only run one or more selected informative tests.

### Conformance Clause 17: CSAF SBOM Matching System

A CSAF SBOM Matching System satisfies the "CSAF SBOM Matching System" conformance profile if the SBOM matching system:

* satisfies the "CSAF Management System" conformance profile.
* is an SBOM database or connects to one.

  > A repository or any other location that can be queried for SBOMs and their content is also considered an SBOM database.
* matches the CSAF Documents within the system to the respective SBOM components.
  This might be done with a probability which gives the user the chance to broaden or narrow the results.
  The process of matching is also referred to as "run of the SBOM matching module".
* provides for each SBOM of the SBOM database a list of matched advisories.
* provides for each SBOM component of the SBOM database a list of matched advisories.
* provides for each CSAF Document a list of matched SBOMs of the SBOM database.
* provides for each CSAF Document a list of matched SBOM components of the SBOM database.
* provides for each vulnerability within a CSAF Document the option to mark a matched SBOM component in the SBOM database as "not remediated",
  "remediation in progress", or "remediation done".
  A switch to mark all SBOM component at once MAY be implemented.
* does not bring up a newer revision of a CSAF Document as a new match if the remediation for the matched SBOM or SBOM component has not changed.
* detects the usage semantic version (as described in section [sec](#version-type-semantic-versioning)).
* is able to trigger a run of the SBOM matching module:
  * manually:
    * per CSAF Document
    * per list of CSAF Documents
    * per SBOM component
    * per list of SBOM components
  * automatically:
    * when a new CSAF Document is inserted (for this CSAF Document)
    * when a new SBOM component is inserted (for this SBOM component)
    * when the Major version in a CSAF Document with semantic versioning changes (for this CSAF Document)

    > These also apply if more than one CSAF Document or SBOM component was added.
    > To reduce the computational efforts the runs can be pooled into one run which fulfills all the tasks at once (batch mode).

  > Manually and automatically triggered runs should not be pooled.

* provides at least the following statistics for the count of SBOM component:
  * matching that CSAF Document at all
  * marked with a given status

### Conformance Clause 18: CSAF 2.0 to CSAF 2.1 Converter{#conformance-clause-18-csaf-2-0-to-csaf-2-1-converter}

A program satisfies the "CSAF 2.0 to CSAF 2.1 Converter" conformance profile if the program fulfills the following two groups of requirements:

Firstly, the program:

* satisfies the "CSAF Producer" conformance profile.
* takes only CSAF 2.0 Documents as input.
* outputs a warning that an additional property was detected and not converted if it detects an additional property in the input.
  The CSAF 2.0 to CSAF 2.1 Converter SHALL ignore that additional property during the conversion.
* additionally satisfies the normative requirements given below.

Secondly, the program fulfills the following for all items of:

* value type `string` with format `date-time`: If the value contains a `60` in the seconds place, the CSAF 2.0 to CSAF 2.1 Converter MUST replace
  the seconds and their fractions with `59.999999`.
  In addition, the converter outputs a warning that leap seconds are now prohibited in CSAF and the value has been replaced.
  The CSAF 2.0 to CSAF 2.1 Converter SHOULD indicate in such warning message whether the value was a valid leap second or not.
* type `/$defs/branches_t`:
  * If a branch item uses the category `legacy`,
    the CSAF 2.0 to CSAF 2.1 Converter MUST replace it with the category `product_name`.
    In addition, the converter outputs a warning that this type does not exist in CSAF 2.1 and have been replaced with the category `product_name`.

    > There is a chance, that this replacement is incorrect or another category is a better fit.
    > Users of the converter are advised to check the content of such documents to make sure the conversion is correct or at least not misleading.
  
  * If any branch category appears multiple times along a path under `/product_tree/branches` and the category is not an excepted one according to
    test [sec](#stacked-branch-categories), the CSAF 2.0 to CSAF 2.1 Converter MUST try to convert the data into a valid product tree by
    applying the following steps to the path:
    1. If the stacked branch category is `vendor`, the vendor items named `Open Source`, `NOASSERTION`, `undefined` and `unknown`
       (white space, dash, hyphen, minus, underscore and case insensitive) MUST be removed.
    2. If the stacked branch category is `product_version` and the item directly before the first `product_version` is a `product_name`:
       * the category of the original `product_name` item MUST be changed to `product_family` and
       * the category of the first `product_version` item MUST be changed to `product_name` and
       * the value of the newly created `product_family` item MUST be prepended at the value of the newly created `product_name` item.

    If the CSAF 2.0 to CSAF 2.1 Converter is able to create a valid product tree,
    it MUST output a warning that an invalid product tree with stacked branch categories was detected and resolved.
    Such a warning MUST include the invalid path as well as the branch categories that were present multiple times.

    > A tool MAY provide a non-default option to suppress this conversion step.

    If the CSAF 2.0 to CSAF 2.1 Converter is unable to create a valid product tree,
    it MUST output an error that an invalid product tree with stacked branch categories was detected and could not be resolved.
    Such a error MUST include the invalid path as well as the branch categories that were present multiple times.

    > A tool MAY provide a non-default option to output the invalid document.

  * If the branch categories `product_version` and `product_version_range` appear along a path under `/product_tree/branches`,
    the CSAF 2.0 to CSAF 2.1 Converter MUST try to convert the data into a valid product tree by
    applying the following steps to the path:

    1. If the branch category `product_version` occurs before the `product_version_range` and the item directly before the first
       `product_version` is a `product_name`:
       * the category of the original `product_name` item MUST be changed to `product_family` and
       * the category of the first `product_version` item MUST be changed to `product_name` and
       * the value of the newly created `product_family` item MUST be prepended at the value of the newly created `product_name` item.
    2. If the branch category `product_version` occurs before the `product_version_range` and the item directly before the first
       `product_version` is a `product_family`:
       * the category of the first `product_version` item MUST be changed to `product_name` and
       * the value of the direct ancestor `product_family` item MUST be prepended at the value of the newly created `product_name` item.

    If the CSAF 2.0 to CSAF 2.1 Converter is able to create a valid product tree,
    it MUST output a warning that an invalid product tree with branch categories `product_version` and `product_version_range` in
    one path was detected and resolved.
    Such a warning MUST include the invalid path as well as the branch category items changed.

    > A tool MAY provide a non-default option to suppress this conversion step.

    If the CSAF 2.0 to CSAF 2.1 Converter is unable to create a valid product tree,
    it MUST output an error that an invalid product tree with branch categories `product_version` and `product_version_range` in
    one path was detected and could not be resolved.
    Such a error MUST include the invalid path as well as the branch category items.

    > A tool MAY provide a non-default option to output the invalid document.

  * If the value of `name` of an item categorized as `product_version_range` and contains an upper open ended product version range,
    the CSAF 2.0 to CSAF 2.1 Converter MUST try to convert the data into a valid product tree by
    applying the following steps to the path:

    1. If value of `name` consists only of one version constraint:
       * the category of the original `product_version_range` item MUST be changed to `product_version` and
       * the version MUST be extracted from the original value and set as new value of `name`.
    2. If value of `name` consists of more than one version constraint and the upper open range is the last version constraint:
       * the category of the original `product_version_range` item MUST be kept and
       * the value `name` MUST be converted into the product version range ending with the version the upper open ended product version
         if that does not change the inclusion boundaries.

    If the CSAF 2.0 to CSAF 2.1 Converter is able to create a valid product tree,
    it MUST output a warning that an invalid product tree with an upper open ended product version range in
    one path was detected and resolved.
    Such a warning MUST include the invalid path as well as the original and new value.

    > A tool MAY provide a non-default option to suppress this conversion step.

    If the CSAF 2.0 to CSAF 2.1 Converter is unable to create a valid product tree,
    it MUST output an error that an invalid product tree with an upper open ended product version range in
    one path was detected and could not be resolved.
    Such a error MUST include the invalid path as well as the original and new value.

    > A tool MAY provide a non-default option to output the invalid document.

  * If the value of `name` of an item categorized as `product_version_range` contains just a single version,
    the CSAF 2.0 to CSAF 2.1 Converter MUST try to convert the data into a valid product tree by
    applying the following steps to the path:

    1. If value of `name` is in the vers format:
       * the category of the original `product_version_range` item MUST be changed to `product_version` and
       * the version MUST be extracted from the version constraint and set as new value of `name`.
    2. If value of `name` is in the vls format:
       * the category of the original `product_version_range` item MUST be changed to `product_version` and
       * the value `name` MUST be kept unchanged.

    If the CSAF 2.0 to CSAF 2.1 Converter is able to create a valid product tree,
    it MUST output a warning that an invalid product tree with a `product_version` declared as `product_version_range` in
    one path was detected and resolved.
    Such a warning MUST include the invalid path as well as value of the product version.

    > A tool MAY provide a non-default option to suppress this conversion step.

    If the CSAF 2.0 to CSAF 2.1 Converter is unable to create a valid product tree,
    it MUST output an error that an invalid product tree with a `product_version` declared as `product_version_range` in
    one path was detected and could not be resolved.
    Such a error MUST include the invalid path as well as value of the product version.

    > A tool MAY provide a non-default option to output the invalid document.

* type `/$defs/full_product_name_t/product_identification_helper/cpe`: If a CPE is invalid, the CSAF 2.0 to CSAF 2.1 Converter SHOULD removed the
  invalid value and output a warning that an invalid CPE was detected and removed. Such a warning MUST include the invalid CPE.
* type `/$defs/full_product_name_t/product_identification_helper/hashes[]/file_hashes[]/algorithm`:
  If the algorithm is known to the implementation or mentioned in this standard, the CSAF 2.0 to CSAF 2.1 Converter MUST ensure its spelling
  is exactly as prescribed by this standard.
  If the algorithm is unknown to the implementation, the CSAF 2.0 to CSAF 2.1 Converter MUST convert it to lowercase and output a warning that
  an unknown hash algorithm was detected and converted.
  Such a warning MUST include the invalid path as well as value of the algorithm.

  > A tool MAY provide a non-default option to suppress this conversion step.

* type `/$defs/full_product_name_t/product_identification_helper/hashes[]/file_hashes[]/value`: The CSAF 2.0 to CSAF 2.1 Converter MUST convert
  the value into a lowercase string.
* type `/$defs/full_product_name_t/product_identification_helper/model_number`:
  * If a model number is given that does not end on a star, the CSAF 2.0 to CSAF 2.1 Converter SHOULD add a `*` to the end and output a
    warning that a partial model number was detected and a star has been added.
    Such a warning MUST include the model number.
  * If the model number contains a `\`, the CSAF 2.0 to CSAF 2.1 Converter MUST escape it by inserting an additional `\` before the character.
  * If the model number contains multiple unescaped `*` after the conversion, the CSAF 2.0 to CSAF 2.1 Converter MUST remove the entry and
    output a warning that a model number with multiple stars was detected and removed.
    Such a warning MUST include the model number.

  > A tool MAY provide a non-default option to interpret all model numbers as complete and therefore does not add any stars.

  > A tool MAY provide a non-default option to interpret the `?` in all model numbers as part of the model number itself and therefore escape it.

  > A tool MAY provide a non-default option to interpret the `*` in all model numbers as part of the model number itself and therefore escape it.

* type `/$defs/full_product_name_t/product_identification_helper/purls`: If a `/$defs/full_product_name_t/product_identification_helper/purl` is given,
  the CSAF 2.0 to CSAF 2.1 Converter MUST convert it into the first item of the corresponding `purls` array.
* type `/$defs/full_product_name_t/product_identification_helper/serial_number`:
  * If a serial number is given that does not end on a star, the CSAF 2.0 to CSAF 2.1 Converter SHOULD add a `*` to the end and output a
    warning that a partial serial number was detected and a star has been added.
    Such a warning MUST include the serial number.
  * If the serial number contains a `\`, the CSAF 2.0 to CSAF 2.1 Converter MUST escape it by inserting an additional `\` before the character.
  * If the serial number contains multiple unescaped `*` after the conversion, the CSAF 2.0 to CSAF 2.1 Converter MUST remove the entry and
    output a warning that a serial number with multiple stars was detected and removed.
    Such a warning MUST include the serial number.

  > A tool MAY provide a non-default option to interpret all serial numbers as complete and therefore does not add any stars.

  > A tool MAY provide a non-default option to interpret the `?` in all serial numbers as part of the serial number itself and therefore escape it.

  > A tool MAY provide a non-default option to interpret the `*` in all serial numbers as part of the serial number itself and therefore escape it.

* `/$schema`: The CSAF 2.0 to CSAF 2.1 Converter MUST set property with the value prescribed by the schema.
* `/document/category`:
  * If the `category` equals `csaf_security_advisory`, the CSAF 2.0 to CSAF 2.1 Converter MUST try to convert the data into a
    valid CSAF Document in this profile according to CSAF 2.1.
    For any version range of affected products that uses the strict `<`, i.e. not `<=`, as comparator of the last version constraint, the CSAF 2.0
    to CSAF 2.1 Converter SHOULD add a new product with the version of the last constraint and add that in the appropriate places as `fixed`.
    The CSAF 2.0 to CSAF 2.1 Converter MUST output a warning that a product was added to the `product_tree` and the corresponding `/vulnerabilities[]`.
    Such warning MUST contain the full product name and its path as well as the paths of the `/vulnerabilities[]` it was added to.
    If the CSAF 2.0 to CSAF 2.1 Converter is unable to create a valid CSAF 2.1 Document according to the profile, it SHALL set the `category` value to
    `csaf_deprecated_security_advisory`.
  * If the `/document/lang` is English or unspecified, the following rules apply:
    * If the `/document/title` starts with the string `Superseded` or the `/document/category` has the value `Superseded` (case-insensitive),
      the CSAF 2.0 to CSAF 2.1 Converter MUST try to convert all data into a valid CSAF Document in the profile "Superseded" according to CSAF 2.1.
    * If the `/document/title` starts with the string `Withdrawn` or the `/document/category` has the value `Withdrawn` (case-insensitive),
      the CSAF 2.0 to CSAF 2.1 Converter MUST try to convert all data into a valid CSAF Document in the profile "Withdrawn" according to CSAF 2.1.
 
    > A tool MAY provide a non-default option to remove or transform certain or all elements the hinder the creation of a valid CSAF Document according
    > to the profile.

    > A tool MAY support this detection for other languages.

    If the CSAF 2.0 to CSAF 2.1 Converter is unable to create a valid CSAF 2.1 Document according to the profile, it SHALL set the `category`
    of the original CSAF Document and output a warning a potentially withdrawn CSAF Document was created which would result in an invalid CSAF.
* `/document/csaf_version`: The CSAF 2.0 to CSAF 2.1 Converter MUST update the value to `2.1`.
* `/document/distribution/tlp/label`: If a TLP label is given, the CSAF 2.0 to CSAF 2.1 Converter MUST convert it according to the table below:
  
  | CSAF 2.0 (using TLP v1.0) | CSAF 2.1 (using TLP v2.0) |
  |---------------------------|---------------------------|
  | `TLP:WHITE`               | `TLP:CLEAR`               |
  | `TLP:GREEN`               | `TLP:GREEN`               |
  | `TLP:AMBER`               | `TLP:AMBER`               |
  | `TLP:RED`                 | `TLP:RED`                 |

  If `/document/distribution/text` contains the string `TLP v2.0: TLP:<ValidTLPLabel>`, the CSAF 2.0 to CSAF 2.1 Converter SHOULD provide an
  option to use this label instead. If the TLP label changes through such conversion in a way that is not reflected in the table above, the
  the CSAF 2.0 to CSAF 2.1 Converter MUST output a warning that the TLP label was taken from the distribution text. Such a warning MUST include
  both values: the converted one based on the table and the one from the distribution text.

  > This is a common case for CSAF 2.0 Documents labeled as `TLP:RED` but actually intended to be `TLP:AMBER+STRICT`.

  If no TLP label was given, the CSAF 2.0 to CSAF 2.1 Converter SHOULD assign `TLP:CLEAR` and output a warning that the default TLP has been set.
* `/document/license_expression`: If any `/document/notes` item in with `category` `legal_disclaimer` contains a valid SPDX license expression,
  the CSAF 2.0 to CSAF 2.1 Converter SHALL convert this value into `license_expression`.
  In addition, the converter outputs an information that license expression was found and set as document license expression.
* `/document/notes`: If any `/document/notes` item contains one of the `category` and `title` combinations specified in
  [sec](#document-property-notes), where the `title` is extended, the CSAF 2.0 to CSAF 2.1 Converter SHALL try to identify whether that extension
  is a specific product name, version or family.
  In such case, the CSAF 2.0 to CSAF 2.1 Coverter SHALL try to add the corresponding products to the note item and output a warning that a potential product
  specific note has been discovered and products have been assigned to it.
  Such warning MUST also include the note and the assigned products.
  If the CSAF 2.0 to CSAF 2.1 Converter is unable to create a valid object, it MUST remove the reference to the products and output a warning that a potential
  product specific note has been discovered and no products could been assigned to it.
* `/document/publisher/category`: If the value is `other`, the CSAF 2.0 to CSAF 2.1 Converter SHOULD output a warning that some parties have
  been regrouped into the new value `multiplier`. An option to suppress this warning MUST exist. In addition, an option SHOULD be provided to
  set the value to `multiplier`.
* `/document/title`: If the value contains the `/document/tracking/id`, the CSAF 2.0 to CSAF 2.1 Converter MUST remove the `/document/tracking/id`
  from the `/document/title`. In addition, separating characters including but not limited to white space, colon, dash and brackets MUST be removed.
* `/vulnerabilities[]/cwes[]`:
  * The CSAF 2.0 to CSAF 2.1 Converter MUST remove all preceding and trailing white space from the `name`.
  * The CSAF 2.0 to CSAF 2.1 Converter MUST determine the CWE specification version the given CWE was selected from by
    using the latest version that matches the `id` and `name` exactly and was published prior to the value of
    `/document/tracking/current_release_date` of the source document.
    If no such version exist, the first matching version published after the value of `/document/tracking/current_release_date`
    of the source document SHOULD be used.

    > This is done to create a deterministic conversion.

    The tool SHOULD implement an option to use the latest available CWE version at the time of the conversion that still matches.

* `/vulnerabilities[]/disclosure_date`: If a `release_date` was given, the CSAF 2.0 to CSAF 2.1 Converter MUST convert its value as value
  into the `disclosure_date` element.
* `/vulnerabilities[]/metrics[]/content/cvss_v4`: If an external reference in the vulnerability linking to the official FIRST.org CVSS v4.0 calculator exists,
  the CSAF 2.0 to CSAF 2.1 Converter MUST convert the vector given in the fragment into a `cvss_v4` object linked to all affected products of the vulnerability.
  
  > A tool MAY implement an option to suppress this conversion.

  If the CSAF 2.0 to CSAF 2.1 Converter is unable to construct a valid object with the information given, the CSAF 2.0 to CSAF 2.1 Converter SHALL
  remove the invalid `cvss_v4` object and output a warning that the automatic conversion of the CVSS v4.0 reference failed.
  Such warning SHOULD include the specific error that occurred.
* `/vulnerabilities[]/metrics[]/content/ssvc_v2`: If a SSVC vector or decision points of an SSVC vector are given in an item of `notes` of the current
  vulnerability using the `title` `SSVC` and the `category` `other`, the CSAF 2.0 to CSAF 2.1 Converter MUST convert that data into the `ssvc_v2`
  object within the current vulnerability.
  If the CSAF 2.0 to CSAF 2.1 Converter is able to construct a valid object without loosing any information, the corresponding `notes` item SHALL
  be removed.
  If the CSAF 2.0 to CSAF 2.1 Converter is unable to construct a valid object with the information given, the CSAF 2.0 to CSAF 2.1 Converter SHALL
  remove the invalid `ssvc_v2` object, keep the original item of `notes` and output a warning that the automatic conversion of the SSVC data failed.
  If the CSAF 2.0 to CSAF 2.1 Converter would loose information during the conversion, the CSAF 2.0 to CSAF 2.1 Converter SHALL remove the `ssvc_v2`
  object, keep the original item of `notes` and output a warning that the automatic conversion of the SSVC data would lead to loosing information.
* `/vulnerabilities[]/notes`: If any `/vulnerabilities[]/notes` item contains one of the `category` and `title` combinations specified in
  [sec](#vulnerabilities-property-notes), where the `title` is extended, the CSAF 2.0 to CSAF 2.1 Converter SHALL try to identify whether that
  extension is a specific product name, version or family.
  In such case, the CSAF 2.0 to CSAF 2.1 Converter SHALL try to add the corresponding products to the note item and output a warning that a potential
  product specific note has been discovered and products have been assigned to it.
  Such warning MUST also include the note and the assigned products.
  If the CSAF 2.0 to CSAF 2.1 Converter is unable to create a valid object, it MUST remove the reference to the products and output a warning that a
  potential product specific note has been discovered and no products could been assigned to it.
* `/vulnerabilities[]/remediations[]`:
  * The CSAF 2.0 to CSAF 2.1 Converter MUST convert any remediation with the category `vendor_fix` into the category `optional_patch`
    if the product in question is in one of the product status groups "Not Affected" or "Fixed" for this vulnerability.
    Otherwise, the category `vendor_fix` MUST stay the same.
    If multiple products are associated with the remediation - either directly or through a product group - and the products belong to different
    product status groups, the CSAF 2.0 to CSAF 2.1 Converter MUST duplicate the remediation, change the category in one instance to `optional_patch`
    and distribute the products accordingly as stated by the conversion rule.
  * The CSAF 2.0 to CSAF 2.1 Converter MUST convert any remediation with the category `none_available` into the category `fix_planned`
    if the product in question is also listed in a remediation of the category `vendor_fix` with a `date` in the future or no `date` at all.
    Consequently, the product MUST be removed from the remediation of the category `vendor_fix`.
    If it was the last product in that remediation, the remediation MUST be removed.
  * The CSAF 2.0 to CSAF 2.1 Converter MUST remove any product from a remediation with the category `none_available`
    if the product in question is also listed in a remediation of the category `vendor_fix` with a `date` in the past or to the exact same time.
    If it was the last product in that remediation, the remediation MUST be removed.
  * In any other case, the CSAF 2.0 to CSAF 2.1 Converter MUST preserve the product in the remediation of the category `none_available`.
  * The CSAF 2.0 to CSAF 2.1 Converter MUST output a warning if a remediation was added, deleted or the value of the category was changed,
    including the products it was changed for.
* The CSAF 2.0 to CSAF 2.1 Converter SHALL provide the JSON path where the warning occurred together with the warning.

> A tool MAY implement options to convert other Markdown formats to GitHub-flavored Markdown.

> A tool MAY implement an additional, non-default option to output an invalid document that can be fixed afterwards. Solely in this case, any
> of the rules above MAY be ignored to avoid data loss.

### Conformance Clause 19: CSAF Library

A library satisfies the "CSAF Library" conformance profile if the library:

* implements all elements as data structures conforming to the syntax and semantics defined in section [sec](#format-validation),
  [sec](#date-and-time), [sec](#schema-elements), [sec](#profiles) and [sec](#additional-conventions).
* checks all elements according to the patterns provided in the JSON schema.
* has a function that checks version ranges.
* has a function that helps to create version ranges.
* provides for each element functions that allow to create, add, modify and delete that element.
* has a function that reads a CSAF Document into the data structure from a
  * file system.
  * URL.
  * data stream.
* provides function for sorting the keys and sorts the keys automatically on output.
* has a function that outputs the data structure as CSAF Document
  * on the file system.
  * as string.
  * into a data stream.
* has a function to determine the filename according to [sec](#filename) and sets the filename per default when saving a CSAF Document.
* generates a new `product_id` for each new element of type `full_product_name_t` unless an ID is given during the creation.
* generates a new `group_id` for each new element of type `product_group_id_t` unless an ID is given during the creation.
* provides a function to retrieve all elements of type `product_id_t` with its corresponding `full_product_name_t/name` and
  `full_product_name_t/product_identification_helper`.
* provides a function to retrieve all `product_identification_helper` and their mapping to elements of type `product_id_t`.
* provides a function to retrieve a VEX status mapping for all data, which includes the combination of vulnerability, product, product status
  and, where necessary according to the profile, the impact statement respectively the action statement.
* provides a function to generate a `full_product_name_t/name` with in `branches` through concatenating the `name` values separated by white space
  of the elements along the path towards this leaf.
* calculates the CVSS scores and severities for existing data for all CVSS versions.
* validates the CVSS scores and severities for existing data for all CVSS versions.

> The library MAY implement an option to retrieve the keys unsorted.

### Conformance Clause 20: CSAF Library with Basic Validation

A CSAF Library satisfies the "CSAF Library with Basic Validation" conformance profile if the CSAF Library:

* satisfies the "CSAF Library" conformance profile.
* satisfies the "CSAF Basic Validator" conformance profile.
* validates the CSAF Document before output according to the "CSAF Basic Validator" and presents the validation result accordingly.
* provide a function to validate the data structure in its current state according to the "CSAF Basic Validator" and presents the validation
  result accordingly.

A CSAF Library does not satisfies the "CSAF Library with Basic Validation" conformance profile if the CSAF Library uses an external library or
program for the "CSAF Basic Validator" part and does not enforce its presence.

### Conformance Clause 21: CSAF Library with Extended Validation

A CSAF Library satisfies the "CSAF Library with Extended Validation" conformance profile if the CSAF Library:

* satisfies the "CSAF Library" conformance profile.
* satisfies the "CSAF Extended Validator" conformance profile.
* validates the CSAF Document before output according to the "CSAF Extended Validator" and presents the validation result accordingly.
* provide a function to validate the data structure in its current state according to the "CSAF Extended Validator" and presents the validation
  result accordingly.

A CSAF Library does not satisfies the "CSAF Library with Extended Validation" conformance profile if the CSAF Library uses an external library or
program for the "CSAF Extended Validator" part and does not enforce its presence.

### Conformance Clause 22: CSAF Library with Full Validation

A CSAF Library satisfies the "CSAF Library with Extended Validation" conformance profile if the CSAF Library:

* satisfies the "CSAF Library" conformance profile.
* satisfies the "CSAF Full Validator" conformance profile.
* validates the CSAF Document before output according to the "CSAF Full Validator" and presents the validation result accordingly.
* provide a function to validate the data structure in its current state according to the "CSAF Full Validator" and presents the validation
  result accordingly.

A CSAF Library does not satisfies the "CSAF Library with Full Validation" conformance profile if the CSAF Library uses an external library or
program for the "CSAF Full Validator" part and does not enforce its presence.

### Conformance Clause 23: CSAF Downloader

A program satisfies the "CSAF Downloader" conformance profile if the program:

* conforms to the process defined in section [sec](#retrieving-rules) by executing all parts that are applicable to the given role.
* supports directory-based and ROLIE-based retrieval.
* is able to execute both steps from section [sec](#retrieving-rules) separately.
* uses a program-specific HTTP User Agent, e.g. consisting of the name and version of the program.
* satisfies those normative requirements in section [sec](#distributing-csaf-documents) that are designated as applying to CSAF Downloaders.

> A tool MAY implement an option to store CSAF Documents that fail any of the steps in section [sec](#retrieving-csaf-documents).

### Conformance Clause 24: CSAF Withdrawer

A program satisfies the "CSAF Withdrawer" conformance profile if the program:

* satisfies the "CSAF Post-Processor" conformance profile.
* keeps the original `/document/tracking/id`.
* adds a new item to the revision history stating the revision metadata of the withdrawal.
* adds the reasoning for withdrawal as specified in section [sec](#profile-7-withdrawn).
* removes the `/product_tree`.
* removes the `/vulnerabilities`.

> A tool MAY implement an option to additionally remove any element that would hinder the production of a valid CSAF.

### Conformance Clause 25: CSAF Superseder

A program satisfies the "CSAF Superseder" conformance profile if the program:

* satisfies the "CSAF Post-Processor" conformance profile.
* keeps the original `/document/tracking/id`.
* adds a new item to the revision history stating the revision metadata of the supersession.
* adds the reasoning for supersession as specified in section [sec](#profile-8-superseded).
* adds the reference to the superseding document as specified in section [sec](#profile-8-superseded).
* removes the `/product_tree`.
* removes the `/vulnerabilities`.

> A tool MAY implement an option to additionally remove any element that would hinder the production of a valid CSAF.

-------
