"""Tests for the definitions module."""

from pathlib import Path

from cmatools.definitions import CONFIGFILE, CONFIGLOGS, PACKAGE, ROOT_DIR, SRC_DIR

DEBUG = True
"""bool: Debugging module-level constant (Default: True)."""


def test_definitions():
    """Test definitions module."""
    assert PACKAGE == "cmatools"
    assert isinstance(SRC_DIR, str)
    assert isinstance(ROOT_DIR, str)
    assert Path(CONFIGFILE).is_file()
    assert Path(CONFIGLOGS).is_file()
    if DEBUG:
        print(f"Source dir: {SRC_DIR}")
        print(f"Root dir: {ROOT_DIR}")
