#!/bin/bash

ORIG_SCHEMA=csaf_2.0/json_schema/csaf_json_schema.json 
STRICT_SCHEMA=csaf_strict_schema.json
CVSS_20_STRICT_SCHEMA=csaf_2.0/referenced_schema/first/cvss-v2.0_strict.json
CVSS_30_STRICT_SCHEMA=csaf_2.0/referenced_schema/first/cvss-v3.0_strict.json
CVSS_31_STRICT_SCHEMA=csaf_2.0/referenced_schema/first/cvss-v3.1_strict.json
VALIDATOR=csaf_2.0/test/validator.py
STRICT_GENERATOR=csaf_2.0/test/generate_strict_schema.py
TESTPATH=csaf_2.0/examples/csaf/$1/*.json

FAIL=0

# go to root of git repository
cd `dirname $0`/../../..

validate() {
  printf "%s" "Testing file $1 against schema ${SCHEMA} ... "
  if python3 ${VALIDATOR} ${SCHEMA} $1 ${CVSS_20_STRICT_SCHEMA} ${CVSS_30_STRICT_SCHEMA} ${CVSS_31_STRICT_SCHEMA}; then
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
python3 "${STRICT_GENERATOR}" "${ORIG_SCHEMA}" > "${STRICT_SCHEMA}"
printf "%s\n" "done"

SCHEMA=${STRICT_SCHEMA}
test_all

exit ${FAIL}
