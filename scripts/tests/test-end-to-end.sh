#!/bin/bash

######################################################################################################################
# Script to run the system end to end tests
######################################################################################################################

# Set python package root dir as script constant
readonly CODE_DIR="$(dirname "$(dirname "${PWD}")")"
# Set tests directory
readonly TESTS_DIR="${CODE_DIR}"/tests/end-to-end

echo " ---- * ----"
echo "Running system tests with pytest"
echo "Python package root: "${CODE_DIR}""
echo "Tests directory: "${TESTS_DIR}""
echo " ---- * ----"

# Discover and run tests on code path. Options include:
# -v verbose flag, -r displays “short test summary info” at end of session, -A lists all info
# --tb traceback print mode (auto/long/short/line/native/no)., e.g. --tb=long

pytest --tb=long -vrA  "${TESTS_DIR}"

######################################################################################################################
# Code review and system context notes
# ====================================
# This script is used during manual testing
# The script is also called as part of the GitHub actions automated tests
######################################################################################################################