#!/bin/bash

######################################################################################################################
# Script to run all system tests
######################################################################################################################

# Set python package code dir as script constant (relative to this script)
readonly CODE_DIR="$(dirname "$(dirname "${PWD}")")"
# Source variables from common
source "${CODE_DIR}/scripts/common/common.sh"
source "${CODE_DIR}/scripts/common/tests.sh"
sleep 6

echo "Running tests under: ${TESTS_DIR}"
sleep 6

echo "Current working directory: ${PWD}"

# Discover and run tests on code path. Options include:
# -v verbose flag, -r displays “short test summary info” at end of session, -A lists all info
# --tb traceback print mode (auto/long/short/line/native/no)., e.g. --tb=long
pytest --tb=long -vrA  "${TESTS_DIR}"

######################################################################################################################
# Code review and system context notes
# ====================================
# This script is used during manual testing
# Not called by any other scripts, not used as part of the GitHub actions automated tests
# Config options
#   - currently the pyproject.toml options take precedence over these script options
#   - retained here so that later the config in pyproject.toml can be relaxed or removed
######################################################################################################################
