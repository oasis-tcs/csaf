#!/bin/bash

STRICT_BUILD=csaf_2.1/build
ORIG_SCHEMA=csaf_2.1/json_schema/csaf_json_schema.json
CSAF_STRICT_SCHEMA=${STRICT_BUILD}/csaf_strict_schema.json
CVSS_20_STRICT_SCHEMA=csaf_2.1/referenced_schema/first/cvss-v2.0_strict.json
CVSS_30_STRICT_SCHEMA=csaf_2.1/referenced_schema/first/cvss-v3.0_strict.json
CVSS_31_STRICT_SCHEMA=csaf_2.1/referenced_schema/first/cvss-v3.1_strict.json
CVSS_40_STRICT_SCHEMA=csaf_2.1/referenced_schema/first/cvss-v4.0_strict.json
SSVC_101_DP_SCHEMA=csaf_2.1/referenced_schema/certcc/Decision_Point-1-0-1.schema.json
SSVC_101_DPVS_SCHEMA=csaf_2.1/referenced_schema/certcc/Decision_Point_Value_Selection-1-0-1.schema.json
VALIDATOR=csaf_2.1/test/validator.py
STRICT_GENERATOR=csaf_2.1/test/generate_strict_schema.py
TESTPATH=csaf_2.1/test/validator/data/$1/*.json
EXCLUDE='oasis_csaf_tc-csaf_2_1-2024-6-1-08-01.json|oasis_csaf_tc-csaf_2_1-2024-6-1-08-02.json|oasis_csaf_tc-csaf_2_1-2024-6-1-08-03.json|oasis_csaf_tc-csaf_2_1-2024-6-1-08-04.json|oasis_csaf_tc-csaf_2_1-2024-6-1-09-05.json|oasis_csaf_tc-csaf_2_1-2024-6-1-37-01.json|oasis_csaf_tc-csaf_2_1-2024-6-1-37-02.json|oasis_csaf_tc-csaf_2_1-2024-6-1-37-03.json|oasis_csaf_tc-csaf_2_1-2024-6-1-37-04.json|oasis_csaf_tc-csaf_2_1-2024-6-1-37-05.json|oasis_csaf_tc-csaf_2_1-2024-6-1-37-06.json|oasis_csaf_tc-csaf_2_1-2024-6-1-46-01.json|oasis_csaf_tc-csaf_2_1-2024-6-1-46-02.json|oasis_csaf_tc-csaf_2_1-2024-6-2-10-01.json|oasis_csaf_tc-csaf_2_1-2024-6-2-20-01.json|oasis_csaf_tc-csaf_2_1-2024-6-2-20-02.json'
EXCLUDE_LEAP='oasis_csaf_tc-csaf_2_1-2024-6-1-37-12.json|oasis_csaf_tc-csaf_2_1-2024-6-1-37-13.json|oasis_csaf_tc-csaf_2_1-2024-6-1-37-14.json'

FAIL=0

# go to root of git repository
cd `dirname $0`/../../..

validate() {
  printf "%s" "Testing file $1 against schema ${SCHEMA} ... "
  if python3 $VALIDATOR $SCHEMA $1 ${CVSS_20_STRICT_SCHEMA} ${CVSS_30_STRICT_SCHEMA} ${CVSS_31_STRICT_SCHEMA} ${CVSS_40_STRICT_SCHEMA} ${SSVC_101_DPVS_SCHEMA} ${SSVC_101_DP_SCHEMA}; then
    printf "%s\n" SUCCESS
  else
    printf "%s\n" FAILED
    FAIL=1
  fi

}

test_all() {
  for i in $(ls -1 ${TESTPATH} | grep -Ev "${EXCLUDE}" | grep -Ev "${EXCLUDE_LEAP}")
  do
    validate $i
  done
}

test_all_strict() {
  for i in $(ls -1 ${TESTPATH} | grep -Ev "${EXCLUDE}" | grep -Ev "${EXCLUDE_LEAP}" )
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
