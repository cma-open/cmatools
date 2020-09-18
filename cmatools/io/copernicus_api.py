# https://cds.climate.copernicus.eu/api-how-to


from pathlib import Path

import cdsapi

from cmatools.io.read_source import SourceData
from cmatools.io.io_common import (datadir_inputs_dir,
    datadir_archives_dir, extract_archive_singlefile)


DEBUG = True

def copernicus_downloads(dataset, content, outputfilepath):

    """Function to wrap api call to download dataset, with options, from Copernicus"""

    c = cdsapi.Client()
    c.retrieve(dataset, content, outputfilepath)
    # Close session after download to prevent ResourceWarning: unclosed socket.socket
    c.session.close()

def copernicus_check_downloads(dataset, content, outputfilepath):

    """Function to wrap api call to download dataset, with options, from Copernicus"""

    c = cdsapi.Client()


    print(type(c))
    print(dir(c))
    print(c.metadata)
    print(c.session.headers)
    #print(c.session.headers["content-length"])
    this=c.retrieve(dataset, content, outputfilepath).headers['content-length']

    print(this)
    # Close session after download to prevent ResourceWarning: unclosed socket.socket
    #c.session.close()
    help(c)


if __name__ == '__main__':
    # Runs entry point function when called as main

    inputs = SourceData('COP')
    inputs.read_input_source_ini()

    if DEBUG:
        print(inputs)
        print(type(inputs))
        print(dir(inputs))
        print(inputs.service)
        print(inputs.dataset)
        #print(inputs.dataset)

    dataset = inputs.dataset
    content =   {
        'format': inputs.format,
        'product_type': 'ensemble_mean',
        'variable': [
            'maximum_temperature',
        ],
        'grid_resolution': '0.25deg',
        'period': '2011_2019',
        'version': '21.0e',
    }
    filename = "eobs.tgz"
    outputfilepath = Path(datadir_archives_dir()) / filename

    print(outputfilepath)
    #copernicus_check_downloads(dataset=dataset, content=content, outputfilepath=outputfilepath)
    copernicus_downloads(dataset=dataset, content=content, outputfilepath=outputfilepath)

    # extract the file to netcdf
    extract_archive_singlefile(filename)
