"""Create example cube data for test and example use."""

# create cubes from range of data sources

# simple
# from arrays
# from csv?
# from dataframe

# maximum use of visualisation .....

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

from cmatools.data_creation.arrays import data_array_sample


def create_simple_cube():
    """Create simple cube."""
    sample_array = data_array_sample(150)
    cube = Cube(sample_array)
    return cube


def create_example_cube3d():
    """Create example cube 3d."""
    # TODO add
    pass


def create_example_cube2d():
    """Create example cube 2d."""
    # TODO add
    pass


# load and view one of the test data cubes to view it !
# maybe extract and load sample of data from the sample cube?


def _mercator_cube(ellipsoid=None):
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
