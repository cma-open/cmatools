"""Descriptive readme file creation."""

from pathlib import Path
from typing import Union


def add_readme(destination: Union[Path, str], content: str) -> None:
    """Write readme file to disk, with supplied text content.

    Parameters
    ----------
    destination
        Location directory on disk to write readme file.
    content
        Text string content to write into the readme file.

    """
    filepath = Path(destination) / "readme.txt"
    with open(filepath, "w") as readme:
        readme.write(content)
