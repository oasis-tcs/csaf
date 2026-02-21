#!/bin/bash

SCHEMA=csaf_2.1/json_schema/extension-metaschema.json
META_SCHEMA=csaf_2.1/json_schema/meta.json
VALIDATOR=csaf_2.1/test/validator.py
TESTPATH=$*

FAIL=0

# go to root of git repository
cd `dirname $0`/../../..

validate() {
  printf "%s" "Testing file $1 against schema ${SCHEMA} ... "
  if python3 ${VALIDATOR} ${SCHEMA} $1 ${META_SCHEMA}; then
    printf "%s\n" SUCCESS
  else
    printf "%s\n" FAILED
    FAIL=1
  fi

}

test_all() {
  for i in ${TESTPATH}
  do
    validate $i
  done
}

test_all

exit ${FAIL}
