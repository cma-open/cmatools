"""Test combined function."""

from cmatools.combine.combine import combined


def test_combined():
    """Test of combined function."""
    result = combined(2, 3)
    expected = 11  # 11 = sum of product and sum ((2*3) + (2+3))
    assert result == expected
