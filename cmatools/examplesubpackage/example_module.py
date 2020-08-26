# module comments
# docstrings

""" Example module showing codestyle defaults

A range of codestyle examples are shown including x, y, z,
List the classes, exceptions and functions (and any other objects)
that are exported by the module, with a one-line summary of each.
Todo: Review content

"""

# import stand library imports
# import standard

# import third party imports
# import thirdparty

# import local app / lib imports
# import app


CONSTANT = 21
CONSTANT_ALT = 55


# class definitions surrounded by two blank lines
# top level function surrounded by two blank lines

# single blank lines around method definitions


def top_level_function(indate):
    """ A simple example function (one line summary)

    Further details, notes examples and param detail
    summarize behavior
    document arguments, return value(s), side effects, exceptions raised,
    and restrictions on when it can be called (all if applicable)
    Optional arguments should be indicated.
    Document whether keyword arguments are part of the interface.

    Args:
       indate (int) : input data as integer

    Returns:
       outdate (int): The return value as integer
    """

    outdate = indate + 1
    return outdate


class ExampleClass:
    """ One line class summary

    Summarize class behaviour and list the public methods and instance variables.
    If the class is intended to be subclassed, and has an additional interface for subclasses,
    this interface should be listed separately (in the docstring).
    The class constructor should be documented in the docstring for its __init__ method.
    """

    def __init__(self, name, form):
        """ One line summary
        Document the class constructor

        """

        self.name = name
        self.form = form

    def addfunction(self):
        """  A simple example function (one line summary)
        Further details, notes examples and param detail
        summarize behavior
        document arguments, return value(s), side effects, exceptions raised,
        and restrictions on when it can be called (all if applicable)
        Optional arguments should be indicated.
        Document whether keyword arguments are part of the interface.
        """

        calc = 1 + 1
        return calc