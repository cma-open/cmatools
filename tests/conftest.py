# Added to catch situation where tests are run before the package has been installed

import pytest

def pytest_report_header(config):
    return "Extra info: example"

def pytest_collectreport(report):

    if report.failed:

        raise pytest.UsageError(
            "- \n"
            "Errors during collection \n"
            "Check package has been installed correctly \n"
            "Have you run 'pip install .' or 'pip install -e .' ? \n"
            "Aborting tests"
            " \n"
        )
