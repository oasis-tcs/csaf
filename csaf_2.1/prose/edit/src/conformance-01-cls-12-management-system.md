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
