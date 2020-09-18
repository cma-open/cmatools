"""
.. module: definitions

Source definitions file to generate constants.
Currently used to generate main code source root path
for use by other modules

"""

import os

""" Constants for CMATOOLS package """

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIGFILE = f"{ROOT_DIR}/cmatools/config.ini"
CONFIGLOGS = f"{ROOT_DIR}/cmatools/config-logs.ini"