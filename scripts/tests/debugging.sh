#!/bin/bash

#######################################################################################
# Script to run to aid debugging for any test issues
#######################################################################################

# Set python package code dir as script constant (relative to this script)
readonly CODE_DIR="$(dirname "$(dirname "${PWD}")")"
# Source variables from common
source "${CODE_DIR}/scripts/common/common.sh"
source "${CODE_DIR}/scripts/common/tests.sh"
echo "Current working directory: ${PWD}"
#pytest -h   # prints options _and_ config file settings
sleep 3

# Confirm current python path, view local, installed paths
echo
echo "Python paths:"
echo
python -c "import sys; print('\n'.join(x for x in sys.path if x))"
echo
sleep 5
echo "Package install status"
echo
pip show "${PACKAGE}"
sleep 4
echo
pip show "tests"
sleep 2
echo
echo "Testing under dir: ${UNIT}/version"
#Run quick test - against version, as quick test example
pytest -rAv  "${UNIT}/version"

#######################################################################################
# Code review and system context notes
# ====================================
# This script is used during development and debugging of package structure setup
# and choosing testing options
# Not called by any other scripts, not used as part of the GitHub actions
# automated tests
#######################################################################################
