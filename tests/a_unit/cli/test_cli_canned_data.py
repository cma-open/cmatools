"""Unit tests for the cli_canned_data tool."""

import argparse
from pathlib import Path
from unittest.mock import patch

from cmatools.cli_canned_data import (
    build_parser,
    cli_arguments,
    cli_canned_data,
    cli_entry_point,
    cli_parse_args,
    cli_parser,
)
from cmatools.definitions import SRC_DIR

DEBUG = True
"""bool: Debugging module-level constant (Default: True)."""

# Define cli filepath
CLI = Path(SRC_DIR, "cmatools", "cli_canned_data.py")
# No constant docstring, to avoid publishing system paths


def test_cli_parser():
    """Test for cli_parser() function."""
    out = cli_parser()
    # Confirm output object is correct parser type
    assert isinstance(out, argparse.ArgumentParser)
    # Confirm cli tool name is correct
    assert out.prog == "CLI-CANNED"


def test_cli_arguments():
    """Test for cli_arguments() function."""
    # Create new parser object to allow testing
    parser = argparse.ArgumentParser()
    # Create cli_arguments object, passing parser
    out = cli_arguments(parser)
    # Confirm expected object type
    assert isinstance(out, argparse.ArgumentParser)


# mock out the cli_parser and cli_arguments functions
@patch("cmatools.cli_canned_data.cli_arguments")
@patch("cmatools.cli_canned_data.cli_parser")
def test_build_parser(mock_parser, mock_arguments):
    """Test for build_parser() function."""
    # Create mock return parser, name as TESTING to aid debugging
    mock_parser.return_value = argparse.ArgumentParser(prog="TESTING")
    # Add an argument to the parser, to mock behaviour of cli_arguments
    mock_parser.return_value.add_argument(
        "testdataset",
        type=str,
        help="Select dataset to download",
        choices=["ALL", "HADCRUT", "HADSST", "HADISDH"],
        default="ALL",
    )
    # Mock out cli_arguments as the new updated parser, with added argument
    mock_arguments.return_value = mock_parser.return_value
    # Create the parser object (behaviour will be mocked)
    parser = build_parser()
    # Confirm expected object type
    assert isinstance(parser, argparse.ArgumentParser)
    if DEBUG:
        print(mock_parser)
        print(mock_arguments)
        print(mock_parser.return_value)
        print(mock_arguments.return_value)
        namespace = parser.parse_args(["ALL"])
        print(namespace)


# mock out build_parser()
@patch("cmatools.cli_canned_data.build_parser")
def test_cli_parse_args(mock_parser):
    """Test for build_parser() function."""
    parser = argparse.ArgumentParser(prog="TESTING")
    parser.add_argument(
        "testdataset",
        type=str,
        help="Select dataset to download",
        choices=["ALL", "HADCRUT", "HADSST", "HADISDH"],
        default="ALL",
    )
    mock_parser.return_value = parser
    # Set test argv as one of the expected values (HADCRUT)
    test_argv = ["HADCRUT"]
    namespace = cli_parse_args(argv=test_argv)
    # Confirm expected object type
    assert isinstance(namespace, argparse.Namespace)
    assert namespace.testdataset == "HADCRUT"
    if DEBUG:
        print(f"Test parser namespace: {namespace}")
        print(vars(namespace))


# Mock out the actual data download, so only the current function is tested
@patch("cmatools.cli_canned_data.download_subset_canned_data")
def test_cli_canned_data(mock_download_subset):
    """Test for cli_canned_data() function."""
    # Set mock output filepath from download subset
    mock_download_subset.return_value = "path/to/output/hadcrut.nc"
    # Create parser and parse to namespace to avoid use of other functions
    parser = argparse.ArgumentParser(prog="TESTING")
    parser.add_argument(
        "dataset",
        type=str,
        help="Select dataset to download",
        choices=["ALL", "HADCRUT", "HADSST", "HADISDH"],
        default="ALL",
    )
    test_namespace = parser.parse_args(["HADCRUT"])
    # Run function, but mock out actual download, just return a path
    file_list = cli_canned_data(test_namespace)
    # Confirm expected function return
    assert isinstance(file_list, list)
    if DEBUG:
        print(f"Test namespace: {test_namespace}")
        print(f"File list: {file_list}")


# Mock out the actual data download, so only the current function is tested
@patch("cmatools.cli_canned_data.cli_parse_args")
@patch("cmatools.cli_canned_data.cli_canned_data")
def test_cli_entry_point(mock_canned_data, mock_parse_args):
    """Test for cli_entry_point() function."""
    # Set arg value
    test_argv = ["HADCRUT"]
    # Set mock output from cli_canned_data
    mock_canned_data.return_value = ["path/to/output/hadcrut.nc"]
    # Set mock output as a namespace object
    parser = argparse.ArgumentParser(prog="TESTING")
    parser.add_argument(
        "dataset",
        type=str,
        help="Select dataset to download",
        choices=["ALL", "HADCRUT", "HADSST", "HADISDH"],
        default="ALL",
    )
    mock_parse_args.return_value = parser.parse_args(test_argv)
    # Run function, internal functions returned are mocked out
    status = cli_entry_point(test_argv)
    # Confirm expected function return
    assert status is None
    if DEBUG:
        print(f"Namespace: {mock_parse_args.return_value}")
