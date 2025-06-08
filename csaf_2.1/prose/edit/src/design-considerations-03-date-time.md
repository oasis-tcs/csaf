## Date and Time

This standard uses the `date-time` format as defined in JSON Schema Draft 2020-12 Section 7.3.1.
In accordance with [cite](#RFC3339) and [cite](#ISO8601-1), the following rules apply:

* The letter `T` separating the date and time SHALL be upper case.
* The separator between date and time MUST be the letter `T`.
* The letter `Z` indicating the timezone UTC SHALL be upper case.
* Fractions of seconds are allowed as specified in the standards mention above with the full stop (`.`) as separator.
* Leap seconds MUST NOT be used.

  > While a full support of RFC 3339 would be preferred, significant challenges have been mentioned by implementers as most libraries are lacking
  > the support for leap seconds.
  > To ensure interoperability, the decision was made to prohibit leap seconds.

Empty timezones MUST NOT be used.
* The ABNF of RFC 3339, section 5.6 applies.

-------
