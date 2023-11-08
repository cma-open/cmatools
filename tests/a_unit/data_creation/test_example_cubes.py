"""Tests for cubes module."""

from pathlib import Path

import cartopy.crs as ccrs
import iris

# from cmatools.data_creation.example_cubes import (
# create_simple_cube,
# load_example_cube2d,
# load_example_cube3d,)
from cmatools.definitions import REPO_DIR
from cmatools.plotting.common import plot_defaults

# import iris.plot as iplt
# import iris.quickplot as qplt
# import matplotlib.pyplot as plt


# from tests.a_unit.data_creation.common import print_all

# import numpy as np
# import pandas as pd


# why geoviews not available ?
# import geoviews


FULL = True


# def test_create_simple_cube():
#     cube = create_simple_cube()
#     print_cube_details(cube)


# def test_load_example_cube3d_tos():
#   cube = load_example_cube3d(REPO_DIR, tos_file)
#  print("Testing cube: 3d")
# print_all(cube, "latitude", "longitude")
# Plotting - not possible via qplt for 3d cubes
# Draw the block plot.
# qplt.pcolormesh(cube)
# plt.show()


# def test_load_example_cube2d_tos():
#    cube = load_example_cube2d(REPO_DIR, tos_file)
#   print("Testing cube: 2d")
#  print_all(cube, "latitude", "longitude")
# Draw the block plot.
#  qplt.pcolormesh(cube)
#  plt.show()


def test_view():
    """Test cube view."""
    file = "tos_O1_2001-2002.nc"
    print("")
    print(REPO_DIR)
    path = Path(REPO_DIR) / "data" / "inputs" / file
    cube = iris.load_cube(str(path))
    # print_cube_details(cube)
    # print_cube_coords(cube)
    # print_time_coord(cube)
    # print_cube_data(cube)
    # print_geog_coord(cube, "latitude", "longitude")

    # index a cube to subset
    # input cube is 3d time, lat, lon
    # get the first element of the first dimension (+ every other dimension)
    # therefore returns the cube for one single time step
    # time moves to be a scalar coord and the cube is 2d
    first = cube[0]
    # print("xxxxxxxxxxxx")
    # print(first.shape)
    # print(first.ndim)
    # print(first)
    # last = cube[-1]
    # print()
    # print(last)

    # Take a 1d slice using array style indexing.
    # EXPLIAN FURTHER >>>>>>
    slice_1d = first[5, :]
    print("slice")
    print(slice_1d)
    # extract data where latitude = 40, but for all lons
    slice_1d = first[40, :]
    print("slice")
    print(slice_1d)
    slice_1d = first[:, 0]

    print("slice")
    print(slice_1d)
    # print(len(slice_1d.data))
    # print()

    # print("scalar")
    # just the first value for time, lat, lon , so gives one data point
    # firstall = cube[0, 0, 0]
    firstall = cube[2, 90, 90]  # is a value...
    print(firstall)
    print("Data:")
    print(firstall.data)
    print(firstall.data.mask)
    # print(type(firstall))
    # print(type(firstall.data))
    # print(type(firstall.data.mask))
    # print("----")

    # cubes modifications for mapping
    # creates a 2d cube from a 3d cube
    # equator_slice = cube.extract(iris.Constraint(latitude=0))
    # print("yyyyyyyyyyyyyyy")
    # print(equator_slice)

    # Take a 1d slice using array style indexing.
    # temperature_1d = cube[5, :]

    # iplt.plot(slice_1d)

    # qplt.plot(slice_1d)  # quickplots use metadata to set title, labels,
    # qplt.plot(first)  # does bort work for 2d plots
    # plt.show()

    # Load plot defaults
    fig, plt, ax = plot_defaults(1)
    # # Set titles
    # fig.suptitle('Example map 1 - title', fontsize=16)
    # ax.set_title("Example 1 ax title")
    # # Load input data
    # lat = first.coord("latitude").points
    # lon = first.coord("longitude").points
    # print(f"lengths: {len(lat)}, {len(lon)}")
    # # x, y: float or array-like, shape (n, )
    # # long , lat
    # ax.scatter(lon[:100], lat[:100], s=40, c='r', alpha=0.9,
    #            transform=ccrs.PlateCarree())
    # #plt.savefig('map.png')
    # #plt.show()

    lat = first.coord("latitude")
    lon = first.coord("longitude")[0:170]
    print(lat)
    print(lat.points)
    # iplt.scatter(lat, lon)
    # if using ax from matplotlib, need to use values, not cubes or coords
    ax.scatter(
        lat.points, lon.points, s=40, c="r", alpha=0.9, transform=ccrs.PlateCarree()
    )

    # Draw the block plot.
    # qplt.pcolormesh(first)

    # plt.show()


# need an example to show extract  point values from cube and plot them .......
# need to show for cubes if is really point data, obs, or gridded coverage ...

# tidy up and repeat fro various hadcrut / crutem data
# consider how to include as gallery ? in the docs /.......

# cube questions to answer

# how does a user know if the cube represents grids or point coverage?
# is this in the metadata or bounds?

# Q. what is the time step with maximum coverage (count) ?

# grids
# 1 degree 180 * 360 = 64,800
# 5 degree 36 * 72 = 2,592
# 10 degree 18 * 36 = 648
