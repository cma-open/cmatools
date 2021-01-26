""" Test the package version
"""

#from importlib.metadata import version
#version('construct')
#'4.3.1'
# TODO update for python 3.8

import pkg_resources
#pkg_resources.get_distribution('cmatools').version

from cmatools.definitions import ROOT_DIR



def test_package_version():

    """Test for current package version"""

    version = pkg_resources.get_distribution('cmatools').version
    print(version)

    # Confirm version is as expected
    #assert isinstance(out, argparse.ArgumentParser)



