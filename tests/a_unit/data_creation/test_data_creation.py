"""Tests for data_creation module."""

import cartopy.crs as ccrs
import iris
import iris.aux_factory
import iris.coords
import iris.quickplot as qplt
import matplotlib.pyplot as plt

# import iris.coords as icoords
import numpy as np

# import numpy.ma as ma
# from cf_units import Unit
from iris.coord_systems import GeogCS
from iris.coords import DimCoord
from iris.cube import Cube

# NEW TODO
# Simple map showing station locations (random points), label by station ID code?
# Map showing numpy data array plotted on global map
# Map iris showing plotted data from an iris cube
# Add labels and gridlines
# Use different resolution grids, mimic as if records were captured at cell centres?


# simple tests
# geopgraphic data - points in geogrpahic space, so all lat / lon
# single data, multi data, height, time

# Purpose is to aid wider system testing by providing a resourc eof sythneti tests data

# Modular - data, coords, metadata, etc

# Resource
#


# setup data locations and observations with multiple
# data points lying in some grid cells.
data_locations = np.array(
    [
        [-90.0, -80, -45.0, 0.0, 1.0, 1.0, 45.0, -80.0],
        [-180.0, -170, -90.0, 0.0, 2.0, 1.0, 90.0, 170.0],
    ]
)
data_values = np.array([2.0, 1.0, 1.0, 1.0, 1.0, 4.0, 2.0, 5.0])

# setup data locations and observations for data in separate grid
# cells lying on the diagonal cells of the grid.
data_locations = np.array([[-90.0, -45.0, 0.0, 45.0], [-180.0, -90.0, 0.0, 90.0]])
data_values = np.array([-2.0, -1.0, 1.0, 2.0])


latitude = DimCoord(np.linspace(-90, 90, 4), standard_name="latitude", units="degrees")

longitude = DimCoord(
    np.linspace(45, 360, 8), standard_name="longitude", units="degrees"
)
cube = Cube(
    np.zeros((4, 8), np.float32), dim_coords_and_dims=[(latitude, 0), (longitude, 1)]
)

# here

# A single cube describes one and only one phenomenon, always has a name, a unit and
# an n-dimensional data array to represents the cube’s phenomenon. In order to locate
# the data spatially, temporally, or in any other higher-dimensional space, a
# collection of coordinates exist on the cube.


# assumes always degrees
def add_geographic_coord(locations, standard_name):
    """Add geographic coordinate."""
    coord = iris.coords.DimCoord(
        locations, standard_name=standard_name, units="degrees"
    )
    # check
    # lon_coord.guess_bounds()
    return coord


# add time


def input_data():
    """Input data."""
    data = np.array([1, 2, 3], dtype=np.int32)
    return data


# def example_lat_lon_cube(inp_data, ):

# TODO check grid_latitude vs latitude?


def example_lat_lon_cube():
    """Return a cube with a latitude and longitude."""
    # Set data that represents locations at which data exists
    latitude_values = np.array([-85, 50, 86], dtype=np.int32)
    longitude_values = np.array([-175, 30, 50, 176], dtype=np.int32)
    # Set data values from the record locations
    data = np.arange(12, dtype=np.int32).reshape((3, 4))
    # data = np.arange(6, dtype=np.int32).reshape((2, 3))
    # data = np.array([1, 2, 3], dtype=np.int32)

    # Create an iris cube from the data values
    cube = Cube(data)
    # Set geographic data coordinate system
    cs = GeogCS(6371229)

    # refactor to function
    coord = DimCoord(
        points=latitude_values,
        standard_name="latitude",
        units="degrees",
        coord_system=cs,
    )

    # check points
    print(f"points: {coord.points}")

    cube.add_dim_coord(coord, 0)
    coord = DimCoord(
        points=longitude_values,
        standard_name="longitude",
        units="degrees",
        coord_system=cs,
    )
    cube.add_dim_coord(coord, 1)
    # Add cube name and units
    cube.long_name = "thingness"
    cube.units = "1"
    return cube


def plot_cube(cube):
    """Plot cube."""
    # Add a contour, and put the result in a variable called contour.
    contour = qplt.contour(cube)
    # Add coastlines to the map created by contour.
    plt.gca().coastlines()
    # Add axes
    # ax = plt.axes()
    # Add contour labels based on the contour we have just created.
    plt.clabel(contour, inline=False)
    plt.show()


def plot_cube_colourmesh(cube):
    """Plot cube colourmesh."""
    qplt.pcolormesh(cube)
    # Add coastlines to the map created by contour.
    plt.gca().coastlines()
    plt.show()


def plot_cube_iris_colourmesh():
    """Plot cube iris colourmesh."""
    temperature = example_lat_lon_cube()
    # iris comes complete with a method to put bounds on a simple point
    # coordinate. This is very useful...
    temperature.coord("latitude").guess_bounds()
    temperature.coord("longitude").guess_bounds()
    # temperature.coord('grid_latitude').guess_bounds()
    # temperature.coord('grid_longitude').guess_bounds()

    # turn the iris Cube data structure into numpy arrays
    gridlons = temperature.coord("longitude").contiguous_bounds()
    gridlats = temperature.coord("latitude").contiguous_bounds()
    # gridlons = temperature.coord('grid_longitude').contiguous_bounds()
    # gridlats = temperature.coord('grid_latitude').contiguous_bounds()
    temperature = temperature.data

    plt.figure(figsize=(16, 8))

    # set up a map
    ax = plt.axes(projection=ccrs.PlateCarree())

    # define the coordinate system that the grid lons and grid lats are on
    # rotated_pole = ccrs.RotatedPole(pole_longitude=177.5, pole_latitude=37.5)
    # plt.pcolormesh(gridlons, gridlats, temperature, transform=rotated_pole)
    plt.pcolormesh(gridlons, gridlats, temperature)

    ax.set_global()
    ax.coastlines()
    ax.gridlines(draw_labels=True)
    plt.show()


def plot_points():
    """Plot points."""
    box_top = 45
    x, y = [-44, -44, 45, 45, -44], [-45, box_top, box_top, -45, -45]
    x = -44
    y = 20

    ax = plt.subplot(212, projection=ccrs.PlateCarree())

    ax.coastlines()
    ax.plot(x, y, marker="o")

    ax.gridlines()

    plt.show()


def plot_map():
    """Plot map."""
    # fig = plt.figure(figsize=(8, 12))
    # fig = plt.figure(figsize=(16, 8))
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.set_global()
    ax.coastlines()
    x = 10
    y = 10
    ax.plot(x, y, marker="o")
    ax.gridlines(draw_labels=True)
    plt.show()


# def test_data_creation_cubes():
#     print(cube)
#     print(cube.data)

# def test_example_lat_lon_cube():
#     example = example_lat_lon_cube()
#     print()
#     print(example)
#     print()
#     print(example.data)
#     print(example.shape)
#     print(example.ndim)
#
# def test_input_data():
#     data = input_data()
#     print(data)
#
#
# def test_plot_cube():
#     example = example_lat_lon_cube()
#     plot_cube(example)
#
#
def test_plot_cube_colourmesh():
    """Test plot cube colourmesh."""
    example = example_lat_lon_cube()
    plot_cube_colourmesh(example)


#
# def test_plot_point():
#     plot_points()


def test_plot_map():
    """Test plot map."""
    plot_map()


def test_plot_cube_iris_colourmesh():
    """Test plot cube iris colourmesh."""
    plot_cube_iris_colourmesh()
