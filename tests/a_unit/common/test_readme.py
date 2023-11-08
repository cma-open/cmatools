"""Tests for readme module."""

from pathlib import Path

from cmatools.common.readme import add_readme

DEBUG = False


def test_readme(tmp_path):
    """Test readme."""
    content = "Text within the readme file."
    add_readme(tmp_path, content)

    readme_file = Path(tmp_path) / "readme.txt"
    assert readme_file.is_file()
    with open(readme_file) as open_readme:
        readme_content = open_readme.read()
        assert readme_content == content
        if DEBUG:
            print(f"File readme exists: {readme_file.is_file()}")
            print(f"Content: {readme_content}")
