"""Simple x,y, point and list data creation."""

import random

import numpy as np

DEBUG = True


def example_data_single_lat_lon() -> tuple:
    """Return single point of lat, lon data.

    Returns
    -------
    tuple
        lat lon values for a single point.
    """
    lat = 10  # lat
    lon = 165  # lon
    return lat, lon


def example_data_lat_lon_series():
    """Return short series of data point in lat, lon with text station ID.

    Returns
    -------
    tuple
        lat, lon and ID values for several data points.
    """
    lat = [10, 60, -40, -70, -40]  # lat
    lon = [45, 80, 120, 90, -100]  # lon
    ID = ["sta1", "sta2", "sta3", "sta4", "sta5"]  # ID values
    return lat, lon, ID


def generate_random_lat_lon(sample, ziplist=False) -> tuple or zip:
    """Return series of lat, lon values, set by sample size.

    Returns
    -------
    tuple or zip
        lat lon values are either tuple of lists, or a zip object.
    """
    # Generate populations to sample from
    # Use div by 100 to generate float values
    latitude_population = [x / 100 for x in range(-9000, 9000)]
    longitude_population = [x / 100 for x in range(-18000, 18000)]
    # Sample from the latitudes
    latitude_values = random.sample(latitude_population, sample)
    # Sample from the longitudes
    longitude_values = random.sample(longitude_population, sample)
    if ziplist is True:
        # Return as a zip object
        return zip(latitude_values, longitude_values)
    else:
        # Return two lists
        return latitude_values, longitude_values


def random_lat_lon(n) -> np.ndarray:
    """Return array of lat lon values, to desired sample size.

    Paramters
    ---------
    n : int
        Sample size number, to generate array size

    Returns
    -------
    np.ndarray
        Numpy array of lat lon values.
    """
    lat_min, lat_max = -90.0, 90.0
    lon_min, lon_max = -180.0, 180.0
    # Set generator with seed, so random results are repeatable
    num_generator = np.random.default_rng(seed=987)
    # Samples are uniformly distributed over the half-open interval [low, high)
    lat = num_generator.uniform(lat_min, lat_max, n)
    lon = num_generator.uniform(lon_min, lon_max, n)
    # Note the high value is exclusive, therefore lat 90 and lon 180 will never occur
    # This is not a significant issue for these examples, but important to note
    if DEBUG:
        print("")
        print(f"lat ndarray head: {lat[:5]}")
        print(f"lon ndarray head: {lon[:5]}")
    return np.array(tuple(zip(lat, lon)))


# TODO further work / review
# check how to set precision levels
# modify functions and tests
