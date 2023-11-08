"""Test the cli_canned_data tool."""

import argparse
from pathlib import Path
from unittest.mock import patch

from cmatools.cli_canned_data import (  # cli_parser,
    build_parser,
    cli_canned_data,
    cli_entry_point,
    cli_parse_args,
)
from cmatools.definitions import SRC_DIR

DEBUG = True
"""bool: Debugging module-level constant (Default: True)."""

# Define cli filepath
CLI = Path(SRC_DIR, "cmatools", "cli_canned_data.py")
# No constant docstring, to avoid publishing system paths


def test_build_parser():
    """Test for build_parser() function."""
    # Create new parser object to allow testing
    parser = build_parser()
    # Confirm expected object type
    assert isinstance(parser, argparse.ArgumentParser)
    # TESTED components
    # -----------------
    # cli_parser(), cli_arguments()


def test_cli_parse_args():
    """Test for build_parser() function."""
    # Set test argv as one of the expected values
    test_argv = ["HADCRUT"]
    namespace = cli_parse_args(argv=test_argv)
    # Confirm expected object type
    assert isinstance(namespace, argparse.Namespace)
    if DEBUG:
        print(namespace)
        print(vars(namespace))
    # TESTED components
    # -----------------
    # build_parser()


# Mock out the data subset function, download to tmp_path
def test_cli_canned_data(tmp_path):
    """Test for cli_canned_data() function."""
    # Create parser and parse to namespace to avoid use of other functions
    parser = argparse.ArgumentParser(prog="TESTING")
    parser.add_argument(
        "dataset",
        type=str,
        help="Select dataset to download",
        choices=["ALL", "HADCRUT", "HADSST", "HADISDH"],
        default="ALL",
    )
    # Create namespace
    test_namespace = parser.parse_args(["HADCRUT"])
    # Run function, but mock out directory, so downloads to temp_path
    with patch("cmatools.canned_data.canned_data.CANNED_DATA", tmp_path):
        file_list = cli_canned_data(test_namespace)
        # Confirm expected function return
        assert isinstance(file_list, list)
        for file in file_list:
            assert Path(file).is_file()
        if DEBUG:
            print(f"Test namespace: {test_namespace}")
            print(f"File list: {file_list}")
    # TESTED components
    # -----------------
    # download_subset_canned_data()


# START HERE - need fix test below

# Mock out the actual data download, so only the current function is tested
@patch("cmatools.cli_canned_data.cli_parse_args")
@patch("cmatools.cli_canned_data.download_subset_canned_data")
def test_cli_entry_point(mock_cli, mock_parse_args):
    """Test for cli_entry_point() function."""
    # Create parser and parse to namespace to avoid use of other functions
    parser = argparse.ArgumentParser(prog="TESTING")
    parser.add_argument(
        "dataset",
        type=str,
        help="Select dataset to download",
        choices=["ALL", "HADCRUT", "HADSST", "HADISDH"],
        default="ALL",
    )
    # Create namespace
    test_namespace = parser.parse_args(["HADCRUT"])
    outcome = cli_entry_point(test_namespace)
    print(outcome)

    # Set mock output from cli_canned_data
    mock_cli.return_value = None
    # Set mock output as a namespace object
    mock_parse_args.return_value = argparse.Namespace(dataset="HADCRUT")
    # Need to pass a value, but this is not used, as functionality is all mocked out
    test_argv = None
    status = cli_entry_point(test_argv)
    # Confirm expected function return
    assert status is None
    # TESTED components
    # -----------------
    # cli_canned_data()
    # cli_parse_args()


# TODO move to user testing ?

# def test_cli_arguments():
#     """Test for cli_arguments() function."""
#     parser = argparse.ArgumentParser()
#     out = cli_arguments(parser)
#     assert isinstance(out, argparse.ArgumentParser)
#     print(out)
#     print()
#     check = out.parse_args(['ALL'])
#     print(check)
#     # test correct arguents have beebn set by check
#     raises error message following arguments are required: Dataset
#     # TODO
#     # unit test or not?
#     #assert
#     message = "missing 1 required positional argument"
#     with pytest.raises(TypeError, match=message):
#         args = out.parse_args()
#     # also can chekc multiple errors???
#     # assertion errors
