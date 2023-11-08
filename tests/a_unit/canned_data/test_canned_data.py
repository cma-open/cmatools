"""Tests for canned_data module."""

import configparser
from pathlib import Path
from unittest.mock import patch

from cmatools.canned_data.canned_data import download_subset_canned_data, return_config

# from cmatools.data_creation.canned_cubes import extract_timesteps, file_sizes
from cmatools.data_creation.example_cubes import create_simple_cube
from cmatools.definitions import REPO_DIR

# Access the config settings that determine canned data downloads
# config = configparser.ConfigParser()
# configfile = f"{ROOT_DIR}/cmatools/canned_data/config.ini"
# config.read(configfile)

# Create list of files expected in Canned data dir
# DATASETS = ["HADCRUT", "HADISST", "HADSST", "HADISDH"]
DATASETS = ["HADCRUT", "HADSST", "HADISDH", "CRUTEM"]
# Get list of file urls from config, to download
# FILES = [config.get(dataset, "NAME") for dataset in DATASETS]
# Set canned data directory
CANNED_DATA = Path(REPO_DIR) / "data" / "canned"

DEBUG = True


def test_setup():
    """Print current test files."""
    # print(FILES)
    # TODO refactor
    print()


def test_return_config():
    """Test for the return_config function."""
    config = return_config()
    assert isinstance(config, configparser.ConfigParser())


# Patch out functions at the location used, not where defined
@patch("cmatools.canned_data.canned_data.extract_timesteps")  # Note the source!
@patch("cmatools.canned_data.canned_data.return_cube_from_url")  # Note the source!
def test_download_subset_canned_data(
    mock_return_cube, mock_extract_timesteps, tmp_path
):
    """Test for the download subset canned data function."""
    # the unit test tests that a netcdf is saved to disk at the stated filepath
    # mock out the two other functions called by this function
    mock_return_cube.return_value = create_simple_cube()
    mock_extract_timesteps.return_value = create_simple_cube()
    # Set dataset name
    dataset = "HADCRUT"
    with patch("cmatools.canned_data.canned_data.CANNED_DATA", tmp_path):
        file = download_subset_canned_data(dataset)
        assert Path(file).is_file()
        if DEBUG:
            print(f"File saved to: {file}")

    # This will cause the actual downloads
    # for data in DATASETS:
    #   print(f"Downloading: {data}")
    #  file = download_subset_canned_data(data)
    # assert Path(file).is_file()


# def test_download_all_canned_data():
#    download_all_canned_data("ALL")

# def test_content_canned_data():
#     for file in FILES:
#         cube = iris.load_cube(str(CANNED_DATA / file))
#         print(cube.summary(shorten=True))
#
# def test_canned_data_file_sizes():
#     report = file_sizes(FILES, CANNED_DATA)
#     pprint(report)
#     assert report["HadCRUT_short.nc"] == "1.5 MB"
