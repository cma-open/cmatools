"""Test and confirm how the package is installed."""

# This module uses subprocess, which can raise security threats.
# The risk have been reviewed via Codacy, Bandit.
# The generic warning on import has been left active, in case of future edits here.
# Each specific use warning has been checked and then ignored, where safe to do so.
# bandit ignore command is # nosec, per line

import subprocess  # nosec  # bandit ignore
from importlib import metadata

import pkg_resources

from cmatools.definitions import PACKAGE, ROOT_DIR


def test_package_installed():
    """Test current package installation location."""
    version = pkg_resources.get_distribution(PACKAGE).version
    print("Version: ", version)
    subprocess.run(["pip", "show", PACKAGE], check=True)  # nosec
    print("Source code root: ", ROOT_DIR)


def test_installed_version():
    """Test for current package version."""
    version = pkg_resources.get_distribution(PACKAGE).version
    assert version == "0.0.1"
    # TODO - replace this test with a call to compare source
    #  version from files vs current installed version
    version_alternative = metadata.version(PACKAGE)
    assert version == version_alternative
