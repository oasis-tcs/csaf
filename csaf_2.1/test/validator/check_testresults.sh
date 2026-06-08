#!/bin/bash

SCHEMA=csaf_2.1/test/validator/testresult_json_schema.json
TESTCASES_SCHEMA=csaf_2.1/test/validator/testcases_json_schema.json
META_SCHEMA=csaf_2.1/json_schema/meta.json
VALIDATOR=csaf_2.1/test/validator.py
TESTPATH=csaf_2.1/test/validator/data/$1/*.result.json

FAIL=0

# go to root of git repository
cd `dirname $0`/../../..

validate() {
  printf "%s" "Testing file $1 against schema ${SCHEMA} ... "
  if python3 $VALIDATOR $SCHEMA $1 ${META_SCHEMA} ${TESTCASES_SCHEMA}; then
    printf "%s\n" SUCCESS
  else
    printf "%s\n" FAILED
    FAIL=1
  fi

}

test_all() {
  for i in $(ls -1 ${TESTPATH})
  do
    validate $i
  done
}

test_all

exit ${FAIL}
