#!/bin/bash

ORIG_SCHEMA=csaf_2.0/json_schema/csaf_json_schema.json 
STRICT_SCHEMA=csaf_strict_schema.json
VALIDATOR=csaf_2.0/test/validator.py
STRICT_GENERATOR=csaf_2.0/test/generate_strict_schema.py
TESTPATH=csaf_2.0/test/validator/data/$1/*.json
EXCLUDE=OASIS_CSAF_TC-CSAF_2_0-2021-6-1-08-01.json
EXCLUDE_STRICT=OASIS_CSAF_TC-CSAF_2_0-2021-6-2-20-01.json

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

test_all() {
  for i in $(ls -1 ${TESTPATH} | grep -v $EXCLUDE)
  do
    validate $i
  done
}

test_all_strict() {
  for i in $(ls -1 ${TESTPATH} | grep -v $EXCLUDE | grep -v ${EXCLUDE_STRICT})
  do
    validate $i
  done
} 

SCHEMA=$ORIG_SCHEMA
test_all

 
printf "%s" "Generating strict schema ... "
python3 "${STRICT_GENERATOR}" "${ORIG_SCHEMA}" > "${STRICT_SCHEMA}"
printf "%s\n" "done"

SCHEMA=${STRICT_SCHEMA}
test_all_strict

exit ${FAIL}
