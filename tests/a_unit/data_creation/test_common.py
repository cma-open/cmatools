"""Tests for common module."""

import numpy as np
import pandas as pd
import pytest

from tests.a_unit.data_creation.common import (
    verify_lat_lon_array,
    verify_lat_lon_dataframe,
    verify_lat_lon_values,
)


def test_verify_lat_lon_values_raises():
    """Test for verify_lat_lon_values function."""
    # Set response message (part)
    message = "value is incorrect"
    # Set invalid values
    lat, lon = 600, 780  # both invalid
    with pytest.raises(AssertionError, match=message):
        verify_lat_lon_values(lat, lon)
    # Set invalid values
    lat, lon = 60, 780  # lon invalid
    with pytest.raises(AssertionError, match=message):
        verify_lat_lon_values(lat, lon)
    # Set invalid values
    lat, lon = 600, 80  # lat invalid
    with pytest.raises(AssertionError, match=message):
        verify_lat_lon_values(lat, lon)


def test_verify_lat_lon_array_raises():
    """Test for verify_lat_lon_array function."""
    # Set response message (part)
    message = "values are not valid"
    # Set invalid values
    latlon = [
        [559.35619062, -72.26208533],
        [59.27626373, -24.98602088],
        [23.23916581, 913.78076821],
    ]
    # Convert list to numpy array
    latlon = np.asarray(latlon)
    with pytest.raises(AssertionError, match=message):
        verify_lat_lon_array(latlon)
    latlon = [
        [59.35619062, -72.26208533],
        [59.27626373, -24.98602088],
        [23.23916581, 913.78076821],
    ]
    # Convert list to numpy array
    latlon = np.asarray(latlon)
    with pytest.raises(AssertionError, match=message):
        verify_lat_lon_array(latlon)


def test_verify_lat_lon_dataframe_raises():
    """Test for verify_lat_lon_dataframe function."""
    # Set response message (part)
    message = "values are not valid"
    # Set invalid values
    latlon = [
        [559.35619062, -72.26208533],
        [59.27626373, -24.98602088],
        [23.23916581, 913.78076821],
    ]
    # Create a test dataframe
    df = pd.DataFrame(latlon, columns=["latitudes", "longitudes"])
    with pytest.raises(AssertionError, match=message):
        verify_lat_lon_dataframe(df, "latitudes", "longitudes")
