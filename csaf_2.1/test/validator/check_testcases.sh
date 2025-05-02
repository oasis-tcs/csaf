#!/bin/bash

SCHEMA=csaf_2.1/test/validator/testcases_json_schema.json
META_SCHEMA=csaf_2.1/json_schema/meta_json_schema.json
VALIDATOR=csaf_2.1/test/validator.py
TESTPATH=csaf_2.1/test/validator/data/
TESTFILE=testcases.json

FAIL=0
DIRFILES=""
TESTFILES=""

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

collect_dir_files() {
  printf "%s\n" "Collect list of files in $1 ... "
  cd $1
  DIRFILES=$(ls -1 */*.json | sort)
}

collect_test_files() {
  printf "%s\n" "Collect list of files in $1 ..."
  NEGATIVE=$(jq '.tests[].failures[].name' $1 -r)
  POSITIVE=$(jq '.tests[].valid[]?.name' $1 -r)
  TESTFILES=$(echo -e "${NEGATIVE}\n${POSITIVE}" | sort)
}

check_files_exist() {
  printf "%s" "Testing files in ${TESTPATH} and ${TESTFILE} are the same... "
    if diff -b <(echo "$1") <(echo "$2"); then
    printf "%s\n" SUCCESS
  else
    printf "%s\n" FAILED
    FAIL=1
  fi
}

validate "${TESTPATH}${TESTFILE}"
collect_dir_files ${TESTPATH}
collect_test_files "${TESTFILE}"
check_files_exist "${DIRFILES}" "${TESTFILES}"


exit ${FAIL}
