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


#def test_cli_simple_version():
#    """ Test of cli tool version
#    """
#    out = subprocess.run(["python", str(CLI), "--version"], text=True, check=True, stdout=subprocess.PIPE)

#    print(out)
#    print(out.stdout)
#    assert out.returncode == 0
#    assert out.stdout.strip() == 'SIMPLE 0.0.1'


def test_cli_simple_help():
    """ Test of cli tool version
    """

    user_args = '--help'
    out = subprocess.run(["python3", str(CLI), user_args], text=True, check=True, stdout=subprocess.PIPE)
    assert out.returncode == 0
    #assert out.stdout.strip() == 'SIMPLE 0.0.1'


def test_cli_simple():
    """ Test of cli tool version
    """
    user_arg_x = '--x=1'
    user_arg_y = '--y=2'
    out = subprocess.run(["python3", str(CLI), user_arg_x, user_arg_y], text=True, check=True, stdout=subprocess.PIPE)
    assert out.returncode == 0

# adapted from
# https://github.com/painless-software/python-cli-test-helpers/blob/master/examples/tests/test_cli.py
def test_cli_module():
    """
    Can this cli be run via Python -m from full path
    """
    cli_call = f'python3 {CLI} --help'
    exit_status = os.system(cli_call)
    assert exit_status == 0

# adapted from
# https://github.com/painless-software/python-cli-test-helpers/blob/master/examples/tests/test_cli.py
def test_runas_module():
    """
    Can this package be run as a Python module?
    """
    #cli_call = f'python -m {CLI} --help'
    cli_call = 'python3 -m cmatools.cli_simple --help'
    exit_status = os.system(cli_call)
    assert exit_status == 0

# adapted from
# https://github.com/painless-software/python-cli-test-helpers/blob/master/examples/tests/test_cli.py
def test_entrypoint():
    """
    Is entrypoint script installed? (setup.py)
    """
    exit_status = os.system('cli-simple --help')
    assert exit_status == 0

#
