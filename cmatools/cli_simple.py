
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

    parser = argparse.ArgumentParser(
        prog='SIMPLE',
        description=f'A simple app to list version of the installed package',
        epilog='  ---  ',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    # Set optional flag to show the app version
    parser.add_argument('--version',
                               action='version',
                               help='Display the current version of the cmatool package',
                               version=f'{parser.prog} {pkg_version}')

    # Set the positional argument name
    parser.add_argument('dataset',
                               default='blended',
                               choices=['blended', 'marine', 'land'],
                               nargs='?', # specify number of arg, required to ensure default is applied
                               help='Type of dataset to select')



    # ArgumentParser.parse_args processes whatever list of strings you pass it.
    # When you pass None, it uses sys.argv[1:] instead
    # This allows testing

    #return parser.parse_args(argv)
    return parser


def main(args):

    if DEBUG:
        print(args)

    print('The cli tool: SIMPLE has run')

def cli_simple_entry_point(argv=None):
    # Read arguments from the command line
    args = parse_args(argv)
    args_parsed = args.parse_args(args)

    #args = parse_args(argv)
    main(args_parsed)

if __name__ == '__main__':
    cli_simple_entry_point()