#!/bin/bash

SCHEMA=csaf_2.1/json_schema/csaf.json
VALIDATOR=csaf_2.1/test/cpe/test-regex.js
DATA_VALID=csaf_2.1/test/cpe/data/valid/cpe.txt
DATA_INVALID=csaf_2.1/test/cpe/data/invalid/cpe.txt

FAIL=0

# go to root of git repository
cd "$(dirname "$0")"/../../.. || exit


validate() {
  printf "Testing file %s against cpe regex from %s ... \n" "$1" "$SCHEMA"
  if node "$VALIDATOR" "$SCHEMA" "$1" "$2"; then
    printf "SUCCESS\n"
  else
    printf "FAILED\n"
    FAIL=1
  fi

}

echo -n "Test conforming (not necessary existing) CPEs... "
DATA=$DATA_VALID
validate $DATA true
printf "done\n"

echo -n "Test non-conforming CPEs... "
DATA=$DATA_INVALID
validate $DATA false
printf "done\n"


exit $FAIL
