#!/bin/bash

ORIG_SCHEMA=csaf_2.0/json_schema/aggregator_json_schema.json
AGGREGATOR_STRICT_SCHEMA=aggregator_strict_schema.json
CSAF_STRICT_SCHEMA=csaf_strict_schema.json 
PROVIDER_STRICT_SCHEMA=provider_strict_schema.json
VALIDATOR=csaf_2.0/test/validator.py
STRICT_GENERATOR=csaf_2.0/test/generate_strict_schema.py
TESTPATH=csaf_2.0/examples/aggregator/*.json

FAIL=0

# go to root of git repository
cd `dirname $0`/../../..

validate() {
  printf "%s" "Testing file $1 against schema ${SCHEMA} ... "
  if python3 ${VALIDATOR} ${SCHEMA} $1 ${CSAF_STRICT_SCHEMA} ${PROVIDER_STRICT_SCHEMA}; then
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

SCHEMA=${ORIG_SCHEMA}
test_all
 
printf "%s" "Generating strict schema ... "
python3 "${STRICT_GENERATOR}" "${ORIG_SCHEMA}" > "${AGGREGATOR_STRICT_SCHEMA}"
printf "%s\n" "done"

SCHEMA=${AGGREGATOR_STRICT_SCHEMA}
test_all

exit ${FAIL}
