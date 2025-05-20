# Profiles

CSAF documents do not have many required fields as they can be used for different purposes.
To ensure a common understanding of which fields are required in a given use case the standard defines profiles.
Each subsection describes such a profile by describing necessary content for that specific use case and providing insights into its purpose.
The value of `/document/category` is used to identify a CSAF document's profile. The following rules apply:

1. Each CSAF document MUST conform the **CSAF Base** profile.
2. Each profile extends the base profile "CSAF Base" - directly or indirect through another profile from the standard - by making additional
   fields from the standard mandatory.
   A profile can always add, but never subtract nor overwrite requirements defined in the profile it extends.
3. Any optional field from the standard can also be added to a CSAF document which conforms with a profile without breaking conformance with
   the profile.
   One and only exempt is when the profile requires not to have a certain set of fields.
4. Values of `/document/category` starting with `csaf_` are reserved for existing, past, upcoming and future profiles defined in the CSAF standard.
5. Values of `/document/category` starting with `csaf_deprecated_` are used for official profiles that are marked deprecated.
   Those profiles are mostly there to allow backwards compatibility, e.g. with older CSAF versions.
   Therefore, they SHOULD NOT be used for newly created CSAF documents.
6. Values of `/document/category` that do not match any of the values defined in section [sec](#profiles) of this standard SHALL be validated against
   the "CSAF Base" profile.
7. Local or private profiles MAY exist and tools MAY choose to support them.
8. If an official profile and a private profile exists, tools MUST validate against the official one from the standard.

## Profile 1: CSAF Base

This profile defines the default required fields for any CSAF document.
Therefore, it is a "catch all" for CSAF documents that do not satisfy any other profile.
Furthermore, it is the foundation all other profiles are build on.

A CSAF document SHALL fulfill the following requirements to satisfy the profile "CSAF Base":

* The following elements MUST exist and be valid:
  * `/$schema`
  * `/document/category`
  * `/document/csaf_version`
  * `/document/distribution/tlp/label`
  * `/document/publisher/category`
  * `/document/publisher/name`
  * `/document/publisher/namespace`
  * `/document/title`
  * `/document/tracking/current_release_date`
  * `/document/tracking/id`
  * `/document/tracking/initial_release_date`
  * `/document/tracking/revision_history[]/date`
  * `/document/tracking/revision_history[]/number`
  * `/document/tracking/revision_history[]/summary`
  * `/document/tracking/status`
  * `/document/tracking/version`
* The value of `/document/category` SHALL NOT be equal to any value that is intended to only be used by another profile nor to the
  (case insensitive) name of any other profile from the standard.
  This does not differentiate between underscore, dash or whitespace.
  To explicitly select the use of this profile the value `csaf_base` SHOULD be used.

> Neither `CSAF Security Advisory` nor `csaf security advisory` are valid values for `/document/category`.

An issuing party might choose to set `/document/publisher/name` in front of a value that is intended to only be used by another
profile to state that the CSAF document does not use the profile associated with this value.
In this case, the (case insensitive) string "CSAF" MUST be removed from the value.
This SHOULD be done if the issuing party is unable or unwilling to use the value `csaf_base`, e.g. due to legal or cooperate identity reasons.

> Both values `Example Company Security Advisory` and `Example Company security_advisory` in `/document/category` use the profile "CSAF Base".
> This is important to prepare forward compatibility as later versions of CSAF might add new profiles.
> Therefore, the values which can be used for the profile "CSAF Base" might change.

## Profile 2: Security incident response

This profile SHOULD be used to provide a response to a security breach or incident.
This MAY also be used to convey information about an incident that is unrelated to the issuing party's own products or infrastructure.

> Example Company might use a CSAF document satisfying this profile to respond to a security incident at ACME Inc. and
the implications on its own products and infrastructure.

A CSAF document SHALL fulfill the following requirements to satisfy the profile "Security incident response":

* The following elements MUST exist and be valid:
  * all elements required by the profile "CSAF Base".
  * `/document/notes` with at least one item which has a `category` of `description`, `details`, `general` or `summary`
    > Reasoning: Without at least one note item which contains information about response to the event referred to this doesn't provide
    > any useful information.
  * `/document/references` with at least one item which has a `category` of `external`
    > The intended use for this field is to refer to one or more documents or websites which provides more details about the incident.
* The value of `/document/category` SHALL be `csaf_security_incident_response`.

## Profile 3: Informational Advisory

This profile SHOULD be used to provide information which are **not related to a vulnerability** but e.g. a misconfiguration.

A CSAF document SHALL fulfill the following requirements to satisfy the profile "Informational Advisory":

* The following elements MUST exist and be valid:
  * all elements required by the profile "CSAF Base".
  * `/document/notes` with at least one item which has a `category` of `description`, `details`, `general` or `summary`
    > Reasoning: Without at least one note item which contains information about the "issue" which is the topic of the advisory it is useless.
  * `/document/references` with at least one item which has a `category` of `external`
    > The intended use for this field is to refer to one or more documents or websites which provide more details about
    > the issue or its remediation (if possible).
    > This could be a hardening guide, a manual, best practices or any other helpful information.
* The value of `/document/category` SHALL be `csaf_informational_advisory`.
* The element `/vulnerabilities` SHALL NOT exist.
  If there is any information that would reside in the element `/vulnerabilities` the CSAF document SHOULD use another profile,
  e.g. "Security Advisory".

If the element `/product_tree` exists, a user MUST assume that all products mentioned are affected.

## Profile 4: Security Advisory

This profile SHOULD be used to provide information which is related to vulnerabilities and corresponding remediations.

A CSAF document SHALL fulfill the following requirements to satisfy the profile "Security Advisory":

* The following elements MUST exist and be valid:
  * all elements required by the profile "CSAF Base".
  * `/product_tree` which lists all products referenced later on in the CSAF document regardless of their state.
  * `/vulnerabilities` which lists all vulnerabilities.
  * `/vulnerabilities[]/notes`
    > Provides details about the vulnerability.
  * `/vulnerabilities[]/product_status`
    > Lists each product's status in regard to the vulnerability.
  * `/vulnerabilities[]/product_status/known_affected`
    > Lists affected products in regard to the vulnerability.
  * For each product given in `/vulnerabilities[]/product_status/fixed`, the corresponding affected version SHALL be given.
    > Corresponding versions are usually in the same `branches` element.
* The value of `/document/category` SHALL be `csaf_security_advisory`.
* The following elements SHOULD exist:
  * `/vulnerabilities[]/product_status/fixed`
    > Lists fixed products in regard to the vulnerability.
  * `/vulnerabilities[]/remediations`
    > Lists for each affected product in regard to the vulnerability appropriate remediations.

## Profile 5: VEX

This profile SHOULD be used to provide information of the "Vulnerability Exploitability eXchange".
The main purpose of the VEX format is to state that and why a certain product is, or is not, affected by a vulnerability.
See [cite](#VEX) for details.

A CSAF document SHALL fulfill the following requirements to satisfy the profile "VEX":

* The following elements MUST exist and be valid:
  * all elements required by the profile "CSAF Base".
  * `/product_tree` which lists all products referenced later on in the CSAF document regardless of their state.
  * `/vulnerabilities` which lists all vulnerabilities.
  * at least one of
    * `/vulnerabilities[]/product_status/fixed`
    * `/vulnerabilities[]/product_status/known_affected`
    * `/vulnerabilities[]/product_status/known_not_affected`
    * `/vulnerabilities[]/product_status/under_investigation`
  * at least one of
    * `/vulnerabilities[]/cve`
    * `/vulnerabilities[]/ids`
  * `/vulnerabilities[]/notes`
    > Provides details about the vulnerability.
* For each item in
  * `/vulnerabilities[]/product_status/known_not_affected` an impact statement SHALL exist as machine readable flag
    in `/vulnerabilities[]/flags` or as human readable justification in `/vulnerabilities[]/threats`.
    For the latter one, the `category` value for such a statement MUST be `impact` and the `details` field SHALL contain
    a description why the vulnerability cannot be exploited.
  * `/vulnerabilities[]/product_status/known_affected` additional product specific information SHALL be provided
    in `/vulnerabilities[]/remediations` as an action statement.
    Optional, additional information MAY also be provide through `/vulnerabilities[]/notes` and `/vulnerabilities[]/threats`.
    > The use of the categories `no_fix_planned` and `none_available` for an action statement is permitted.
  > Even though Product status lists Product IDs, Product Group IDs can be used in the `remediations` and `threats` object.
  > However, it MUST be ensured that for each Product ID the required information according to its product status as stated
  > in the two points above is available. This implies that all products with the status `known_not_affected` MUST have an
  > impact statement and all products with the status `known_affected` MUST have additional product specific information
  > regardless of whether that is referenced through the Product ID or a Product Group ID.
* The value of `/document/category` SHALL be `csaf_vex`.

## Profile 6: Deprecated Security Advisory

This profile MAY be used to provide information which is related to vulnerabilities and corresponding remediations,
e.g. when converting CSAF documents from older CSAF versions or a human-readable format.
It SHOULD NOT be used for newly created documents.
The profile "Security Advisory" from section [sec]{profiles-profile-4-security-advisory} SHOULD be used instead.

> The definition of the profile "Deprecated Security Advisory" in CSAF 2.1 matches the definition of profile "Security Advisory" in CSAF 2.0.

A CSAF document SHALL fulfill the following requirements to satisfy the profile "Deprecated Security Advisory":

* The following elements MUST exist and be valid:
  * all elements required by the profile "CSAF Base".
  * `/product_tree` which lists all products referenced later on in the CSAF document regardless of their state.
  * `/vulnerabilities` which lists all vulnerabilities.
  * `/vulnerabilities[]/notes`
    > Provides details about the vulnerability.
  * `/vulnerabilities[]/product_status`
    > Lists each product's status in regard to the vulnerability.
* The value of `/document/category` SHALL be `csaf_deprecated_security_advisory`.

## Profile 7: Withdrawn

This profile MUST be used for any CSAF document that is withdrawn. It MUST NOT be used for any superseded document.

A CSAF document SHALL fulfill the following requirements to satisfy the profile "Withdrawn":

* The following elements MUST exist and be valid:
  * all elements required by the profile "CSAF Base".
  * `/document[]/notes` with exactly one item using the `category` `description`
    describing the original content and the reasons for the withdrawal
    > Other items, such as a legal disclaimer, may exist alongside the required one.

    The `title` MUST be `Reasoning for Withdrawal` for English or an unspecified document language.
    For any other language, it SHOULD be the language specific translation of that term.
  * `/document/tracking/revision_history` with at least 2 entries. Any previous items MUST NOT be removed.
    > A CSAF document cannot be withdrawn during the initial release to its specified target group.
    > In such case, the CSAF document should not be released at all.
    > If it was shared previously in draft status, then the `/document/tracking/status` is kept in `draft`.
* The value of `/document/category` SHALL be `csaf_withdrawn`.
* The elements `/product_tree` and `/vulnerabilities` SHALL NOT exist.

The CSAF document MAY link to additional information through `/document/references`.

## Profile 8: Superseded

This profile MUST be used for any CSAF document that is superseded. It MUST NOT be used for any withdrawn document.

A CSAF document SHALL fulfill the following requirements to satisfy the profile "Superseded":

* The following elements MUST exist and be valid:
  * all elements required by the profile "CSAF Base".
  * `/document[]/notes` with exactly one item using the `category` `description`
      > Other items, such as a legal disclaimer, may exist alongside the required one.

    The `title` MUST be `Reasoning for Supersession` for English or an unspecified document language.
    For any other language, it SHOULD be the language specific translation of that term.
  * `/document/tracking/revision_history` with at least 2 entries. Any previous items MUST NOT be removed.
    > A CSAF document cannot be superseded during the initial release to its specified target group.
    > In such case, the CSAF document should not be released at all.
    > If it was shared previously in draft status, then the `/document/tracking/status` is kept in `draft`.
  * `/document/references` containing at least one item with `category` `external`
    The `summary` MUST start with `Superseding Document` for English or an unspecified document language.
    For any other language, it SHOULD be the language specific translation of that term.
* The value of `/document/category` SHALL be `csaf_superseded`.
* The elements `/product_tree` and `/vulnerabilities` SHALL NOT exist.

-------
