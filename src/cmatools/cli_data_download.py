"""Command line application tool for data download of CRUTEM or HadCRUT data.

Datasets can be sourced from either the HadObs or CEDA websites.
Initially for version 5.0.0.0, later to be updated for further versions.

"""
# first pass
# call from cli and downloads from hadobs - chooses hadsst or hadcrut
# - MINIMAL OPTIONS as an example
# test via example calls shell script
# add code comment to show how could be expanded
# uses local set dir so they can be used


import argparse

from cmatools.io.io_common import download
from cmatools.io.read_source import SourceData

DEBUG = True
"""int: Module level constant documented inline (Default: True)."""


def cli_parser() -> argparse.ArgumentParser:
    """Create parser with named arguments."""
    # Can also add prog title to output, if ommitted the filename is used
    # (e.g. cli-simple,py)
    parser = argparse.ArgumentParser(
        # Also possible to add prog title to output,
        # if ommitted the filename is used (e.g. cli_data_download.py)
        prog="CLI-DATA-DOWNLOAD",
        description="A simple example app to aid download of data from remote sources",
        epilog="  ---  ",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    # Arguments in argparse can be optional, positional or required
    # Add named arguments (that is required for the tool to run)
    # Set the argument type and limit choices from a list

    parser.add_argument(
        "--portal",
        type=str,
        help="Data source portal",
        required=True,
        choices=["CEDA", "HADOBS"],
    )
    parser.add_argument(
        "--dataset",
        type=str,
        help="Dataset to be downloaded",
        required=True,
        choices=["CRUTEM", "HADCRUT"],
    )

    # Returns a parser object
    return parser


def cli_parse_args(argv=None) -> argparse.Namespace:
    """
    Parse the passed arguments into an argparse namespace object.

    :param argv:
    :return: argpase.Namespace
    """
    # instantiate cli parser object
    parser = cli_parser()
    # Parse the arguments
    # ArgumentParser.parse_args processes whatever list of strings you pass it.
    # When you pass None, it uses sys.argv[1:] instead
    # This allows testing

    return parser.parse_args(argv)


def cli_data_download(parsed_args) -> bool:
    """
    Run the requested data download.

    :param parsed_args:
    :return:
    """
    if DEBUG:
        print("The cli tool: Data Download has run")
        print(f"Parsed args: {parsed_args}")

    inputs = SourceData(parsed_args.portal, parsed_args.dataset)
    inputs.read_input_source_ini()

    if DEBUG:
        print(f"Downloading {parsed_args.dataset} from {parsed_args.portal}")
        print(f"Downloading: {inputs.download}")

    try:
        download(inputs.download)
        return True
    except Exception:
        return False

    # analysis_sum = parsed_args.x * parsed_args.y
    # print(f'The sum is: {analysis_sum}')


def cli_data_download_entry_point(argv=None):
    """Pass parsed command line arguments to the data download function.

    :param argv:
    :return: None
    """
    # Read arguments from the command line
    # Parsed arguments are present as object attributes
    # Pass the parsed arguments to the cli function
    cli_data_download(cli_parse_args(argv))


if __name__ == "__main__":
    # Runs entry point function when called as main
    cli_data_download_entry_point()
