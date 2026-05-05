### Conformance Clause 21: CSAF Library with Extended Validation

A CSAF Library satisfies the "CSAF Library with Extended Validation" conformance profile if the CSAF Library:

* satisfies the "CSAF Library" conformance profile.
* satisfies the "CSAF Extended Validator" conformance profile.
* validates the CSAF Document before output according to the "CSAF Extended Validator" and presents the validation result accordingly.
* provide a function to validate the data structure in its current state according to the "CSAF Extended Validator" and presents the validation
  result accordingly.

A CSAF Library does not satisfies the "CSAF Library with Extended Validation" conformance profile if the CSAF Library uses an external library or
program for the "CSAF Extended Validator" part and does not enforce its presence.
