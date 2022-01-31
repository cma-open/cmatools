"""Tests for downloads module."""

from shapely.coords import CoordinateSequence
from shapely.geometry import Point

from cmatools.data_creation.downloads import natural_earth_points

DEBUG = True


def test_natural_earth_points():
    """Tests for natural_earth_points function."""
    # Set points as natural earth populated places
    points = natural_earth_points()
    # Expect points to be a list of shapely geometry Points
    assert isinstance(points, list)
    # Expect x,y as lon, lat format
    for point in points:
        # Verify valid lat lon values
        # Expect x,y as lon,lat
        assert (-180 <= point.x <= 180) is True  # lon check
        assert (-90 <= point.y <= 90) is True  # lat check
        # Verify expected object types
        assert isinstance(point, Point)
        assert point.geom_type == "Point"
        assert isinstance(point.coords, CoordinateSequence)
        if DEBUG:
            print(point)
