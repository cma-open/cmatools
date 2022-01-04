"""Configuration for pytest."""

# Added to catch situations where tests are run before the package has been installed

import pytest


def pytest_report_header(config):
    """Add additional text to output reports."""
    return 'Extra info: example'


def pytest_collectreport(report):
    """Report message to user if test collection fails."""
    if report.failed:

        raise pytest.UsageError(
            '- \n'
            'Errors during collection \n'
            'Check package has been installed correctly \n'
            "Have you run 'pip install .' or 'pip install -e .' ? \n"
            'Aborting tests'
            ' \n'
        )
