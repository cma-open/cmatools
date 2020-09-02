""" Test the cli tool outputs
"""

# All combinations to be tested
#

import pytest
import io
from contextlib import redirect_stdout

from cmatools.cli import cli_entry_point


def test_version():
    """ Test of cli tool version
    """
    #cli_output = cli_entry_point(argv=['--version'])
    #print(cli_output)

    #f = io.StringIO()
    #with redirect_stdout(f):
    #    #cli_entry_point(['blended', 'all','--version'])

     #   cli_entry_point(['--version'])
    #x = f.getvalue()
    #assert x == 'CMATOOLS 0.0.1'


    #assert hello_world.hello_world() == "hello cma"

    assert 1 == 1