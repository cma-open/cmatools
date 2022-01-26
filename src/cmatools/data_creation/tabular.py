"""Access or create tabular data for testing and example use."""

import random
from pathlib import Path

import pandas as pd

from cmatools.data_creation.simple import generate_random_lat_lon
from cmatools.definitions import ROOT_DIR


def example_csv_data() -> pd.DataFrame:
    """Return dataframe tabular data object.

    Returns
    -------
    pd.Dataframe
        Sample of station records with ID, lat, lon data.
    """
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


def example_csv_data_index() -> pd.DataFrame:
    """Return dataframe tabular data object, with set index.

    Returns
    -------
    pd.Dataframe
        Sample of station records with ID as the index and lat, lon data.
    """
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
    stations.set_index("ID", inplace=True, verify_integrity=True)
    return stations


# TODO note this is limited by possible unique sample size of lat lon
# What is really needed is unique lat/lon combinations, not indiv lat lon
# TODO - generate another version of land vs sea options


def generate_synthetic_stations(sample, save=False) -> pd.DataFrame:
    """Return dataframe tabular data object, with set index.

    Parameters
    ----------
    sample: int
        Sampe size to set number of records, rows
    save: bool, optional


    Returns
    -------
    pd.Dataframe
        Synthetic stations data with latitudes and longitudes values.
    """
    # Take a specified sample size from a population
    # Create the station IDs (1st object)
    station_values = random.sample(range(0, sample + 1), sample)
    # Add ID text to station values, list comprehension
    station_values = [f"ID{i}" for i in station_values]
    # Create the station latitudes, longitudes (2nd object, 3rd object)
    latitude_values, longitude_values = generate_random_lat_lon(sample)
    # Zip the three objects
    data_zipped = zip(station_values, latitude_values, longitude_values)
    # Pass the zipped object as the data parameter
    # Pass the column names
    df = pd.DataFrame(data_zipped, columns=["IDs", "latitudes", "longitudes"])

    # TODO add option to set IDs as index, then also modify save
    if save is True:
        # Set output filename
        name = "synthetic-stations.txt"
        # TODO modify to use data dir as set by config
        path = Path(ROOT_DIR) / "cmatools" / "_data" / name
        # Saving to CSV file with tab delimiter, no index column
        df.to_csv(path, sep="\t", index=False)
    return df
