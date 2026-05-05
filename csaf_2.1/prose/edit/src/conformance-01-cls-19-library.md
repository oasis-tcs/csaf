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
* provides a function to generate a `full_product_name_t/name` within `branches` through concatenating the `name` values separated by white space
  of the elements along the path towards this leaf.
* provides a function to generate a combined subpath name for an element of type `subpath_t` through concatenating separated by white space:
  * the `category` with `_` replaced by white space and
  * the `name` value of the product identified by the Product ID in `next_product_reference`.
* provides a function to generate a `full_product_name_t/name` within `product_paths` through concatenating separated by white space:
  * the `name` value of the product identified by the Product ID in `beginning_product_reference` and
  * the combined subpath name for all elements in `subpaths` in their order.
* calculates the CVSS scores and severities for existing data for all CVSS versions.
* validates the CVSS scores and severities for existing data for all CVSS versions.

> The library MAY implement an option to retrieve the keys unsorted.
