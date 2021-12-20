#!/bin/bash

#######################################################################################
# Script to delete the Sphinx docs build directory
#######################################################################################

# Set python package root dir as script constant
readonly CODE_DIR="$(dirname "$(dirname "${PWD}")")"
# Source variables from common
source "${CODE_DIR}/scripts/common/common.sh"

# Set documentation directories
readonly DOCS_DIR="${CODE_DIR}/docs"
readonly OUTPUT_DIR="${CODE_DIR}/docs/build"

echo " ---- * ----"
echo "Deleting Sphinx build directory"
echo "Python package root: ${CODE_DIR}"
echo "Sphinx output build files: ${OUTPUT_DIR}"
echo " ---- * ----"

# Delete sphinx docs build
rm -rf "${OUTPUT_DIR}"
