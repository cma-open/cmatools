#!/bin/bash

#######################################
# Script to build system documentation
# Outputs to /docs/build
#######################################

# Set python package root dir as script constant
readonly CODE_DIR="$(dirname "$(dirname "$PWD")")"
# Set documentation directories
readonly DOCS_DIR=$CODE_DIR/docs
readonly INPUT_DIR=$CODE_DIR/docs/source
readonly OUTPUT_DIR=$CODE_DIR/docs/build
# Set named docs subdirectories
readonly API_DIR=$CODE_DIR/docs/source/api
readonly TEMPLATE_DIR=$CODE_DIR/docs/source/templates
readonly PACKAGE="cmatools"

echo " ---- * ----"
echo "Creating Sphinx system documentation"
echo "Python package root: $CODE_DIR"
echo "Sphinx source doc files: $INPUT_DIR"
echo "Sphinx output build files: $OUTPUT_DIR"
echo "Sphinx API dir: $API_DIR"
echo "Sphinx template dir: $TEMPLATE_DIR"
echo " ---- * ----"

# Generate source files from current installed package / subpackages, sphinx-apidoc is a tool for automatic
# generation of Sphinx sources using the autodoc extension documents a whole package
# Templates and options allow customisation of output doc pages

# sphinx-apidoc -f  --module-first --no-headings --templatedir=$TEMPLATE_DIR -o $API_DIR $CODE_DIR/cmatools
sphinx-apidoc -f  --module-first --templatedir=$TEMPLATE_DIR -o $API_DIR $CODE_DIR/src/$PACKAGE

# Build sphinx docs and make html files
sphinx-build -v -b html $INPUT_DIR $OUTPUT_DIR