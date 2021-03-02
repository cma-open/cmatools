""" Test python hello world
"""

from cmatools.helloworld import hello_world


def test_hello_world():
    """Test of hello world print function"""

    assert hello_world.hello_world() == "hello cma"
