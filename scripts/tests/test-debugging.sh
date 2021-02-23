#!/bin/bash

######################################################################################################################
# Script to run to aid debugging for any test issues
######################################################################################################################

# Source code, variables from common.sh
source common.sh

echo "Current working directory: ${PWD}"

#pytest -h   # prints options _and_ config file settings
echo

# Confirm current python path, view local, installed paths
echo
echo "Pythonpaths:"
echo
python -c "import sys; print('\n'.join(x for x in sys.path if x))"
echo

echo "Package install status"
pip show "${PACKAGE}"


######################################################################################################################
# Code review and system context notes
# ====================================
# This script is used during development and debugging of package structure setup and choosing testing options
# Not called by any other scripts, not used as part of the GitHub actions automated tests
######################################################################################################################
