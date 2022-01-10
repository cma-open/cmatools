"""Test the simple analysis cli tool."""

# This module uses subprocess, which can raise security threats.
# The risk have been reviewed via Codacy, Bandit.
# The generic warning on import has been left active, in case of future edits here.
# Each specific use warning has been checked and then ignored, where safe to do so.
# bandit ignore command is # nosec, per line

import subprocess  # nosec  # bandit ignore
from pathlib import Path

from cmatools.definitions import PACKAGE, SRC_DIR

# Define cli filepath
CLI = Path(SRC_DIR, PACKAGE, "cli_simple_analysis.py")
"""str: Filepath to command line tool module."""
MODULE = "cmatools.cli_simple_analysis"
"""str: Module name."""
TOOL = "cli-simple-analysis"
"""str: Script command name."""


def test_cli_help_from_path():
    """Test cli run via Python at command prompt.

    Uses a call to --help option to test the cli tool is working
    """
    user_args = "--help"
    out = subprocess.run(["python3", str(CLI), user_args], check=True)  # nosec
    assert out.returncode == 0


def test_cli_args_from_path():
    """Test cli tool run with args from full path.

    Uses a call with arguments set to test analysis outputs
    """
    user_arg_x = "2"
    user_arg_y = "4"
    out = subprocess.run(  # nosec
        ["python3", str(CLI), user_arg_x, user_arg_y], check=True
    )  # nosec
    assert out.returncode == 0


def test_cli_run_as_module():
    """Test the package can run as a Python module.

    Uses a call to the module directly, with the --help option to test cli tool
    """
    out = subprocess.run(["python3", "-m", MODULE, "--help"], check=True)  # nosec
    assert out.returncode == 0


def test_cli_run_as_entrypoint():
    """Test the entrypoint script can be called.

    Allows verification that CLI tool is correctly installed? (via setup.py)
    """
    # Note - the script tool name is set in the entry_points section of setup.py
    # TODO add a documentation cross ref here
    out = subprocess.run([TOOL, "--help"], check=True)  # nosec
    assert out.returncode == 0
