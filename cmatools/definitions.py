"""
.. module: definitions
Source definitions file to generate constants
Currently used to generate main code source root path
for use by other modules

"""

import os

""" The root directory for CMATOOLS package"""
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))