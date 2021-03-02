""" Test the cli_simple tool outputs
"""

# All combinations to be tested
#

import argparse
from pathlib import Path

from cmatools.cli_hello_world import cli_parse_args, cli_parser, cli_hello

from cmatools.definitions import ROOT_DIR, PACKAGE

# Define cli filepath
CLI = Path(ROOT_DIR, PACKAGE, "cli_hello_world.py")


def test_cli_parser():

    """Test for cli_parser() function."""

    out = cli_parser()
    # Confirm output object is correct parser type
    assert isinstance(out, argparse.ArgumentParser)
    # Confirm cli tool name is correct
    assert out.prog == "CLI-HELLO"


def test_cli_parse_args():

    """Test for cli_parse_args() function"""

    user_args = ["John"]

    parsed_args = cli_parse_args(user_args)

    print(parsed_args)
    print(type(parsed_args))

    assert isinstance(parsed_args, argparse.Namespace)

    assert parsed_args.user == "John"


def test_cli_hello():
    """Test for cli_hello() function """
    parsed_args = argparse.Namespace(user="John")
    output = cli_hello(parsed_args)
    assert output == "Hello: John"
