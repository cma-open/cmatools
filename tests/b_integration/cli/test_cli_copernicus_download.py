"""Test the cli_coperncius_download tool."""

import argparse
from pathlib import Path

from cmatools.definitions import SRC_DIR

DEBUG = True
"""bool: Debugging module-level constant (Default: True)."""

package = "cmatools"
tool = "cli_copernicus_download"

# Define cli tool filepath
CLI = Path(SRC_DIR, package, tool)
"""str: Filepath to command line tool module."""

# TODO - fix these via mock


def test_cli_copernicus_download():
    """Test for cli_coperncius_download() function."""
    parsed_args = argparse.Namespace(portal="COP", dataset="E-OBS", dryrun="True")

    print(parsed_args)


# mock out the source data settings

# output = cli_analysis(parsed_args)
# # Default analysis is product: 1 * 2 = 2
# assert output == 2
#
# parsed_args = argparse.Namespace(
#     x=1, y=2, sum=True, max=None, combined=False, verbose=False
# )
# output = cli_analysis(parsed_args)
# # Sum analysis: 1 + 2 = 3
# assert output == 3
