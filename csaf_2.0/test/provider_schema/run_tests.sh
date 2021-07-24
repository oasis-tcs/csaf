#!/bin/bash

ORIG_SCHEMA=csaf_2.0/json_schema/provider_json_schema.json
CSAF_STRICT_SCHEMA=csaf_strict_schema.json 
PROVIDER_STRICT_SCHEMA=provider_strict_schema.json
VALIDATOR=csaf_2.0/test/validator.py
STRICT_GENERATOR=csaf_2.0/test/generate_strict_schema.py

FAIL=0

# go to root of git repository
cd `dirname $0`/../../..

validate() {
  echo -n "Testing file $1 against schema $SCHEMA ... "
  if python3 $VALIDATOR $SCHEMA $1 $CSAF_STRICT_SCHEMA; then
    echo SUCCESS
  else
    echo FAILED
    FAIL=1
  fi

}

SCHEMA=$ORIG_SCHEMA
validate csaf_2.0/examples/provider-metadata/example-01-provider-metadata.json
 
echo -n "Generating strict schema ... "
python3 $STRICT_GENERATOR $ORIG_SCHEMA > $PROVIDER_STRICT_SCHEMA
echo done

SCHEMA=$PROVIDER_STRICT_SCHEMA
validate csaf_2.0/examples/provider-metadata/example-01-provider-metadata.json

exit $FAIL
