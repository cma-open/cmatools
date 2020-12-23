#!/bin/bash

#######################################
# Script to install miniconda to $HOME
# required at initial system setup
# required for testing (after uninstall)
# NOTES:
# Time required <= 10 mins
#######################################

# Set Conda base as script constant
export CONDA_BASE=https://repo.anaconda.com/miniconda/
# Set conda version as script constant - this
export CONDA_VERS=Miniconda3-latest-Linux-x86_64.sh
# Set SHA hash from download site
SHA_NO='1314b90489f154602fd794accfc90446111514a5a72fe1f71ab83e07de9504a7'
# Set temp location for conda downloads as script constant
readonly CONDA_TEMP="conda_temp"
# Downloaded miniconda filename in temp
FILE="$HOME/$CONDA_TEMP/$CONDA_VERS"
# Set the miniconda version directory, within $HOME, as a script constant
readonly MINICONDA="miniconda3"

# Create dir within $HOME for miniconda download
cd ~
echo "Creating conda_temp directory in $HOME"
mkdir -p $CONDA_TEMP   # mkdir -p does not throw error if dir already exists

# Download miniconda into $CONDA_TEMP
cd $CONDA_TEMP
echo "Downloading miniconda"
wget $CONDA_BASE$CONDA_VERS

# Use most recent error code to confirm if download was a success
if [[ "$?" != 0 ]]; then
    echo "Error downloading file: check current version and site address"
else
    echo "File downloaded"
fi

# Verify download against SHA hash
sha_check="$(echo "$SHA_NO $FILE" | sha256sum --check)"
echo $sha_check

case ${sha_check} in
  *"OK"*)
    echo -n "Download file verified"
    ;;
  * )
    echo "SHA codes do not match - check download files"
    exit;;
esac

# Install miniconda, silent install - non-interactive
echo " --------------------------------------------------"
echo "Installing Miniconda"
echo ""
echo "This is a slow process, please be patient"
echo " --------------------------------------------------"
# -b Batch mode with no PATH modifications to ~/.bashrc. Assumes that you agree to the license agreement.
# Does not edit the .bashrc or .bash_profile files.
chmod +x $CONDA_VERS
bash $CONDA_VERS -b -p ~/$MINICONDA

# Source conda commands
source ~/$MINICONDA/bin/activate

# Inititalise conda
conda init

# Prevent autoactivation of base environment
conda config --set auto_activate_base false
echo " --------------------------------------------------"