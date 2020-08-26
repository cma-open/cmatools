# resources
# https://stackoverflow.com/questions/7498595/python-argparse-add-argument-to-multiple-subparsers
# https://stackoverflow.com/questions/33645859/how-to-add-common-arguments-to-argparse-subcommands
# http://www.chiark.greenend.org.uk/doc/python3/html/library/argparse.html
# https://sphinx-argparse.readthedocs.io/en/stable/sample.html
# https://stackoverflow.com/questions/60209079/how-to-test-if-name-main-with-passing-command-line-arguments?noredirect=1&lq=1

"""

Command line application tool for CMATOOLS

Allows CMA observation datasets to be examined by type

"""

import sys
import argparse
import pkg_resources

import pandas as pd

# TODO add notes to clarify normal split of funtionality out into seperate files, but data kept
# here for ease of building prototype

# command line interface / command line application
# cli tool to list all observations datasets, or subdivided by marine or land

# used in the form

# python cli.py [command] [options] argument

# commands: all (list all) or pick (random)
# options:  limit the selection to netcdf
# argument:  dataset (marine, land, blended)

# the output is a printout of the pandas dataframe object

DEBUG = True

# Input data, TODO move to be read from file


data = {'dataset': ['data1', 'data2', 'data3', 'data4', 'data5', 'data6'],
       'category': ['blended', 'marine', 'land', 'land', 'marine', 'marine'],
       'format': ['.netcdf', '.csv', '.csv', '.zip', '.netcdf', '.netcdf']
       }

datapd = pd.DataFrame(data)


def observations(args):
    """ Select and return the type of cma observation from user defined selection

    :param args:
    :return:
    """

    # Select from the dataframe based on the input dataset category
    obs_selection = datapd.loc[datapd['category'] == args.dataset]
    # There should always be a selection, all data entries should have a category
    return obs_selection

def check_netcdf(args, obs_selection):
    """ Check for netcdf flag and if present, select only netcdf records

    """

    if args.netcdf:
        obs_netcdf = obs_selection.loc[obs_selection['format'] == '.netcdf']
        return obs_netcdf
    else:
        return obs_selection

def all(args):
    return check_netcdf(args, observations(args))

def pick(args):
    obs = check_netcdf(args, observations(args))
    # sample returns 1 value as default, using n=1 for clarity and testing of other values
    sample = obs.sample(n=1)
    return sample

# Take the version nunmber from the package version in setup
pkg_version = pkg_resources.get_distribution("cmatools").version

# change name to set_parser or similar
def parse_args(argv=None):
    """Function to wrap parsing of arguments from the command line """


    # Create parent parser object. Paren tis used to ensure common arguments for optional subcommands
    parent_parser = argparse.ArgumentParser(prog='CMATOOLS',
                                        add_help=False
                                        )
    # add_help=False is used to avoid conflict with subparsers, when parents is used to inherit options
    # https://docs.python.org/3/library/argparse.html#parents

    # Can also add prog title to output, prog='CMATOOLS', if ommitted the filename is used (e.g. cli,py)

    # Set optional flag to show the app version
    parent_parser.add_argument('--version',
                               action='version',
                               help='Display the current version of the cmatool package',
                               version=f'{parent_parser.prog} {pkg_version}')

    # Set the positional argument name
    parent_parser.add_argument('dataset',
                               default='blended',
                               choices=['blended', 'marine', 'land'],
                               nargs='?', # specify number of arg, required to ensure default is applied
                               help='Type of dataset to select')

    # Set optional flag
    parent_parser.add_argument('--netcdf',
                               action='store_true',
                               help='Limit selection to netcdf datasets only')

    # Create parent parser object. Add description that will appear in the cli app help output
    parser = argparse.ArgumentParser(
        prog='CMATOOLS',
        description=f'A simple app to list CMA observations datasets. Version {pkg_version}',
        epilog='  ---  ',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        parents=[parent_parser]
    )

    subparsers = parser.add_subparsers(title='sub-commands', description='Valid sub-commands',
                                       help='Choose the data selection method', dest='Subcommand', required=True)

    # Set the commands - by using subparsers
    all_parser = subparsers.add_parser('all', help='List all categories of datasets', parents=[parent_parser])
    pick_parser = subparsers.add_parser('pick', help='Pick one example dataset category at random', parents=[parent_parser])

    all_parser.set_defaults(func=all)

    pick_parser.set_defaults(func=pick)

    # ArgumentParser.parse_args processes whatever list of strings you pass it.
    # When you pass None, it uses sys.argv[1:] instead
    # This allows testing

    #return parser.parse_args(argv)
    return parser



def main(args):

    # Read arguments from the command line
    #parser = parse_args(sys.argv[1:])
    #args = parse_args()
    #args = parser.parse_args()
    #args = sub_parser.parse_args()

    if DEBUG:
        print(args)
    output = args.func(args) # Call the default function, based on the command arguments passed
    if not output.empty:
        print(output)
    else:
        print('Search criteria returned no datasets')

def cli_entry_point(argv=None):
    # Read arguments from the command line
    #args = parse_args(argv)
    args = parse_args(argv)
    args_parsed = args.parse_args(args)

    # args = parse_args(argv)
    main(args_parsed)

    #main(args)

if __name__ == '__main__':
    cli_entry_point()

# TODO list options
# Add logging, as example to log each run, inputs and outputs