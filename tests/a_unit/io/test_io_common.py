"""Tests for io_common module."""

import os
from unittest.mock import patch

import pytest

from cmatools.definitions import ROOT_DIR
from cmatools.io.io_common import check_access, return_datadir_root_dir

# extract_archive_singlefile,; return_datadir_inputs_dir,; write_source_config,
# from pathlib import Path


DEBUG = True

# TODO refactor
# def test_extract_archive_singlefile():
#
#     filename = "eobs.tgz"
#     extractedfile = extract_archive_singlefile(filename)
#     file = Path(return_datadir_inputs_dir() / extractedfile)
#     print("Test ouput")
#     print(extractedfile)
#     print(file)
#
#     assert file.is_file()
#
#
# def test_write_source_config():
#
#     archivename = 'arcfile'
#     extractfilename = 'extfile'
#
#     write_source_config(archivename,extractfilename)


def test_return_datadir_root_dir_repo_input():
    """Test datadir root value with arg: input."""
    assert return_datadir_root_dir('repo') == ROOT_DIR


def test_return_datadir_root_dir_temp_input(tmp_path):
    """Test datadir root value with arg: custom path."""
    root_dir = tmp_path / 'fake_sub_dir'
    root_dir.mkdir()
    assert return_datadir_root_dir(root_dir) == root_dir


# Can't know value of home ~ , so use mock
# Mocked home dir will not be accessible, so also need to mock check_access()
@patch('cmatools.io.io_common.check_access')
def test_return_datadir_root_dir_home_input(function_mock, monkeypatch):
    """Test datadir root value with arg: home ~."""
    monkeypatch.setattr(os.path, 'expanduser', lambda home: '/home/name/datadir')
    function_mock.return_value = True
    assert return_datadir_root_dir('~') == '/home/name/datadir'


def test_return_datadir_root_dir_bad_inputs():
    """Test exception raised."""
    with pytest.raises(Exception):
        return_datadir_root_dir('epor')


def test_check_access_raises_exception():
    """Test exception raised."""
    root_dir = '/home/name/not_a_subdir'
    with pytest.raises(FileNotFoundError):
        check_access(root_dir)


def test_check_access():
    """Test check access function."""
    # Root repo dir should be accessible
    assert check_access(ROOT_DIR)
    # User home root dir should be accessible
    root_dir = os.path.expanduser('~')
    assert check_access(root_dir)
