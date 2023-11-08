"""Load canned (static) cube data for tests and example use."""

# create cubes from range of data sources

# simple
# from arrays
# from csv?
# from dataframe

# maximum use of visualisation .....

from pathlib import Path

import humanize
import iris
import numpy as np
from iris.coord_systems import Mercator

#    (
#    GeogCS,
#    LambertAzimuthalEqualArea,
#    LambertConformal,
#    Mercator,
#    RotatedGeogCS,
#    Stereographic,
#    TransverseMercator,
# )
from iris.coords import DimCoord
from iris.cube import Cube

# from cmatools.data_creation.arrays import data_array_sample
from cmatools.definitions import REPO_DIR

CRUTEM = "CRUTEM.5.0.0.0.anomalies.nc"
tos_file = "tos_O1_2001-2002.nc"
hadcrut_file = "HadCRUT.5.0.1.0.analysis.anomalies.ensemble_mean.nc"
HADCRUT = "HadCRUT.5.0.1.0.analysis.anomalies.ensemble_mean.nc"


def file_sizes(files: list, directory: Path) -> dict:
    """Report file sizes."""
    file_report = {}
    for file in files:
        filepath = Path(directory) / file
        file_size = filepath.stat().st_size
        human_file_size = humanize.naturalsize(file_size)
        # print(f"File: {file},  size: {humanize.naturalsize(file_size)}")
        file_report[file] = human_file_size
    return file_report


def load_example_cube3d(dir, file):
    """Load example cube 3d."""
    print(f"Loading file: {file}")
    path = Path(dir) / "data" / "inputs" / file
    cube = iris.load_cube(str(path))
    return cube


def load_example_cube2d(dir, file):
    """Load example cube 2d."""
    print(f"Loading file: {file}")
    path = Path(dir) / "data" / "inputs" / file
    cube = iris.load_cube(str(path))
    # index a cube to subset, input cube is 3d time, lat, lon
    # get the first element of the first dimension (time) (+ every other dimension)
    # therefore returns the cube for one single time step
    # time moves to be a scalar coord and the cube is then 2d
    cube2d = cube[0]
    return cube2d


def load_3dcube_crutem():
    """Load 3d cube crutem."""
    print(f"Loading file: {CRUTEM}")
    path = Path(REPO_DIR) / "data" / "inputs" / CRUTEM
    cube = iris.load_cube(str(path))
    return cube


def load_3dcube_hadcrut():
    """Load 3d cube hadcrut."""
    print(f"Loading file: {HADCRUT}")
    path = Path(REPO_DIR) / "data" / "inputs" / HADCRUT
    cube = iris.load_cube(str(path))
    return cube


def extract_timesteps(cube, start_year, end_year):
    """Extract timesteps."""
    """Extract last n timesteps from a 3d + cube"""
    # Constrain the period by year, and extract the data
    constraint = iris.Constraint(
        time=lambda cell: start_year <= cell.point.year <= end_year
    )
    new_cube = cube.extract(constraint)
    return new_cube


def save_netcdf(cube: Cube, output_name):
    """Save netcdf."""
    filepath = Path(REPO_DIR) / "data" / "inputs" / output_name
    iris.save(cube, filepath)


# load and view one of the test data cubes to view it !
# maybe extract and load sample of data from the sample cube?


def _mercator_cube(self, ellipsoid=None):
    """Mercator cube."""
    data = np.arange(12).reshape(3, 4)
    cube = Cube(data, "air_pressure_anomaly")
    merc = Mercator(49.0, ellipsoid)
    coord = DimCoord(
        np.arange(3), "projection_y_coordinate", units="m", coord_system=merc
    )
    cube.add_dim_coord(coord, 0)
    coord = DimCoord(
        np.arange(4), "projection_x_coordinate", units="m", coord_system=merc
    )
    cube.add_dim_coord(coord, 1)
    return cube
