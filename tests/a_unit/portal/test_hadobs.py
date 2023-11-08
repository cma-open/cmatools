"""Tests for hadobs module."""

from pathlib import Path

from cmatools.definitions import REPO_DIR
from cmatools.portal.hadobs import (  # check_hadobs_dataset_netcdfs,
    check_hadobs_file_access,
)

HADCRUT = "https://www.metoffice.gov.uk/hadobs/hadcrut5/data/current/download.html"
HADISDH = "https://www.metoffice.gov.uk/hadobs/hadisdh/downloadland4312020.html"

LOGS = Path(REPO_DIR) / "logs"
test_logs = LOGS / "compliance" / "hadcrut"

# def test_check_hadobs_dataset_netcdfs():
#   print("----")
#  check_hadobs_dataset_netcdfs(HADCRUT, test_logs=test_logs)

# TODO - all tests are created here initially
#  then moved to unit, integration, end to end etc


# def test_check_hadobs_file_access():
#     test_logs = LOGS / "portal" / "hadcrut"
#     # return a list of accessible files, of specified type, from url
#     result = check_hadobs_file_access(HADCRUT, ".nc" , test_logs)
#     # assert the result list is not empty
#     assert result is True


def test_check_hadobs_file_access_fails():
    """Test to check hadobs file access."""
    test_logs = LOGS / "portal" / "hadisdh"
    result = check_hadobs_file_access(HADISDH, filetype=".txt", test_logs=test_logs)
    assert result is True
