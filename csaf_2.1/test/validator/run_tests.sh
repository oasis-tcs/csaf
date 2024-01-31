#!/bin/bash

STRICT_BUILD=csaf_2.1/build
ORIG_SCHEMA=csaf_2.1/json_schema/csaf_json_schema.json
CSAF_STRICT_SCHEMA=${STRICT_BUILD}/csaf_strict_schema.json
CVSS_20_STRICT_SCHEMA=csaf_2.1/referenced_schema/first/cvss-v2.0_strict.json
CVSS_30_STRICT_SCHEMA=csaf_2.1/referenced_schema/first/cvss-v3.0_strict.json
CVSS_31_STRICT_SCHEMA=csaf_2.1/referenced_schema/first/cvss-v3.1_strict.json
VALIDATOR=csaf_2.1/test/validator.py
STRICT_GENERATOR=csaf_2.1/test/generate_strict_schema.py
TESTPATH=csaf_2.1/test/validator/data/$1/*.json
EXCLUDE=oasis_csaf_tc-csaf_2_1-2024-6-1-08-01.json
EXCLUDE_STRICT=oasis_csaf_tc-csaf_2_1-2024-6-2-20-01.json

FAIL=0

# go to root of git repository
cd `dirname $0`/../../..

validate() {
  printf "%s" "Testing file $1 against schema ${SCHEMA} ... "
  if python3 $VALIDATOR $SCHEMA $1 ${CVSS_20_STRICT_SCHEMA} ${CVSS_30_STRICT_SCHEMA} ${CVSS_31_STRICT_SCHEMA}; then
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
mkdir -p ${STRICT_BUILD}
python3 "${STRICT_GENERATOR}" "${ORIG_SCHEMA}" > "${CSAF_STRICT_SCHEMA}"
printf "%s\n" "done"

SCHEMA=${CSAF_STRICT_SCHEMA}
test_all_strict

exit ${FAIL}
