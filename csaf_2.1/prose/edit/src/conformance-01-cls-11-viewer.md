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
