""" Test and confirm how the package is installed """

import pkg_resources
import subprocess

from cmatools.definitions import ROOT_DIR

PACKAGE="cmatools"

def test_package_installed():

    """Test for current package installation location"""

    version = pkg_resources.get_distribution(PACKAGE).version
    print(version)
    subprocess.run(["pip", "show", PACKAGE], check=True)

