"""Test the package version."""

# from importlib.metadata import version
# version('cmatools')

# TODO update for python 3.8

import pkg_resources

# from cmatools.definitions import ROOT_DIR


def test_package_version():
    """Test current package version."""
    version = pkg_resources.get_distribution("cmatools").version
    assert version == "0.0.1"
