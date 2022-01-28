"""Tests for simple module."""

import numpy as np
from numpy.testing import assert_allclose

from cmatools.data_creation.simple import (
    example_data_lat_lon_series,
    example_data_single_lat_lon,
    generate_random_lat_lon,
    random_lat_lon,
)
from tests.a_unit.data_creation.common import verify_lat_lon_values

DEBUG = True


def test_example_data_single():
    """Test example_data_single_lat_lon function."""
    # Set lat lon values
    lat, lon = example_data_single_lat_lon()
    # Verify values are int
    assert isinstance(lat, int)
    assert isinstance(lon, int)
    # Verify valid lat lon values
    verify_lat_lon_values(lat, lon)
    # Verify data values
    assert lat == 10
    assert lon == 165


def test_example_data_series():
    """Test example_data_single_lat_lon_series function."""
    # Set lat, lon, ID series
    lat, lon, ID = example_data_lat_lon_series()
    # Verify data types
    assert isinstance(lat, list)
    assert isinstance(lon, list)
    assert isinstance(ID, list)
    # Verify valid lat lon values in lists
    for (lat_val, lon_val, ID_val) in zip(lat, lon, ID):
        verify_lat_lon_values(lat_val, lon_val)
        if DEBUG:
            print(f"Lat: {lat_val}, Lon: {lon_val}, ID: {ID_val}")
    # Verify selected data values
    assert lat[0] == 10
    assert lon[0] == 45
    # Verify full content of data (short series)
    assert lat == [10, 60, -40, -70, -40]  # lat
    assert lon == [45, 80, 120, 90, -100]  # lon
    assert ID == ["sta1", "sta2", "sta3", "sta4", "sta5"]  # IDs


def test_generate_lat_lon():
    """Test generate_alt_lon function."""
    sample = 50
    # Set lat lon
    lat, lon = generate_random_lat_lon(sample)
    # Verify expected types
    assert isinstance(lat, list)
    assert isinstance(lon, list)
    # Check expected lengths, based on selected sample
    assert len(lat) == sample
    assert len(lon) == sample
    # Verify valid lat lon values in lists
    for (lat_val, lon_val) in zip(lat, lon):
        verify_lat_lon_values(lat_val, lon_val)


def test_generate_lat_lon_ziplist():
    """Test generate_lat_lon function, list output."""
    sample = 50
    # set latlon
    latlon = generate_random_lat_lon(sample, ziplist=True)
    assert isinstance(latlon, list)
    assert len(latlon) == sample
    # Verify valid lat lon values in the list
    for (lat, lon) in latlon:
        verify_lat_lon_values(lat, lon)


def test_random_lat_lon():
    """Test random_lat_lon function."""
    n = 5
    # set random lat lon values
    latlon = random_lat_lon(n)
    assert isinstance(latlon, np.ndarray)
    assert len(list(latlon)) == n
    # Confirm expected single data values
    actual = latlon[0]  # First element in the array
    expected = [59.35619062, -72.26208533]
    # Raises an AssertionError if two objects are not equal up to desired tolerance.
    assert_allclose(actual, expected)
    # Confirm a short extract of the array s as expected
    short_array = latlon[0:3]
    expected = [
        [59.35619062, -72.26208533],
        [59.27626373, -24.98602088],
        [23.23916581, 13.78076821],
    ]
    # Raises an AssertionError if two objects are not equal up to desired tolerance.
    assert_allclose(short_array, expected)
    # Can also test the entire array, not just an indiv value
    expected = [
        [59.35619062, -72.26208533],
        [59.27626373, -24.98602088],
        [23.23916581, 13.78076821],
        [-38.52986805, -82.08639721],
        [-52.45293244, 62.27547252],
    ]
    # Raises an AssertionError if two objects are not equal up to desired tolerance.
    assert_allclose(latlon, expected)

    if DEBUG:
        print("ndarray head:")
        print(latlon[:5])
