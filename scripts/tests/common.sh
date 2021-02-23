#!/bin/bash

######################################################################################################################
# Script to hold common code used by the test scripts
######################################################################################################################

# Set python package root dir as script constant
readonly CODE_DIR="$(dirname "$(dirname "${PWD}")")"
readonly PACKAGE="cmatools"
# Set coverage config file as script constant
readonly COV_CONFIG="${CODE_DIR}"/.coveragerc
# Get location of the installed package (local if editable install, site-packages if full install)
PACKAGE_DIR=$(python -c 'import inspect; \
import pathlib; import cmatools; \
package = pathlib.Path(inspect.getfile(cmatools)); \
print(str(package.parent)) \
')
# Set tests directory
readonly TESTS_DIR="${CODE_DIR}"/tests

echo " ---- * ----"
echo "Running system tests with pytest"
echo "Script source package root directory: ${CODE_DIR}"
echo "Installed package root directory: ${PACKAGE_DIR}"
echo "Script tests directory: ${TESTS_DIR}"
echo " ---- * ----"

######################################################################################################################
# Code review and system context notes
# ====================================
# Further refactor could extract code into functions
######################################################################################################################
