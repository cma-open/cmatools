#!/bin/bash

######################################################################################################################
# Script to system unit tests
######################################################################################################################

# Set python package root dir as script constant
readonly CODE_DIR="$(dirname "$(dirname "${PWD}")")"
# Set tests directory
readonly TESTS_DIR="${CODE_DIR}"/tests/unit

echo " ---- * ----"
echo "Running system tests with pytest"
echo "Python package root: "${CODE_DIR}""
echo "Tests directory: "${TESTS_DIR}""
echo " ---- * ----"

# pytest --tb=long -vrA  "${TESTS_DIR}"

# Discover and run tests on specified path, with coverage stats
pytest --cov-report term-missing:skip-covered --cov="${CODE_DIR}"/cmatools "${TESTS_DIR}"
echo " ---- "
echo "  # End of unit tests"
echo " ---- "


######################################################################################################################
# Code review and system context notes
# ====================================
# This script is used during manual testing
# The script is also called as part of the GitHub actions automated tests
######################################################################################################################
