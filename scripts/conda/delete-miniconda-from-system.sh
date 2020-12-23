#!/bin/bash

#######################################
# Script to delete miniconda from $HOME
# Completely removes conda from the system
# For use with testing / re-installs
# Deletes ~/$MINICONDA
# Deletes ~/$CONDA_TEMP
#######################################

# Set the miniconda version directory, within $HOME, as a script constant
readonly MINICONDA="miniconda3"

# Set temp location for conda downloads as script constant
readonly CONDA_TEMP="conda_temp"


while true; do
    read -p "Do you want to completely remove Miniconda from your system?" yn
    case $yn in
        [Yy]* )
          cd ~;
          echo "---"
          echo "Removing Miniconda installation from $HOME";
          echo "This is a slow process, please be patient";
          # Remove dir, recursive, force, verbose output
          rm -rfv $MINICONDA/;
          echo "Removing conda_temp directory from $HOME";
          rm -rfv $CONDA_TEMP/;
          break;;
        [Nn]* )
          exit;;
        * )
          echo "Please answer yes or no.";;
    esac
done

echo ""
echo "--------------------------------"
echo "Miniconda has been deleted from: $HOME/$MINICONDA"
echo "--------------------------------"
echo "Donwload files have been deleted from: $HOME/$CONDA_TEMP"
echo "--------------------------------"
echo ""