"""Source definitions file to generate constants.

Currently used to generate main code source root path and package name
for use by other modules
"""

import os

# TODO convert to use pathlib
# Set constants for CMATOOLS package

SRC_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
"""str: Package src directory."""

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
"""str: Package root directory."""

CONFIGFILE = f'{SRC_DIR}/cmatools/config.ini'
"""str: Config file location."""

CONFIGLOGS = f'{SRC_DIR}/cmatools/config-logs.ini'
"""str: Config logs ini file location."""

# TODO check r.e. take name from setup.py to minimise duplication
PACKAGE = 'cmatools'  # Set the package name
"""str: Package name."""
