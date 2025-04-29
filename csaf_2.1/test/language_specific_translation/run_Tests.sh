#!/bin/bash

SCHEMA=csaf_2.1/test/language_specific_translation/translations_json_schema.json
META_SCHEMA=csaf_2.1/json_schema/meta_json_schema.json
VALIDATOR=csaf_2.1/test/validator.py
TESTPATH=csaf_2.1/language_specific_translation/
TESTFILE=translations.json

FAIL=0

# go to root of git repository
cd `dirname $0`/../../..

validate() {
  printf "%s" "Testing file $1 against schema ${SCHEMA} ... "
  if python3 $VALIDATOR $SCHEMA $1 ${META_SCHEMA}; then
    printf "%s\n" SUCCESS
  else
    printf "%s\n" FAILED
    FAIL=1
  fi

}

validate "${TESTPATH}${TESTFILE}"

exit ${FAIL}
