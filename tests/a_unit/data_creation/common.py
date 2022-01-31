"""Common code for use by tests."""

import numpy as np

DEBUG = False


def verify_lat_lon_values(lat: int, lon: int):
    """Verify if single latitude and longitude values are valid.

    Parameters
    ----------
    lat : int
        Latitude
    lon : int
        Longitude
    """
    try:
        assert (-90 <= lat <= 90) is True, "Latitude value is incorrect"
        assert (-180 <= lon <= 180) is True, "Longitude value is incorrect"
    except AssertionError:
        raise
    if DEBUG:
        print(f"Lat: {lat}, Lon: {lon}")


def verify_lat_lon_array(array: np.ndarray):
    """Verify an array of latitude and longitude values are valid.

    Parameters
    ----------
    array : np.ndarray
        Array of latitude and longitude values
    """
    # Kept for reference (would not use this)
    # Check max element within the entire array
    # assert array.max() <= 180, "Array has values greater than 180"
    # assert array.min() >= -90, "Array has values less than -90"

    # Extract lat, lon to new arrays
    lat = array[:, 0]  # Extract lat values
    lon = array[:, 1]  # Extract lon values
    try:
        assert np.all((lat <= 90) & (lat >= -90)), "Latitude values are not valid"
        assert np.all((lon <= 180) & (lat >= -180)), "Longitude values are not valid"
    except AssertionError:
        raise


def verify_lat_lon_dataframe(df, lat, lon):
    """Verify a dataframe of latitude and longitude values are valid.

    Parameters
    ----------
    df : pd.Dataframe
        Dataframe object holding lat lon data
    lat : str
        Name of latitude data column
    lon : str
        Name of longitude data column
    """
    # Test if all values are within valid range
    valid_lats = df[lat].between(-90, 90)
    valid_lons = df[lon].between(-180, 180)
    # True if all values are True
    assert valid_lats.all(), "Latitude values are not valid"
    assert valid_lons.all(), "Longitude values are not valid"
