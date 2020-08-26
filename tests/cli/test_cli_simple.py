""" Test the cli_simple tool outputs
"""

# All combinations to be tested
#

import pytest
import io
import subprocess
from pathlib import Path
from contextlib import redirect_stdout

from cmatools.cli import cli_entry_point
from cmatools.definitions import ROOT_DIR

# Define cli filepath
CLI = Path(ROOT_DIR, 'cmatools','cli_simple.py')



def test_cli_simple_version():
    """ Test of cli tool version
    """
    out = subprocess.run(["python", str(CLI), "--version"], text=True, check=True, stdout=subprocess.PIPE)

    print(out)
    print(out.stdout)
    assert out.returncode == 0
    assert out.stdout.strip() == 'SIMPLE 0.0.1'


def test_cli_simple_all():
    """ Test of cli tool version
    """
    out = subprocess.run(["python", str(CLI), "--all"], text=True, check=True, stdout=subprocess.PIPE)

    print(out)
    print(out.stdout)
    assert out.returncode == 0
    assert out.stdout.strip() == 'SIMPLE 0.0.1'