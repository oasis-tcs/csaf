#!/bin/bash

SCHEMA=registry/id/schema/id-registry.schema.json
CSAF_SCHEMA=csaf_2.1/json_schema/csaf.json
META_SCHEMA=csaf_2.1/json_schema/meta.json
VALIDATOR=csaf_2.1/test/validator.py
ID_PATH=registry/id/
REGISTRY_FILE=id-registry.json

REGISTRY_SYSTEM_NAMES=""
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

collect_system_names() {
  printf "%s" "Collect list of registered system names in $1 ... "
  SYSTEM_NAME=$(jq "${2}" $1 -r)
  declare -g $3="$(echo -e "${SYSTEM_NAME}")"
  printf "%s\n" "DONE"
}

check_uniqueness() {
  printf "%s" "Check uniqueness of system names in $1 ... "
  if [ $(echo -e "$2" | wc -l) -eq $(echo "$2" | sort -u | wc -l) ] ; then
    printf "%s\n" SUCCESS
  else
    printf "%s\n" FAILED
    FAIL=1
  fi
}


validate "${ID_PATH}${REGISTRY_FILE}"

collect_system_names "${ID_PATH}${REGISTRY_FILE}" ".entries[].system_name" "REGISTRY_SYSTEM_NAMES"
echo "${REGISTRY_SYSTEM_NAMES}" | sed 's/^/\t- /g'

check_uniqueness "${ID_PATH}${REGISTRY_FILE}" "${REGISTRY_SYSTEM_NAMES}"

exit ${FAIL}
