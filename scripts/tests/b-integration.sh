#!/bin/bash

######################################################################################################################
# Script to run all integration tests
######################################################################################################################

# Set python package code dir as script constant (relative to this script)
readonly CODE_DIR="$(dirname "$(dirname "${PWD}")")"
# Source variables from common
source "${CODE_DIR}/scripts/common/common.sh"
source "${CODE_DIR}/scripts/common/tests.sh"
sleep 6

echo "Running tests under: ${INTEGRATION}"
sleep 4

# Discover and run tests on code path. Options include:
# -v verbose flag, -r displays “short test summary info” at end of session, -A lists all info
# --tb traceback print mode (auto/long/short/line/native/no)., e.g. --tb=long
pytest --tb=long -vrA  "${INTEGRATION}"

######################################################################################################################
# Code review and system context notes
# ====================================
# This script is used during manual testing
# The script is also called as part of the GitHub actions automated tests
######################################################################################################################
