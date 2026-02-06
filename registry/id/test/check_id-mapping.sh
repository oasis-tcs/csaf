#!/bin/bash

SCHEMA=registry/id/schema/id-mapping.schema.json
CSAF_SCHEMA=csaf_2.1/json_schema/csaf.json
META_SCHEMA=csaf_2.1/json_schema/meta.json
ID_REGISTRY_SCHEMA=registry/id/schema/id-registry.schema.json
VALIDATOR=csaf_2.1/test/validator.py
ID_PATH=registry/id/
MAPPING_FILE=id-mapping.json
REGISTRY_FILE=id-registry.json

FAIL=0
REGISTRY_SYSTEM_NAMES=""
MAPPING_SYSTEM_NAMES=""

# go to root of git repository
cd `dirname $0`/../../..

validate() {
  printf "%s" "Testing file $1 against schema ${SCHEMA} ... "
  if python3 $VALIDATOR $SCHEMA $1 ${CSAF_SCHEMA} ${ID_REGISTRY_SCHEMA} ${META_SCHEMA}; then
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

check_contains() {
  printf "%s\n" "Check system name are RVISC ... "
  for i in `echo -e "$1" | sort -u`; do
    printf "\t- %s ... " "$i"
    for j in `echo -e "$2" | sort -u`; do
      # printf "\n\t\t- %s ... " "$j"
      if [ "$i" == "$j" ] ; then
        printf "%s\n" "FOUND"
        continue 2
      fi
    done
    printf "%s\n" "MISSING"
    FAIL=1
  done
}

validate "${ID_PATH}${MAPPING_FILE}"

collect_system_names "${ID_PATH}${REGISTRY_FILE}" ".entries[].system_name" "REGISTRY_SYSTEM_NAMES"
echo "${REGISTRY_SYSTEM_NAMES}" | sed 's/^/\t- /g'

collect_system_names "${ID_PATH}${MAPPING_FILE}" ".entries[].registered_system_name | select( . != null )" "MAPPING_SYSTEM_NAMES"
echo "${MAPPING_SYSTEM_NAMES}" | sed 's/^/\t- /g'

check_uniqueness "${ID_PATH}${MAPPING_FILE}" "${MAPPING_SYSTEM_NAMES}"

check_contains "${MAPPING_SYSTEM_NAMES}" "${REGISTRY_SYSTEM_NAMES}"

exit ${FAIL}
