""" Test and confirm how the package is installed """

import pkg_resources

from cmatools.definitions import ROOT_DIR


def test_package_installed():

    """Test for current package installation location"""

    version = pkg_resources.get_distribution("cmatools").version
    print(version)


