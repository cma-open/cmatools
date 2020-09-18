# outdated - check then delete


from pathlib import Path
import tarfile

import iris

from cmatools.io.io_common import extract_archive_singlefile

# change to project ini level value
DEBUG = True


from cmatools.io.io_common import datadir_inputs_dir
filename = "eobs.tgz"
outputfilepath = Path(datadir_inputs_dir()) / filename


with tarfile.open(outputfilepath, 'r') as archive:
    print(archive.getmembers())
    print(archive.list(verbose=False))
    content_filename = archive.list(verbose=False)

    # for situation where there is only 1 file in the archive
    # open as a file-like object, in memory
    fileobj = archive.extractfile(content_filename)
    cubes = iris.load(fileobj)
    print(cubes)