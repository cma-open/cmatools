"""Example data analysis module - creating output data in netcdf format."""

# Initially for use so the system tests have some netcdf output data to test
# Later to expand into sections for data input, processing, outputs for an analysis run
# 1. initially just set a named CF standards version,
# and ensure that is kept in the output file
# 2. run analysis that take a user set year date range setting to customise output


# TODO
# modify - just need to create a simple cube from code, simple cube, out as netcdf
# create simple csv from file
# use report and validate to check contents
# then expand to use a ref source file to build metadata and content for the cube/netcdf
# possibly link to simple plot for early visualisation ?????


# import standard library imports
from pathlib import Path

# import third party imports
import iris

# import local app / lib
from cmatools.definitions import REPO_DIR

sea_temp = "tos_O1_2001-2002.nc"
sea_temp_file = Path(REPO_DIR) / "data" / "inputs" / sea_temp
copy_file = Path(REPO_DIR) / "data" / "outputs" / "tos_copy.nc"
output_file = Path(REPO_DIR) / "data" / "outputs" / "tos_output_cf_original.nc"
updated_file = Path(REPO_DIR) / "data" / "outputs" / "tos_output_cf_updated.nc"


def load_object_and_save(source, output_file, convention=None, override=None):
    """Load cube from source and save to file."""
    # Use string as iris cant deal with PosixPath
    cubes = iris.load_cubes(str(source))
    # Extract the first cube from cubelist
    cube = cubes[0]
    if override:
        # Set iris config so that CF conventions metadata are
        # updated in the output file, from input cube metadata
        iris.config.netcdf.conventions_override = True
    if convention:
        # Update metadata in the loaded cube
        cube.attributes["Conventions"] = convention
    # Save to a netcdf file
    iris.save(cube, str(output_file))


def load_and_save(source_file, output_file, convention=None, override=None):
    """Load and save."""
    # Use string as iris cant deal with PosixPath
    cubes = iris.load_cubes(str(source_file))
    # Extract the first cube from cubelist
    cube = cubes[0]
    if override:
        # Set iris config so that CF conventions metadata are updated
        # in output file, from cube metadata
        iris.config.netcdf.conventions_override = True
    if convention:
        # Update metadata in the loaded cube
        cube.attributes["Conventions"] = convention
    # Save to a netcdf file
    iris.save(cube, str(output_file))


def verify_cube_metadata(*args):
    """Verify cube metadata."""
    # convert to strings
    files = []
    for arg in args:
        file = str(arg)
        files.append(file)
    # load and view the output files
    # cubes = iris.load(str(args))
    cubes = iris.load(files)
    print(cubes)

    print("----------------------- output files -------------------------------")

    for cube in cubes:
        print(cube)
        print("------------------------------------------------------")


def main():
    """Load and save data, print and verify metadata."""
    # load and save a netcdf with no override or modification of metadata
    load_and_save(sea_temp_file, copy_file)
    # load and save a netcdf with  override and with no modification of metadata
    load_and_save(sea_temp_file, output_file, override=True)
    # load and save a netcdf with override and with modification of metadata
    load_and_save(sea_temp_file, updated_file, convention="CF-999", override=True)

    print(copy_file)
    #
    verify_cube_metadata(copy_file, output_file, updated_file)


if __name__ == "__main__":
    # Runs when called as main
    main()


# TODO developer notes
# initially a simple script
# then move to use the config scripts for data dir output
# then change to use small range of input for the analysis
# when saved out to a new netcdf and checked,
# the CF of the file typically matches the version used by Iris
# in order to retain original update, or set the CF conventions
# in the output data, need to use iris config
