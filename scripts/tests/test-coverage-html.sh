#!/bin/bash

######################################################################################################################
# Script to run system tests with coverage calculation - uses pytest-cov
######################################################################################################################

# Set python package root dir as script constant
readonly CODE_DIR="$(dirname "$(dirname "${PWD}")")"
# Set coverage config file as script constant
readonly COV_CONFIG="${CODE_DIR}"/.coveragerc
# Set tests directory
readonly TESTS_DIR="${CODE_DIR}"/tests
# Set coverage report directory and subdirectories
readonly REPORT_DIR="${CODE_DIR}"/logs/tests/htmlcov
readonly REPORT_UNIT_DIR="${REPORT_DIR}"/unit
readonly REPORT_USER_DIR="${REPORT_DIR}"/user-interface
readonly REPORT_INTEGRATION_DIR="${REPORT_DIR}"/integration
readonly REPORT_END_DIR="${REPORT_DIR}"/end-to-end


echo " ---- * ----"
echo "Running system tests with coverage and pytest"
echo "Python package root: "${CODE_DIR}""
echo "Tests directory: "${TESTS_DIR}""
echo "Reports directory: "${REPORT_DIR}""
echo " ---- * ----"

cd "${CODE_DIR}"



## Test unit tests
pytest --cov-report html:"${REPORT_UNIT_DIR}" --cov="${CODE_DIR}"/cmatools "${TESTS_DIR}"/unit
# Generate test report in logs directory
coverage html -d "${REPORT_UNIT_DIR}" --rcfile="${COV_CONFIG}" --skip-covered --skip-empty --title "Coverage unit tests"
# Open report in browser
firefox  "${REPORT_UNIT_DIR}"/index.html

## Test integration tests
pytest --cov-report html:"${REPORT_INTEGRATION_DIR}" --cov="${CODE_DIR}"/cmatools "${TESTS_DIR}"/integration
# Generate test report in logs directory
coverage html -d "${REPORT_INTEGRATION_DIR}" --rcfile="${COV_CONFIG}" --skip-covered --skip-empty --title "Coverage integration tests"
# Open report in browser
firefox  "${REPORT_INTEGRATION_DIR}"/index.html

## Test end to end tests
pytest --cov-report html:"${REPORT_END_DIR}" --cov="${CODE_DIR}"/cmatools "${TESTS_DIR}"/end-to-end
# Generate test report in logs directory
coverage html -d "${REPORT_END_DIR}" --rcfile="${COV_CONFIG}" --skip-covered --skip-empty --title "Coverage end-to-end tests"
# Open report in browser
firefox  "${REPORT_END_DIR}"/index.html

## Test user interface tests
#pytest --cov-report html:"${REPORT_USER_DIR}" --cov="${CODE_DIR}"/cmatools "${TESTS_DIR}"/user
# Call main user focussed module, by module name (not path)
pytest --cov-report html:"${REPORT_USER_DIR}" --cov=cmatools.cli_hello_world "${TESTS_DIR}"/user-interface
# Generate test report in logs directory
coverage html -d "${REPORT_USER_DIR}" --rcfile="${COV_CONFIG}" --skip-covered --skip-empty --title "Coverage user interface tests"
# Open report in browser
firefox  "${REPORT_USER_DIR}"/index.html


######################################################################################################################
# Code review and system context notes
# ====================================
# This script is used during manual testing
# This allow easy comparison of coverage stats for each test type (via individual html tabs in browser)
# Not called by any other scripts, not used as part of the GitHub actions automated tests
# Ideally a simple combined summary report, hsowin g% per type would be useful, but has not proved possible to date
# Goals and targets
# Running both unit tests and integration tests - for a whole app - should give close to 100% coverage
######################################################################################################################




