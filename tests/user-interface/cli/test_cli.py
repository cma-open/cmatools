""" Test the cli tool
"""

# All combinations to be tested


import subprocess
from pathlib import Path


from cmatools.cli_hello_world import cli_entry_point
from cmatools.definitions import ROOT_DIR

# Define cli filepath
CLI = Path(ROOT_DIR, "cmatools", "cli_hello_world.py")


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
    user_arg_user = "John"
    out = subprocess.run(["python3", str(CLI), user_arg_user], check=True)
    assert out.returncode == 0


def test_cli_run_as_module():
    """
    Can package be run as a Python module?

    uses call to --help option to test cli tool is working
    """

    out = subprocess.run(
        ["python3", "-m", "cmatools.cli_hello_world", "--help"], check=True
    )
    assert out.returncode == 0


def test_cli_run_as_entrypoint():
    """
    Can the entrypoint script be called? is it installed? (via setup.py)
    """

    # note - the name is set in the entry_points section of setup.py
    out = subprocess.run(["cli-hello", "--help"], check=True)
    assert out.returncode == 0


#
