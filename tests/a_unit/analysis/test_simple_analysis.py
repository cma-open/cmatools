"""Test the simple analysis module."""

from cmatools.analysis.simple_analysis import (
    analysis_max,
    analysis_product,
    analysis_sum,
)

# TODO consider label by test type (unit, integration etc), remove dirs


def test_analysis_product():
    """Test analysis product."""
    result = analysis_product(2, 5)
    expected = 10  # 2 * 5
    assert result == expected


def test_analysis_sum():
    """Test analysis sum."""
    result = analysis_sum(2, 5)
    expected = 7  # 2 + 5
    assert result == expected


def test_analysis_max():
    """Test analysis maximum."""
    result = analysis_max(2, 5)
    expected = 5  # 5 > 2
    assert result == expected
