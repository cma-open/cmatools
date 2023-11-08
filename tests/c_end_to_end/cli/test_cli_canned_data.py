"""End to end test for the cli canned_data analysis tool."""

# PURPOSE
# tests the end-to-end process flow of the cli tool by testing
# user input (via config file)
# the dataset urls are accessible
# the tool runs and downloads data to local CANNED_DATA dir
# downloaded files are as expected (via filesize, TODO could also hash)
#


# This module uses subprocess, which can raise security threats.
# The risk have been reviewed via Codacy, Bandit.
# The generic warning on import has been left active, in case of future edits here.
# Each specific use warning has been checked and then ignored, where safe to do so.
# bandit ignore command is # nosec, per line

import configparser
import json
import subprocess  # nosec  # bandit ignore
from pathlib import Path
from pprint import pprint

from compliance_checker.runner import CheckSuite, ComplianceChecker

from cmatools.canned_data.canned_data import return_config
from cmatools.definitions import REPO_DIR
from cmatools.io.common import file_sizes, report_file_size_from_url, validate_netcdf

# Define cli tool name
TOOL = "cli-canned"
"""str: Script command name."""

# Create list of files expected in Canned data dir
# NOTE - currently limited selected list being used because
# HADCRUT is currently failing some tests, will be fixed later,
# HADISDH also excluded as it returns a cubelist not a cube

DATASETS = ["HADCRUT", "HADSST", "CRUTEM"]
# DATASETS = ["HADSST", "CRUTEM"]  # TODO add hadcrut back when netcdfs are valid
# Get list of file urls from config, to download
config = return_config()
FILES = [config.get(dataset, "NAME") for dataset in DATASETS]

# Set the local canned data location
CANNED_DATA = Path(REPO_DIR) / "data" / "canned"

DEBUG = True

# As these tests also use input from the config file, the tests also
# validate the initial config step of the cli system process.


def test_config_is_valid():
    """Test config."""
    # config file can be read (user scripted input)
    config = return_config()
    assert isinstance(config, configparser.ConfigParser)


def test_url_access():
    """Test URL access."""
    # Get list of urls from config, to download
    config = return_config()
    urls = [config.get(dataset, "URL") for dataset in DATASETS]
    for url in urls:
        size = report_file_size_from_url(url)
        assert isinstance(size, str)


# Simple, but not generally recommend end-to-end test is simply to run the cli tool
# and then inspect the outputs. Many limitations, inc need to ensure correct
# initial state, e.g. empty directory, or existing files present.


def test_cli_run_as_entrypoint_with_args_all():
    """Test cli tool download."""
    # Remove existing files
    # list the files in canned data dir
    files = [p for p in Path(CANNED_DATA).iterdir() if p.is_file()]
    for file in files:
        # remove the canned data files
        file.unlink()
    # Confirm CANNED_DATA is empty
    assert any(Path(CANNED_DATA).iterdir()) is not True

    # Run the tool to download canned data
    out = subprocess.run([TOOL, "ALL"], check=True)  # nosec
    assert out.returncode == 0

    # list the files in canned data dir
    files = [p for p in Path(CANNED_DATA).iterdir() if p.is_file()]
    if DEBUG:
        print(f"Canned data dir: {CANNED_DATA}")
        print(f"Content: {str(files)}")

    # Check downloaded files are as expected
    # create a dict report of file size
    report = file_sizes(FILES, CANNED_DATA)
    if DEBUG:
        print("File size report")
        pprint(report)

    # assert report["HadCRUT_short.nc"] == "1.5 MB"  # TODO restate later
    assert report["HadSST_short.nc"] == "770.4 kB"
    assert report["CRUTEM_short.nc"] == "1.5 MB"


def test_validate_netcdfs():
    """Test downloaded files in canned data are valid netcdfs."""
    for file in FILES:
        filepath = CANNED_DATA / file
        assert validate_netcdf(filepath) is True


# Note - this test works ok for small numbers of files
# If testing large numbers of output files then a sample eg x% of files
# should be selected and tested
# def test_cfchecker_netcdf():
#     """Test netcdf files against CF conventions - using cf-checker."""
#     for file in FILES:
#         filepath = CANNED_DATA / file
#         #filepath = "/home/h02/jwinn/github-repos/cmatools/cmatools/data/canned/
#         HadSST_short.nc"
#         try:
#             out = subprocess.run(
#             ["cfchecker", "-v", "auto", filepath], check=True)  # nosec
#             if DEBUG:
#                 print("---")
#                 print(f"Process (cfchecker): {out}")
#                 print(f"Return code status (cfchecker): {out.returncode}")
#             # returncode is 0 if the cfchecker passes and finds no errors
#             assert out.returncode == 0
#             # TODO add option to write out reports
#              to disk for failing tests, under logs?
#             # logs/tests/end-to-end
#
#         except subprocess.CalledProcessError as e:
#             print(f"cf-checker failed for : {file}")
#             print(f"stdout output: {e.output}")
#             print("---")
#             raise


# START HERE - remove the command line tool, use the python version
# add log output per file
# note works via URLS ?

# Load all available checker classes
check_suite = CheckSuite()
check_suite.load_all_available_checkers()


def test_compliance_checker_netcdf(tmp_path):
    """Test netcdf files against CF conventions - using compliance-checker."""
    for file in FILES:
        # test = "cf:1.7"  # convention version to test against
        # option = "cf:enable_appendix_a_checks"

        path = str(CANNED_DATA / file)  # tool does not work with pathlib
        checker_names = ["cf:1.7"]  # state one version to test against
        verbose = 2  # 0, 1, 2
        # criteria = 'normal'  # strict, lenient
        criteria = "lenient"  # strict, lenient
        output_filename = str(tmp_path / "report.json")
        output_format = "json"
        # run the compliance checker on the file
        return_value, errors = ComplianceChecker.run_checker(
            path,
            checker_names,
            verbose,
            criteria,
            output_filename=output_filename,
            output_format=output_format,
        )

        message = (
            f"{file} is compliant: {return_value}  "
            f"(test errors: {errors}, criteria={criteria}, {checker_names[0]})"
        )
        print(message)

        # HOW - to add CF version, eg 1.7 ? and apendixc checks ?

        # Open the JSON output and get the compliance scores
        with open(output_filename, "r") as fp:
            cc_data = json.load(fp)
            # get the single element from the list of checker_names and use a key
            scored = cc_data[checker_names[0]]["scored_points"]
            possible = cc_data[checker_names[0]]["possible_points"]
            print(f"{file} scored: {scored} / {possible}")
            # TODO enable logging to file
            # log.debug('CC Scored {}
            # out of {} possible points'.format(scored, possible))

        # test that file is compliant
        assert return_value is True, message


# CODE REVIEW NOTE / REFACTOR
# This end-to-end tests is currently similar to the existing integration tests
# This is because the example cli tool is simplistic
# For more advanced systems there will a greater distinction between test types
# Therefore keeping here as a simple example
