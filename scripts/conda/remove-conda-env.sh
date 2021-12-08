#!/bin/bash

#######################################################################################
# Script to remove the named conda env
# For use with testing
# This script does NOT delete miniconda, just deletes the named conda environment
#######################################################################################

# Set the name of the conda environment to be removed as a script constant
readonly ENV_NAME="cmatools-env"
# Set the miniconda version directory, within $HOME, as a script constant
readonly MINICONDA="miniconda3"

# Source commands from conda profile script, so that the deactivate
# command can be called
source "~/${MINICONDA}/etc/profile.d/conda.sh"

# Script can't run from within an active conda env, so first deactivate
conda deactivate

# Interactive prompt
# Require the user to confirm environment removal
while true; do
    read -p "Do you want to delete the current conda environment: ${ENV_NAME}?" yn
    case $yn in
        [Yy]* )
          echo "---"
          echo "Removing the conda environment";
          echo "This is a slow process, please be patient";
          conda remove --name "${ENV_NAME}" --all;
          break;;
        [Nn]* )
          exit;;
        * )
          echo "Please answer yes or no.";;
    esac
done

echo ""
echo "--------------------------------"
echo "Conda environment: ${ENV_NAME} has been removed"
echo "--------------------------------"
echo ""
