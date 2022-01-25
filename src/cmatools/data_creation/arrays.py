"""Array data for test and example use."""

import numpy as np


def data_array() -> np.ndarray:
    """Return simple data array.

    Returns
    -------
    np.ndarray
        Simple 1D data array
    """
    data = [1, 2, 3]
    data = np.array(data, dtype=np.int32)
    return data


def data_array_sample(sample=50) -> np.ndarray:
    """Return data array of set sample size.

    Parameters
    ----------
    sample : int, optional
        number of sample elements to create.

    Returns
    -------
    np.ndarray
        Simple 1D data array, set by default value or parameter sample size.

    """
    data = range(0, sample)
    data = np.array(data, dtype=np.int32)
    return data


def data_locations_and_values_array() -> tuple:
    """Return tuple of two data arrays.

    Returns
    -------
    tuple
        Two data arrays representing lat/lon and data values.
    """
    # TODO - edit as currently not grid cell aware
    # setup data locations and observations
    # with multiple data points lying in some grid cells.
    latitudes = [-90.0, -80, -45.0, 0.0, 1.0, 1.0, 45.0, -80.0]
    longitudes = [-180.0, -170, -90.0, 0.0, 2.0, 1.0, 90.0, 170.0]
    latlon = [latitudes, longitudes]
    data_locations = np.array(latlon)
    data_values = [2.0, 1.0, 1.0, 1.0, 1.0, 4.0, 2.0, 5.0]
    data_values = np.array(data_values)
    return data_locations, data_values


def data_locations_and_values_array_other() -> tuple:
    """Return tuple of two data arrays.

    Returns
    -------
    tuple
        Two data arrays representing lat/lon and data values.
    """
    # TODO - edit as currently not grid cell aware
    # setup data locations and observations
    # for data in separate grid cells lying on the diagonal cells of the grid.
    latitudes = [-90.0, -45.0, 0.0, 45.0]
    longitudes = [-180.0, -90.0, 0.0, 90.0]
    latlon = [latitudes, longitudes]
    data_locations = np.array(latlon)
    data_values = [-2.0, -1.0, 1.0, 2.0]
    data_values = np.array(data_values)
    return data_locations, data_values
