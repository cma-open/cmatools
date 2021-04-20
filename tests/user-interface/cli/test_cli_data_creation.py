""" Test the cli data tool
"""


import subprocess
from pathlib import Path


from cmatools.definitions import ROOT_DIR, PACKAGE

# Define cli filepath
CLI = Path(ROOT_DIR, PACKAGE, "cli_data_creation.py")


def test_cli_help_from_path():
    """
    Can cli be run via Python from full path

    uses call to --help option to test cli tool is working
    """

    user_args = "--help"
    out = subprocess.run(["python3", str(CLI), user_args], check=True)

    assert out.returncode == 0


def test_cli_args_from_path():
    """
    Test of cli tool with args from full path

    uses call with arguments set to test analysis outputs
    """
    user_arg = "netcdf"
    out = subprocess.run(["python3", str(CLI), user_arg], check=True)
    assert out.returncode == 0


def test_cli_run_as_module():
    """
    Can package be run as a Python module?

    uses call to --help option to test cli tool is working
    """

    out = subprocess.run(
        ["python3", "-m", "cmatools.cli_data_creation", "--help"], check=True
    )
    assert out.returncode == 0


def test_cli_run_as_entrypoint():
    """
    Can the entrypoint script be called? is it installed? (via setup.py)
    """

    # note - the name is set in the entry_points section of setup.py
    out = subprocess.run(["cli-data", "--help"], check=True)
    assert out.returncode == 0