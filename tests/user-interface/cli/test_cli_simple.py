""" Test the cli_simple tool outputs
"""

# All combinations to be tested
#
import os
import pytest
import io
import subprocess
from pathlib import Path
from contextlib import redirect_stdout

from cmatools.cli import cli_entry_point
from cmatools.definitions import ROOT_DIR

# Define cli filepath
CLI = Path(ROOT_DIR, 'cmatools','cli_simple.py')



def test_cli_simple_help_from_path():
    """
    Can cli be run via Python from full path

    uses call to --help option to test cli tool is working
    """

    user_args = '--help'
    out = subprocess.run(["python3", str(CLI), user_args], check=True)

    assert out.returncode == 0


def test_cli_simple_args_from_path():
    """
    Test of cli tool with args from full path

    uses call with arguments set to test analysis outputs
    """
    user_arg_x = '--x=1'
    user_arg_y = '--y=2'
    out = subprocess.run(["python3", str(CLI), user_arg_x, user_arg_y], check=True)
    assert out.returncode == 0


def test_cli_simple_run_as_module():
    """
    Can package be run as a Python module?

    uses call to --help option to test cli tool is working
    """

    out = subprocess.run(["python3", '-m', 'cmatools.cli_simple', '--help'], check=True)
    assert out.returncode == 0


def test_cli_simple_run_as_entrypoint():
    """
    Can the entrypoint script be called? is it installed? (via setup.py)
    """

    # note - the name is set in the entry_points section of setup.py
    out = subprocess.run(['cli-simple', '--help'], check=True)
    assert out.returncode == 0


#
