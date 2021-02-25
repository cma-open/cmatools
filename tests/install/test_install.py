"""Test and confirm how the package is installed"""

import pkg_resources
import subprocess

from cmatools.definitions import ROOT_DIR

PACKAGE = "cmatools"


def test_package_installed():
    """Test for current package installation location"""

    version = pkg_resources.get_distribution(PACKAGE).version
    print("Version: ", version)
    subprocess.run(["pip", "show", PACKAGE], check=True)
    print("Source code root: ", ROOT_DIR)


def test_installed_version():
    """Test for current package version"""

    version = pkg_resources.get_distribution(PACKAGE).version
    assert version == "0.0.1"
    # TODO - replace this tests with a call to compare source version from files vs current installed version
