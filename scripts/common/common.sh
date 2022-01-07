#!/bin/bash

#######################################################################################
# Script to hold common code used by scripts
#######################################################################################

# Assume CODE_DIR is always set by the calling script

# Set script constants
readonly SRC_DIR="${CODE_DIR}/src"
readonly SCRIPTS_DIR="${CODE_DIR}/scripts"
readonly PACKAGE="cmatools"

# Get location of the installed package
# (local if editable install, site-packages if full install)
PACKAGE_DIR=$(python -c 'import inspect; \
import pathlib; import cmatools; \
package = pathlib.Path(inspect.getfile(cmatools)); \
print(str(package.parent)) \
')

echo " ---- * ----"
echo "Package name: ${PACKAGE}"
echo "Package root directory: ${CODE_DIR}"
echo "Source (src) directory: ${SRC_DIR}"
echo "Scripts directory: ${SCRIPTS_DIR}"
echo "Installed package directory: ${PACKAGE_DIR}"
echo " ---- * ----"

#######################################################################################
# Code review and system context notes
# ====================================
# Further refactor could extract code into functions
#######################################################################################
