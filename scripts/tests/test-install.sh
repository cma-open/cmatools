#!/bin/bash

######################################################################################################################
# Script to run the install tests
######################################################################################################################

# Source code, variables from common.sh
source common.sh

echo "Current working directory: ${PWD}"

# Discover and run tests on code path. Options include:
# -v verbose flag, -r displays “short test summary info” at end of session, -A lists all info
# --tb traceback print mode (auto/long/short/line/native/no)., e.g. --tb=long
pytest --tb=long -vrA  "${TESTS_DIR}/install"

######################################################################################################################
# Code review and system context notes
# ====================================
# This script is used during manual testing
# Not called by any other scripts, not used as part of the GitHub actions automated tests
# Config options
#   - currently the pyproject.toml options take precedence over these script options
#   - retained here so that later the config in pyproject.toml can be relaxed or removed
######################################################################################################################
