"""Download and store canned data locally via download from HadObs."""

import configparser
from pathlib import Path

import iris

from cmatools.data_creation.canned_cubes import extract_timesteps
from cmatools.definitions import REPO_DIR, ROOT_DIR
from cmatools.io.common import return_cube_from_url

# # Set names for downloaded files
# HADSST_SHORT = "HADSST_short.nc"
# HADCRUT_SHORT = "HADCRUT_short.nc"
# CRUTEM_SHORT = "CRUTEM_short.nc"
# HADISDH_SHORT = "HADISDH_short.nc"
# tos_file = "tos_O1_2001-2002.nc"
#
# FILES = [HADCRUT_SHORT, CRUTEM_SHORT, HADSST_SHORT, HADISDH_SHORT, tos_file]

# Set local canned data dir path
CANNED_DATA = Path(REPO_DIR) / "data" / "canned"

SOURCE_PATH = ""


DEBUG = True


def return_config():
    """Return config object."""
    # Access the config settings that determine canned data download source files
    config = configparser.ConfigParser()
    configfile = f"{ROOT_DIR}/cmatools/canned_data/config.ini"
    config.read(configfile)
    return config


def download_subset_canned_data(dataset: str) -> str:
    """Save cube to netcdf, from source url after extracting time range.

    Paramaters
    ----------
    dataset
        Name of source dataset to access and subset, as defined by config.ini file in
    src/cmatools/canned_data/config.ini
    The time constraints used are set within the config.ini file.

    Returns
    -------
    str
        Output filepath to the saved netcdf
    """
    config = return_config()
    url = config.get(dataset, "URL")
    start_year = config.get(dataset, "START")
    end_year = config.get(dataset, "END")
    filename = config.get(dataset, "NAME")
    # Set output filepath
    outfilepath = CANNED_DATA / filename
    # Create cube from remote url
    cube = return_cube_from_url(url)
    if DEBUG:
        print(f"Cube from url: {cube}")
        print(f"Output path: {outfilepath}")
        print(f"Cube has lazy data?: {cube.has_lazy_data()}")
    # Return a new cube, constrained to a reduced time range
    extracted_cube = extract_timesteps(cube, int(start_year), int(end_year))
    if DEBUG:
        print(f"Extracted cube: {extracted_cube}")
        print(f"Extracted cube has lazy data?: {extracted_cube.has_lazy_data()}")
    # Save cube to disk
    iris.save(extracted_cube, outfilepath)
    # Return filepath to the saved netcdf on disk
    return outfilepath
    # -----------------------------     TESTING     -----------------------------
    # unit: a_unit/canned_data/test_canned_data.py
    # integration: b_integration/canned_data/test_canned_data.py
    # ---------------------------------------------------------------------------
