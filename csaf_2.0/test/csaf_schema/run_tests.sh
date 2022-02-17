#!/bin/bash

ORIG_SCHEMA=csaf_2.0/json_schema/csaf_json_schema.json 
STRICT_SCHEMA=csaf_strict_schema.json
VALIDATOR=csaf_2.0/test/validator.py
STRICT_GENERATOR=csaf_2.0/test/generate_strict_schema.py

FAIL=0

# go to root of git repository
cd `dirname $0`/../../..

validate() {
  echo -n "Testing file $1 against schema $SCHEMA ... "
  if python3 $VALIDATOR $SCHEMA $1; then
    echo SUCCESS
  else
    echo FAILED
    FAIL=1
  fi

}

SCHEMA=$ORIG_SCHEMA
for i in `ls -1 csaf_2.0/examples/csaf/*.json`
do
  validate $i
done

 
echo -n "Generating strict schema ... "
python3 $STRICT_GENERATOR $ORIG_SCHEMA > $STRICT_SCHEMA
echo done

SCHEMA=$STRICT_SCHEMA
for i in `ls -1 csaf_2.0/examples/csaf/*.json`
do
  validate $i
done

exit $FAIL
