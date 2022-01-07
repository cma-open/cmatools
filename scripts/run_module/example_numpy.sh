#!/bin/bash

# Run the example_numpy module

# Set python package scripts dir as script constant
readonly PARENT_SCRIPTS_DIR="$(dirname "${PWD}")"

# Source code, variables from common.sh
source "${PARENT_SCRIPTS_DIR}/common/common.sh"

echo
echo "Running module from python at command line"
echo "---"

module="${SRC_DIR}/cmatools/examplesubpackage/example_numpy.py"

python3 "${module}"
echo
