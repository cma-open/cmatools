"""Source definitions file to generate constants.

Currently used to generate main code source root path and package name
for use by other modules
"""

import os

# TODO convert to use pathlib

# Docstring not added here to avoid display of filepaths in documentation

# Set constants for CMATOOLS package
SRC_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CONFIGFILE = f"{SRC_DIR}/cmatools/config.ini"
CONFIGLOGS = f"{SRC_DIR}/cmatools/config-logs.ini"

# TODO check take name from setup.py or VERSION to avoid duplication
PACKAGE = "cmatools"  # Set the package name
"""str: Package name."""

if __name__ == "__main__":
    # Print and confirms current constants
    print(f"Source dir: {SRC_DIR}")
    print(f"Root dir: {ROOT_DIR}")
    print(f"Config file: {CONFIGFILE}")
