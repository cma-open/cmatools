"""Command line application tool for data download from Copernicus."""

import argparse
import configparser

from cmatools.definitions import CONFIGFILE, CONFIGLOGS, ROOT_DIR
from cmatools.io.copernicus_api import copernicus_check_downloads, copernicus_downloads
from cmatools.io.io_common import (  # download,
    extract_archive_singlefile,
    return_datadir_archives_dir,
    return_datadir_inputs_dir,
)
from cmatools.io.read_source import SourceData

# TODO move these out to copernicus location ????
# read from user-editable config file
config = configparser.ConfigParser()
config.read(CONFIGFILE)
datadir_root = config.get('DATADIR', 'ROOT')
datadir_inputs = config.get('DATADIR', 'INPUTS')
datadir_archives = config.get('DATADIR', 'ARCHIVES')

DEBUG = True
"""int: Module level constant documented inline (Default: True)."""


def cli_parser() -> argparse.ArgumentParser:
    """Create parser with set arguments."""
    parser = argparse.ArgumentParser(
        # Also possible to add prog title to output,
        # if ommitted the filename is used (e.g. cli-simple.py)
        prog='CLI-COPERNICUS-DOWNLOAD',
        description='A simple example app to aid download of data from Copernicus',
        epilog='  ---  ',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    # Arguments in argparse can be optional, positional or required
    # Add named arguments (that is required for the tool to run)
    # Set the argument type and limit choices from a list

    parser.add_argument(
        '--portal', type=str, help='Data source portal', required=True, choices=['COP']
    )
    parser.add_argument(
        '--dataset',
        type=str,
        help='Dataset to be downloaded',
        required=True,
        choices=['E-OBS', 'OTHER'],
    )
    parser.add_argument(
        '--dryrun',
        type=str,
        help='Dry run of dataset to be downloaded, '
             'test only, no data will be downloaded',
        required=True,
        choices=['True', 'False'],
    )

    # Returns a parser object
    return parser


def cli_parse_args(argv=None) -> argparse.Namespace:
    """
    Parse the arguments into an argparse namespace object.

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


def cli_copernicus_download(parsed_args):
    """Run the requested data download.

    :param parsed_args:
    :return:
    """
    if DEBUG:
        print('The cli tool: Copernicus Data Download has run')
        print(f'Parsed args: {parsed_args}')

    inputs = SourceData(parsed_args.portal, parsed_args.dataset)
    inputs.read_input_source_ini()

    dataset = inputs.long
    content = {
        'format': inputs.format,
        'product_type': inputs.product_type,
        'variable': inputs.variables,
        'grid_resolution': inputs.grid_res,
        'period': inputs.period,
        'version': inputs.version,
    }
    filename = 'eobs.tgz'

    # Set download dir path ofr the compressed archive file
    # Downloads to archive dir
    outputfilepath = return_datadir_archives_dir() / filename

    if DEBUG:
        print(
            f'Downloading: {parsed_args.dataset}, {dataset} '
            f'data from {parsed_args.portal}'
        )
        print(f'Downloading content: {content}')

    # Move later to different location

    if parsed_args.dryrun == 'True':
        copernicus_check_downloads(dataset, content)

    else:
        copernicus_downloads(dataset, content, outputfilepath)
        print(f'Copernicus tar file downloaded to: {outputfilepath} ')
        # At this stage of dev - assuming tar archives will contain a singe file
        extract_archive_singlefile(
            return_datadir_archives_dir(), return_datadir_inputs_dir(), filename
        )

    return None


def cli_copernicus_download_entry_point(argv=None):
    """
    Pass the parsed command line arguments to the data download function.

    :param argv:
    :return: None
    """
    # Read arguments from the command line
    # Parsed arguments are present as object attributes
    # Pass the parsed arguments to the cli function
    cli_copernicus_download(cli_parse_args(argv))


if __name__ == '__main__':
    # Runs entry point function when called as main
    cli_copernicus_download_entry_point()
    # print current status
    print(f'Debug status: {DEBUG}')
    print(f'Logs: {CONFIGLOGS}')
    print(f'Root: {ROOT_DIR}')
