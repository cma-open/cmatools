"""Tests for canned_data module."""

from pathlib import Path
from unittest.mock import patch

from cmatools.canned_data.canned_data import download_subset_canned_data

DEBUG = True


def test_download_subset_canned_data(tmp_path):
    """Test for download_subset_canned_data function."""
    dataset = "HADCRUT"
    with patch("cmatools.canned_data.canned_data.CANNED_DATA", tmp_path):
        file = download_subset_canned_data(dataset)
        assert Path(file).is_file()
        if DEBUG:
            print(f"File saved to: {file}")
