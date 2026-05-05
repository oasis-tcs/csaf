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
  In this case, there SHALL be a _Group configurator_ which is able to change the values which are used to prefill fields in
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
