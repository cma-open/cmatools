#!/bin/bash

#######################################################################################
# Script to create named conda environment
# Uses environment_dev.yml file
#######################################################################################

# Set code root directory as script constant
readonly CODE_DIR="$(dirname $(dirname "${PWD}"))"
# Set name of environment file holding dependencies list
CONA_ENV_FILE='environment_dev.yml'


echo "Creating conda environment from: ${CONA_ENV_FILE}"
conda env create -f "${CODE_DIR}/${CONA_ENV_FILE}"

echo " --------------------------------------------------"
