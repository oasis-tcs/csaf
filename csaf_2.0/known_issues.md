# List of known issues in CSAF 2.0

## List of issues fixed by Errata 01

- The [aggregator_json_schema.json](./json_schema/aggregator_json_schema.json) has a typo as it states that the field `mirror` is
  required in [line 178](https://github.com/oasis-tcs/csaf/blob/5757eeb192f30dbf1752d15365e335c3408ce4df/csaf_2.0/json_schema/aggregator_json_schema.json#L178),
  but the field is actually named `mirrors` in [line 187](https://github.com/oasis-tcs/csaf/blob/5757eeb192f30dbf1752d15365e335c3408ce4df/csaf_2.0/json_schema/aggregator_json_schema.json#L187).
  This was fixed in [936f338](https://github.com/oasis-tcs/csaf/commit/936f338f0d57da21852e10937f72c8f8fa6bcfe7).

## List of isses not addressed in an Errata

- The CPE pattern is not anchored correctly which allows invalid CPEs.
  See [#693](https://github.com/oasis-tcs/csaf/issues/693).
  Addressed in CSAF 2.0 through the [FAQ](./guidance/faq.md#the-cpe-pattern-changed-from-csaf-20-to-csaf-21-why).
- The prose mentions in different places `/document/language` and `/$defs/language_t` which are not defined in the schema.
  See [#897](https://github.com/oasis-tcs/csaf/issues/897).
  