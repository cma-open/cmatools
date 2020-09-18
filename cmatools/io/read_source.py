import configparser
from cmatools.definitions import ROOT_DIR

config = configparser.ConfigParser()

configfile = f"{ROOT_DIR}/cmatools/config.ini"

class SourceData():

    def __init__(self, service):
        self.service=service
        self.dataset=None
        self.format=None
        #self.format=self.read_input_source_ini(service)


    def read_input_source_ini(self):
        """Read input sources from the ini file"""

        config.read(configfile)

        if self.service == 'COP':

            self.dataset = config.get("SOURCES", "COP_DATASET")
            self.format = config.get("SOURCES", "COP_FORMAT")
            product_type = config.get("SOURCES", "COP_PRODUCT_TYPE")
            variables = config.get("SOURCES", "COP_VARIABLES")
            grid_res = config.get(("SOURCES"), "COP_GRID_RES")
            period = config.get("SOURCES", "COP_PERIOD")
            version = config.get("SOURCES", "COP_VERSION")

