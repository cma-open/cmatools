""" Test the cli_simple tool outputs
"""

# All combinations to be tested
#

import pytest
import io
import subprocess
import argparse
from pathlib import Path
from contextlib import redirect_stdout

from cmatools.cli_simple import cli_parse_args, cli_parser, cli_analysis

from cmatools.definitions import ROOT_DIR

# Define cli filepath
CLI = Path(ROOT_DIR, 'cmatools','cli_simple.py')


def test_cli_parser():

    """Test for cli_parser() function."""

    out = cli_parser()
    # Confirm output object is correct parser type
    assert  isinstance(out, argparse.ArgumentParser)
    # Confirm cli tool name is correct
    assert out.prog == 'SIMPLE'


def test_cli_parse_args():

    """Test for cli_parse_args() function"""

    user_args = ['--x', '1', '--y', '2']

    parsed_args = cli_parse_args(user_args)

    print(parsed_args)
    print(type(parsed_args))

    assert isinstance(parsed_args, argparse.Namespace)

    assert parsed_args.x == 1
    assert parsed_args.y == 2

def test_cli_analysis():
    """Test for cli_analysis() function """
    parsed_args = argparse.Namespace(x=1, y=2)
    output = cli_analysis(parsed_args)
    assert output == 2

