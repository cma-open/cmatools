"""Test the cli_data_download tool outputs."""

import argparse
from pathlib import Path

from cmatools.cli_data_download import cli_data_download, cli_parse_args, cli_parser
from cmatools.definitions import SRC_DIR

DEBUG = True
"""bool: Debugging module-level constant (Default: True)."""

# Define cli filepath
CLI = Path(SRC_DIR, "cmatools", "cli_simple_analysis.py")
"""str: Filepath to command line tool module."""


def test_cli_parser():
    """Test for cli_parser() function."""
    out = cli_parser()
    # Confirm output object is correct parser type
    assert isinstance(out, argparse.ArgumentParser)
    # Confirm cli tool name is correct
    assert out.prog == "CLI-DATA-DOWNLOAD"


def test_cli_parse_args():
    """Test for cli_parse_args() function."""
    user_args = ["--portal=CEDA", "--dataset=HADCRUT"]
    parsed_args = cli_parse_args(user_args)
    if DEBUG:
        print(f"Parsed args: {parsed_args}")
    assert isinstance(parsed_args, argparse.Namespace)
    assert parsed_args.portal == "CEDA"
    assert parsed_args.dataset == "HADCRUT"


# TODO mark as slow
# Keep this simple test, but mock so no actual download occurs
def test_cli_data_download():
    """Test for cli_data_download() function."""
    parsed_args = argparse.Namespace(portal="CEDA", dataset="HADCRUT")
    output = cli_data_download(parsed_args)
    # Expect True, indicates download success
    assert output is True
