#!/bin/bash

######################################################################################################################
# Script to run system tests with coverage calculation - uses pytest-cov
# Allow code coverage for each category of tests to be compared
######################################################################################################################

# Set python package root dir as script constant
readonly CODE_DIR="$(dirname "$(dirname "${PWD}")")"
# Set coverage config file as script constant
readonly COV_CONFIG="${CODE_DIR}"/.coveragerc
# Set tests directory
readonly TESTS_DIR="${CODE_DIR}"/tests

echo " ---- * ----"
echo "Running system tests with coverage and pytest"
echo "Python package root: "${CODE_DIR}""
echo "Tests directory: "${TESTS_DIR}""
echo " ---- * ----"

cd "${CODE_DIR}"/tests

# Discover and run tests on specified path, with coverage stats

# Test unit tests
pytest --cov-report term-missing:skip-covered --cov="${CODE_DIR}"/cmatools "${TESTS_DIR}"/unit
echo " ---- "
echo "  # End of unit tests"
echo " ---- "

# Test unit test and integration tests combined
pytest --cov-report term-missing:skip-covered --cov="${CODE_DIR}"/cmatools "${TESTS_DIR}"/integration "${TESTS_DIR}"/unit
echo " ---- "
echo "  # End of combined: unit +  integration tests"
echo " ---- "

# Test end to end tests
pytest --cov-report term-missing:skip-covered --cov="${CODE_DIR}"/cmatools "${TESTS_DIR}"/end-to-end
echo " ---- "
echo "  # End of end-to-end tests"
echo " ---- "

# Call main user focussed module, by module name (not path)
pytest --cov-report term-missing:skip-covered --cov=cmatools.cli_hello_world "${TESTS_DIR}"/user-interface
echo " ---- "
echo "  # End of user-interface tests"
echo " ---- "


######################################################################################################################
# Code review and system context notes
# ====================================
#
# This script is used during manual testing
# Not called by any other scripts, not used as part of the GitHub actions automated tests
# The GitHub action use similar commands to create coverage reports to view via the Actions / Builds
# Goals and targets
# Running both unit tests and integration tests - for a whole app - should give close to 100% coverage
######################################################################################################################