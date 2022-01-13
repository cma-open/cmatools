"""Tests for the definitions module."""

from pathlib import Path
from unittest.mock import patch

from cmatools.definitions import (
    CONFIGFILE,
    CONFIGLOGS,
    PACKAGE,
    ROOT_DIR,
    SRC_DIR,
    main,
)

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


# Mock out the unknowable values
def test_main(capsys):
    """Test main prints constants to stdout."""
    with patch("cmatools.definitions.SRC_DIR", "test_src_path"):
        with patch("cmatools.definitions.ROOT_DIR", "test_root_path"):
            with patch("cmatools.definitions.CONFIGFILE", "test_file"):
                main()
                captured = capsys.readouterr()
                expected = (
                    "Source dir: test_src_path\nRoot dir: "
                    "test_root_path\nConfig file: test_file\n"
                )
                assert captured.out == expected
