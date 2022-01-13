"""Copernicus API access module.

Functions to access data download via the Copernicus API

Notes
-----
See:

    $  https://cds.climate.copernicus.eu/api-how-to

"""

from pathlib import Path

import cdsapi
import humanize

DEBUG = True
"""bool : Debugging level, module constant."""


def copernicus_downloads(
    dataset: str, content: dict[str, any], outputfilepath: Path
) -> None:
    """Wrap api call to download dataset, with options, from Copernicus.

    Parameters
    ----------
    dataset
        The first parameter.
    content
        The second parameter.
    outputfilepath
        Path to output location.
    """
    c = cdsapi.Client()
    c.retrieve(dataset, content, outputfilepath)
    # Close session after download to prevent ResourceWarning: unclosed socket.socket
    c.session.close()


def copernicus_check_downloads(dataset: str, content: dict[str, any]) -> None:
    """Check api call to dataset, with options, from Copernicus.

    Parameters
    ----------
    dataset
        The first parameter.
    content
        The second parameter.
    """
    c = cdsapi.Client()
    print(f"Request headers: {c.session.headers}")
    result = c.retrieve(dataset, content, target=None)
    print(f"Result content type: {result.content_type}")
    print(f"Result file size: {humanize.naturalsize(result.content_length)}")
    if DEBUG:
        print(result)
    c.session.close()


if __name__ == "__main__":
    pass
