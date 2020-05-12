#!/bin/bash

# Creates conda environment
# Takes env name and dependency requirements from the yaml file

echo "Creating conda environment"
conda env create -f environment.yml

echo " --------------------------------------------------"
echo "       <<  Close and reopen terminal   >>"
echo " --------------------------------------------------"
