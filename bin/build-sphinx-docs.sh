#!/bin/bash

# Build documentation and output to standard location

CODE_DIR="$(dirname "$PWD")"
echo "$CODE_DIR"
DOCS_DIR=$CODE_DIR/docs
# Make paths to sphinx docs and output
INPUT_DIR=$CODE_DIR/docs/source/
echo "$INPUT_DIR"
OUTPUT_DIR=$CODE_DIR/docs/build
echo "$OUTPUT_DIR"
API_DIR=$CODE_DIR/docs/source/api
echo "$API_DIR"
TEMPLATEDIR=$CODE_DIR/docs/source/templates
echo " ---- * ----"

# Generate source files from current installed package / subpackages
# sphinx-apidoc -f  --module-first --no-headings --templatedir=$TEMPLATEDIR -o $API_DIR $CODE_DIR/cmatools

sphinx-apidoc -f  --module-first --templatedir=$TEMPLATEDIR -o $API_DIR $CODE_DIR/cmatools


# Build sphinx docs and make html
sphinx-build -v -b html $INPUT_DIR $OUTPUT_DIR