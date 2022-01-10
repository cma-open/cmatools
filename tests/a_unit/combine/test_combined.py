"""Test combined function."""

from unittest.mock import patch

from cmatools.combine.combine import combined


@patch("cmatools.combine.combine.analysis_product")
@patch("cmatools.combine.combine.analysis_sum")
def test_combined(mock_sum, mock_product):
    """Test of combined function."""
    mock_sum.return_value = 4
    mock_product.return_value = 4
    # Call combined function. Note the arg values are ignored because
    # the functions within combined have been mocked
    result = combined(2, 3)
    # analysis_product will return 4, analysis_sum will return 4
    expected = 8  # 8 = the sum of mocks ( 4 + 4)
    assert result == expected
