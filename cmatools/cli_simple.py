
"""

Command line application tool for SIMPLE

Allows development and testing of simple command line tool

"""

import sys
import argparse

DEBUG = True


def cli_parser() -> argparse.ArgumentParser :
    """Function to wrap parsing of arguments from the command line """

    # Can also add prog title to output, if ommitted the filename is used (e.g. cli-simple,py)

    parser = argparse.ArgumentParser(
        prog='SIMPLE',
        description=f'A simple app',
        epilog='  ---  ',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    # Arguments in argparse can be optional, positional or required
    # Add named arguments (that is required for the tool to run)
    # Set the argument type and limit choices from a list
    parser.add_argument("--x", type=int, help="the x value", required=True, choices=[0,1,2,3,4,5])
    parser.add_argument("--y", type=int, help="the y value", required=True, choices=[0,1,2,3,4,5])

    # Returns a parser object
    return parser

def cli_parse_args(argv=None) -> argparse.Namespace:
    # instantiate cli parser object
    parser = cli_parser()
    # Parse the arguments
    # ArgumentParser.parse_args processes whatever list of strings you pass it.
    # When you pass None, it uses sys.argv[1:] instead
    # This allows testing

    return parser.parse_args(argv)

def cli_analysis(parsed_args):

    if DEBUG:
        print(parsed_args)

    print('The cli tool: SIMPLE has run')
    print(f'The x value is: {parsed_args.x}')
    print(f'The y value is: {parsed_args.y}')

    analysis_sum = parsed_args.x * parsed_args.y
    print(f'The sum is: {analysis_sum}')
    return analysis_sum


def cli_simple_entry_point(argv=None):

    # Read arguments from the command line
    # Parsed arguments are present as object attributes
    # Pass the parsed arguments to the cli analysis function
    cli_analysis(cli_parse_args(argv))

if __name__ == '__main__':
    # Runs entry point function when called as main
    cli_simple_entry_point()