#!/bin/bash
./csaf_2.0/test/csaf_schema/run_tests.sh
./csaf_2.0/test/provider_schema/run_tests.sh
./csaf_2.0/test/aggregator_schema/run_tests.sh

./csaf_2.0/test/validator/run_tests.sh