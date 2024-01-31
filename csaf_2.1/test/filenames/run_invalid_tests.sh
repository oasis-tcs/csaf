#!/bin/bash

TESTPATH=$*

FAIL=0

# go to root of git repository
cd `dirname $0`/../../..

check() {
  printf "%s" "Testing that filename of $1 is invalid ... "
  paikalta --labels FAILED,SUCCESS $1 && FAIL=1
}

test_all() {
  for i in ${TESTPATH}
  do
    check $i
  done
} 

test_all

exit ${FAIL}
