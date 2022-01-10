"""Tests for the write config module."""

# TODO add module ref to link in docs

from unittest.mock import patch

from cmatools.common import write_config

# use mock to test that the write config function writes to disk


def test_write_config(tmp_path):
    """Test that config writes to disk."""
    # Create subdir in temp dir
    d = tmp_path / "logs"
    d.mkdir()
    # Patch ROOT_DIR, at point it is used, to write to a known temp dir
    with patch("cmatools.common.write_config.ROOT_DIR", tmp_path):
        assert (tmp_path / "logs" / "config.log").exists() is False
        write_config.write_config()
    assert len(list(tmp_path.iterdir())) == 1
    assert (tmp_path / "logs" / "config.log").exists()
    assert (tmp_path / "logs" / "config.log").is_file()
