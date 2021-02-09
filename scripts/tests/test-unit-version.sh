#!/bin/bash

#######################################
# Script to run system tests
# Run the unit tests for version
#######################################

# Set python package root dir as script constant
readonly CODE_DIR="$(dirname "$(dirname "${PWD}")")"
# Set tests directory
readonly TESTS_DIR="${CODE_DIR}"/tests

echo " ---- * ----"
echo "Running system tests with pytest"
echo "Python package root: ${CODE_DIR}"
echo "Tests directory: ${TESTS_DIR}"
echo " ---- * ----"

# Discover and run tests on code path,
# -v verbose flag
# -r displays “short test summary info” at end of session, -A lists all info

# Run pytests on the unit tests subdirectory - version check only
pytest -rAv  "${TESTS_DIR}"/unit/version
