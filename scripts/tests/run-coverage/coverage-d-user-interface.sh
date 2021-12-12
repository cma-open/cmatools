#!/bin/bash

######################################################################################################################
# Script to test: user interface tests
######################################################################################################################

# Set python package code dir as script constant (relative to this script)
readonly CODE_DIR="$(dirname "$(dirname "$(dirname "${PWD}")")")"
# Source variables from common
source "${CODE_DIR}/scripts/common/common.sh"
source "${CODE_DIR}/scripts/common/tests.sh"
sleep 4
echo "Running tests under: ${INTERFACE}"
sleep 4
echo "Current working directory: ${PWD}"

# Discover and run tests on specified path, with coverage stats
pytest --cov-report term-missing:skip-covered --cov="${PACKAGE}" "${INTERFACE}"

######################################################################################################################
# Code review and system context notes
# ====================================
# This script is used during manual testing
# The script is also called as part of the GitHub actions automated tests
######################################################################################################################
