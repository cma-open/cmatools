"""Test the cli_simple_analysis tool outputs."""

import argparse
from pathlib import Path

from cmatools.cli_simple_analysis import cli_analysis, cli_parse_args, cli_parser
from cmatools.definitions import SRC_DIR

DEBUG = True
"""bool: Debugging module-level constant (Default: True)."""

# Define cli filepath
CLI = Path(SRC_DIR, 'cmatools', 'cli_simple_analysis.py')
"""str: Filepath to command line tool module."""


def test_cli_parser():
    """Test for cli_parser() function."""
    out = cli_parser()
    # Confirm output object is correct parser type
    assert isinstance(out, argparse.ArgumentParser)
    # Confirm cli tool name is correct
    assert out.prog == 'CLI-SIMPLE-ANALYSIS'


def test_cli_parse_args():
    """Test for cli_parse_args() function."""
    user_args = ['1', '2']
    parsed_args = cli_parse_args(user_args)
    if DEBUG:
        print(f'Parsed args: {parsed_args}')
    assert isinstance(parsed_args, argparse.Namespace)
    assert parsed_args.x == 1
    assert parsed_args.y == 2


def test_cli_analysis():
    """Test for cli_analysis() function."""
    parsed_args = argparse.Namespace(
        x=1, y=2, sum=False, max=False, combined=False, verbose=False
    )
    output = cli_analysis(parsed_args)
    # Default analysis is product: 1 * 2 = 2
    assert output == 2

    parsed_args = argparse.Namespace(
        x=1, y=2, sum=True, max=None, combined=False, verbose=False
    )
    output = cli_analysis(parsed_args)
    # Sum analysis: 1 + 2 = 3
    assert output == 3

    parsed_args = argparse.Namespace(
        x=1, y=5, sum=False, max=True, combined=False, verbose=False
    )
    output = cli_analysis(parsed_args)
    # Max analysis: 5 > 1
    assert output == 5

    parsed_args = argparse.Namespace(
        x=1, y=5, sum=False, max=False, combined=True, verbose=False
    )
    output = cli_analysis(parsed_args)
    # Combined analysis: (1*5) + (1+5) = 11
    assert output == 11
