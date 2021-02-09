#!/bin/bash

#####################################################################################################################
# Template shell script file
# Act as reminder for code style and format
# Follow Google shell script code style
# Text examples taken from:
# https://google.github.io/styleguide/shellguide.html#s7-naming-conventions
#####################################################################################################################

# Reminders:

# Top level comment at top of the file to explain content

# Functions also have comments, e.g.

#######################################
# Get configuration directory.
# Globals:
#   SOMEDIR
# Arguments:
#   None
# Outputs:
#   Writes location to stdout
#######################################

# Variable expansion
# quote your variables; prefer "${var}" over "$var".
var=0
"${var}"
echo "Value is ${var}"
# Quoting

# Normally Always quote strings containing variables, command substitutions, spaces or shell meta characters
# Use arrays for safe quoting of lists of elements, especially command-line flags.

# 'Single' quotes indicate that no substitution is desired.
# "Double" quotes indicate that substitution is required/tolerated.

# "quote command substitutions"
# Note that quotes nested inside "$()" don't need escaping.
flag="$(some_command and its args "$@" 'quoted separately')"

# "quote variables"
echo "${flag}"

# quote examples
echo "Python package root: "${CODE_DIR}""   # Incorrect
echo "Python package root: ${CODE_DIR}"     # Correct


# Command substitution
# Use $(command) instead of backticks.

# This is preferred:
var="$(command "$(command1)")"

# Use an explicit path when doing wildcard expansion of filenames.

# cp ./* dirname

# Function names

# Lower-case, with underscores to separate words.
function get_dir() {
  echo "${SOMEDIR}"
}

# Variable names

# Lower-case, with underscores to separate words.
for zone in "${zones[@]}"; do
  something_with "${zone}"
done


# Constants and Environment variable names

# Constant
readonly PATH_TO_FILES='/some/path'
readonly VERBOSE = 'true'
readonly DEBUG = 'false'




