"""Command line application tool to download canned data for example and test use."""

import argparse

import pkg_resources

from cmatools.canned_data.canned_data import download_subset_canned_data

DEBUG = True

# Take the version number from the package version in setup
pkg_version = pkg_resources.get_distribution("cmatools").version


def cli_parser() -> argparse.ArgumentParser:
    """Create parser object for arguments from the command line.

    Returns
    -------
    parser : argparse.ArgumentParser
    """
    parser = argparse.ArgumentParser(
        # Adds cli app title, if omitted the filename is used (e.g. cli-simple.py)
        prog="CLI-CANNED",
        description="A tool to download example netcdf canned data files from HadObs.",
        epilog="  ---  ",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    # Returns a parser object, with the metadata and arguments set
    return parser
    # -----------------------------     TESTING     -----------------------------
    # unit: a_unit/cli/test_cli_canned_data.py
    # ---------------------------------------------------------------------------


def cli_arguments(parser) -> argparse.ArgumentParser:
    """Add cli tool arguments to an existing parser.

    Parameters
    ----------
    parser : argparse.ArgumentParser
        An argparse parser

    Returns
    -------
    parser : argparse.ArgumentParser
        Parser object, with specified arguments
    """
    # Arguments in argparse can be optional, positional or required,
    # Set to required to force user input
    # Add named arguments (required for the tool to run)
    # Set the argument type (e.g. int) and limit choices from a list
    parser.add_argument(
        "dataset",
        type=str,
        help="Select dataset to download",
        choices=["ALL", "HADCRUT", "HADSST", "CRUTEM"],
        default="ALL",
    )
    # Returns a parser object, with the arguments set
    return parser
    # -----------------------------     TESTING     -----------------------------
    # unit: a_unit/cli/test_cli_canned_data.py
    # ---------------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    """Build parser with program details and arguments set.

    Returns
    -------
    parser : argparse.ArgumentParser

    """
    # Instantiate cli parser object
    parser = cli_parser()
    # Add the arguments
    cli_arguments(parser)
    # Returns a parser object, with the arguments set
    return parser
    # -----------------------------     TESTING     -----------------------------
    # unit: a_unit/cli/test_cli_canned_data.py
    # integration: b_integration/cli/test_cli_canned_data.py
    # ---------------------------------------------------------------------------


def cli_parse_args(argv=None) -> argparse.Namespace:
    """Parse the passed arguments into an argparse namespace object.

    Parameters
    ----------
    argv : str
       The arguments from the command line

    Returns
    -------
    parser.parse_args(argv) : argparse.Namespace
        The namespace object holding the command line arguments
    """
    # Instantiate cli parser object
    # Add the arguments
    parser = build_parser()
    # Parse the arguments
    # ArgumentParser.parse_args processes whatever list of strings you pass it.
    # When you pass None, it uses sys.argv[1:] instead, this allows testing
    namespace = parser.parse_args(argv)
    return namespace
    # -----------------------------     TESTING     -----------------------------
    # unit: a_unit/cli/test_cli_canned_data.py
    # integration: b_integration/cli/test_cli_canned_data.py
    # ---------------------------------------------------------------------------


def cli_canned_data(parsed_args) -> list:
    """Download canned data from hadobs.

    Parameters
    ----------
    parsed_args : argparse.Namespace
        The command line arguments parsed into a namespace object

    Returns
    -------
    list
        List of filepaths to the canned data downloaded and subset
    """
    file_list = []
    if parsed_args.dataset == "ALL":
        hadsst_file = download_subset_canned_data("HADSST")
        hadcrut_file = download_subset_canned_data("HADCRUT")
        # hadisdh_file = download_subset_canned_data("HADISDH")
        crutem_file = download_subset_canned_data("CRUTEM")
        files = [hadsst_file, hadcrut_file, crutem_file]
        file_list.append(files)
    else:
        dataset_file = download_subset_canned_data(parsed_args.dataset)
        file_list.append(dataset_file)
    return file_list
    # -----------------------------     TESTING     -----------------------------
    # unit: a_unit/cli/test_cli_canned_data.py
    # integration: b_integration/cli/test_cli_canned_data.py
    # ---------------------------------------------------------------------------


def cli_entry_point(argv=None) -> None:
    """Wrap the parsed command line arguments to the download function.

    Parameters
    ----------
    argv : str
       The command line arguments

    Returns
    -------
    None
    """
    # Read arguments from the command line
    # Parsed arguments are present as object attributes
    # Pass the parsed arguments to the cli data function
    # The entrypoint returns none
    cli_canned_data(cli_parse_args(argv))
    # -----------------------------     TESTING     -----------------------------
    # unit: a_unit/cli/test_cli_canned_data.py
    # integration: b_integration/cli/test_cli_canned_data.py
    # ---------------------------------------------------------------------------
