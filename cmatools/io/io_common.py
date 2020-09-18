import configparser
import os
from pathlib import Path
import tarfile

from cmatools.definitions import ROOT_DIR, CONFIGFILE, CONFIGLOGS

# read from user-editable config file
config = configparser.ConfigParser()
config.read(CONFIGFILE)

# Read from the source config list to set directory for analysis output files for download
outputs = config.get("DATADIR", "OUTPUTS")
# set the location where local input data will be saved, after download
datadir_root = config.get("DATADIR", "ROOT")
datadir_inputs = config.get("DATADIR", "INPUTS")
datadir_archives = config.get("DATADIR", "ARCHIVES")


DEBUG = True

def datadir_archives_dir():
    archivedir = Path(return_datadir_root_dir()) / datadir_inputs
    archivedir.mkdir(parents=True, exist_ok=True)
    if DEBUG:
        print(archivedir)
    return archivedir

def datadir_inputs_dir():
    inputdir = Path(return_datadir_root_dir()) / datadir_inputs
    inputdir.mkdir(parents=True, exist_ok=True)
    if DEBUG:
        print(datadir_inputs)
        print(inputdir)
    return inputdir

def return_datadir_root_dir():
    user_root_dir = os.path.expanduser(datadir_root)
    if DEBUG:
        print(datadir_root)
        print(user_root_dir)
    return user_root_dir

def write_source_config(archivename, extractname):

    """ write archive content names from data input source files"""

    config = configparser.ConfigParser()
    config.read(CONFIGLOGS)
    #config.add_section('SECTION_NAME')

    config['SOURCES']['COP_ARCHIVENAME'] = archivename
    config['SOURCES']['COP_FILENAME'] = extractname

    with open(CONFIGLOGS, 'w') as configfile:
        config.write(configfile)


def extract_archive_singlefile(filename):
    """ extract downloaded files

    expects file to be in location specified in ini file
    """

    archivefilepath = Path(datadir_archives_dir()) / filename
    with tarfile.open(archivefilepath, 'r') as archive:
        print(archive.getmembers())
        print(archive.getnames()[0])
        content_filename = archive.getnames()[0]
        print("--------")
        # extract all files
        archive.extract(archive.getnames()[0], path=datadir_inputs_dir())
        print("extracted")
        print(content_filename)

        return content_filename


def extract_archive_multi(filename):
    """ extract downloaded files

    expects file to be in location specified in ini file
    """

    outputfilepath = Path(datadir_inputs_dir()) / filename
    with tarfile.open(outputfilepath, 'r') as archive:
        print(archive.getmembers())
        print(archive.getnames())

        # extract all files
        archive.extractall(datadir_inputs_dir())