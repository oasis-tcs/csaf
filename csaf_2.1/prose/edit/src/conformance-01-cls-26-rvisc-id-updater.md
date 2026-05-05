### Conformance Clause 26: CSAF RVISC ID Updater

A program satisfies the "CSAF RVISC ID Updater" conformance profile if the program fulfills the two following groups of requirements:

The program:

* satisfies the "CSAF Post-Processor" conformance profile.
* applies the corresponding assignment from [cite](#RVISC-M) to each item in `/vulnerabilities[]/ids[]`
  whose `system_name` is not contained in [cite](#RVISC-R).
* applies the corresponding assignment from [cite](#RVISC-M) to each item in `/vulnerabilities[]/ids[]`
  whose `system_name` is contained in [cite](#RVISC-R) but the `text` does not conform the entry.
* satisfies the normative requirements given below.

The program SHALL provide the following options:

* an option to insert an automatically generated revision history entry detailing the changes applied and
  make necessary updates to elements in `/document/tracking` (commit mode).
* an option to set selected or all parameters for the commit mode manually which take precedence over the automated generated values.
* an option to do a dry-run which does not apply the changes but just displays them.
* an option to interactively accept or discard changes.
* an option to ignore certain values for `system_name`.
* an option to output all items in `/vulnerabilities[]/ids[]` whose `system_name` is not contained in [cite](#RVISC-R).
* an option to output all items in `/vulnerabilities[]/ids[]` whose `system_name` is contained in [cite](#RVISC-R)
  but the `text` does not conform the entry.
* an option to map an existing `system_name` to a new value or apply a transformation to a `text`
  based on the `system_name` value and a `precondition`.
