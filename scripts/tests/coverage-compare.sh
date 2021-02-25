#!/bin/bash

######################################################################################################################
# Script to run system tests with coverage calculation - uses pytest-cov
# Allows code coverage for each category of tests to be compared
######################################################################################################################

# Source code, variables from common.sh
source common.sh

echo "Current working directory: ${PWD}"
# Discover and run tests on specified path, with coverage stats

# Run each type of test
#  - unit
#  - unit + integration combined
#  - end-to-end
#  - user focussed

# TODO - check use of skip-covered

# Test unit tests
pytest --cov-config="${COV_CONFIG}" \
       --cov-report term-missing:skip-covered \
       --cov="${PACKAGE}" "${TESTS_DIR}/unit"
echo " ---- "
echo "  # End of unit tests"
echo " ---- "
#
# Test unit test and integration tests combined
pytest --cov-config="${COV_CONFIG}" \
       --cov-report term-missing:skip-covered \
       --cov="${PACKAGE}" "${TESTS_DIR}"/integration "${TESTS_DIR}"/unit
echo " ---- "
echo "  # End of combined: unit +  integration tests"
echo " ---- "

# Test end to end tests
pytest --cov-config="${COV_CONFIG}" \
       --cov-report term-missing \
       --cov="${PACKAGE}" "${TESTS_DIR}"/end-to-end
echo " ---- "
#--cov-report term-missing:skip-covered \
echo "  # End of end-to-end tests"
echo " ---- "

# Call main user focussed module, by module name (not path)
test_module="cmatools.cli_hello_world"
pytest --cov-config="${COV_CONFIG}" \
       --cov-report term-missing:skip-covered \
       --cov="${test_module}" "${TESTS_DIR}"/user-interface
echo " ---- "
echo "  # End of user-interface tests"
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