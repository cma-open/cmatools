"""Copernicus API access module.

Functions to access data download via the Copernicus API

Notes
-----
See:

    $  https://cds.climate.copernicus.eu/api-how-to

"""


import cdsapi
import humanize

DEBUG = True
"""bool : Debugging level, module constant."""


def copernicus_downloads(dataset: str, content: str, outputfilepath: str) -> None:
    """Wrap api call to download dataset, with options, from Copernicus.

    Parameters
    ----------
    dataset
        The first parameter.
    content
        The second parameter.
    outputfilepath
    """
    c = cdsapi.Client()
    c.retrieve(dataset, content, outputfilepath)
    # Close session after download to prevent ResourceWarning: unclosed socket.socket
    c.session.close()


def copernicus_check_downloads(dataset: str, content: str) -> None:
    """Check api call to dataset, with options, from Copernicus.

    Parameters
    ----------
    dataset
        The first parameter.
    content
        The second parameter.
    """
    c = cdsapi.Client()
    print(f'Request headers: {c.session.headers}')
    result = c.retrieve(dataset, content, target=None)
    print(f'Result content type: {result.content_type}')
    print(f'Result file size: {humanize.naturalsize(result.content_length)}')
    if DEBUG:
        print(result)
    c.session.close()


if __name__ == '__main__':
    pass
