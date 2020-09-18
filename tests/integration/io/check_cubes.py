
from pathlib import Path
import tarfile

import iris

from cmatools.io.io_common import datadir_inputs_dir
from cmatools.io.io_common import extract_archive_singlefile

# change to project ini level value
DEBUG = True

filename = "eobs.tgz"
outputfilepath = Path(datadir_inputs_dir()) / filename

extracted_file = 'tx_ens_mean_0.25deg_reg_2011-2019_v21.0e.nc'
extractedfilepath = Path(datadir_inputs_dir()) / extracted_file


cubes = iris.load(str(extractedfilepath))[0]
print(cubes)