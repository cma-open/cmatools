# Added to catch situation where tests are run before the package has been installed

import pytest

def pytest_collectreport(report):

    if report.failed:

        raise pytest.UsageError(

            "Errors during collection \n"
            "Check package has been installed correctly \n"
            "Have you run 'python setup.py install' or 'pip install .'  ? \n"
            "Aborting tests"
        )