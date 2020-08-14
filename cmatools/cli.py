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

DEBUG = False

# Input data, TODO move to be read from file


data = {'dataset': ['data1', 'data2', 'data3', 'data4', 'data5', 'data6'],
       'category': ['blended', 'marine', 'land', 'land', 'marine', 'marine'],
       'format': ['.netcdf', '.csv', '.csv', '.zip', '.netcdf', '.netcdf']
       }

datapd = pd.DataFrame(data)


def observations(args):
    # Select from the dataframe based on the input dataset category
    obs_selection = datapd.loc[datapd['category'] == args.dataset]
    # There should always be a selection, all data entries should have a category
    return obs_selection

def check_netcdf(args, obs_selection):
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

# Create parser object. Add description that will appear in the cli app help output
parser = argparse.ArgumentParser(
    prog='CMATOOLS',
    description=f'A simple app to list CMA observations datasets. Version {pkg_version}',
    epilog='  ---  '
)
# Can also add prog title to output, prog='CMATOOLS', if ommitted the filename is used (e.g. cli,py)

# Set optional flag to show the app version
parser.add_argument('--version', action='version', help='The current tool version', version=f'{parser.prog} {pkg_version}')

# Set the positional argument name
parser.add_argument('dataset', default='all', choices=['blended', 'marine', 'land'], help='Type of dataset to select')

# Set optional flag
parser.add_argument('--netcdf', action='store_true',  help='Limit selection to netcdf datasets')


subparsers = parser.add_subparsers(title='subcommands', description='Valid subcommands',
                                   help='Data selection method', dest='Subcommand', required=True)
# Set the commands - by using subparsers
all_parser = subparsers.add_parser('all', help='List all datasets')
pick_parser = subparsers.add_parser('pick', help='Pick an example dataset at random')

# Set the positional argument
#all_parser.add_argument('dataset', default='all', help='Type of dataset to select')

# Set the optional arguments (flags)
#all_parser.add_argument('--netcdf', action='store_true',  help='Limit selection to netcdf datasets')
all_parser.set_defaults(func=all)

# set the positional argument
#pick_parser.add_argument('dataset', default='all', help='Type of dataset to select')

# set the optional argument (flags)
#pick_parser.add_argument('--netcdf',  action='store_true', help='Limit selection to netcdf datasets')
pick_parser.set_defaults(func=pick)


def obsdata():
    args = parser.parse_args()
    if DEBUG:
        print(args)
    output = args.func(args) # Call the default function, based on the command arguments passed
    if not output.empty:
        print(output)
    else:
        print('Search criteria returned no datasets')

if __name__ == '__main__':
    obsdata()

# TODO list options
# Add logging, as example to log each run, inputs and outputs