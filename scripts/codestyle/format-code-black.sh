#!/bin/bash

#######################################
# Script to run "black" code formatter
# Runs on the main package and test dir
#######################################

# Set python package root dir as script constant
readonly CODE_DIR="$(dirname "$(dirname "$PWD")")"

echo "--------------------------------"
echo "Apply black code style format"
echo "Code root directory: $CODE_DIR"
echo "--------------------------------"

# Run black formatter, change files in place
black $CODE_DIR/src/cmatools
black $CODE_DIR/tests