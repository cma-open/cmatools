"""Access natural earth download data via cartopy."""

import cartopy.io


def natural_earth_points() -> list:
    """Return list fo geometry points.

    Returns
    -------
    list
        List of shapely geometry points for populated places.
    """
    # Set populated places dataset
    fname = cartopy.io.shapereader.natural_earth(
        resolution="110m", category="cultural", name="populated_places_simple"
    )
    # Acces data via shapereader
    # Use feature geometries to list data points
    points = list(cartopy.io.shapereader.Reader(fname).geometries())
    return points
