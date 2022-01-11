"""Test the cli_coperncius_download tool."""

import argparse
from pathlib import Path

from cmatools.cli_copernicus_download import (
    cli_copernicus_download,
    cli_parse_args,
    cli_parser,
)
from cmatools.definitions import SRC_DIR

DEBUG = True
"""bool: Debugging module-level constant (Default: True)."""

package = "cmatools"
tool = "cli_copernicus_download"

# Define cli tool filepath
CLI = Path(SRC_DIR, package, tool)
"""str: Filepath to command line tool module."""


def test_cli_parser():
    """Test for cli_parser() function."""
    out = cli_parser()
    # Confirm output object is correct parser type
    assert isinstance(out, argparse.ArgumentParser)
    # Confirm cli tool name is correct
    assert out.prog == "CLI-COPERNICUS-DOWNLOAD"


def test_cli_parse_args():
    """Test for cli_parse_args() function."""
    user_args = ["--portal=COP", "--dataset=E-OBS", "--dryrun=True"]
    parsed_args = cli_parse_args(user_args)
    if DEBUG:
        print(f"Parsed args: {parsed_args}")
    assert isinstance(parsed_args, argparse.Namespace)
    assert parsed_args.portal == "COP"
    assert parsed_args.dataset == "E-OBS"
    assert parsed_args.dryrun == "True"


#
#
def test_cli_copernicus_download_dryrun():
    """Test for cli_coperncius_download() function."""
    parsed_args = argparse.Namespace(portal="COP", dataset="E-OBS", dryrun="True")

    # Simple unit test for outcome of the download out the source data settings
    status = cli_copernicus_download(parsed_args)
    assert status is True


# TODO mark as slow
# Keep this simple test, but mock so no actual download occurs
def test_cli_copernicus_download():
    """Test for cli_coperncius_download() function."""
    parsed_args = argparse.Namespace(portal="COP", dataset="E-OBS", dryrun="False")

    # Simple unit test for outcome of the download out the source data settings
    status = cli_copernicus_download(parsed_args)
    assert status is True
