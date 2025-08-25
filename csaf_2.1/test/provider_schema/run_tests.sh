#!/bin/bash

STRICT_BUILD=csaf_2.1/build
ORIG_SCHEMA=csaf_2.1/json_schema/provider.json
CSAF_STRICT_SCHEMA=${STRICT_BUILD}/csaf_strict_schema.json
CVSS_20_STRICT_SCHEMA=csaf_2.1/referenced_schema/first/cvss-v2.0_strict.json
CVSS_30_STRICT_SCHEMA=csaf_2.1/referenced_schema/first/cvss-v3.0_strict.json
CVSS_31_STRICT_SCHEMA=csaf_2.1/referenced_schema/first/cvss-v3.1_strict.json
CVSS_40_STRICT_SCHEMA=csaf_2.1/referenced_schema/first/cvss-v4.0.1_strict.json
META_SCHEMA=csaf_2.1/json_schema/meta.json
PROVIDER_STRICT_SCHEMA=${STRICT_BUILD}/provider_strict_schema.json
SSVC_101_DP_SCHEMA=csaf_2.1/referenced_schema/certcc/Decision_Point-1-0-1.schema.json
SSVC_101_DPVS_SCHEMA=csaf_2.1/referenced_schema/certcc/Decision_Point_Value_Selection-1-0-1.schema.json
VALIDATOR=csaf_2.1/test/validator.py
STRICT_GENERATOR=csaf_2.1/test/generate_strict_schema.py
TESTPATH=csaf_2.1/examples/provider-metadata/*.json

FAIL=0

# go to root of git repository
cd `dirname $0`/../../..

validate() {
  printf "%s" "Testing file $1 against schema ${SCHEMA} ... "
  if python3 ${VALIDATOR} ${SCHEMA} $1 ${CSAF_STRICT_SCHEMA} ${CVSS_20_STRICT_SCHEMA} ${CVSS_30_STRICT_SCHEMA} ${CVSS_31_STRICT_SCHEMA} ${CVSS_40_STRICT_SCHEMA} ${META_SCHEMA} ${SSVC_101_DPVS_SCHEMA} ${SSVC_101_DP_SCHEMA}; then
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
mkdir -p ${STRICT_BUILD}
python3 "${STRICT_GENERATOR}" "${ORIG_SCHEMA}" > "${PROVIDER_STRICT_SCHEMA}"
printf "%s\n" "done"

SCHEMA=${PROVIDER_STRICT_SCHEMA}
test_all

exit ${FAIL}
