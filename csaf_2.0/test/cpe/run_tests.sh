#!/bin/bash

SCHEMA=csaf_2.0/json_schema/csaf_json_schema.json
VALIDATOR=csaf_2.0/test/cpe/test-regex.js
CPE_BASE_URL=https://nvd.nist.gov/feeds/xml/cpe/dictionary/
CPE_2_3=official-cpe-dictionary_v2.3
CPE_2_2=official-cpe-dictionary_v2.2

FAIL=0

# go to root of git repository
cd "$(dirname "$0")"/../../.. || exit

get_dictionary() {
  rm "${2}"*
  wget "$1$2"
  gunzip -f "$2"
}

prepare_23_dictionary() {
  # Get CPE 2.3 fields
  # Correctly decode special characters
  grep '<cpe-23:cpe23-item name=' "$CPE".xml | sed -e 's/^.*<cpe-23:cpe23-item name="//' -e 's/"\/\?>$//' \
    | sed -e 's/\\&amp;/\\\&/g' \
    | sed -e 's/\\&quot;/\\"/g' \
    > "$CPE".txt
}

prepare_22_dictionary() {
  # Get CPE 2.2 fields
  # Correctly decode special characters
  grep '<cpe-item name=' "$CPE".xml | sed -e 's/^.*<cpe-item name="//' -e 's/">$//' > "$CPE".txt
}

validate() {
  printf "Testing file %s against cpe regex from %s ... \n" "$1" "$SCHEMA"
  if node "$VALIDATOR" "$SCHEMA" "$1"; then
    printf "SUCCESS\n"
  else
    printf "FAILED\n"
    FAIL=1
  fi

}

echo -n "Test CPE 2.3 ... "
CPE=$CPE_2_3
get_dictionary $CPE_BASE_URL ${CPE}.xml.gz
prepare_23_dictionary $CPE
validate $CPE.txt
printf "done\n"

echo -n "Test CPE 2.2 ... "
CPE=$CPE_2_2
get_dictionary $CPE_BASE_URL ${CPE}.xml.gz
prepare_22_dictionary $CPE
validate $CPE.txt
printf "done\n"


exit $FAIL
