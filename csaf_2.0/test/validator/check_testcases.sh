#!/bin/bash

SCHEMA=csaf_2.0/test/validator/testcases_json_schema.json 
VALIDATOR=csaf_2.0/test/validator.py
TESTPATH=csaf_2.0/test/validator/data/testcases.json

FAIL=0

# go to root of git repository
cd `dirname $0`/../../..

validate() {
  printf "%s" "Testing file $1 against schema ${SCHEMA} ... "
  if python3 $VALIDATOR $SCHEMA $1; then
    printf "%s\n" SUCCESS
  else
    printf "%s\n" FAILED
    FAIL=1
  fi

}

validate ${TESTPATH}

exit ${FAIL}
