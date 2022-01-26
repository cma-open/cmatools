"""Tests for data creation tabular data."""

from unittest.mock import patch

import numpy as np
import pandas as pd
from numpy.testing import assert_equal

from cmatools.data_creation.tabular import (
    example_csv_data,
    example_csv_data_index,
    generate_synthetic_stations,
)

# TODO check and use via refactor
# from tests.a_unit.data_creation.common import verify_lat_lon

DEBUG = True
LEVEL = 0  # 1 for higher debug output, 0 for no further output


def print_df_details_main(df):
    """Print selected metadata for the pandas dataframe."""
    print("")
    print(f"df columns: {df.columns}")
    print("df dtypes:")
    print(df.dtypes)
    print(f"df ndim: {df.ndim}")
    print(f"df shape: {df.shape}")
    print(f"df size: {df.size}")
    print(f"df head: {df.head()}")  # Selection of first 5 values
    print(f"df tail: {df.tail()}")  # Selectino of last 5 values
    print("")


def print_df_details_additional(df):
    """Print additional metadata for the pandas dataframe."""
    print("")
    print(f"df attrs: {df.attrs}")
    print(f"df axes: {df.axes}")
    print(f"df flags: {df.flags}")
    print(f"df values: {df.values}")
    print("")
    print(f"df: {df}")


def test_example_csv_data():
    """Test example_csv_data function."""
    df = example_csv_data()
    assert isinstance(df, pd.DataFrame)
    # Use .loc to access a group of rows and columns by label(s) or a boolean array.
    # Test the first value from data are as expected (numeric index)
    assert df.loc[0, "lat"] == 17.1167
    assert df.loc[0, "lon"] == -61.7833

    # TODO potn move to another test function re validation
    # Verify lat, lon values are correct (range, order)
    # Identify invalid lat, lon values as a series
    invalid_lats = (df["lat"] >= 90) & (df["lat"] <= -90)
    invalid_lons = (df["lon"] >= 180) & (df["lon"] <= -180)
    assert isinstance(invalid_lats, pd.Series)
    assert isinstance(invalid_lons, pd.Series)
    # Check if any of the pd series is True (indicates invalid data is present_
    any_invalid_lats = invalid_lats.any()  # True if any values are True
    any_invalid_lons = invalid_lons.any()  # True if any values are True
    # Verify expected instance types
    assert isinstance(any_invalid_lats, np.bool_)
    assert isinstance(any_invalid_lons, np.bool_)
    # Verify no invalid data is present
    assert_equal(any_invalid_lats, False)
    assert_equal(any_invalid_lons, False)
    # DUPLICATE test - keeping above lines for reference !
    # Between method can also be used to check data value range
    # Test if all values are within valid range
    valid_lats = df["lat"].between(-90, 90).all()  # True if all values are True
    valid_lons = df["lon"].between(-180, 180).all()  # True if all values are True
    # Verify that all valid checks are True
    assert_equal(valid_lats, True)
    assert_equal(valid_lons, True)
    # Optional print for debug / training / dev use
    if DEBUG:
        print_df_details_main(df)
        if LEVEL:
            print_df_details_additional(df)


def test_example_csv_data_index():
    """Test example_csv_data_index function."""
    df = example_csv_data_index()
    assert isinstance(df, pd.DataFrame)
    # Use .loc to access a group of rows and columns by label(s) or a boolean array.
    # Test the first value from data are as expected (string index)
    assert df.loc["ACW00011604", "lat"] == 17.1167
    assert df.loc["ACW00011604", "lon"] == -61.7833
    # Test if all values are within valid range
    valid_lats = df["lat"].between(-90, 90).all()  # True if all values are True
    valid_lons = df["lon"].between(-180, 180).all()  # True if all values are True
    # Verify that all valid checks are True
    assert_equal(valid_lats, True)
    assert_equal(valid_lons, True)
    # Optional print for debug / training / dev use
    if DEBUG:
        print_df_details_main(df)
        if LEVEL:
            print_df_details_additional(df)


def test_generate_synthetic_stations():
    """Test generate_synthetic_stations."""
    sample = 50
    df = generate_synthetic_stations(sample)
    assert isinstance(df, pd.DataFrame)
    # Not possible to check actual values, as randomly generated

    # Is possible to test data ranges
    # Test if all values are within valid range
    valid_lats = df["latitudes"].between(-90, 90).all()  # True if all values True
    valid_lons = df["longitudes"].between(-180, 180).all()  # True if all values True
    # Verify that all valid checks are True
    assert_equal(valid_lats, True)
    assert_equal(valid_lons, True)
    # Optional print for debug / training / dev use
    if DEBUG:
        print_df_details_main(df)
        if LEVEL:
            print_df_details_additional(df)


# TODO refactor fo ROOT vs REPO dir
def test_generate_synthetic_stations_save(tmp_path):
    """Test generate_synthetic_stations, with save to file."""
    sample = 50
    # patch to replace module level variable, save location, with tmp_path
    with patch("cmatools.data_creation.tabular.ROOT_DIR", tmp_path):
        outputdir = tmp_path / "cmatools" / "_data"
        outputdir.mkdir(parents=True)  # Create subdir and parents
        assert outputdir.exists()  # Confirm dir exists
        # Generate the dataframe output and save to file
        df = generate_synthetic_stations(sample, save=True)
        assert isinstance(df, pd.DataFrame)  # Confirm dataframe type
        outputfile = outputdir / "synthetic-stations.txt"
        assert outputfile.exists()  # Confirm output file now exists


# TODO refactor to use common validate function from
# TODO - schema validation here ?
