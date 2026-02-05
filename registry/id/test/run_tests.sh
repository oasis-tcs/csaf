#!/bin/bash

SCHEMA=registry/id/schema/id-registry.schema.json
META_SCHEMA=csaf_2.1/json_schema/meta.json
VALIDATOR=csaf_2.1/test/validator.py
STRICT_GENERATOR=csaf_2.1/test/generate_strict_schema.py
TESTPATH=registry/id/
TESTFILE=id-registry.json

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
