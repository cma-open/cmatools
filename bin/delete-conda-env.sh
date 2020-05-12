#!/bin/bash

# Script to delete current conda environment
# Used to re-set the system , e.g. prior to a new full installation

conda deactivate

while true; do
    read -p "Do you want to delete the current conda environment?" yn
    case $yn in
        [Yy]* ) echo "Removing the conda environment";
          echo "This is a slow process, please be patient";
          conda remove --name cmatools-env --all;
          break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done
echo ""
echo "Conda environment removed"
echo ""