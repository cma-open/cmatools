#!/bin/bash

#######################################################################################
# Script to generate a requirements.txt file, based on active imports within package
#######################################################################################

# Set code root directory as script constant
readonly CODE_DIR="$(dirname $(dirname "${PWD}"))"

# Source variables from common
source "${CODE_DIR}/scripts/common/common.sh"


pipreqs "${SRC_DIR}" --print
echo " --------------------------------------------------"
