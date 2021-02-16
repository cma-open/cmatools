#!/bin/bash

######################################################################################################################
# Script to run the install tests
######################################################################################################################

# Set python package root dir as script constant
readonly CODE_DIR="$(dirname "$(dirname "${PWD}")")"
readonly PACKAGE="cmatools"

PACKAGE_DIR=$(python -c 'import inspect; \
import pathlib; import cmatools; \
package = pathlib.Path(inspect.getfile(cmatools)); \
print(str(package.parent)) \
')

# Set tests directory - relative to installed code root
readonly TESTS_DIR="${PACKAGE_DIR}"/tests/install

echo " ---- * ----"
echo "Running system tests with pytest"
echo "Script source package root directory: ${CODE_DIR}"
echo "Installed package root directory: ${PACKAGE_DIR}"
echo "Script tests directory: ${TESTS_DIR}"
echo " ---- * ----"

# Discover and run tests on code path. Options include:
# -v verbose flag, -r displays “short test summary info” at end of session, -A lists all info
# --tb traceback print mode (auto/long/short/line/native/no)., e.g. --tb=long

pytest --tb=long -vrA  "${TESTS_DIR}"

######################################################################################################################
# Code review and system context notes
# ====================================
# This script is used during manual testing
# Not called by any other scripts, not used as part of the GitHub actions automated tests
######################################################################################################################
