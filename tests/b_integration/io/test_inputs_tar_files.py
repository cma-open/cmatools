"""Test extracted tarfiles netcdf can be read as a cube."""

import tarfile
from pathlib import Path

import iris

from cmatools.io.io_common import return_datadir_inputs_dir

# TODO - refactor
# TODO add code to deal with file does not exist yet

# change to project ini level value
DEBUG = True

filename = 'eobs.tgz'
outputfilepath = Path(return_datadir_inputs_dir()) / filename


def test_tarfile_read_cubes(tmp_path):
    """Test read in netcdf via iris."""
    with tarfile.open(outputfilepath, 'r') as archive:
        print(f'Archive members: {archive.getmembers()}')
        print(f'Archive names: {archive.getnames()}')
        # For situations where there is only 1 file in the archive
        content_filename = archive.getnames()[0]
        print(f'Content filename: {content_filename}')
        archive.extract(content_filename, path=tmp_path)
        cubes = iris.load(str(tmp_path / content_filename))
        # iris does not deal with pathlib well yet
        print(cubes)
        print(f'Cube type for cubes[0]: {type(cubes[0])}')
        assert isinstance(cubes[0], iris.cube.Cube)
