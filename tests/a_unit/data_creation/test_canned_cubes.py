"""Tests for cubes module."""

from pathlib import Path

# why geoviews not available ?
# import geoviews
import humanize
import iris

from cmatools.data_creation.canned_cubes import (
    extract_timesteps,
    file_sizes,
    save_netcdf,
)

# load_3dcube_crutem,; load_3dcube_hadcrut,; load_example_cube2d,; load_example_cube3d,
from cmatools.definitions import REPO_DIR

# import cartopy.crs as ccrs


# import iris.plot as iplt
# import iris.quickplot as qplt
# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd


# from cmatools.plotting.common import plot_defaults
# from tests.a_unit.data_creation.common import print_all

FULL = True

#  A coordinate does not have data, instead it has points and bounds

HADSST_SHORT = "HADSST_short.nc"
HADCRUT_SHORT = "HADCRUT_short.nc"
CRUTEM_SHORT = "CRUTEM_short.nc"
HADISDH_SHORT = "HADISDH_short.nc"

crutem_file = "CRUTEM.5.0.0.0.anomalies.nc"
tos_file = "tos_O1_2001-2002.nc"
hadcrut_file = "HadCRUT.5.0.1.0.analysis.anomalies.ensemble_mean.nc"
tg_file = "tg_ens_mean_0.25deg_reg_2011-2020_v23.1e.nc"

FILES = [HADCRUT_SHORT, CRUTEM_SHORT, HADSST_SHORT, HADISDH_SHORT, tos_file]


def test_canned_data_sizes():
    """Test canned data sizes."""
    files = [HADCRUT_SHORT, CRUTEM_SHORT, HADSST_SHORT, HADISDH_SHORT, tos_file]
    # EOBS_SHORT
    for file in files:
        filepath = Path(REPO_DIR) / "data" / "inputs" / file
        file_size = filepath.stat().st_size
        print(f"File: {file},  size: {humanize.naturalsize(file_size)}")


def test_canned_data_file_sizes():
    """Test canned data file sizes."""
    files = [HADCRUT_SHORT, CRUTEM_SHORT, HADSST_SHORT, HADISDH_SHORT, tos_file]
    file_report = file_sizes(files)
    print(file_report)


def test_cube_summary_info():
    """Test cube summary information."""
    for file in FILES:
        print()
        path = Path(REPO_DIR) / "data" / "inputs" / file
        cube = iris.load_cube(str(path))
        print(cube.summary)
        print()
        print(cube.summary(shorten=True))


#
# def test_load_cube3d_hadcrut():
#     print("")
#     print(f"File: {hadcrut_file} ")
#     file = Path(REPO_DIR) / "data" / "inputs" / hadcrut_file
#     file_size = file.stat().st_size
#     print(f"File size: {humanize.naturalsize(file_size)}")
#     cube = load_example_cube3d(REPO_DIR, hadcrut_file)
#     print("Testing cube: 3d")
#     print_all(cube, "latitude", "longitude")

# Plotting - not possible via qplt for 3d cubes
# Draw the block plot.
# qplt.pcolormesh(cube)
# plt.show()
#
# def test_load_cube3d_crutem():
#     print("")
#     print(f"File: {crutem_file} ")
#     file = Path(REPO_DIR) / "data" / "inputs" / crutem_file
#     file_size = file.stat().st_size
#     print(f"File size: {humanize.naturalsize(file_size)}")
#     cube = load_example_cube3d(REPO_DIR, crutem_file)
#     print("Testing cube: 3d")
#     print_all(cube, "latitude", "longitude")

# Plotting - not possible via qplt for 3d cubes
# Draw the block plot.
# qplt.pcolormesh(cube)
# plt.show()

# def test_load_cube3d_crutem_short():
#     print("")
#     print(f"File: {CRUTEM_SHORT} ")
#     file = Path(REPO_DIR) / "data" / "inputs" / CRUTEM_SHORT
#     file_size = file.stat().st_size
#     print(f"File size: {humanize.naturalsize(file_size)}")
#     cube = load_example_cube3d(REPO_DIR, CRUTEM_SHORT)
#     print("Testing cube: 3d")
#     print_all(cube, "latitude", "longitude")
#
# def test_load_cube3d_hadcrut_short():
#     print("")
#     print(f"File: {HADCRUT_SHORT} ")
#     file = Path(REPO_DIR) / "data" / "inputs" / HADCRUT_SHORT
#     file_size = file.stat().st_size
#     print(f"File size: {humanize.naturalsize(file_size)}")
#     cube = load_example_cube3d(REPO_DIR, HADCRUT_SHORT)
#     print("Testing cube: 3d")
#     print_all(cube, "latitude", "longitude")

# PRINT and visualise the ensemble realisations in hadcrut .....

# def test_extract_cubes():
#     cube_crutem = load_3dcube_crutem()
#     crutem_extract = extract_timesteps(cube_crutem, 2010, 2020)
#     print("!!!!!")
#     print(crutem_extract)
#     print_all(crutem_extract, "latitude", "longitude")
#     return crutem_extract
#
# def test_save_netcdf():
#     cube_crutem = load_3dcube_crutem()
#     crutem_extract = extract_timesteps(cube_crutem, 2010, 2020)
#     save_netcdf(crutem_extract, "CRUTEM_short.nc")
#

#
# def test_extract_cubes_hadcrut():
#     cube = load_3dcube_hadcrut()
#     cube_extract = extract_timesteps(cube, 2010, 2020)
#     print("!!!!!")
#     print(cube_extract)
#     print_all(cube_extract, "latitude", "longitude")
#     return cube_extract
#
# def test_save_netcdf_hadcrut():
#     cube = load_3dcube_hadcrut()
#     cube_extract = extract_timesteps(cube, 2010, 2020)
#     save_netcdf(cube_extract, "HADCRUT_short.nc")


def test_save_netcdf_hadsst():
    """Test save netcdf hadsst data."""
    # file = "HadSST.4.0.1.0_actuals_median.nc"
    # file = "HadISDH.landRH.4.3.1.2020f_FLATgridHOM5by5_anoms8110.nc"
    #
    # print(f"Loading file: {file}")
    # path = Path(REPO_DIR) / "data" / "temp" / file
    # cube = iris.load_cube(str(path), "rh_abs")
    # print(cube)
    # cube_extract = extract_timesteps(cube, 2010, 2020)
    # print("lllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll")
    # print(cube_extract)
    # save_netcdf(cube_extract, "HADISDH_short.nc")
    # print("")

    file = "tg_ens_mean_0.25deg_reg_2011-2020_v23.1e.nc"
    print(f"Loading file: {file}")
    path = Path(REPO_DIR) / "data" / "inputs" / file
    cube = iris.load_cube(str(path))
    print(cube)
    cube_extract = extract_timesteps(cube, 2017, 2020)
    print("lllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll")
    print(cube_extract)
    save_netcdf(cube_extract, "EOBS_short.nc")
    print("")

    # file = "tos_O1_2001-2002.nc"
    # path = Path(REPO_DIR) / "data" / "inputs" / file
    # cube = iris.load_cube(str(path))
    # print(cube)
    # print()
    # print(cube.summary)
    # print()
    # print(cube.summary(shorten=True))


# def test_load_cube2d_hadcrut():
#     cube = load_example_cube2d(REPO_DIR, hadcrut_file)
#     print("Testing cube: 2d")
#     print_all(cube, "latitude", "longitude")
#     # Draw the block plot.
#     qplt.pcolormesh(cube)
#     plt.show()

#
#
# def test_load_example_cube3d_tos():
#     cube = load_example_cube3d(REPO_DIR, tos_file)
#     print("Testing cube: 3d")
#     print_all(cube, "latitude", "longitude")
#     # Plotting - not possible via qplt for 3d cubes
#     # Draw the block plot.
#     #qplt.pcolormesh(cube)
#     #plt.show()
#
#
# def test_load_example_cube2d_tos():
#     cube = load_example_cube2d(REPO_DIR, tos_file)
#     print("Testing cube: 2d")
#     print_all(cube, "latitude", "longitude")
#     # Draw the block plot.
#     qplt.pcolormesh(cube)
#     plt.show()
#
#
# def test_load_example_cube3d_tos():
#     cube = load_example_cube3d(REPO_DIR, crutem_file)
#     print("Testing cube: 3d")
#     print_all(cube, "latitude", "longitude")
#     # Plotting - not possible via qplt for 3d cubes
#     # Draw the block plot.
#     #qplt.pcolormesh(cube)
#     #plt.show()
#
#
# def test_load_example_cube2d_tos():
#     cube = load_example_cube2d(REPO_DIR, crutem_file)
#     print("Testing cube: 2d")
#     print_all(cube, "latitude", "longitude")
#     # Draw the block plot.
#     qplt.pcolormesh(cube)
#     plt.show()


# def test_view():
#     file = "tos_O1_2001-2002.nc"
#     print("")
#     print(REPO_DIR)
#     path = Path(REPO_DIR) / "data" / "inputs" / file
#     cube = iris.load_cube(str(path))
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
# first = cube[0]
# print("xxxxxxxxxxxx")
# print(first.shape)
# print(first.ndim)
# print(first)
# last = cube[-1]
# print()
# print(last)

# Take a 1d slice using array style indexing.
# EXPLIAN FURTHER >>>>>>
# slice_1d = first[5, :]
# extract data where latitude = 40, but for all lons
# slice_1d = first[40, :]
# slice_1d = first[:, 0]

# print("slice")
# print(slice_1d)
# print(len(slice_1d.data))
# print()

# print("scalar")
# just the first value for time, lat, lon , so gives one data point
# firstall = cube[0,0,0]
# firstall = cube[2,90,90]  #  is a value...
# print(firstall)
# print("Data:")
# print(firstall.data)
# print(firstall.data.mask)
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
# fig, plt, ax = plot_defaults(1)
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

# lat = first.coord("latitude")
# lon = first.coord("longitude")[0:170]
# print(lat)
# print(lat.points)
# iplt.scatter(lat, lon)
# if using ax from matplotlib, need to use values, not cubes or coords
# ax.scatter(lat.points, lon.points, s=40, c='r', alpha=0.9,
#            transform=ccrs.PlateCarree())


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
