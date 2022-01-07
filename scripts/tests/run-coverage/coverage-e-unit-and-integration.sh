#!/bin/bash

######################################################################################################################
# Script to run system tests with coverage calculation - uses pytest-cov
# Allows code coverage for each category of tests to be compared
######################################################################################################################

# Set python package code dir as script constant (relative to this script)
readonly CODE_DIR="$(dirname "$(dirname "$(dirname "${PWD}")")")"
# Source variables from common
source "${CODE_DIR}/scripts/common/common.sh"
source "${CODE_DIR}/scripts/common/tests.sh"
sleep 4
echo "Running tests under: ${UNIT} and ${INTEGRATION}"
sleep 4
echo "Current working directory: ${PWD}"

# Run combined unit + integration tests
#  - unit + integration combined

# TODO - check use of skip-covered

# Test unit test and integration tests combined
pytest --cov-config="${COV_CONFIG}" \
       --cov-report term-missing:skip-covered \
       --cov="${PACKAGE}" "${UNIT}" "${INTEGRATION}"
echo " ---- "
echo "  # End of combined: unit +  integration tests"
echo " ---- "


######################################################################################################################
# Code review and system context notes
# ====================================
# This script is used during manual testing
# Not called by any other scripts, not used as part of the GitHub actions automated tests
# The GitHub action use similar commands to create coverage reports to view via the Actions / Builds

# Goals and targets
# Running both unit tests and integration tests - for a whole app - should give close to 100% coverage

# Notes
# Using a cd to the tests dir, then relative paths to test gives cleaner / shorter paths in outputs
######################################################################################################################
