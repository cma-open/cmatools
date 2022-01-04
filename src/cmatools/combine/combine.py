"""Example module containing functions to illustrate integration testing."""

from cmatools.analysis.simple_analysis import analysis_product, analysis_sum


def combined(x, y):
    """Sum of output from calling two functions."""
    combined = analysis_product(x, y) + analysis_sum(x, y)
    return combined
