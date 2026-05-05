### Conformance Clause 5: CVRF CSAF Converter

A program satisfies the "CVRF CSAF Converter" conformance profile if the program fulfills the following two groups of requirements:

Firstly, the program:

* satisfies the "CSAF Producer" conformance profile.
* takes only CVRF documents as input.
* issues a warning that an additional property was detected and not converted if it detects an additional property in the input.
  Such a warning SHALL include the additional property and its path.
  The CVRF CSAF Converter SHALL ignore that additional property during the conversion.
* includes in every error and warning the relevant paths and values ​​from the original file that triggered the alert,
  unless otherwise specified in this standard.
* additionally satisfies the normative requirements given below.

Secondly, the program fulfills the following for all items of:

* value type `string` with format `date-time`: If the value contains a `60` in the seconds place, the CVRF CSAF Converter SHALL replace the seconds
  and their fractions with `59.999999`.
  In addition, the converter issues a warning that leap seconds are now prohibited in CSAF and the value has been replaced.
  The CVRF CSAF Converter SHOULD indicate in such warning message whether the value was a valid leap second or not.
* type `/$defs/branches_t`:
  * If any `prod:Branch` instance has the type `Legacy`, `Realm`, or `Resource`,
    the CVRF CSAF Converter SHALL replace those with the category `product_name`.
    In addition, the converter issues a warning that those types do not exist in CSAF 2.1 and have been replaced with the category `product_name`.

    > There is a chance, that this replacement is incorrect or another category is a better fit.
    > Users of the converter are advised to check the content of such documents to make sure the conversion is correct or at least not misleading.

  * If any `Branch Type` appears multiple times along a path under `/prod:ProductTree/prod:Branch` and the `Branch Type` does not map to
    an excepted category according to test [sec](#stacked-branch-categories), the CVRF CSAF Converter SHALL try to convert the data into
    a valid product tree by applying the following steps to the path:
    1. If the stacked `Branch Type` is `Vendor`, the vendor items named `Open Source`, `NOASSERTION` `undefined` and `unknown`
       (white space, dash, hyphen, minus, underscore and case insensitive) SHALL be removed.
    2. If the stacked `Branch Type` is `Product Version` and the item directly before the first `Product Version` is a `Product Name`:
       * the category of the original `Product Name` item SHALL be changed to `product_family` and
       * the category of the first `Product Version` item SHALL be changed to `product_name` and
       * the value of the newly created `product_family` item SHALL be prepended at the value of the newly created `product_name` item.

    If the CVRF CSAF Converter is able to create a valid product tree,
    it SHALL issue a warning that an invalid product tree with stacked branch types was detected and resolved.
    Such a warning SHALL include the invalid path as well as the branch types that were present multiple times.

    > A tool MAY provide a non-default option to suppress this conversion step.

    If the CVRF CSAF Converter is unable to create a valid product tree,
    it SHALL issue an error that an invalid product tree with stacked branch types was detected and could not be resolved.
    Such a error SHALL include the invalid path as well as the branch types that were present multiple times.

    > A tool MAY provide a non-default option to output the invalid document.
* type `/$defs/full_product_name_t/product_identification_helper/cpe`: If a CPE is invalid,
  the CVRF CSAF Converter SHOULD remove the invalid value and issue a warning that an invalid CPE was detected and removed.
* type `/$defs/version_t`: If any element doesn't match the semantic versioning,
  replace the all elements of type `/$defs/version_t` with the corresponding integer version.
  For that, CVRF CSAF Converter sorts the items of `/document/tracking/revision_history` by `number` ascending according to the rules of CVRF.
  Then, it replaces the value of `number` with the index number in the array (starting with 1).
  The value of `/document/tracking/version` is replaced by value of `number` of the corresponding revision item.
  The match SHALL be calculated by the original values used in the CVRF document.
  If this conversion was applied, for each Revision the original value of `cvrf:Number` SHALL be set as `legacy_version` in the converted document.
* `/document/acknowledgments[]/organization` and `/vulnerabilities[]/acknowledgments[]/organization`:
  If more than one `cvrf:Organization` instance is given, the CVRF CSAF Converter converts the first one into the `organization`.
  In addition, the converter issues a warning that information might be lost during conversion of document or vulnerability acknowledgment.
* `/document/category`:
  * If the `cvrf:DocumentType` is Security Advisory (case-insensitive), the CVRF CSAF Converter SHALL try to convert the data
    into a valid CSAF Document in this profile according to CSAF 2.1.

    > A tool MAY offer rules to create the missing fixed products from version ranges, if applicable.

    If the CVRF CSAF Converter is unable to create a valid CSAF 2.1 Document according to the profile, it SHALL set the `category` value to
    `csaf_deprecated_security_advisory`.
  * If one or more CVRF elements containing an `xml:lang` attribute exist and their value is English or
    the document language of the CVRF document is unspecified,
    the following rules apply:
    * If the `cvrf:DocumentTitle` starts with the string `Superseded` or the `cvrf:DocumentType` starts with `Superseded` (case-insensitive),
      the CVRF CSAF Converter SHALL try to convert all data into a valid CSAF Document in the profile "Superseded" according to CSAF 2.1.
    * If the `cvrf:DocumentTitle` starts with the string `Withdrawn` or the `cvrf:DocumentType` starts with `Withdrawn` (case-insensitive),
      the CVRF CSAF Converter SHALL try to convert all data into a valid CSAF Document in the profile "Withdrawn" according to CSAF 2.1.

    > A tool MAY provide a non-default option to remove or transform certain or all elements the hinder the creation of a valid CSAF Document according
    > to the profile.

    > A tool MAY support this detection for other languages.

    If the CVRF CSAF Converter is unable to create a valid CSAF 2.1 Document according to the profile, it SHALL set the `category`
    according to the conversion rules and issue a warning a potentially withdrawn CSAF Document was created which would result in an invalid CSAF.
* `/document/lang`: If one or more CVRF elements containing an `xml:lang` attribute exist and contain the exact same value,
  the CVRF CSAF Converter converts this value into `lang`.
  If the values of `xml:lang` attributes are not equal, the CVRF CSAF Converter issues a warning that the language could not be
  determined and possibly a document with multiple languages was produced.
  In addition, it SHOULD also present all values of `xml:lang` attributes as a set in the warning.
* `/document/license_expression`: If any `cvrf:Note` item with `Type` `Legal Disclaimer` contains valid SPDX license expressions,
  the CVRF CSAF Converter SHALL apply the following rules to the list of candidates:
  * If the list contains only one element, the CVRF CSAF Converter SHALL set this value as value of `license_expression`.
    In addition, the converter issues a warning that a license expression was found and set as the document license expression.
  * If multiple SPDX license expressions are found, the CVRF CSAF Converter issues a warning that multiple SPDX license expressions were found
    and therefore no document license expression could be determined.
    This warning SHALL include the list of all SPDX license expressions and their associated paths.

  > A tool MAY implement an option to suppress this conversion.

* `/document/notes`: If any `cvrf:Note` item contains one of the `category` and `title` combinations specified in [sec](#document-property---notes),
  where the `title` is extended, the CVRF CSAF Converter SHALL try to identify whether that extension is a specific product name, version or family.
  In such case, the CVRF CSAF Converter SHALL try to add the corresponding products to the note item and issue a warning that a potential product
  specific note has been discovered and products have been assigned to it.
  Such warning SHALL also include the note and the assigned products.
  If the CVRF CSAF Converter is unable to create a valid object, it SHALL remove the reference to the products and issue a warning that a potential
  product specific note has been discovered and no products could been assigned to it.
* `/document/publisher/name` and `/document/publisher/namespace`:
  Sets the value as given in the configuration of the program or the corresponding argument the program was invoked with.
  If values from both sources are present, the program SHOULD prefer the latter one.
  The program SHALL NOT use hard-coded values.
* `/document/tracking/id`: If the element `cvrf:ID` contains any newline sequence or leading or trailing white space,
  the CVRF CSAF Converter removes those characters.
  In addition, the converter issues a warning that the ID was changed.
* `/product_tree/product_path[]`: For each element `prod:Relationship`, the CVRF CSAF Converter SHALL apply the following rules:
  * The value of the attribute `ProductReference` is set as the value of `beginning_product_reference`.
  * The first `prod:FullProductName` instance is converted into the `full_product_name`.
    If more than one `prod:FullProductName` instance is given,
    the CVRF CSAF Converter SHALL issue a warning that information might be lost during conversion of product paths.
    Such warning SHOULD contain the values of all `prod:FullProductName` instances skipped.
  * The CVRF CSAF Converter constructs the first item of `subpaths` by converting the value of `RelationType` into `category`
    and the value of the attribute `RelatesToProductReference` into `next_product_reference`.

    > A tool MAY provide an option to collapse chained product path elements into the appropriate number of product path elements,
    > if this is possible without the loss of correct information.
    > Usually, collapsing chained product paths is not possible if
    > * a product (type: `full_product_name_t`) defined by a product path element in the chain is referenced in other parts of the document, or
    > * a product (type: `full_product_name_t`) defined by a product path element in the chain contains a `product_identification_helper`
    >   element.
    > For examples, see appendix [sec](#collapsing-product-paths).

* `/vulnerabilities[]/cwes[]`:
  * The CVRF CSAF Converter SHALL remove all preceding and trailing white space from the `name`.
  * The CVRF CSAF Converter SHALL determine the CWE specification version the given CWE was selected from by
    using the latest version that matches the `id` and `name` exactly and was published prior to the value of
    `/document/tracking/current_release_date` of the source document.
    If no such version exist, the first matching version published after the value of `/document/tracking/current_release_date`
    of the source document SHOULD be used.

    > This is done to create a deterministic conversion.

    If the CWE does not match at all, the CVRF CSAF Converter SHALL omit this CWE and issue a warning that an invalid CWE was found and has
    been removed.
  * If a `vuln:CWE` instance refers to a CWE category or view, the CVRF CSAF Converter SHALL omit this instance and issues a
    warning that this CWE has been removed as its usage is not allowed in vulnerability mappings.
* `/vulnerabilities[]/disclosure_date`: If a `vuln:ReleaseDate` was given,
  the CVRF CSAF Converter SHALL convert its value into the `disclosure_date` element.
* `/vulnerabilities[]/ids`: If a `vuln:ID` element is given, the CVRF CSAF Converter converts it into the first item of the `ids` array.
  Then, the CVRF CSAF Converter SHALL execute the following steps at the converted object:
  * If an `system_name` was given, the CVRF CSAF Converter SHALL test whether it belongs to a registered
  vulnerability ID system in RVISC.
  * If the `system_name` belongs to an RVISC entry, the CVRF CSAF Converter SHALL execute
    test [sec](#matching-text-for-registered-id-system).
    * If the test passes, no further action is needed.
    * If the test fails, the CVRF CSAF Converter SHALL try to convert the entry based on the mapping
      given in [cite](#RVISC-M).
      * If the mapping succeeds and passes test [sec](#matching-text-for-registered-id-system), the CVRF CSAF Converter SHALL issue
        a warning that an ID from a registered vulnerability system was detected and converted.
      * If the mapping succeeds but does not passes test [sec](#matching-text-for-registered-id-system) or the mapping fails,
        the CVRF CSAF Converter SHALL issue a warning that an ID from a registered vulnerability system was detected and
        but could not be converted automatically.
        Such warning SHALL state the reason for failure.
        This includes also if the mapping is not implemented.

      > A tool MAY provide a non-default option to suppress this conversion step.

      The output SHALL include the original values and, if applicable, the converted ones.

  * If the `system_name` does not belong to an RVISC entry, the CVRF CSAF Converter SHALL try to convert the entry based on the
    mapping given in [cite](#RVISC-M).
    * If no matching mapping exists, the CVRF CSAF Converter SHALL issue a warning that an ID from a potentially
      unregistered vulnerability system was detected and no change occurred.
    * If the mapping succeeds and passes test [sec](#matching-text-for-registered-id-system), the CVRF CSAF Converter SHALL
      issue a warning that an ID from a vulnerability system with a known mapping was detected and converted.
    * If the mapping succeeds but does not passes test [sec](#matching-text-for-registered-id-system) or the mapping fails otherwise,
      the CVRF CSAF Converter SHALL issue a warning that an ID from a vulnerability system with a known mapping was detected
      and but could not be converted automatically.
      Such warning SHALL state the reason for failure.
      This includes also if the mapping is not implemented.

    > A tool MAY provide a non-default option to suppress this conversion step.

    The output SHALL include the original values and, if applicable, the converted ones.

* `/vulnerabilities[]/metrics[]`:
  * For any CVSS v4 element, the CVRF CSAF Converter SHALL compute the `baseSeverity` from the `baseScore` according to
    the rules of the applicable CVSS standard. (CSAF CVRF v1.2 predates CVSS v4.0.)
  * For any CVSS v3 element, the CVRF CSAF Converter SHALL compute the `baseSeverity` from the `baseScore` according to
    the rules of the applicable CVSS standard.
  * If no `product_id` is given, the CVRF CSAF Converter appends all Product IDs which are listed under `../product_status` in
    the arrays `known_affected`, `first_affected` and `last_affected`.
    If none of these arrays exist, the CVRF CSAF Converter issues an error that no matching Product ID was found for this score element.
  * If a `vectorString` is missing, the CVRF CSAF Converter issues an error that the CVSS element could not be converted as
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
       The CVRF CSAF Converter issues a warning that this value was guessed from the element's namespace.

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
       The CVRF CSAF Converter issues a warning that this value was guessed from the global namespace.
       If more than one CVSS namespace is present and the element is not clearly defined via the namespace,
       this step SHALL be skipped without a decision.

        *Example 4:*

        ```
          xmlns:cvssv3="https://www.first.org/cvss/cvss-v3.0.xsd" => 3.0
        ```

    4. Retrieve the CVSS version from a config value, which defaults to `3.0`.
       (As CSAF CVRF v1.2 predates CVSS v3.1.) The CVRF CSAF Converter issues a warning that this value was taken from the config.
* `/vulnerabilities[]/metrics[]/content/cvss_v4`: If an external reference in the vulnerability linking to the official FIRST.org CVSS v4.0 calculator exists,
  the CVRF CSAF Converter SHALL convert the vector given in the fragment into a `cvss_v4` object linked to all affected products of the vulnerability.

  > A tool MAY implement an option to suppress this conversion.

  If the CVRF CSAF Converter is unable to construct a valid object with the information given, the CVRF CSAF Converter SHALL
  remove the invalid `cvss_v4` object and issue a warning that the automatic conversion of the CVSS v4.0 reference failed.
  Such warning SHOULD include the specific error that occurred.
* `/vulnerabilities[]/notes`: If any `vuln:Note` item contains one of the `category` and `title` combinations specified in
  [sec](#vulnerabilities-property-notes), where the `title` is extended, the CVRF CSAF Converter SHALL try to identify whether that extension is
  a specific product name, version or family.
  In such case, the CVRF CSAF Converter SHALL try to add the corresponding products to the note item and issue a warning that a potential product
  specific note has been discovered and products have been assigned to it.
  Such warning SHALL also include the note and the assigned products.
  If the CVRF CSAF Converter is unable to create a valid object, it SHALL remove the reference to the products and issue a warning that a potential
  product specific note has been discovered and no products could been assigned to it.
* `/vulnerabilities[]/remediations[]`:
  * If neither `product_ids` nor `group_ids` are given, the CVRF CSAF Converter appends all Product IDs which are listed under
    `../product_status` in the arrays `known_affected`, `first_affected` and `last_affected` into `product_ids`.
    If none of these arrays exist, the CVRF CSAF Converter issues an error that no matching Product ID was found for this remediation element.
  * The CVRF CSAF Converter SHALL convert any remediation with the type `Vendor Fix` into the category `optional_patch` if the product in
    question is in one of the product status groups "Not Affected" or "Fixed" for this vulnerability.
    Otherwise, the category `vendor_fix` SHALL be set.
    If multiple products are associated with the remediation - either directly or through a product group - and the products belong to
    different product status groups, the CVRF CSAF Converter SHALL duplicate the remediation, change the category in one instance
    to `optional_patch` and distribute the products accordingly as stated by the conversion rule.
  * The CVRF CSAF Converter SHALL convert any remediation with the type `None Available` into the category `fix_planned`
    if the product in question is also listed in a remediation of the type `Vendor Fix` with a `Date` in the future or no `Date` at all.
    Consequently, the product SHALL be removed from the remediation of the category `vendor_fix`.
    If it was the last product in that remediation, the remediation SHALL be removed.
  * The CVRF CSAF Converter SHALL remove any product from a remediation with the type `None Available`
    if the product in question is also listed in a remediation of the type `Vendor Fix` with a `Date` in the past or to the exact same time.
    If it was the last product in that remediation, the remediation SHALL be removed.
  * In any other case, the CVRF CSAF Converter SHALL preserve the product in the remediation of the category `none_available`.
  * The CVRF CSAF Converter SHALL issue a warning if a remediation was added, deleted or the value of the category was changed,
    including the products it was changed for.
