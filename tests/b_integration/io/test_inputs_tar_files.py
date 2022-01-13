"""Test extracted tarfiles netcdf can be read as a cube."""

import tarfile
from pathlib import Path

import iris

from cmatools.definitions import ROOT_DIR

# TODO - refactor
# TODO add code to deal with file does not exist yet

# change to project ini level value
DEBUG = True

filename = "hadcrut_example.tar.gz"
canned_data = f"{ROOT_DIR}/tests/_data"
test_data_file = Path(canned_data) / filename


def test_tarfile_read_cubes(tmp_path):
    """Test read in netcdf via iris."""
    with tarfile.open(test_data_file, "r") as archive:
        print(f"Archive members: {archive.getmembers()}")
        print(f"Archive names: {archive.getnames()}")
        # For situations where there is only 1 file in the archive
        content_filename = archive.getnames()[0]
        print(f"Content filename: {content_filename}")
        archive.extract(content_filename, path=tmp_path)
        # iris does not deal with pathlib well yet, convert to string
        cubes = iris.load(str(tmp_path / content_filename))
        print(cubes)
        print(f"Cube type for cubes[0]: {type(cubes[0])}")
        assert isinstance(cubes[0], iris.cube.Cube)
