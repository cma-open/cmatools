#!/bin/bash

# Notes and record of setting up miniconda
# This is only required occasionaly for system setup or full testing
# Time required <= 10 mins

# Run this script, follow terminal prompts, then close and reopen terminal
# Create dir within $home for miniconda download
cd ~
echo "Creating conda_temp directory in $HOME"
mkdir -p conda_temp   # mkdir -p does not throw error if dir already exists
cd conda_temp

# Download miniconda
export CONDA_BASE=https://repo.anaconda.com/miniconda/
export CONDA_VERS=Miniconda3-latest-Linux-x86_64.sh
echo "Downloading miniconda"
wget $CONDA_BASE$CONDA_VERS

# Use most recent error code to confirm if download was a success
if [[ "$?" != 0 ]]; then
    echo "Error downloading file: check current version and site address"
else
    echo "File downloaded"
fi

# Install miniconda
echo "Installing Miniconda"
echo " --------------------------------------------------"
echo "       <<  Follow terminal prompts     >>"
echo "       <<  Close and reopen terminal   >>"
echo "       <<  when installation completes >>"
echo " --------------------------------------------------"
bash $CONDA_VERS

echo " --------------------------------------------------"
echo "       <<  Close and reopen terminal   >>"
echo " --------------------------------------------------"