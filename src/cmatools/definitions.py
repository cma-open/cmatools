"""
.. module: definitions

Source definitions file to generate constants.
Currently used to generate main code source root path and package name
for use by other modules

"""

import os

# Set the root dir relative to this file
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Set the package name
# TODO check r.e. take name from setup.py to minimise duplication
PACKAGE = "cmatools"