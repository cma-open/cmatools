#!/bin/bash

#######################################################################################
# Script to run unit tests - on selected subsets of packages or modules
#######################################################################################

# Set python package code dir as script constant (relative to this script)
readonly CODE_DIR="$(dirname "$(dirname "${PWD}")")"
# Source variables from common
source "${CODE_DIR}/scripts/common/common.sh"
source "${CODE_DIR}/scripts/common/tests.sh"
sleep 4

# Edit - select subset to run tests during dev
SELECTED="${TESTS_DIR}/a_unit/common"

echo "Running tests under: ${SELECTED}"
sleep 3

# Discover and run tests on code path. Options include:
# -v verbose flag, -r displays “short test summary info” at end of session,
# -A lists all info
# --tb traceback print mode (auto/long/short/line/native/no)., e.g. --tb=long
pytest --tb=long -vrA  "${SELECTED}"

#######################################################################################
# Code review and system context notes
# ====================================
# This script is used during manual testing
#######################################################################################
