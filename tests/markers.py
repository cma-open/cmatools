"""Custom markers used across the test suite."""

import os

import pytest

# Test if remote test environment variable is True/False
REMOTE = os.environ.get("REMOTE_TESTS") in ("True", "true")
# Create custom pytest marker, for use elsewhere via decorator
localonly = pytest.mark.skipif(REMOTE, reason="Only runs locally due to API auth")
