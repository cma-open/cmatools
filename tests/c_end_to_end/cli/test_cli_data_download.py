"""Test the cli_data_download tool outputs."""

# TODO review and edit this

import argparse
from pathlib import Path

from cmatools.cli_data_download import cli_data_download
from cmatools.definitions import SRC_DIR

DEBUG = True
"""bool: Debugging module-level constant (Default: True)."""

# Define cli filepath
CLI = Path(SRC_DIR, "cmatools", "cli_simple_analysis.py")
"""str: Filepath to command line tool module."""


# TODO mark as slow
# Keep this simple test, but mock so no actual download occurs
def test_cli_data_download():
    """Test for cli_data_download() function."""
    parsed_args = argparse.Namespace(portal="CEDA", dataset="HADCRUT")
    output = cli_data_download(parsed_args)
    # Expect True, indicates download success
    assert output is True
