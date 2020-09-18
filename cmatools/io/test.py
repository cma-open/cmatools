from pathlib import Path

import cdsapi

from cmatools.io.read_source import SourceData
from cmatools.io.io_common import datadir_inputs

filename = "eobs.tgz"
outputfilepath = Path(datadir_inputs) / filename

print(outputfilepath)