import argparse

import pkg_resources

# Replace click with the name of your tool:
pkg_version = pkg_resources.get_distribution("cmatools").version

# cli too to list all observations datasets, or subdivided by marine or land

# used in the form
# python cli.py [command] [options] argument
# commands are list or pick (random)
# options can limit the selection to netcdf or csv
# argument is dataset type (default all, or ocean, land, blended)

def observationsg(args):
    output = '{0}, {1}!'.format(args.greeting, args.name)
    if args.caps:
        output = output.upper()
    print(output)

def list(args):
    print("list the list")
    output = '{0}, {1}!'.format(args.netcdf, args.dataset)
    print(output)
    #print(parser.version)
    pass

def pick(args):
    print("pick of list")
    pass

parser = argparse.ArgumentParser()
parser.add_argument('--version', action='version', help="Shows current tool version", version=pkg_version)
#parser.add_argument('--version', action='version', version="1.1.1")

subparsers = parser.add_subparsers()

# set the commands
list_parser = subparsers.add_parser('list')
pick_parser = subparsers.add_parser('pick')

# set the positional argument
list_parser.add_argument('dataset', help='Type of dataset to select')

# set the optional arguments (flags)
list_parser.add_argument('--netcdf', action='store_true',  help='Limit selection to netcdf datasets')
#hello_parser.add_argument('--caps', action='store_true', help='uppercase the output')
list_parser.set_defaults(func=list)

# set the positional argument
pick_parser.add_argument('dataset', help='Type of dataset to select')

# set the optional argument (flags)
pick_parser.add_argument('--netcdf',  action='store_true', help='Limit selection to netcdf datasets')
#goodbye_parser.add_argument('--caps', action='store_true', help='uppercase the output')
pick_parser.set_defaults(func=pick)

#parser.parse_args(['--version'])

def obsdata():
    args = parser.parse_args()
    args.func(args) # call the default function, based on the command arguments passed

if __name__ == '__main__':
    obsdata()
