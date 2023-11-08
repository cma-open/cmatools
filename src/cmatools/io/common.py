"""Common input/output code."""

import re
import subprocess
import tempfile
from pathlib import Path
from typing import Union
from urllib.parse import urljoin

import humanize
import iris
import requests
from bs4 import BeautifulSoup
from iris.cube import Cube
from netCDF4 import Dataset
from requests.exceptions import RequestException

from cmatools.definitions import REPO_DIR

LOGS = Path(REPO_DIR) / "logs"

DEBUG = True


def return_filename_from_url(url: Union[Path, str]) -> str:
    """Return the filename as text string.

    Paramaters
    ---------
    url  Remote url to dataset file

    Returns
    -------
    str  The filename of the url
    """
    try:
        with requests.get(url) as r:
            if "Content-Disposition" in r.headers.keys():
                fname = re.findall("filename=(.+)", r.headers["Content-Disposition"])[0]
            else:
                fname = url.split("/")[-1]
            if DEBUG:
                print(f"Filename: {fname}, type: {type(fname)}")
                print(f"Content-Type: {r.headers['Content-Type']}")
                print(f"Full headers: {r.headers}")
                print("---")
            return fname
    except RequestException as e:
        print(e)
    # -----------------------------     TESTING     -----------------------------
    # unit: a_unit/io/test_common.py
    # ---------------------------------------------------------------------------


def return_cube_from_url(url: Union[Path, str]) -> Cube:
    """Return an iris cube from a url.

    Paramaters
    ---------
    url  Remote url to dataset file

    Returns
    -------
    Cube  An iris.cube.Cube
    """
    resp = requests.get(url, allow_redirects=True)
    # Open file and write the contents
    with tempfile.NamedTemporaryFile(suffix=".nc") as tmp:
        tmp.write(resp.content)
        cube = iris.load_cube(tmp.name)
        # Prevent FileNotFoundError due to data missing in tempfile
        cube.data  # Realise lazy data
    return cube
    # -----------------------------     TESTING     -----------------------------
    # unit: a_unit/io/test_common.py
    # ---------------------------------------------------------------------------


def report_file_size_from_url(url: Union[Path, str]) -> str:
    """Report file size from file url.

    Paramaters
    ---------
    url  Remote url to dataset file

    Returns
    -------
    str  String of filesize, human readable summary format
    """
    # Access request response without downloading body content
    with requests.get(url, stream=True) as response:
        filesize = humanize.naturalsize(response.headers["Content-Length"])
    return filesize
    # -----------------------------     TESTING     -----------------------------
    # unit: a_unit/io/test_common.py
    # ---------------------------------------------------------------------------


def file_sizes(files: list, directory: Path) -> dict:
    """Files sizes."""
    file_report = {}
    for file in files:
        filepath = Path(directory) / file
        file_size = filepath.stat().st_size
        human_file_size = humanize.naturalsize(file_size)
        # Add file and file size to report dictionary
        file_report[file] = human_file_size

    return file_report


# TODO add note re local files vs urls
def validate_netcdf(filepath: Union[Path, str]) -> bool:
    """Validate netcdfs."""
    try:
        with Dataset(filepath, "r", format="NETCDF4"):
            return True
    except OSError as err:
        print(f"File type error {err=}, {type(err)=}")
        raise
    # TODO Catch further errors as discovered
    except BaseException as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise


# Note - this tools works with both URLS and local files
def compliance_checker(filepath, criteria, logs):
    """Check netcdf files against CF conventions - using compliance-checker."""
    test = "cf:1.7"  # convention version to test against
    # criteria = "normal"  # options are from lenient, normal, strict
    # criteria = "lenient"  # options are from lenient, normal, strict
    option = "cf:enable_appendix_a_checks"
    # filepath = CANNED_DATA / file
    # filepath = "/home/h02/jwinn/github-repos/cmatools/cmatools/data/canned/
    # HadSST_short.nc"
    file = return_filename_from_url(filepath)
    output = logs / file

    try:
        out = subprocess.run(
            [
                "compliance-checker",
                "-v",
                "-v",
                "-v",
                f"--criteria={criteria}",
                f"--test={test}",
                f"--option={option}",
                f"--output={output}",
                filepath,
            ],
            check=True,
        )  # nosec
        if DEBUG:
            print("---")
            print(f"Process: {out}")
            print(f"Return code status: {out.returncode}")
        return out
        # TODO add option to write out reports to disk for failing tests, under logs?
        # logs/tests/end-to-end

    except subprocess.CalledProcessError as e:
        print("--")
        print(e)
        print(f"Test for file: {filepath}")
        print(f"Test failed, returncode: {e.returncode}")
        print(f"stdout output: {e.output}")
        raise e
        # return e


# Note - this test works ok for small numbers of files
# If testing large numbers of output files then a sample eg x% of files
# should be selected and tested
# Note - does not work with remote URLS, only local files.
def cfchecker_netcdf(filepath, logs):
    """Check netcdf files against CF conventions - using cf-checker."""
    # filepath = "/home/h02/jwinn/github-repos/cmatools/cmatools/data/canned/
    # HadSST_short.nc"
    out = subprocess.run(["cfchecks", "-v", "auto", filepath], check=True)  # nosec
    if DEBUG:
        print("---")
        print(f"Process: {out}")
        print(f"Return code status: {out.returncode}")
    return out

    # TODO add option to write out reports to disk for failing tests, under logs?
    # logs/tests/end-to-end


# def search_dataset(href):
#    return href and filetype in href


def list_files_from_html(url, filetype):
    """Return list of files of type, from remote html page."""
    # Parse the download page url via BeautifulSoup
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    # function to find a subset of the html href links
    # TODO check, replace with lambda?
    def search_dataset(href):
        return href and filetype in href

    # Find all links with the dataset filetype
    # links var is in html format, e.g. with a href= and labels
    links = soup.find_all(href=search_dataset)

    # Get the url for each link from the page, append to list
    href_links = []  # empty list to hold the links
    for link in links:
        href_link = link.get("href")
        # This href_link is the html link,
        # relative to the download page, not a full url
        # Append this link to the list
        href_links.append(href_link)

    # Add back the base url to the relative links
    # Empty list to hold full url paths
    full_filetype_urls = []

    for filetype_url in href_links:
        #
        full_url = urljoin(url, filetype_url)
        if DEBUG:
            print(f"url to file: {full_url}")
        full_filetype_urls.append(full_url)

    if DEBUG:
        print("---")
        print(f"Source url: {url}")
        print(f"Total dataset links of filetype {filetype}: {len(links)}")
        print("---")

    # Return the full url paths to each url of requested filetype, as a list
    return full_filetype_urls


def check_url(url):
    """Check URL."""
    response = requests.head(url)
    if response.status_code == 200:
        return True
    else:
        return False
