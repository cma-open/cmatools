"""Common methods for input / output file and data processing."""

import configparser
import os
import tarfile
from pathlib import Path

import requests

from cmatools.definitions import CONFIGFILE, CONFIGLOGS, ROOT_DIR

# Read from user-editable config file
config = configparser.ConfigParser()
config.read(CONFIGFILE)
# Get directory for analysis output files for download
datadir_outputs = config.get('DATADIR', 'OUTPUTS')
# Get location where local input data will be saved, after download
datadir_root = config.get('DATADIR', 'ROOT')
datadir_inputs = config.get('DATADIR', 'INPUTS')
datadir_archives = config.get('DATADIR', 'ARCHIVES')

# TODO check and add equiv func for scratchdir, or refactor to deal with both dirs

DEBUG = True


def return_datadir_root_dir(datadir_root: str) -> None:
    """Set datadir root directory, based on user config input.

    Parameters
    ----------
    datadir_root
        The value set within user editable config file.
    """
    # TODO add link to config file
    # Deal with optional use of home dir
    if datadir_root == 'repo':
        root_dir = ROOT_DIR
    # Deal with optional use of home dir
    elif datadir_root == '~':
        root_dir = os.path.expanduser('~')
    # Set path based on user selected config value
    else:
        root_dir = datadir_root
    if DEBUG:
        print(f'Root data directory user config setting: {datadir_root}')
        print(f'Root data directory path set as: {root_dir}')

    # Validate the user selected datadir is a directory and files are writeable
    if check_access(root_dir):
        return root_dir
    else:
        raise Exception(
            'Datadir root directory not accessible: check value of '
            'DATADIR / ROOT in config.ini'
        )


def return_datadir_archives_dir() -> Path:
    """Get and create datadir archives directory within datadir."""
    archivedir = Path(return_datadir_root_dir(datadir_root)) / datadir_archives
    archivedir.mkdir(parents=True, exist_ok=True)
    if DEBUG:
        print(f'Archive data directory path: {archivedir}')
    return archivedir


def return_datadir_inputs_dir() -> Path:
    """Get and create datadir input directory within datadir."""
    inputdir = Path(return_datadir_root_dir(datadir_root)) / datadir_inputs
    inputdir.mkdir(parents=True, exist_ok=True)
    if DEBUG:
        print(f'Input data directory path: {inputdir}')
    return inputdir


def return_datadir_outputs_dir() -> Path:
    """Get and create datadir output directory within datadir."""
    outputdir = Path(return_datadir_root_dir(datadir_root)) / datadir_outputs
    outputdir.mkdir(parents=True, exist_ok=True)
    if DEBUG:
        print(f'Outputs data directory: {datadir_outputs}')
    return outputdir


def write_source_config(archivename, extractname) -> None:
    """Write archive content names from data input source files."""
    # TODO refactor
    config = configparser.ConfigParser()
    config.read(CONFIGLOGS)
    # config.add_section('SECTION_NAME')
    config['SOURCES']['COP_ARCHIVENAME'] = archivename
    config['SOURCES']['COP_FILENAME'] = extractname
    with open(CONFIGLOGS, 'w') as configfile:
        config.write(configfile)


def extract_archive_singlefile(
        archivedir: Path, inputsdir: Path, filename: str) -> str:
    """Extract files from tarfile.

    Parameters
    ----------
    archivedir
        The directory holding tarfiles.
    inputsdir
        The directory where tarfile contents will be extracted to.
    filename
        The filename of the tarfile archive.

    Returns
    -------
    str
        The content filename within the tarfile archive .
    """
    # Set the full path to the archive file
    archivefilepath = archivedir / filename
    with tarfile.open(archivefilepath, 'r') as archive:
        if DEBUG:
            print(archive.getmembers())
            print(archive.getnames()[0])
        content_filename = archive.getnames()[0]
        print('---')
        # extract all files
        archive.extract(archive.getnames()[0], path=inputsdir)
        print(f'Tar file extracted to: {inputsdir}/{content_filename}')
        return content_filename


def extract_archive_multi(filename: str) -> None:
    """Extract all files from archive.

    Parameters
    ----------
    filename
        The filename of the tarfile archive.
    """
    # TODO refactor
    outputfilepath = Path(return_datadir_inputs_dir()) / filename
    with tarfile.open(outputfilepath, 'r') as archive:
        print(archive.getmembers())
        print(archive.getnames())
        # Extract all files
        archive.extractall(return_datadir_inputs_dir())


def download(url) -> None:
    """Download requested file from URL.

    Parameters
    ----------
    url
        The full url path to the file to download.
    """
    # Set as path object
    urlpath = Path(url)
    # Get filename from url
    urlfilename = urlpath.name
    # Set full path + name to downloaded location
    file_path = return_datadir_inputs_dir() / urlfilename
    # Open in binary mode
    with open(file_path, 'wb') as file:
        # Get response request
        response = requests.get(url)
        # Check if an error has occurred
        response.raise_for_status()
        # Deal with potentially missing encoding header
        encoding = 'None listed'
        if 'Content-Encoding' in response.headers:
            encoding = response.headers['Content-Encoding']
        if DEBUG:
            print(f'Request sent: {response.request.headers}')
            print(
                f'Request response Content-Type: {response.headers["content-type"]} '
                f'with Content-Encoding: {encoding}'
            )
            print(f'Request response status code: {response.status_code}')
            print(f'Request response headers: {response.headers}')
            print(f'Response response filename: {urlfilename}')
            print(f'Download destination: {file_path}')
        # Write downloaded content to file (raw response bytes)
        file.write(response.content)


def check_access(directory: str) -> bool:
    """Check if the directory is accessible and writeable.

    Parameters
    ----------
    directory
        The directory to be checked

    Returns
    -------
    bool
       Returns True if directory is accessible
    """
    path = Path(directory)
    file = path / 'test.txt'
    try:
        file.touch(exist_ok=True)
        file.unlink()  # Remove file
        return True
    except FileNotFoundError as error:
        print(error)
        print('Check that root dir has been correctly set in config.ini')
        raise FileNotFoundError
