"""Write selected config settings to disk."""

import configparser
from datetime import datetime
from pathlib import Path

from cmatools.definitions import CONFIGFILE, ROOT_DIR
from cmatools.io.io_common import return_datadir_root_dir

# Read from user-editable config file
config = configparser.ConfigParser()
config.read(CONFIGFILE)
app_env = config.get("APP", "ENVIRONMENT")
datadir_root = config.get("DATADIR", "ROOT")
datadir_inputs = config.get("DATADIR", "INPUTS")
datadir_archives = config.get("DATADIR", "ARCHIVES")
logs_config = config.get("LOGS", "CONFIG")
scratchdir_root = config.get("SCRATCHDIR", "ROOT")

DEBUG = True
"""bool: Debugging level, module constant (Default: True)."""


def write_config():
    """Write elements from config file to disk."""
    log = Path(ROOT_DIR) / logs_config
    if DEBUG:
        print(f"Log: {log}")
    # TODO expand functionality
    # Just POC, to show simple write out to log file
    with open(log, "w") as filehandle:
        filehandle.write(f'Log time: {datetime.now().strftime("%Y-%m-%d %H:%M")}\n')
        filehandle.write(f"App dev stage: {app_env}\n")
        filehandle.write(f"DataDir root: {datadir_root}\n")
        filehandle.write(
            f"DataDir root full: " f"{return_datadir_root_dir(datadir_root)}\n"
        )
        filehandle.write(f"Inputs: {datadir_inputs}\n")
        filehandle.write(f"ScratchDir root: {scratchdir_root}\n")
        if DEBUG:
            filehandle.write(f"Archive: {datadir_archives}\n")
