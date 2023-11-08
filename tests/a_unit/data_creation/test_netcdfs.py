"""Tests for netcdf data creation."""
# various use of tests files

# print ncdump -h
# etc

import subprocess

from cmatools.data_creation.netcdfs import (
    create_cf_compliant_netcdf,
    create_corrupt_netcdf,
)

DEBUG = True


def test_create_corrupt_netcdf():
    """Test create corrupt netcdf."""
    netcdf = create_corrupt_netcdf()
    print(netcdf)


def test_create_cf_compliant_netcdf(tmp_path):
    """Test create cf compliant netcdf."""
    netcdf = create_cf_compliant_netcdf(tmp_path)

    print(netcdf)
    if DEBUG:
        # show netcdf contents
        nccheck = subprocess.run(
            ["ncdump", "-h", netcdf], capture_output=True, text=True
        )
        print(nccheck.stdout)
        print()
