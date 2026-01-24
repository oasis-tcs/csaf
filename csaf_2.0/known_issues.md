# List of known issues in CSAF 2.0

## List of issues fixed by Errata 01

- The [aggregator_json_schema.json](./json_schema/aggregator_json_schema.json) has a typo as it states that the field `mirror` is
  required in [line 178](https://github.com/oasis-tcs/csaf/blob/5757eeb192f30dbf1752d15365e335c3408ce4df/csaf_2.0/json_schema/aggregator_json_schema.json#L178),
  but the field is actually named `mirrors` in [line 187](https://github.com/oasis-tcs/csaf/blob/5757eeb192f30dbf1752d15365e335c3408ce4df/csaf_2.0/json_schema/aggregator_json_schema.json#L187).
  This was fixed in [936f338](https://github.com/oasis-tcs/csaf/commit/936f338f0d57da21852e10937f72c8f8fa6bcfe7).

## List of issues not addressed in an Errata

- The CPE pattern is not anchored correctly which allows invalid CPEs.
  See [#693](https://github.com/oasis-tcs/csaf/issues/693).
  Addressed in CSAF 2.0 through the [FAQ](./guidance/faq.md#the-cpe-pattern-changed-from-csaf-20-to-csaf-21-why).
- The prose mentions in different places `/document/language` and `/$defs/language_t` which are not defined in the schema.
  See [#897](https://github.com/oasis-tcs/csaf/issues/897).
- The tests 6.1.1 and 6.1.4 are missing the `flags` path.
  See [#909](https://github.com/oasis-tcs/csaf/issues/909).
- Example 42 lists `Cisco AnyConnect Secure Mobility Client 4.9.04053`.
  However, in the product formed by the relationship the version is `2.3.185`.
  Even though this is not impossible it creates confusion as it is not explained in detail.
  See [#926](https://github.com/oasis-tcs/csaf/issues/926).
- In [section 3.2.3.9 Product Status](https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html#3239-vulnerabilities-property---product-status),
  the standard does not mention `flags` as a potential source for more information regarding the reasoning for `known_not_affected`.
  See [#935](https://github.com/oasis-tcs/csaf/issues/935).
- The link in the reference to [VERS](https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html#vers) is not longer working.
  See [#1117](https://github.com/oasis-tcs/csaf/issues/1117).
- The test description of [test 6.1.26](https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html#6126-prohibited-document-category-name)
  does not clearly state that given matching and preprocessing rules apply for names and values.
  Also, it does not provide guidance regarding the dash characters.
  See [#1250](https://github.com/oasis-tcs/csaf/issues/1250).
