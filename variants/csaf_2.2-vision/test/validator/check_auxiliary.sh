#!/bin/bash

STRICT_BUILD=csaf_2.1/build
SSVC_STRICT_SCHEMA=${STRICT_BUILD}/DecisionPoint_2_0_0_strict.schema.json
SSVC_200_DP_SCHEMA=csaf_2.1/referenced_schema/certcc/DecisionPoint_2_0_0.schema.json
VALIDATOR=csaf_2.1/test/validator.py
STRICT_GENERATOR=csaf_2.1/test/generate_strict_schema.py
TESTPATH=csaf_2.1/test/validator/auxiliary/ssvc/$1/*.json

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
  for i in $(ls -1 ${TESTPATH})
  do
    validate $i
  done
}

SCHEMA=$SSVC_200_DP_SCHEMA
test_all

printf "%s" "Generating strict schema ... "
mkdir -p ${STRICT_BUILD}
python3 "${STRICT_GENERATOR}" "${SSVC_200_DP_SCHEMA}" > "${SSVC_STRICT_SCHEMA}"
printf "%s\n" "done"

SCHEMA=${SSVC_STRICT_SCHEMA}
test_all

exit ${FAIL}
