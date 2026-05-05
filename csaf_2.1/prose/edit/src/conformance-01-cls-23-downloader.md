### Conformance Clause 23: CSAF Downloader

A program satisfies the "CSAF Downloader" conformance profile if the program:

* conforms to the process defined in section [sec](#retrieving-rules) by executing all parts that are applicable to the given role.
* supports directory-based and ROLIE-based retrieval.
* is able to execute both steps from section [sec](#retrieving-rules) separately.
* uses a program-specific HTTP User Agent, e.g. consisting of the name and version of the program.
* satisfies those normative requirements in section [sec](#distributing-csaf-documents) that are designated as applying to CSAF Downloaders.

> A tool MAY implement an option to store CSAF Documents that fail any of the steps in section [sec](#retrieving-csaf-documents).
