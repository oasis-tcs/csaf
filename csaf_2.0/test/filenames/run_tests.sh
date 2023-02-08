#!/bin/bash

CHECK=csaf_2.0/test/filenames/check.py
TESTPATH=$*

FAIL=0

# go to root of git repository
cd `dirname $0`/../../..

check() {
  printf "%s" "Testing filename of $1 ... "
  if python3 ${CHECK} $1; then
    printf "%s\n" SUCCESS
  else
    printf "%s\n" FAILED
    FAIL=1
  fi
}

test_all() {
  for i in ${TESTPATH}
  do
    check $i
  done
} 

test_all

exit ${FAIL}
