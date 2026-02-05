#!/bin/bash

SCHEMA=registry/id/schema/id-registry.schema.json
CSAF_SCHEMA=csaf_2.1/json_schema/csaf.json
META_SCHEMA=csaf_2.1/json_schema/meta.json
VALIDATOR=csaf_2.1/test/validator.py
TESTPATH=registry/id/
TESTFILE=id-registry.json

FAIL=0

# go to root of git repository
cd `dirname $0`/../../..

validate() {
  printf "%s" "Testing file $1 against schema ${SCHEMA} ... "
  if python3 $VALIDATOR $SCHEMA $1 ${CSAF_SCHEMA} ${META_SCHEMA}; then
    printf "%s\n" SUCCESS
  else
    printf "%s\n" FAILED
    FAIL=1
  fi

}

validate "${TESTPATH}${TESTFILE}"

exit ${FAIL}
