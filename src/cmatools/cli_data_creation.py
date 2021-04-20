"""

A simple Command line application tool to create netcdfs

Creates several netcdf files in the data/outputs directory
"""

# Standard library imports.
import argparse
import pkg_resources
import sys

from cmatools.analysis.data_creation import main



DEBUG = True

# Take the version number from the package version in setup
pkg_version = pkg_resources.get_distribution("cmatools").version


def cli_parser() -> argparse.ArgumentParser:
    """Factory function to create parser object for arguments from the command line

    Returns
    -------
    parser : argparse.ArgumentParser

    """
    parser = argparse.ArgumentParser(
        # Adds cli app title, if ommitted the filename is used (e.g. cli-simple.py)
        prog="CLI-DATA",
        description="A simple command line app to create output netcdf data",
        epilog="  ---  ",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    # Returns a parser object, with the metadata and arguments set
    return parser


def cli_arguments(parser) -> argparse.ArgumentParser:
    """Adds cli tool arguments to an existing parser

    Parameters
    ----------
    parser : argparse.ArgumentParser
        An argparse parser

    Returns
    -------
    parser : argparse.ArgumentParser
        Parser object, with specified arguments

    """

    # Arguments in argparse can be optional, positional or required, set to required to force user input
    # Add named arguments (required for the tool to run)
    # Set the argument type (e.g. int) and limit choices from a list
    parser.add_argument("Data", type=str, help="Select data type for outputs", choices=["netcdf"])

    # Returns a parser object, with the arguments set
    return parser


def build_parser() -> argparse.ArgumentParser:
    """Function to build a parser with program details and arguments set

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


def cli_parse_args(argv=None) -> argparse.Namespace:
    """Function to parse the passed arguments into an argparse namespace object

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

    return parser.parse_args(argv)


def cli_data(parsed_args) -> None:

    """Function to create output data

    Parameters
    ----------
    parsed_args : argparse.Namespace
        The command line arguments parsed into a namespace object

    Returns
    -------
    None

    """

    main()


def cli_entry_point(argv=None) -> None:

    """Function to wrap passing the parsed command line arguments to
    the analysis function

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

    cli_data(cli_parse_args(argv))

    # The entrypoint returns none


if __name__ == "__main__":
    # Runs entry point function when called as main
    cli_entry_point()

    if DEBUG:
        print("------")
        print(f"Number of arguments: {len(sys.argv)} arguments.")
        print(f"Argument List: {str(sys.argv)}")
        print("------")
