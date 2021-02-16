""" Test python end to end system
"""

# TODO
# Just a copy of the integration tests for now
# WIP - test passes but is a dummy test, needs replacing


from cmatools.combine.combine import combined


def test_combined():
    """Test of combined function"""

    assert combined() == "this hello cma"
