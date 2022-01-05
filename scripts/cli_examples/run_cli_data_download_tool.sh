#!/bin/bash

#  Example use of the cli-data-downlaod command line tool - with user arguments

# Usage
# Call the command by name, supplies user specified arguments

cli-data-download --x=1 --y=2 --portal=HADOBS --dataset=CRUTEM

echo " --- "
echo ""

cli-data-download --x=1 --y=2 --portal=CEDA --dataset=CRUTEM

echo " --- "
echo ""

cli-data-download --x=1 --y=2 --portal=HADOBS --dataset=HADCRUT

echo " --- "
echo ""

cli-data-download --x=1 --y=2 --portal=CEDA --dataset=HADCRUT
