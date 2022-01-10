"""Command line application - a simple analysis tool example.

Example
-------
Example text here including
literal blocks::

    $ python cli_simple_analysis.py

"""

import argparse
import sys

import pkg_resources

from cmatools.analysis.simple_analysis import (
    analysis_max,
    analysis_product,
    analysis_sum,
)
from cmatools.combine.combine import combined

DEBUG = True
"""bool: Debugging level, module level constant (Default: True)."""


# Take the version number from the package version in setup
pkg_version = pkg_resources.get_distribution("cmatools").version


def cli_parser() -> argparse.ArgumentParser:
    """Create parser with arguments set.

    Examples
    --------
    Examples should be written in doctest format, and should illustrate how
    to use the function.
    >>> print([i for i in example_generator(4)])
    [0, 1, 2, 3]
    """
    parser = argparse.ArgumentParser(
        prog="CLI-SIMPLE-ANALYSIS",
        description="A simple app to conduct analysis on two integers",
        epilog="  ---  ",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    # Arguments in argparse can be positional or optional
    # Set the argument type and limit choices from a list

    parser.add_argument("x", type=int, help="the x value", choices=[0, 1, 2, 3, 4, 5])
    parser.add_argument("y", type=int, help="the y value", choices=[0, 1, 2, 3, 4, 5])

    parser.add_argument(
        "--verbose",
        action="store_true",  # Set attribute to true is optional flag is used
        # store_true action requires no input argument
        dest="verbose",  # Set attribute name
        help="Display verbose print output",
    )

    parser.add_argument(
        "--version",
        action="version",  # Prints version information and exits when invoked
        help="Display the version of the cli tool",
        version=f"{parser.prog} {pkg_version}",
    )

    # Further options max, sum, combined are mutually exclusive options
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--sum", dest="sum", action="store_true", help="Sum the integers together"
    )

    group.add_argument(
        "--max",
        dest="max",
        action="store_true",
        help="Find the max value of the integers",
    )

    group.add_argument(
        "--combined",
        dest="combined",
        action="store_true",
        help="Combined analysis: sum the product with the sum of the integers",
    )

    # Returns a parser object
    return parser


def cli_parse_args(argv=None) -> argparse.Namespace:
    """Parse arguments into an argparse namsepace object.

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


def cli_analysis(parsed_args):
    """Run simple analysis on the passed x and y arguments.

    :param parsed_args:
    :return:
    """
    # Determine the analysis type based on the flags used, or return default analysis
    if parsed_args.sum:
        analysis_result = analysis_sum(parsed_args.x, parsed_args.y)
        analysis_method = "sum"
    elif parsed_args.max:
        analysis_result = analysis_max(parsed_args.x, parsed_args.y)
        analysis_method = "max"
    elif parsed_args.combined:
        # Combined method is the sum of the integers product and the integers sum
        # Combined function calls analysis_product and analysis_sum functions
        analysis_result = combined(parsed_args.x, parsed_args.y)
        analysis_method = "combined"
    else:
        # Set the default behaviour if no other options selected
        analysis_result = analysis_product(parsed_args.x, parsed_args.y)
        analysis_method = "default:product"

    # Modify output if optional verbose flag has been used
    if parsed_args.verbose:
        print(f"Parsed args object: {parsed_args}")
        print("The cli tool: SIMPLE has run")
        print(f"Simple analysis method: {analysis_method}")
        print(f"The x value is: {parsed_args.x}")
        print(f"The y value is: {parsed_args.y}")
        print(f"The result is: {analysis_result}")
    else:
        print(analysis_result)

    return analysis_result


def cli_entry_point(argv=None):
    """Pass command line arguments to the analysis function.

    :param argv:
    :return: None
    """
    # Read arguments from the command line
    # Parsed arguments are present as object attributes
    # Pass the parsed arguments to the cli analysis function
    cli_analysis(cli_parse_args(argv))


if __name__ == "__main__":
    # Runs entry point function when called as main
    cli_entry_point()

    if DEBUG:
        print("------")
        print(f"Number of arguments: {len(sys.argv)} arguments.")
        print(f"Argument List: {str(sys.argv)}")
        print("------")
