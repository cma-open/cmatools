"""Example use of global data points."""

import random
from pathlib import Path

# import cartopy.crs as ccrs
# import cartopy.io
# import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from cmatools.data_creation.simple import generate_random_lat_lon
from cmatools.definitions import ROOT_DIR

# Main examples - direct use of data, not via iris cubes
# 1. Plot one point on a global map
# 2. Plot several point on a map - from a python object / var
# 3. Plot several points on a map from a fixed input file (text file, static)
# 4. Plot several points on a map from a dynamic data download (see below)

# dynamic data download, e.g. ghncd station file, download then select
# random sample, and plot those, e.g. 20% of stations)
# Example 4 above allows end to end testing

# TODO
# explore geopands
# https://geopandas.org/en/stable/gallery/cartopy_convert.html

# -------------------------------------------------------------------------------------


def example_csv_data():
    """Csv data."""
    name = "ghcnd-stations-top.txt"
    path = Path(ROOT_DIR) / "cmatools" / "_data" / name
    # Read in data from csv, set column names (ID, lat, lon)
    stations = pd.read_csv(
        path,
        delim_whitespace=True,
        header=None,
        usecols=[0, 1, 2],
        names=["ID", "lat", "lon"],
    )
    return stations


def random_lat_lon(n=1, lat_min=-90.0, lat_max=90.0, lon_min=-180.0, lon_max=180.0):
    """Produce an array with of pairs lat, lon."""
    lat = np.random.uniform(lat_min, lat_max, n)
    lon = np.random.uniform(lon_min, lon_max, n)

    return np.array(tuple(zip(lat, lon)))


# TODO note this is limited by possible unique sample size of lat lon
# What is really needed is unique lat/lon combinations, not indiv lat lon
# TODO - generate another version of land vs sea options


def generate_synthetic_stations(sample, save=False):
    """Generate synthetic stations."""
    name = "synthetic-stations.txt"

    # TODO modify to use  data dir as set by config
    path = Path(ROOT_DIR) / "cmatools" / "_data" / name
    # Take a specified sample size from a population
    # Create the station IDs (1st object)
    station_values = random.sample(range(0, sample + 1), sample)
    # Add ID text to station values
    station_values = [f"ID{i}" for i in station_values]
    # Create the station latitudes, longitudes (2nd object, 3rd object)
    latitude_values, longitude_values = generate_random_lat_lon(sample)
    # Zip the three objects
    data_zipped = zip(station_values, latitude_values, longitude_values)
    # Pass the zipped object as the data parameter
    # Pass the column names
    df = pd.DataFrame(data_zipped, columns=["IDs", "latitudes", "longitudes"])

    if save is True:
        # Saving to CSV file with tab delimiter, no index column
        df.to_csv(path, sep="\t", index=False)
    return df


# TODO - use pandas schema to check datasets
# ADD tests to make sure that lat lon are used correctly in maps lat/lon vs lon/lat


# Sources
# -------
# https://stackoverflow.com/questions/25340427/how-to-add-a-point-feature-shapefile-to-map-using-cartopy
