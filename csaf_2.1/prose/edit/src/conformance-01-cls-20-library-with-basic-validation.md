### Conformance Clause 20: CSAF Library with Basic Validation

A CSAF Library satisfies the "CSAF Library with Basic Validation" conformance profile if the CSAF Library:

* satisfies the "CSAF Library" conformance profile.
* satisfies the "CSAF Basic Validator" conformance profile.
* validates the CSAF Document before output according to the "CSAF Basic Validator" and presents the validation result accordingly.
* provide a function to validate the data structure in its current state according to the "CSAF Basic Validator" and presents the validation
  result accordingly.

A CSAF Library does not satisfies the "CSAF Library with Basic Validation" conformance profile if the CSAF Library uses an external library or
program for the "CSAF Basic Validator" part and does not enforce its presence.
