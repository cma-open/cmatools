"""Read values from user editable configuration file."""

import configparser

from cmatools.definitions import SRC_DIR

config = configparser.ConfigParser()

# Set path to user edited config file
configfile = f'{SRC_DIR}/cmatools/config.ini'
# Not supplied with docstring so filepath is not visible in sphinx docs


class SourceData:
    """Class to read config values from ini file based on selected user options.

    A simple interface to get values from the user editable configuration file, based
     on selections made by the user.Used by the command line interface (CLI) tool
     for data download.

    Parameters
    ----------
    service : str
        Service name of the data download server. Possible selections are set within
        :func:`cmatools.cli_data_download.cli_parser`.
    dataset : str
        Dataset name to be downloaded. Possible selections are set within
        :func:`cmatools.cli_data_download.cli_parser`.


    Attributes
    ----------
    service : str
        Data download service name
    dataset : str
        Dataset name to be downloaded
    """

    def __init__(self, service, dataset):
        self.service = service
        self.dataset = dataset
        self.long = None
        self.format = None
        self.server = None
        self.filename = None
        self.path = None
        self.download = None
        self.product_type = None
        self.variables = None
        self.grid_res = None
        self.period = None
        self.version = None

    def read_input_source_ini(self):
        """Read input sources from the ini config file."""
        config.read(configfile)

        if self.service == 'COP':
            if self.dataset == 'E-OBS':
                self.long = config.get('COP', 'COP_DATASET')

            self.format = config.get('COP', 'COP_FORMAT')
            self.product_type = config.get('COP', 'COP_PRODUCT_TYPE')
            self.variables = config.get('COP', 'COP_VARIABLES')
            self.grid_res = config.get(('COP'), 'COP_GRID_RES')
            self.period = config.get('COP', 'COP_PERIOD')
            self.version = config.get('COP', 'COP_VERSION')

        if self.service == 'CEDA':
            self.server = config.get('CEDA', 'SERVER')
            if self.dataset == 'CRUTEM':
                self.filename = config.get('CEDA', 'CRUTEM_FILENAME')
                self.path = config.get('CEDA', 'CRUTEM_PATH')
            if self.dataset == 'HADCRUT':
                self.filename = config.get('CEDA', 'HADCRUT_FILENAME')
                self.path = config.get('CEDA', 'HADCRUT_PATH')

        if self.service == 'HADOBS':
            self.server = config.get('HADOBS', 'SERVER')
            if self.dataset == 'CRUTEM':
                self.filename = config.get('HADOBS', 'CRUTEM_FILENAME')
                self.path = config.get('HADOBS', 'CRUTEM_PATH')
            if self.dataset == 'HADCRUT':
                self.filename = config.get('HADOBS', 'HADCRUT_FILENAME')
                self.path = config.get('HADOBS', 'HADCRUT_PATH')

        # Set full download path to file
        self.download = f'{self.server}{self.path}{self.filename}'

    def validate(self):
        """Validate the ini config file values."""
        # Not used
        pass
