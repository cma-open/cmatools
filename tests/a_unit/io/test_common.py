"""Tests for cmatools.io.common module."""

import subprocess
from pathlib import Path

import pytest
from iris.cube import Cube

from cmatools.definitions import REPO_DIR, SRC_DIR
from cmatools.io.common import (
    cfchecker_netcdf,
    check_url,
    compliance_checker,
    list_files_from_html,
    report_file_size_from_url,
    return_cube_from_url,
    return_filename_from_url,
    validate_netcdf,
)

LOGS = Path(REPO_DIR) / "logs"

# Set test resources
hadcrut_url = (
    "https://www.metoffice.gov.uk/hadobs/hadcrut5/data/current/analysis"
    "/HadCRUT.5.0.1.0.analysis.anomalies.ensemble_mean.nc"
)
hadisdh_url = (
    "https://www.metoffice.gov.uk/hadobs/hadisdh/data/"
    "HadISDH.landq.4.3.1.2020f_FLATgridHOM5by5_anoms8110.nc"
)
hadsst_url = (
    "https://www.metoffice.gov.uk/hadobs/hadsst4/data/netcdf"
    "/HadSST.4.0.1.0_median.nc"
)

# Set canned data directory
CANNED_DATA = Path(REPO_DIR) / "data" / "canned"
DATA = Path(SRC_DIR) / "cmatools" / "_data"
# Test datasets
DATASET = "HadCRUT_short.nc"
INVALID_NAME = "ghcnd-stations-top.txt"
# Need to access local test resources
FILE = CANNED_DATA / DATASET
INVALID_FILE = DATA / INVALID_NAME


def test_return_filename_from_url():
    """Test for return_filename_from_url function."""
    # Test via HadCRUT
    output = return_filename_from_url(hadcrut_url)
    expected = "HadCRUT.5.0.1.0.analysis.anomalies.ensemble_mean.nc"
    assert output == expected
    # Test via HadISDH
    output = return_filename_from_url(hadisdh_url)
    expected = "HadISDH.landq.4.3.1.2020f_FLATgridHOM5by5_anoms8110.nc"
    assert output == expected


def test_return_cube_from_url():
    """Test for return_cube_from_url function."""
    cube = return_cube_from_url(hadcrut_url)
    assert isinstance(cube, Cube)  # Test via HadCRUT
    cube = return_cube_from_url(hadcrut_url)
    assert isinstance(cube, Cube)  # Test via HadISDH


def test_report_filesize_from_url():
    """Test for report_filesize_from_url function."""
    filesize = report_file_size_from_url(hadcrut_url)
    assert filesize == "31.8 MB"
    filesize = report_file_size_from_url(hadisdh_url)
    assert filesize == "60.0 MB"


def test_validate_netcdf():
    """Test for validate_netcdf function."""
    result = validate_netcdf(FILE)
    assert result is True


def test_validate_netcdf_raises():
    """Test for validate_netcdf function."""
    with pytest.raises(OSError):
        validate_netcdf(INVALID_FILE)


def test_compliance_checker_pass():
    """Test netcdf via compliance-checker."""
    # Test the checker runs and passes with no failures to report
    # TODO need to find and use a netcdf that passes
    test_logs = LOGS / "compliance"
    test_logs.mkdir(parents=True, exist_ok=True)
    out = compliance_checker(hadsst_url, criteria="lenient", logs=test_logs)
    assert out.returncode == 0


def test_compliance_checker_raises():
    """Test netcdf via compliance-checker."""
    test_logs = LOGS / "compliance"
    test_logs.mkdir(parents=True, exist_ok=True)
    with pytest.raises(subprocess.CalledProcessError):
        out = compliance_checker(hadsst_url, criteria="strict", logs=test_logs)
        print(f"Report logs written to: {test_logs}")
        print(out)


def test_cfchecker_pass():
    """Test files pass netcdf checks via cf-checker."""
    test_logs = LOGS / "cfchecker"
    test_logs.mkdir(parents=True, exist_ok=True)
    out = cfchecker_netcdf(CANNED_DATA / "CRUTEM_short.nc", logs=test_logs)
    assert out.returncode == 0


def test_cfchecker_fails():
    """Test files pass netcdf checks via cf-checker."""
    test_logs = LOGS / "cfchecker"
    test_logs.mkdir(parents=True, exist_ok=True)
    with pytest.raises(subprocess.CalledProcessError):
        out = cfchecker_netcdf(CANNED_DATA / "HadCRUT_short.nc", logs=test_logs)
        print(f"Report logs written to: {test_logs}")
        print(out)


def test_list_files_from_html():
    """Test list_files_from_html function."""
    url = "https://www.metoffice.gov.uk/hadobs/hadcrut5/data/current/download.html"
    files = list_files_from_html(url, ".nc")
    assert isinstance(files, list)
    for file in files:
        assert check_url(file)


def test_check_url():
    """Test check url."""
    # TODO add, check best location for this test
    url = "https://www.metoffice.gov.uk/hadobs/hadcrut5/data/current/download.html"
    outcome = check_url(url)
    print(outcome)
    url = (
        "https://www.metoffice.gov.uk"
        "/hadobs/hadcrut5/data/current/non-infilled/diagnostics"
        "/HadCRUT.5.0.1.0.ensemble_series.southern_hemisphere.annual.nc"
    )
    outcome = check_url(url)
    print(outcome)
