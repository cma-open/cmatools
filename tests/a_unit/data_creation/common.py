"""Common code for use by tests."""

import numpy as np

DEBUG = False
FULL = False


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


# ------------------------------------------------------------------------------------
# VERBOSE output  - prints


def print_cube_details(cube):
    """Print full metadata of a cube."""
    print()
    print("--------------------------------------------------------------------------")
    print(f"Cube print output: {cube.ndim}d cube, {cube.standard_name}")
    print("--------------------------------------------------------------------------")
    print(cube)
    if FULL:
        print("---")
        print(f"Cube metadata print output: {cube.ndim}d cube, {cube.standard_name}")
        print("---")
        print(cube.metadata)


def print_cube_coords(cube):
    """Print cube coordinates."""
    print()
    print("--------------------------------------------------------------------------")
    print(f"Cube coords:  {cube.ndim}d cube, {cube.standard_name}")
    print("--------------------------------------------------------------------------")
    coord_names = [coord.name() for coord in cube.coords()]
    print(f"Cube has {len(coord_names)} coords: {coord_names}")
    for name in coord_names:
        coord = cube.coord(name)
        print(
            f"Coord standard name: {coord.standard_name}, "
            f"Long name: {coord.long_name}, Coord units: {coord.units}"
        )


def print_time_coord(cube):
    """Print cube time coordinate."""
    time_coord = cube.coord("time")
    print()
    print("--------------------------------------------------------------------------")
    print(
        f"Time coord: {cube.ndim}d cube, {cube.standard_name}, "
        f"length {len(time_coord.points)} "
    )
    print("--------------------------------------------------------------------------")
    print(f"Time coord metadata: {time_coord.metadata}")
    print(f"Time coord units: {repr(time_coord.units)}")
    print("---")
    print("Slice time coord (first) [0]:")
    print(time_coord[0])
    print("Slice time coord (last) [-1]:")
    print(time_coord[-1])
    print("---")

    # Set vars as lower and upper bounds arrays
    lower_bounds = time_coord.bounds[:, 0]
    upper_bounds = time_coord.bounds[
        :,
        1,
    ]
    # Calculate array of bounds ranges
    bounds_range = upper_bounds - lower_bounds
    # Calculate average across the array
    average_bounds_range = np.average(bounds_range)
    print(f"Time units are in: {time_coord.units}")
    print(f"Average bounds range: {average_bounds_range:.3}")


def print_cube_data(cube):
    """Print cube data."""
    print()
    print("--------------------------------------------------------------------------")
    print(f"Cube data: {cube.ndim}d cube, {cube.standard_name}")
    print("--------------------------------------------------------------------------")
    print(f"Data type: {type(cube.data)}")
    print(f"Data shape: {cube.data.shape}")
    print(f"Data units: {cube.units}")
    print(
        f"Data summary stats: "
        f"max {cube.data.max():.3}, "
        f"min {cube.data.min():.3}, mean {cube.data.mean():.3}"
    )
    # print(f"Length of data in first time step: {len(cube.data[0])}")
    data_array = cube.data.size
    non_masked = cube.data.count()
    percent = (non_masked / data_array) * 100
    #  print to 3 significant places
    print(
        f"Size of data array: {cube.data.size}, "
        f"count of non-masked {cube.data.count()} ({percent:.3}%)"
    )
    # ree
    # df = pd.DataFrame(cube.data[0])
    # print(df.describe())
    print("---")
    # add info on masked values here .....
    if FULL:
        # TODO check and edit
        # print(f"Slice cube data [:1], length: len(cube.data[:1])")
        print("---")
        print(cube.data[0])  # show first element


def print_geog_coord(cube, lat, lon):
    """Print cube geographic coordinates."""
    print()
    print("--------------------------------------------------------------------------")
    print(f"Print geographic coords: {cube.ndim}d cube, {cube.standard_name}")
    print("--------------------------------------------------------------------------")
    coord_names = [coord.name() for coord in cube.coords()]
    # Check that the two named geog coords are in coord list
    if all(geocoord in coord_names for geocoord in [lat, lon]):
        lat_coord = cube.coord(lat)
        lon_coord = cube.coord(lon)
        print(lat_coord.metadata)
        print(lon_coord.metadata)
        print(
            f"Coord lengths: lat {len(lat_coord.points)}, "
            f"lon {len(lon_coord.points)} "
        )
        if lat_coord.coord_system:
            print(f"lat coord system: {lat_coord.coord_system}")
        if lon_coord.coord_system:
            print(f"lon coord system: {lon_coord.coord_system}")
    else:
        print("Coords not present")
    coordsys = cube.coord_system("GeogCS")
    if coordsys:
        print(f"Coord system: {cube.coord_system('GeogCS')}")
    else:
        print("Coord system not present")


def print_resolution(cube, lat, lon):
    """Print cube coord resolution."""
    print("---")
    if cube.coord(lat).units == "degrees":
        lat_points = cube.coord(lat).points
        lat_res = 180 / len(lat_points)
    if cube.coord(lon).units == "degrees":
        lon_points = cube.coord(lon).points
        lon_res = 360 / len(lon_points)
    # TODO refactor
    print(f"Cube grid resolution: {lat_res} by {lon_res} degrees")
    # try:
    #    print(f"Cube grid resolution: {lat_res} by {lon_res} degrees")
    # except:
    #    print("Cube coords not in degrees")
    print("-")


def print_all(cube, lat, lon):
    """Print all cube metadata and full data information."""
    coord_names = [coord.name() for coord in cube.coords()]
    # Check that the two named geog coords are in coord list
    if all(geocoord in coord_names for geocoord in [lat, lon]):
        pass
    else:
        raise ValueError("Incorrect geog coord names")

    print_cube_details(cube)
    print_cube_coords(cube)
    print_time_coord(cube)
    print_cube_data(cube)
    print_geog_coord(cube, lat, lon)
    print_resolution(cube, lat, lon)


# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
