#!/bin/bash

#####################################################################################################################
# Selected simple shell script uses shell script file format
# To act as reminders or sources for future scripts
#####################################################################################################################



conda deactivate

while true; do
    read -p "Do you want to delete the current conda environment?" yn
    case $yn in
        [Yy]* ) echo "Removing the conda environment";
          echo "This is a slow process, please be patient";
          conda remove --name cmatool-env --all;
          break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done


# check user

if [ "$USER" == "user-name" ]; then
    echo "---"
    echo "Running the script as user: ${USER}"
    echo "---"
else
    echo "Only run this script with write permission to the destination directory"
    echo "Solution = switch to the name user account account, then re-run"
    echo "Exiting the script"
    sleep 8
    exit;
fi
