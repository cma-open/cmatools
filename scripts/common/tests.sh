#!/bin/bash

#######################################################################################
# Script to hold common code used by the test scripts
#######################################################################################

# Assume CODE_DIR is always set by the calling script

# Set coverage config file as script constant
readonly COV_CONFIG="${CODE_DIR}"/.coveragerc
# Set tests directory
readonly TESTS_DIR="${CODE_DIR}"/tests

echo "Running system tests with: pytest"
echo "Tests directory: ${TESTS_DIR}"
echo "Coverage config file: ${COV_CONFIG}"
echo " ---- * ----"

# Set test subdirectories
readonly UNIT="${TESTS_DIR}/a_unit"
readonly INTEGRATION="${TESTS_DIR}/b_integration"
readonly END2END="${TESTS_DIR}/c_end-to-end"
readonly INTERFACE="${TESTS_DIR}/d_user-interface"

#######################################################################################
# Code review and system context notes
# ====================================
# Further refactor could extract code into functions
#######################################################################################
