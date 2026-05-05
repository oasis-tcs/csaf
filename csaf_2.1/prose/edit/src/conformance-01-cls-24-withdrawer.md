### Conformance Clause 24: CSAF Withdrawer

A program satisfies the "CSAF Withdrawer" conformance profile if the program:

* satisfies the "CSAF Post-Processor" conformance profile.
* keeps the original `/document/tracking/id`.
* adds a new item to the revision history stating the revision metadata of the withdrawal.
* adds the reasoning for withdrawal as specified in section [sec](#profile-7-withdrawn).
* removes the `/product_tree`.
* removes the `/vulnerabilities`.

> A tool MAY implement an option to additionally remove any element that would hinder the production of a valid CSAF.
