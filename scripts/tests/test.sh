#!/bin/bash

#######################################
# Script to run system tests
#######################################

# Set python package root dir as script constant
readonly CODE_DIR="$(dirname "$(dirname "${PWD}")")"
# Set tests directory
readonly TESTS_DIR="${CODE_DIR}"/tests

echo " ---- * ----"
echo "Running system tests with pytest"
echo "Python package root: "${CODE_DIR}""
echo "Tests directory: "${TESTS_DIR}""
echo " ---- * ----"

# Discover and run tests on code path,
# -v verbose flag
# -r displays “short test summary info” at end of session, -A lists all info

#pytest -r -l --tb=long  $testdir

pytest -rA  "${TESTS_DIR}"
