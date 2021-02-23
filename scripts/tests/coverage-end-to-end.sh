#!/bin/bash

######################################################################################################################
# Script to test: end-to-end tests
######################################################################################################################

# Source code, variables from common.sh
source common.sh

echo "Current working directory: ${PWD}"

# Discover and run tests on specified path, with coverage stats
pytest --cov-report term-missing:skip-covered --cov="${PACKAGE}" "${TESTS_DIR}/end-to-end"

######################################################################################################################
# Code review and system context notes
# ====================================
# This script is used during manual testing
# The script is also called as part of the GitHub actions automated tests
######################################################################################################################