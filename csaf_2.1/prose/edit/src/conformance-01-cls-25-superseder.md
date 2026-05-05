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
