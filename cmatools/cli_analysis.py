
"""

Command line application tool for SIMPLE

Allows development and testing of simple command line tool o

"""

import sys
import argparse
import pkg_resources

import pandas as pd

DEBUG = True

# Take the version nunmber from the package version in setup
pkg_version = pkg_resources.get_distribution("cmatools").version


def parse_args(argv=None):
    """Function to wrap parsing of arguments from the command line """

    # Can also add prog title to output, if ommitted the filename is used (e.g. cli-simple,py)

    # Arguments in argparse can be optional, positional or required

    parser = argparse.ArgumentParser(
        prog='ANALYSIS',
        description=f'An app to carry out analysis for the installed package',
        epilog='  ---  ',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    # Set optional flag to show the app version
    # Adds the optional argument to the cli, with the long name flag
    parser.add_argument('--version',
                               action='version',
                               help='Display the current version of the cmatool package',
                               version=f'{parser.prog} {pkg_version}')

    # ArgumentParser.parse_args processes whatever list of strings you pass it.
    # When you pass None, it uses sys.argv[1:] instead
    # This allows testing

    #return parser.parse_args(argv)
    return parser


def cli_run(args_parsed):

    if DEBUG:
        print(args_parsed)

    print('The cli tool: ANALYSIS has run')

def cli_analysis_entry_point(argv=None):
    # Read arguments from the command line
    args = parse_args(argv)

    # parsed arguments are present as object attributes
    args_parsed = args.parse_args(args)

    #args = parse_args(argv)
    cli_run(args_parsed)

if __name__ == '__main__':
    cli_analysis_entry_point()