#!/bin/bash

#  Example use of the cli-copernicus-downlaod command line tool - with user arguments

# Usage
# Call the command by name, supplies user specified arguments

# Dry run - check but dont download
cli-copernicus-download --portal=COP --dataset=E-OBS --dryrun=True

echo " --- "
echo ""

# Run data download tool
cli-copernicus-download --portal=COP --dataset=E-OBS --dryrun=False
