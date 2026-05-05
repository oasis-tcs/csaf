### Conformance Clause 9: CSAF Translator

A program satisfies the "CSAF Translator" conformance profile if the program fulfills the two following groups of requirements:

The program:

* satisfies the "CSAF Post-Processor" conformance profile.
* translates at least one value.
* preserves the same semantics and form across translations.
* satisfies the normative requirements given below and does not add or remove other elements than required below.

The resulting translated document:

* does not use the same `/document/tracking/id` as the original document.
  The translated document can use a completely new `/document/tracking/id` or compute one by using the original `/document/tracking/id` as
  a prefix and adding an ID from the naming scheme of the issuer of the translated version.
  It SHOULD NOT use the original `/document/tracking/id` as a suffix.
  If an issuer uses a CSAF Translator to publish his advisories in multiple languages they MAY use the combination of
  the original `/document/tracking/id` and translated `/document/lang` as a `/document/tracking/id` for the translated document.

  > Note that the term "publish" is used in this conformance profile independent of whether the specified target group is the public
    or a closed group.

* provides the `/document/lang` property with a value matching the language of the translation.
* provides the `/document/source_lang` to contain the language of the original document (and SHOULD only be set by CSAF Translators).
* has the value `translator` set in `/document/publisher/category`
* includes a reference to the original advisory as first element of the array `/document/references[]`.
* MAY contain translations for elements in arrays of `references_t` after the first element.
  However, it SHALL keep the original URLs as references at the end.
