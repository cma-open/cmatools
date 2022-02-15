#!/bin/bash

#######################################################################################
# Script to run all tests for - cli_canned_data module
#######################################################################################

# Source code, variables from common.sh
source common.sh

echo "Current working directory: ${PWD}"

# Discover and run tests on code path. Options include:
# -v verbose flag, -r displays “short test summary info” at end of session,
# -A lists all info
# --tb traceback print mode (auto/long/short/line/native/no)., e.g. --tb=long

readonly UNIT=True
readonly INTEGRATION=True
readonly END2END=True
readonly USER=True

UNIT_DIR="${TESTS_DIR}/a_unit/cli"
INTEGRATION_DIR="${TESTS_DIR}/b_integration/cli"

if [ "$UNIT" == "True" ]; then
    echo "---"
    echo "Running unit tests at ${UNIT_DIR}"
    echo "---"
    pytest --tb=long -vrA  "${UNIT_DIR}"
    echo "----------------"
    echo "End - unit tests"
    echo "----------------"
fi

if [ "$INTEGRATION" == "True" ]; then
    echo "---"
    echo "Running integration tests at ${INTEGRATION_DIR}"
    echo "---"
    pytest --tb=long -vrA  "${INTEGRATION_DIR}"
    echo "----------------"
    echo "End - integration tests"
    echo "----------------"
fi

#######################################################################################
# Code review and system context notes
# ====================================
# This script is used during manual testing
# The script is also called as part of the GitHub actions automated tests
#######################################################################################