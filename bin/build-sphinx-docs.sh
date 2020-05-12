#!/bin/bash

# Build documentation and output to standard location

CODE_DIR="$(dirname "$PWD")"
echo "$CODE_DIR"
DOCS_DIR=$CODE_DIR/docs
# Make paths to sphinx docs and output
INPUT_DIR=$CODE_DIR/docs/source
echo "$INPUT_DIR"
OUTPUT_DIR=$CODE_DIR/docs/build
echo "$OUTPUT_DIR"

# Generate source files from current range of installed HadCRUT package / subpackages
sphinx-apidoc -f -o $INPUT_DIR $CODE_DIR/cmatools

# Build sphinx docs and make html
sphinx-build -v -b html $INPUT_DIR $OUTPUT_DIR