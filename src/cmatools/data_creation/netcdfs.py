"""Netcdf creation."""

# add example use of netcdfs

# 1 file = 1 cube
# 1 file = cubelist, but can be all loaded
# 1 files = multiple data, cant be loaded as cube, but can be loaded via
# iris.load(path, constraint or name)

# pros and cons of netcdf access and storage

from pathlib import Path

import numpy as np
from netCDF4 import Dataset


def create_corrupt_netcdf():
    """Create corrupt netcdf."""
    # `truncate -s -5 <filename>
    pass


def create_non_cf_compliant_netcdf():
    """Amend a netcdf to remove metadata to return a non-compliant netcdf."""
    pass


def create_cf_compliant_netcdf(destination):
    """Create simple netcdf file that is CF compliant."""
    # reminder
    # netcdfs hold dimensions, variables and attributes
    # source https://unidata.github.io/python-training/workshop/Bonus/netcdf-writing/
    # Build NetCDF manually
    file = "example_netcdf.nc"
    filepath = Path(destination) / file
    # create a new netcdf file
    ncfile = Dataset(filepath, "w")
    # add file attributes
    ncfile.title = "Dataset title"
    ncfile.title = "Dataset subtitle"
    ncfile.description = "Example description of the dataset"
    ncfile.setncattr("Conventions", "CF-1.7")
    ncfile.settncattr("Cell methods", "cell methods calculation")

    # comment="2m air temperature over land blended with sea water temperature
    # at a depth of 20cm expressed as monthly "
    #       "anomalies relative to 1961-1990 climatology.",
    # TODO - refactor
    # history = "Data set built at: add time"  # TODO
    # institution = "Institute name(s)"
    # reference = "citations reference"
    # source = "source datasets"
    # version = "version"
    # licence = "licence"
    # compliance = "UID for compliance report file"

    # add cell methods?
    # coord_system, circular, var_name

    # create the time dimension (dimensions have a name and length)
    # setting length to 0 or none make it unlimited, it can grow, be appended to
    ncfile.createDimension("time", None)
    # create lat and lon dimensions
    lat_dim = ncfile.createDimension("lat", 90)  # latitude axis
    lon_dim = ncfile.createDimension("lon", 180)  # longitude axis

    # add variables (name, type, shape, and data values)
    # shape of variable is specified by tuple of dimension names.
    # variables have named attributes, e.g. units

    # Define "coordinate variables" with the same names as dimensions,
    lat = ncfile.createVariable("lat", np.float32, ("lat",))
    lat.units = "degrees_north"
    lat.long_name = "latitude"
    lon = ncfile.createVariable("lon", np.float32, ("lon",))
    lon.units = "degrees_east"
    lon.long_name = "longitude"

    # Define time variable
    time = ncfile.createVariable("time", np.float64, ("time",))
    time.units = "hours since 1850-01-01"
    time.long_name = "time"

    # Define a 3D variable to hold the data
    temp = ncfile.createVariable(
        "temp", np.float64, ("time", "lat", "lon")
    )  # unlimited dimension is leftmost
    temp.units = "K"  # degrees Kelvin
    temp.standard_name = "air_temperature"  # this is a CF standard name
    temp.setncattr("long_name", "a longer name text")

    # Add dummy temp data
    nlats = len(lat_dim)
    nlons = len(lon_dim)
    ntimes = 3
    # Write latitudes, longitudes.
    lat[:] = -90.0 + (180.0 / nlats) * np.arange(nlats)  # south pole to north pole
    lon[:] = (180.0 / nlats) * np.arange(nlons)  # Greenwich meridian eastward
    # create a 3D array of random numbers
    data_arr = np.random.uniform(low=290, high=320, size=(ntimes, nlats, nlons))
    # Write the data.  This writes the whole 3D netCDF variable all at once.
    temp[:, :, :] = data_arr  # Appends data along unlimited dimension

    ncfile.close()
    return filepath
