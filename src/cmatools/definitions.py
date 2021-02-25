"""
.. module: definitions

Source definitions file to generate constants.
Currently used to generate main code source root path
for use by other modules

"""

import os

""" Constants for the package """

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Set the package name
# TODO check r.e. takename from setup.py
PACKAGE = "cmatools"