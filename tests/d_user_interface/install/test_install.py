"""Test and confirm how the package is installed."""

import subprocess  # nosec  # bandit ignore
from importlib import metadata

import pkg_resources

from cmatools.definitions import PACKAGE, ROOT_DIR


def test_package_installed():
    """Test current package installation location."""
    version = pkg_resources.get_distribution(PACKAGE).version
    print('Version: ', version)
    subprocess.run(['pip', 'show', PACKAGE], check=True)
    print('Source code root: ', ROOT_DIR)


def test_installed_version():
    """Test for current package version."""
    version = pkg_resources.get_distribution(PACKAGE).version
    assert version == '0.0.1'
    # TODO - replace this test with a call to compare source
    #  version from files vs current installed version
    version_alternative = metadata.version(PACKAGE)
    assert version == version_alternative
