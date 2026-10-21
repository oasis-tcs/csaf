### Conformance Clause 18: CSAF 2.0 to CSAF 2.1 Converter{#conformance-clause-18-csaf-2-0-to-csaf-2-1-converter}

A program satisfies the "CSAF 2.0 to CSAF 2.1 Converter" conformance profile if the program fulfills the following two groups of requirements:

Firstly, the program:

- satisfies the "CSAF Producer" conformance profile.
- takes CSAF 2.0 Documents as input.
- rejects invalid CSAF 2.0 Documents unless forced by the user to proceed with a certain option.
  The existence of such option is OPTIONAL.

  > If a program has no option to force the processing of invalid CSAF 2.0 documents,
  > this does not necessarily mean that the program cannot be a compliant CSAF 2.0 to CSAF 2.1 Converter.

- issues a warning that an additional property was detected and not converted if it detects an additional property in the input.
  Such a warning SHALL include the additional property and its path.
  The CSAF 2.0 to CSAF 2.1 Converter SHALL ignore that additional property during the conversion.
- includes in every error and warning the relevant paths and values ​​from the original file that triggered the alert,
  unless otherwise specified in this standard.
- additionally satisfies the normative requirements given below.

Secondly, the program fulfills the following for all items of:

- value type `string` with format `date-time`: If the value contains a `60` in the seconds place, the CSAF 2.0 to CSAF 2.1 Converter
  SHALL replace the seconds and their fractions with `59.999999`.
  In addition, the converter issues a warning that leap seconds are now prohibited in CSAF and the value has been replaced.
  The CSAF 2.0 to CSAF 2.1 Converter SHOULD indicate in such warning message whether the value was a valid leap second or not.
- type `$['$defs'].branches_t`:
  - If a branch item uses the category `legacy`,
    the CSAF 2.0 to CSAF 2.1 Converter SHALL replace it with the category `product_name`.
    In addition, the converter issues a warning that this type does not exist in CSAF 2.1 and have been replaced with the category `product_name`.

    > There is a chance, that this replacement is incorrect or another category is a better fit.
    > Users of the converter are advised to check the content of such documents to make sure the conversion is correct or at least not misleading.
  
  - If any branch category appears multiple times along a path under `$.product_tree.branches` and the category is not an excepted one according to
    test [sec](#stacked-branch-categories), the CSAF 2.0 to CSAF 2.1 Converter SHALL try to convert the data into a valid product tree by
    applying the following steps to the path:
    1. If the stacked branch category is `vendor`, the vendor items named `Open Source`, `NOASSERTION`, `undefined` and `unknown`
       (white space, dash, hyphen, minus, underscore, invisible character and case insensitive on both sides) SHALL be removed.
    2. If the stacked branch category is `product_version` and the item directly before the first `product_version` is a `product_name`:
       - the category of the original `product_name` item SHALL be changed to `product_family` and
       - the category of the first `product_version` item SHALL be changed to `product_name` and
       - the value of the newly created `product_family` item SHALL be prepended at the value of the newly created `product_name` item.

    If the CSAF 2.0 to CSAF 2.1 Converter is able to create a valid product tree,
    it SHALL issue a warning that an invalid product tree with stacked branch categories was detected and resolved.
    Such a warning SHALL include the invalid path as well as the branch categories that were present multiple times.

    > A tool MAY provide a non-default option to suppress this conversion step.

    If the CSAF 2.0 to CSAF 2.1 Converter is unable to create a valid product tree,
    it SHALL issue an error that an invalid product tree with stacked branch categories was detected and could not be resolved.
    Such a error SHALL include the invalid path as well as the branch categories that were present multiple times.

    > A tool MAY provide a non-default option to output the invalid document.

  - If the branch categories `product_version` and `product_version_range` appear along a path under `$.product_tree.branches`,
    the CSAF 2.0 to CSAF 2.1 Converter SHALL try to convert the data into a valid product tree by
    applying the following steps to the path:

    1. If the branch category `product_version` occurs before the `product_version_range` and the item directly before the first
       `product_version` is a `product_name`:
       - the category of the original `product_name` item SHALL be changed to `product_family` and
       - the category of the first `product_version` item SHALL be changed to `product_name` and
       - the value of the newly created `product_family` item SHALL be prepended at the value of the newly created `product_name` item.
    2. If the branch category `product_version` occurs before the `product_version_range` and the item directly before the first
       `product_version` is a `product_family`:
       - the category of the first `product_version` item SHALL be changed to `product_name` and
       - the value of the direct ancestor `product_family` item SHALL be prepended at the value of the newly created `product_name` item.

    If the CSAF 2.0 to CSAF 2.1 Converter is able to create a valid product tree,
    it SHALL issue a warning that an invalid product tree with branch categories `product_version` and `product_version_range` in
    one path was detected and resolved.
    Such a warning SHALL include the invalid path as well as the branch category items changed.

    > A tool MAY provide a non-default option to suppress this conversion step.

    If the CSAF 2.0 to CSAF 2.1 Converter is unable to create a valid product tree,
    it SHALL issue an error that an invalid product tree with branch categories `product_version` and `product_version_range` in
    one path was detected and could not be resolved.
    Such a error SHALL include the invalid path as well as the branch category items.

    > A tool MAY provide a non-default option to output the invalid document.

  - If the value of `name` of an item categorized as `product_version_range` and contains an upper open ended product version range,
    the CSAF 2.0 to CSAF 2.1 Converter SHALL try to convert the data into a valid product tree by
    applying the following steps to the path:

    1. If value of `name` consists only of one version constraint:
       - the category of the original `product_version_range` item SHALL be changed to `product_version` and
       - the version SHALL be extracted from the original value and set as new value of `name`.
    2. If value of `name` consists of more than one version constraint and the upper open range is the last version constraint:
       - the category of the original `product_version_range` item SHALL be kept and
       - the value `name` SHALL be converted into the product version range ending with the version the upper open ended product version
         if that does not change the inclusion boundaries.

    If the CSAF 2.0 to CSAF 2.1 Converter is able to create a valid product tree,
    it SHALL issue a warning that an invalid product tree with an upper open ended product version range in
    one path was detected and resolved.
    Such a warning SHALL include the invalid path as well as the original and new value.

    > A tool MAY provide a non-default option to suppress this conversion step.

    If the CSAF 2.0 to CSAF 2.1 Converter is unable to create a valid product tree,
    it SHALL issue an error that an invalid product tree with an upper open ended product version range in
    one path was detected and could not be resolved.
    Such a error SHALL include the invalid path as well as the original and new value.

    > A tool MAY provide a non-default option to output the invalid document.

  - If the value of `name` of an item categorized as `product_version_range` contains just a single version,
    the CSAF 2.0 to CSAF 2.1 Converter SHALL try to convert the data into a valid product tree by
    applying the following steps to the path:

    1. If value of `name` is in the VERS format:
       - the category of the original `product_version_range` item SHALL be changed to `product_version` and
       - the version SHALL be extracted from the version constraint and set as new value of `name`.
    2. If value of `name` is in the vls format:
       - the category of the original `product_version_range` item SHALL be changed to `product_version` and
       - the value `name` SHALL be kept unchanged.

    If the CSAF 2.0 to CSAF 2.1 Converter is able to create a valid product tree,
    it SHALL issue a warning that an invalid product tree with a `product_version` declared as `product_version_range` in
    one path was detected and resolved.
    Such a warning SHALL include the invalid path as well as value of the product version.

    > A tool MAY provide a non-default option to suppress this conversion step.

    If the CSAF 2.0 to CSAF 2.1 Converter is unable to create a valid product tree,
    it SHALL issue an error that an invalid product tree with a `product_version` declared as `product_version_range` in
    one path was detected and could not be resolved.
    Such a error SHALL include the invalid path as well as value of the product version.

    > A tool MAY provide a non-default option to output the invalid document.

- type `$['$defs'].full_product_name_t..product_identification_helper..cpe`: If a CPE is invalid,
  the CSAF 2.0 to CSAF 2.1 Converter SHOULD remove the invalid value and issue a warning that an invalid CPE was detected and removed.
- type `$['$defs'].full_product_name_t..product_identification_helper..hashes`:
  The CSAF 2.0 to CSAF 2.1 Converter SHALL keep the order of the items during the conversion.
  If a value occurs multiple times, the CSAF 2.0 to CSAF 2.1 Converter SHALL convert only the first one and therefore making sure that
  all items are unique.
- type `$['$defs'].full_product_name_t..product_identification_helper..hashes[*]..file_hashes`:
  The CSAF 2.0 to CSAF 2.1 Converter SHALL keep the order of the items during the conversion.
  If a value occurs multiple times, the CSAF 2.0 to CSAF 2.1 Converter SHALL convert only the first one and therefore making sure that
  all items are unique.
- type `$['$defs'].full_product_name_t..product_identification_helper..hashes[*]..file_hashes[*]..algorithm`:
  If the algorithm is known to the implementation or mentioned in this standard, the CSAF 2.0 to CSAF 2.1 Converter SHALL ensure its spelling
  is exactly as prescribed by this standard.
  If the algorithm is unknown to the implementation, the CSAF 2.0 to CSAF 2.1 Converter SHALL convert it to lowercase and issue a warning that
  an unknown hash algorithm was detected and converted.

  > A tool MAY provide a non-default option to suppress this conversion step.

- type `$['$defs'].full_product_name_t..product_identification_helper..hashes[*]..file_hashes[*]..value`: The CSAF 2.0 to CSAF 2.1 Converter SHALL convert
  the value into a lowercase string.
- type `$['$defs'].full_product_name_t..product_identification_helper..model_numbers[*]`:

  > The values were implicitly open ended in CSAF 2.0 which resulted in ambiguity.
  > A fixed-length matching was not possible.
  > CSAF 2.1 requires that values ​​intended to be interpreted as "starts with" be explicitly marked with an asterisk (`*`) at the end.

  - If a model number is given that does not end on a star, the CSAF 2.0 to CSAF 2.1 Converter SHOULD add a `*` to the end and
    issue a warning that a partial model number was detected and a star has been added.
  - If the model number contains a `\`, the CSAF 2.0 to CSAF 2.1 Converter SHALL escape it by inserting an additional `\` before the character.
  - If the model number contains multiple unescaped `*` after the conversion, the CSAF 2.0 to CSAF 2.1 Converter SHALL remove the entry and
    issue a warning that a model number with multiple stars was detected and removed.

  > A tool MAY provide a non-default option to interpret all model numbers as complete and therefore does not add any stars.

  > A tool MAY provide a non-default option to interpret the `?` in all model numbers as part of the model number itself and therefore escape it.

  > A tool MAY provide a non-default option to interpret the `*` in all model numbers as part of the model number itself and therefore escape it.

- type `$['$defs'].full_product_name_t..product_identification_helper..purls`: If a `$['$defs'].full_product_name_t..product_identification_helper..purl` is given,
  the CSAF 2.0 to CSAF 2.1 Converter SHALL convert it into the first item of the corresponding `purls` array.
- type `$['$defs'].full_product_name_t..product_identification_helper..sbom_urls`:
  The CSAF 2.0 to CSAF 2.1 Converter SHALL keep the order of the items during the conversion.
  If a value occurs multiple times, the CSAF 2.0 to CSAF 2.1 Converter SHALL convert only the first one and therefore making sure that
  all items are unique.
- type `$['$defs'].full_product_name_t..product_identification_helper..serial_numbers[*]`:

  > The values were implicitly open ended in CSAF 2.0 which resulted in ambiguity.
  > A fixed-length matching was not possible.
  > CSAF 2.1 requires that values ​​intended to be interpreted as "starts with" be explicitly marked with an asterisk (`*`) at the end.

  - If a serial number is given that does not end on a star, the CSAF 2.0 to CSAF 2.1 Converter SHOULD add a `*` to the end and
    issue a warning that a partial serial number was detected and a star has been added.
  - If the serial number contains a `\`, the CSAF 2.0 to CSAF 2.1 Converter SHALL escape it by inserting an additional `\` before the character.
  - If the serial number contains multiple unescaped `*` after the conversion, the CSAF 2.0 to CSAF 2.1 Converter SHALL remove the entry and
    issue a warning that a serial number with multiple stars was detected and removed.

  > A tool MAY provide a non-default option to interpret all serial numbers as complete and therefore does not add any stars.

  > A tool MAY provide a non-default option to interpret the `?` in all serial numbers as part of the serial number itself and therefore escape it.

  > A tool MAY provide a non-default option to interpret the `*` in all serial numbers as part of the serial number itself and therefore escape it.

- type `$['$defs'].full_product_name_t..product_identification_helper..skus`:
  The CSAF 2.0 to CSAF 2.1 Converter SHALL keep the order of the items during the conversion.
  If a value occurs multiple times, the CSAF 2.0 to CSAF 2.1 Converter SHALL convert only the first one and therefore making sure that
  all items are unique.
- type `$['$defs'].full_product_name_t..product_identification_helper..skus[*]`:
  
  > The values were implicitly open ended in CSAF 2.0 which resulted in ambiguity.
  > A fixed-length matching was not possible.
  > CSAF 2.1 requires that values ​​intended to be interpreted as "starts with" be explicitly marked with an asterisk (`*`) at the end.

  - If a stock keeping unit is given that does not end on a star, the CSAF 2.0 to CSAF 2.1 Converter SHOULD add a `*` to the end and
    issue a warning that a partial stock keeping unit was detected and a star has been added.
  - If the stock keeping unit contains a `\`,
    the CSAF 2.0 to CSAF 2.1 Converter SHALL escape it by inserting an additional `\` before the character.
  - If the stock keeping unit contains multiple unescaped `*` after the conversion, the CSAF 2.0 to CSAF 2.1 Converter SHALL remove the entry and
    issue a warning that a stock keeping unit with multiple stars was detected and removed.

  > A tool MAY provide a non-default option to interpret all stock keeping units as complete and therefore does not add any stars.

  > A tool MAY provide a non-default option to interpret the `?` in all stock keeping units as part of the stock keeping unit
  > itself and therefore escape it.

  > A tool MAY provide a non-default option to interpret the `*` in all stock keeping units as part of the stock keeping unit
  > itself and therefore escape it.

- type `$['$defs'].full_product_name_t..product_identification_helper..x_generic_uris`:
  The CSAF 2.0 to CSAF 2.1 Converter SHALL keep the order of the items during the conversion.
  If a value occurs multiple times, the CSAF 2.0 to CSAF 2.1 Converter SHALL convert only the first one and therefore making sure that
  all items are unique.
- `$['$schema']`: The CSAF 2.0 to CSAF 2.1 Converter SHALL set property with the value prescribed by the schema.
- `$.document.category`:
  - If the `category` equals `csaf_security_advisory`, the CSAF 2.0 to CSAF 2.1 Converter SHALL try to convert the data into a
    valid CSAF Document in this profile according to CSAF 2.1.
    For any version range of affected products that uses the strict `<`, i.e. not `<=`, as comparator of the last version constraint, the CSAF 2.0
    to CSAF 2.1 Converter SHOULD add a new product with the version of the last constraint and add that in the appropriate places as `fixed`.
    The CSAF 2.0 to CSAF 2.1 Converter SHALL issue a warning that a product was added to the `product_tree` and the corresponding `$.vulnerabilities[*]`.
    Such warning SHALL contain the full product name and its path as well as the paths of the `$.vulnerabilities[*]` it was added to.
    The CSAF 2.0 to CSAF 2.1 Converter MAY have a non-default option to assign organization-wide IDs to any vulnerability not
    containing a CVE nor any other vulnerability ID and therefore failing test [sec](#vulnerability-id).
    Issuing parties are responsible to keep track of assigned IDs to prevent the assignment of the same ID  for different issues.
    If the CSAF 2.0 to CSAF 2.1 Converter is unable to create a valid CSAF 2.1 Document according to the profile,
    it SHALL set the `category` value to `csaf_deprecated_security_advisory`.
  - If the `$.document.lang` is English or unspecified, the following rules apply:
    - If the `$.document.title` starts with the string `Superseded` or the `$.document.category` has the value `Superseded` (case-insensitive),
      the CSAF 2.0 to CSAF 2.1 Converter SHALL try to convert all data into a valid CSAF Document in the profile "Superseded" according to CSAF 2.1.
    - If the `$.document.title` starts with the string `Withdrawn` or the `$.document.category` has the value `Withdrawn` (case-insensitive),
      the CSAF 2.0 to CSAF 2.1 Converter SHALL try to convert all data into a valid CSAF Document in the profile "Withdrawn" according to CSAF 2.1.
 
    > A tool MAY provide a non-default option to remove or transform certain or all elements the hinder the creation of a valid CSAF Document
    > according to the profile.

    > A tool MAY support this detection for other languages.

    If the CSAF 2.0 to CSAF 2.1 Converter is unable to create a valid CSAF 2.1 Document according to the profile, it SHALL set the `category`
    of the original CSAF Document and issue a warning a potentially withdrawn CSAF Document was created which would result in an invalid CSAF.
- `$.document.csaf_version`: The CSAF 2.0 to CSAF 2.1 Converter SHALL update the value to `2.1`.
- `$.document.distribution.tlp.label`: If a TLP label is given, the CSAF 2.0 to CSAF 2.1 Converter SHALL convert it according to [tab](#tab:tlp-labels-across-csaf-versions).

  If `$.document.distribution.text` contains the string `TLP v2.0: TLP:` followed by a valid TLP v2.0 label as defined in the CSAF 2.1 JSON schema,
  the CSAF 2.0 to CSAF 2.1 Converter SHOULD provide an option to use this label instead.

  If the TLP label changes during such a conversion in a way not listed in [tab](#tab:tlp-labels-across-csaf-versions),
  the CSAF 2.0 to CSAF 2.1 Converter SHALL issue a warning that the TLP label was taken from the distribution text.
  This warning SHALL include both values: the value converted using the table and the value from the distribution text.

  > This is a common case for CSAF 2.0 Documents labeled as `TLP:RED` but actually intended to be `TLP:AMBER+STRICT`.

  If no TLP label was given, the CSAF 2.0 to CSAF 2.1 Converter SHOULD assign `TLP:CLEAR` and issue a warning that the default TLP has been set.
- `$.document.involvement`:
  - If the user passes an `involvement` element to the CSAF 2.0 to CSAF 2.1 Converter, the tool SHALL insert that element into
   `$.document.involvement` and omit the conversion of all elements in `$.vulnerabilities[*].involvements`.
  - If any vulnerability item contains an `involvements` element and the user provided an `involvement` element,
    the CSAF 2.0 to CSAF 2.1 Converter SHOULD issue a warning that all elements in `$.vulnerabilities[*].involvements` omitted as
    the user provided `involvement` takes precedence.
  - If any vulnerability item contains an `involvements` element and the user did not provide an `involvement` element,
    the CSAF 2.0 to CSAF 2.1 Converter SHALL try to convert the data into a valid CSAF Document by apply the following process:
    1. The CSAF 2.0 to CSAF 2.1 Converter assigns each vulnerability containing an `involvements` element a document-local vuln ID with the
       prefix `VULN-`, followed by the current value of counter for the vulnerabilities containing an `involvements` element.
       The counter starts with `1` and is zero-padded to four digits before appended to the prefix.

       > If the counter is at `1000` no additional padding is needed anymore.

    2. The CSAF 2.0 to CSAF 2.1 Converter SHALL create for each `involvements` item a conversion ID which is constructed as follows:
       - The filename is computed from the `$.document.tracking.id` according to the rules of [sec](#filename).
         Remaining `+` in that string are replaced by `_`.
         The file extension `.json` is removed from the string.
       - This string is extended by appending the `dl_vuln_id` of the vulnerability the `involvements` item is found in followed
         by the item number inside the current `involvements`.
         The counter for the item number starts with `1` and is zero-padded to four digits.
       This conversion ID identifies an involvement item with in a CSAF document locally
       and provides collision resistance if the filenames of the processed files are sufficiently different.

    3. The CSAF 2.0 to CSAF 2.1 Converter SHALL create for each `party` mentioned in the `involvements` a new entry in `entities`
       and assign a `entity_id` by prepending the mandatory prefix `EID-` to the conversion ID of that `involvements` item.

       > This create a new entry in `$.document.involvement.entities` per `involvements` item.

       The CSAF 2.0 to CSAF 2.1 Converter SHALL convert the value of `party` into the value of `category`.
       If the value of `party` is `other`, the CSAF 2.0 to CSAF 2.1 Converter SHOULD issue a warning that some parties have been
       regrouped into new category values.
       An option to suppress this warning SHALL exist.
       In addition, an option SHOULD be provided to set one of the new values directly.

       > Entities can be corrected through a mapping in a later step.

    4. The CSAF 2.0 to CSAF 2.1 Converter SHALL create an entity for the publisher of the CSAF 2.0 document with the same `name`
       and `category` as stated in the `$.document.publisher` object.
       The `entity_id` SHALL be `EID-Publisher`.
    5. If the user provides a mapping which contains `entities` to CSAF 2.0 to CSAF 2.1 Converter,
       the tool SHALL replace entries that contain a matching `entity_id` with the corresponding entry from the mapping.
       The CSAF 2.0 to CSAF 2.1 Converter SHALL skip this step, if not mapping was provided by the user.
    6. Each item of the `involvements` array inside the current vulnerability is converted using the following subprocess:
       - The CSAF 2.0 to CSAF 2.1 Converter SHALL create a new `action` and add the document-local vuln ID of the current vulnerability
         into `dl_vuln_ids` of the action.
       - The `action_id` is constructed by prepending the prefix `ACN-` to the conversion ID of that `involvements` item.
       - If the `summary` was given, the CSAF 2.0 to CSAF 2.1 Converter SHALL convert its value as value into the `summary` element.
       - If the `date` was given, the CSAF 2.0 to CSAF 2.1 Converter SHALL convert its value as value into the `date` element.
         If the `date` is missing, the CSAF 2.0 to CSAF 2.1 Converter SHOULD stop the subprocess and discard the `action` unless the user
         instructed the tool to add the element with an empty value.
         In the first case, the CSAF 2.0 to CSAF 2.1 Converter SHALL issue a warning that an involvement without date was detected and
         removed.
         If the CSAF 2.0 to CSAF 2.1 Converter was instructed to add an empty date, it SHALL issue a warning that an involvement without
         date was detected and converted into an invalid action with empty `date`.

         > In such case, the user is expected to add missing dates from other sources.

       - The CSAF 2.0 to CSAF 2.1 Converter SHALL use the [tab](#tab:involvement-status-and-category-mapping-from-csaf-2-0) to set the
         `category` and `status`.
       - The CSAF 2.0 to CSAF 2.1 Converter SHOULD have an option to extract additional details about the entity from the `summary`,
         if applicable.
         If that option is given, the CSAF 2.0 to CSAF 2.1 Converter SHALL insert the additionally extracted details in the corresponding
         fields and issue a warning that additional details were found and used to enrich the `entity`.
         Such warning SHOULD provide the full enriched `entity` element and the `summary` that the content was extracted from.
       - The CSAF 2.0 to CSAF 2.1 Converter SHALL set the `acting_entity_refs` and `receiving_entity_refs` according to the content
         of the current `involvements` item using the corresponding entry from the list of entities.
         As default, the entity that corresponds to the `party` is referenced in the `acting_entity_refs`.
         If the `summary` shows that the `party` is the receiver, the entity that corresponds to the `party` is referenced in
         the `receiving_entity_refs`.
       - To determine the entity that is not given in the CSAF 2.0 document, the CSAF 2.0 to CSAF 2.1 Converter SHALL apply the
         following steps in this order:
         1. If the missing entity can be derived from the context, e.g. through the content of the `summary`,
            the respective entity SHALL be used.
            In most cases, this will lead to inserting `EID-Publisher` into the `receiving_entity_refs` respectively `acting_entity_refs`.
            The CSAF 2.0 to CSAF 2.1 Converter SHALL NOT make up an entity not given in the `summary`.
         2. If the context suggests that the `involvements` item matches one of the categories that do not need a recipient,
            the respective `category` SHALL be used.
            The CSAF 2.0 to CSAF 2.1 Converter SHALL reference the corresponding action `referenced_action_ids`
            if required by the `category` value.
            If the value cannot be determined with certainty, this step is unsuccessful.
         3. If the steps mentioned above are unsuccessful or inconclusive, the CSAF 2.0 to CSAF 2.1 Converter SHALL stop the subprocess
            and discard the `action` unless the user instructed the tool to add the action with partial data.
            In the first case, the CSAF 2.0 to CSAF 2.1 Converter SHALL issue a warning that an involvement without sufficient data was
            detected, could not be converted automatically and therefore was removed.
            If the CSAF 2.0 to CSAF 2.1 Converter was instructed to add the action with partial data, it SHALL issue a warning that an involvement without sufficient data was detected and only partially converted.
    7. The CSAF 2.0 to CSAF 2.1 Converter SHALL provide an option to collapse entities.
       If that option is selected, the CSAF 2.0 to CSAF 2.1 Converter SHALL map all items from `entities` into groups where each group
       contains only members that differ only in their `entity_id`.
       The first one of each group which becomes the representative of that group.
       References to other elements of the group are replaced with a reference to the representative of the group.
       Then, the CSAF 2.0 to CSAF 2.1 Converter SHALL remove all items from `entities` except for the representative of the groups.
    8. The CSAF 2.0 to CSAF 2.1 Converter SHALL provide an option to collapse actions.
       If that option is selected, the CSAF 2.0 to CSAF 2.1 Converter SHALL map all items from `actions` which are not referenced in
       any `referenced_action_ids` into groups where each group contains only members that differ only in their `dl_vuln_ids`.
       The first one of each group which becomes the representative of that group.
       The CSAF 2.0 to CSAF 2.1 Converter SHALL collect all values from `dl_vuln_ids` within one group and insert the values into
       `dl_vuln_ids` of the representative of that group.
       Then, the CSAF 2.0 to CSAF 2.1 Converter SHALL remove all items from `actions` except for the representative of the groups.
    During the conversion, the CSAF 2.0 to CSAF 2.1 Converter SHALL NOT invent data or set values in any other way than described above.
    If the CSAF 2.0 to CSAF 2.1 Converter is unable to create a valid CSAF 2.1 Document, it SHALL remove the `involvement`
    from the CSAF Document and issue a warning that `$.vulnerabilities[*].involvements` could not be converted automatically
    and therefore have been removed.
- `$.document.license_expression`: If any `$.document.notes` item in with `category` `legal_disclaimer` contains a valid SPDX license expression,
  the CSAF 2.0 to CSAF 2.1 Converter SHALL apply the following rules for the list of candidates:
  - If this list contains only one element, the CSAF 2.0 to CSAF 2.1 Converter SHALL set this value as value of `license_expression`.
    In addition, the converter issues a warning that license expression was found and set as document license expression.
  - If multiple SPDX license expressions are found, the CSAF 2.0 to CSAF 2.1 Converter issues a warning that multiple
    SPDX license expressions were found and therefore no document license expression could be determined.
    Such a warning SHALL include the list of all SPDX license expressions and their associated paths.

  > A tool MAY implement an option to suppress this conversion.

- `$.document.notes`: If any `$.document.notes` item contains one of the `category` and `title` combinations specified in
  [tab](#tab:document-property-notes) of section [sec](#document-property---notes), where the `title` is extended,
  the CSAF 2.0 to CSAF 2.1 Converter SHALL try to identify whether that extension is a specific product name, version or family.
  In such case, the CSAF 2.0 to CSAF 2.1 Converter SHALL try to add the corresponding products to the note item and issue a warning that a
  potential product specific note has been discovered and products have been assigned to it.
  Such warning SHALL also include the note and the assigned products.
  If the CSAF 2.0 to CSAF 2.1 Converter is unable to create a valid object, it SHALL remove the reference to the products and issue a warning that a potential
  product specific note has been discovered and no products could been assigned to it.
- `$.document.publisher.category`: If the value is `other`, the CSAF 2.0 to CSAF 2.1 Converter SHOULD issue a warning that some parties have
  been regrouped into the new value `multiplier`. An option to suppress this warning SHALL exist. In addition, an option SHOULD be provided to
  set the value to `multiplier`.
- `$.document.publisher.contact`:
  - If a `$.document.publisher.contact_details` element is present,
    the CSAF 2.0 to CSAF 2.1 Converter SHALL convert its content into the value of the `details` property.
  - If a URL to a Public OpenPGP Key was provided in the `$.document.publisher.contact_details` element and
    the URL fulfills the requirements of the property `public_openpgp_key_url`,
    the CSAF 2.0 to CSAF 2.1 Converter SHALL set it as the content of that property.
  - The CSAF 2.0 to CSAF 2.1 Converter SHOULD extract the matching email address from the content of the
    `$.document.publisher.contact_details` element, if applicable, or use the first email address and set it as value of `email`.
  - The CSAF 2.0 to CSAF 2.1 Converter SHALL provide configuration options and corresponding arguments to set these values if they are not present.
    If values from both sources are present, the program SHOULD prefer the latter one.
    It SHOULD provide an option to overwrite the values extracted from the document.
    The program SHALL NOT use hard-coded values.
- `$.document.title`: If the value contains the `$.document.tracking.id`, the CSAF 2.0 to CSAF 2.1 Converter SHALL remove the `$.document.tracking.id`
  from the `$.document.title`. In addition, separating characters including but not limited to white space, colon, dash and brackets SHALL be removed.
- `$.product_tree.product_paths[*]`: For each element in `$.product_tree.relationships[*]`, the CSAF 2.0 to CSAF 2.1 Converter
  SHALL apply the following rules:
  - The value of `product_reference` is set as the value of `beginning_product_reference`.
  - The CSAF 2.0 to CSAF 2.1 Converter constructs the first item of `subpaths` by setting the value of `category` into `category`
    and the value of `relates_to_product_reference` into `next_product_reference`.

    > A tool MAY provide an option to collapse chained product path elements into the appropriate number of product path elements,
    > if this is possible without the loss of correct information.
    > Usually, collapsing chained product paths is not possible if
    > - a product (type: `full_product_name_t`) defined by a product path element in the chain is referenced in other parts of the document, or
    > - a product (type: `full_product_name_t`) defined by a product path element in the chain contains a `product_identification_helper`
    >   element.
    > For examples, see appendix [sec](#collapsing-product-paths).

- `$.vulnerabilities[*].cwes[*]`:
  - The CSAF 2.0 to CSAF 2.1 Converter SHALL remove all preceding and trailing white space from the `name`.
  - The CSAF 2.0 to CSAF 2.1 Converter SHALL determine the CWE specification version the given CWE was selected from by
    using the latest version that matches the `id` and `name` exactly and was published prior to the value of
    `$.document.tracking.current_release_date` of the source document.
    If no such version exist, the first matching version published after the value of `$.document.tracking.current_release_date`
    of the source document SHOULD be used.

    > This is done to create a deterministic conversion.

    The tool SHOULD implement an option to use the latest available CWE version at the time of the conversion that still matches.

- `$.vulnerabilities[*].disclosure_date`: If a `release_date` was given, the CSAF 2.0 to CSAF 2.1 Converter SHALL convert its value as value
  into the `disclosure_date` element.
- `$.vulnerabilities[*].ids`:  If an `system_name` was given, the CSAF 2.0 to CSAF 2.1 Converter SHALL test whether it belongs to a registered
  vulnerability ID system in RVISC.
  - If the `system_name` belongs to an RVISC entry, the CSAF 2.0 to CSAF 2.1 Converter SHALL execute
    test [sec](#matching-text-for-registered-id-system).
    - If the test passes, no further action is needed.
    - If the test fails, the CSAF 2.0 to CSAF 2.1 Converter SHALL try to convert the entry based on the mapping
      given in [cite](#RVISC-M).
      - If at least one matching mapping is ambiguous, the CSAF 2.0 to CSAF 2.1 Converter SHALL issue
        a warning that an ID from a registered vulnerability system was detected and not converted as the mapping was ambiguous.
        Such warning SHALL contain all matching mappings known from [cite](#RVISC-M).
        The program SHOULD provide an option to force a user-defined conversion.
      - If the mapping succeeds and passes test [sec](#matching-text-for-registered-id-system), the CSAF 2.0 to CSAF 2.1 Converter SHALL
        issue a warning that an ID from a registered vulnerability system was detected and converted.
      - If the mapping succeeds but does not passes test [sec](#matching-text-for-registered-id-system) or the mapping fails,
        the CSAF 2.0 to CSAF 2.1 Converter SHALL issue a warning that an ID from a registered vulnerability system was detected and
        but could not be converted automatically.
        Such warning SHALL state the reason for failure.
        This includes also if the mapping is not implemented.

      > A tool MAY provide a non-default option to suppress this conversion step.

      The output SHALL include the original values and, if applicable, the converted ones.

  - If the `system_name` does not belong to an RVISC entry, the CSAF 2.0 to CSAF 2.1 Converter SHALL try to convert the entry based on the
    mapping given in [cite](#RVISC-M).
    - If no matching mapping exists, the CSAF 2.0 to CSAF 2.1 Converter SHALL issue a warning that an ID from a potentially
      unregistered vulnerability system was detected and no change occurred.
    - If the mapping succeeds and passes test [sec](#matching-text-for-registered-id-system), the CSAF 2.0 to CSAF 2.1 Converter SHALL
      issue a warning that an ID from a vulnerability system with a known mapping was detected and converted.
    - If the mapping succeeds but does not passes test [sec](#matching-text-for-registered-id-system) or the mapping fails otherwise,
      the CSAF 2.0 to CSAF 2.1 Converter SHALL issue a warning that an ID from a vulnerability system with a known mapping was detected
      and but could not be converted automatically.
      Such warning SHALL state the reason for failure.
      This includes also if the mapping is not implemented.

    > A tool MAY provide a non-default option to suppress this conversion step.

    The output SHALL include the original values and, if applicable, the converted ones.

- `$.vulnerabilities[*].metrics[*].content.cvss_v4`: If an external reference in the vulnerability linking to the official FIRST.org CVSS v4.0
  calculator exists, the CSAF 2.0 to CSAF 2.1 Converter SHALL convert the vector given in the fragment into a `cvss_v4` object linked to all
  affected products of the vulnerability.
  
  > A tool MAY implement an option to suppress this conversion.

  If the CSAF 2.0 to CSAF 2.1 Converter is unable to construct a valid object with the information given, the CSAF 2.0 to CSAF 2.1 Converter SHALL
  remove the invalid `cvss_v4` object and issue a warning that the automatic conversion of the CVSS v4.0 reference failed.
  Such warning SHOULD include the specific error that occurred.
- `$.vulnerabilities[*].metrics[*].content.ssvc_v2`: If a SSVC vector or decision points of an SSVC vector are given in an item of `notes` of the current
  vulnerability using the `title` `SSVC` and the `category` `other`, the CSAF 2.0 to CSAF 2.1 Converter SHALL convert that data into the `ssvc_v2`
  object within the current vulnerability.
  If the CSAF 2.0 to CSAF 2.1 Converter is able to construct a valid object without losing any information, the corresponding `notes` item SHALL
  be removed.
  If the CSAF 2.0 to CSAF 2.1 Converter is unable to construct a valid object with the information given, the CSAF 2.0 to CSAF 2.1 Converter SHALL
  remove the invalid `ssvc_v2` object, keep the original item of `notes` and issue a warning that the automatic conversion of the SSVC data failed.
  If the CSAF 2.0 to CSAF 2.1 Converter would lose information during the conversion, the CSAF 2.0 to CSAF 2.1 Converter SHALL remove the `ssvc_v2`
  object, keep the original item of `notes` and issue a warning that the automatic conversion of the SSVC data would lead to losing information.
- `$.vulnerabilities[*].notes`: If any `$.vulnerabilities[*].notes` item contains one of the `category` and `title` combinations specified in
  [tab](#tab:vulnerabilities-property-notes) of section [sec](#vulnerabilities-property-notes), where the `title` is extended,
  the CSAF 2.0 to CSAF 2.1 Converter SHALL try to identify whether that extension is a specific product name, version or family.
  In such case, the CSAF 2.0 to CSAF 2.1 Converter SHALL try to add the corresponding products to the note item and issue a warning that a potential
  product specific note has been discovered and products have been assigned to it.
  Such warning SHALL also include the note and the assigned products.
  If the CSAF 2.0 to CSAF 2.1 Converter is unable to create a valid object, it SHALL remove the reference to the products and issue a warning that a
  potential product specific note has been discovered and no products could been assigned to it.
- `$.vulnerabilities[*].remediations[*]`:
  - The CSAF 2.0 to CSAF 2.1 Converter SHALL convert any remediation with the category `vendor_fix` into the category `optional_patch`
    if the product in question is in one of the product status groups "Not Affected" or "Fixed" for this vulnerability.
    Otherwise, the category `vendor_fix` SHALL stay the same.
    If multiple products are associated with the remediation - either directly or through a product group - and the products belong to different
    product status groups, the CSAF 2.0 to CSAF 2.1 Converter SHALL duplicate the remediation, change the category in one instance to `optional_patch`
    and distribute the products accordingly as stated by the conversion rule.
  - The CSAF 2.0 to CSAF 2.1 Converter SHALL convert any remediation with the category `none_available` into the category `fix_planned`
    if the product in question is also listed in a remediation of the category `vendor_fix` with a `date` in the future or no `date` at all.
    Consequently, the product SHALL be removed from the remediation of the category `vendor_fix`.
    If it was the last product in that remediation, the remediation SHALL be removed.
  - The CSAF 2.0 to CSAF 2.1 Converter SHALL remove any product from a remediation with the category `none_available`
    if the product in question is also listed in a remediation of the category `vendor_fix` with a `date` in the past or to the exact same time.
    If it was the last product in that remediation, the remediation SHALL be removed.
  - In any other case, the CSAF 2.0 to CSAF 2.1 Converter SHALL preserve the product in the remediation of the category `none_available`.
  - The CSAF 2.0 to CSAF 2.1 Converter SHALL issue a warning if a remediation was added, deleted or the value of the category was changed,
    including the products it was changed for.

> A tool MAY implement options to convert other Markdown formats to GitHub-flavored Markdown.

> A tool MAY implement an additional, non-default option to output an invalid document that can be fixed afterwards.
> Solely in this case, any of the rules above MAY be ignored to avoid data loss.

Mapping TLP labels per CSAF version:

| CSAF 2.0 (using TLP v1.0) | CSAF 2.1 (using TLP v2.0) |
|:--------------------------|:--------------------------|
| `TLP:WHITE`               | `TLP:CLEAR`               |
| `TLP:GREEN`               | `TLP:GREEN`               |
| `TLP:AMBER`               | `TLP:AMBER`               |
| `TLP:RED`                 | `TLP:RED`                 |

Table: Comparison of values for `$.document.distribution.tlp.label` across CSAF versions 2.0 and 2.1.{#tab:tlp-labels-across-csaf-versions}

Mapping of involvements `status`:

| CSAF 2.0 `status`   | CSAF 2.1 `status` | CSAF 2.1 Default `category` |
|:--------------------|:------------------|:----------------------------|
| `completed`         | `completed`       | `coordination`              |
| `contact_attempted` | `attempted`       | `notification`              |
| `disputed`          | `completed`       | `dispute`                   |
| `in_progress`       | `in_progress`     | `coordination`              |
| `not_contacted`     | `deferred`        | `notification`              |
| `open`              | `outstanding`     | `coordination`              |

Table: Mapping of values into `$.document.involvement.actions[*]` from CSAF versions 2.0 to 2.1.{#tab:involvement-status-and-category-mapping-from-csaf-2-0}
