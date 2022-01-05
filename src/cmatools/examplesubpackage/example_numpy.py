# -*- coding: utf-8 -*-

"""Example NumPy style docstrings.

This module demonstrates documentation as specified by the `NumPy
Documentation HOWTO`_. Docstrings may extend over multiple lines. Sections
are created with a section header followed by an underline of equal length.

Example
-------
Examples can be given using either the ``Example`` or ``Examples``
sections. Sections support any reStructuredText formatting, including
literal blocks::

    $ python example_numpy.py


Section breaks are created with two blank lines. Section breaks are also
implicitly created anytime a new section starts. Section bodies *may* be
indented:

Notes
-----
    This is an example of an indented section. It's like any other section,
    but the body is indented to help it stand out from surrounding text.

If a section is indented, then a section break is created by
resuming unindented text.

This file source:
https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html#example-numpy
See also notes in the wiki  https://github.com/cma-open/cmatools/wiki/Naming-conventions

    This file has been added to and amended to include code style examples and
    further functional code, so the module can be well covered by tests

Attributes
----------
module_level_variable1 : int
    Module level variables may be documented in either the ``Attributes``
    section of the module docstring, or in an inline docstring immediately
    following the variable.

    Either form is acceptable, but the two should not be mixed. Choose
    one convention to document module level variables and be consistent
    with it.

CONSTANT : int
    Module constants are capitalised by convention and may be useful to distinguish
    from module level variables

DEBUG : bool
    The debug print status set for the module


.. _NumPy Documentation HOWTO:
   https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt

"""

DEBUG = True

CONSTANT = 21

module_level_variable1 = 12345

module_level_variable2 = 98765
"""int: Module level variable documented inline.

The docstring may span multiple lines. The type may optionally be specified
on the first line, separated by a colon.
"""


def function_with_types_in_docstring(param1, param2):
    """Compare if param1 is greater than param2.

    Example function with types documented in the docstring.

    Function tests if param1 is greater than param2 (True) otherwise
    returns False.

    `PEP 484`_ type annotations are supported. If attribute, parameter, and
    return types are annotated according to `PEP 484`_, they do not need to be
    included in the docstring:

    Parameters
    ----------
    param1 : int
        The first parameter.
    param2 : str
        The second parameter.

    Returns
    -------
    bool
        True if successful, False otherwise.

    .. _PEP 484:
        https://www.python.org/dev/peps/pep-0484/

    """
    result = None
    try:
        converted_param2 = int(param2)
        if param1 > converted_param2:
            result = True
        else:
            result = False
    except ValueError:
        print('Parameter 2 must be a string representing a number using digits [0-10]')
        raise ValueError
    except TypeError:
        print('Parameter 1 must be an integer')
        raise TypeError
    print(f'Function called with: {param1} and {param2}')
    print(f'Function returns: {result}')
    return result


def function_with_pep484_type_annotations(param1: int, param2: str) -> bool:
    """Compare if param1 is greater than param2.

    Example function with PEP 484 type annotations.

    The return type must be duplicated in the docstring to comply
    with the NumPy docstring style.

    Parameters
    ----------
    param1
        The first parameter.
    param2
        The second parameter.

    Returns
    -------
    bool
        True if successful, False otherwise.

    """
    result = None
    try:
        converted_param2 = int(param2)
        if param1 > converted_param2:
            result = True
        else:
            result = False
    except ValueError:
        print('Parameter 2 must be a string representing a number using digits [0-10]')
        raise ValueError
    except TypeError:
        print('Parameter 1 must be an integer')
        raise TypeError
    print(f'Function called with: {param1} and {param2}')
    print(f'Function returns: {result}')
    return result


def module_level_function(param1, param2=None, *args, **kwargs):
    """Evaluate to true if any paramaters are greater than 100.

    This is an example of a module level function.

    Function parameters should be documented in the ``Parameters`` section.
    The name of each parameter is required. The type and description of each
    parameter is optional, but should be included if not obvious.

    This example function calculates if any of the params are greater than
    a target value of 100, and if so returns True

    If *args or **kwargs are accepted,
    they should be listed as ``*args`` and ``**kwargs``.

    The format for a parameter is::

        name : type
            description

            The description may span multiple lines. Following lines
            should be indented to match the first line of the description.
            The ": type" is optional.

            Multiple paragraphs are supported in parameter
            descriptions.

    Parameters
    ----------
    param1 : int
        The first parameter.
    param2 : :obj:`str`, optional
        The second parameter.
    *args
        Variable length argument list.
    **kwargs
        Arbitrary keyword arguments.

    Returns
    -------
    bool
        True if successful, False otherwise.

        The return type is not optional. The ``Returns`` section may span
        multiple lines and paragraphs. Following lines should be indented to
        match the first line of the description.

        The ``Returns`` section supports any reStructuredText formatting,
        including literal blocks::

            {
                'param1': param1,
                'param2': param2
            }

    Raises
    ------
    AttributeError
        The ``Raises`` section is a list of all exceptions
        that are relevant to the interface.
    ValueError
        If `param2` is equal to `param1`.
    ValueError
        If `param2` is not a string
    """
    if param1 == param2:
        print(f'param1: {param1}, param2: {param2}')
        error_message = 'param1 may not be equal to param2'
        print(error_message)
        raise ValueError(error_message)
    # Collect the params and find the max value
    value_list = []
    value_list.append(param1)
    if param2:
        if type(param2) != str:
            error_message = 'param2 must be a string'
            print(error_message)
            raise ValueError(error_message)
        else:
            converted_param2 = int(param2)
            value_list.append(converted_param2)

    if args:
        for x in args:
            if type(x) != int:
                error_message = 'args values must be integers'
                print(error_message)
                raise ValueError(error_message)
            value_list.append(x)
    if kwargs:
        print('Metadata content')
        for key, value in kwargs.items():
            print(f'{key}: {value}')
            if key == 'verbose' and value is True:
                print('Additional verbose output: ......................')

    # Find max value from the compiled list
    max_value = max(value_list)
    print(
        f'param1: {param1}, param2: {param2}, args: {args}, '
        f'kwargs: {kwargs}. Max value: {max_value}'
    )

    # Function returns True if any of the params are greater than 100
    target_value = 100
    if max_value > target_value:
        return True
    else:
        return False


def example_generator(n):
    """Yield next number.

    Generators have a ``Yields`` section instead of a ``Returns`` section.

    Parameters
    ----------
    n : int
        The upper limit of the range to generate, from 0 to `n` - 1.

    Yields
    ------
    int
        The next number in the range of 0 to `n` - 1.

    Raises
    ------
        The ``Raises`` section is a list of all exceptions
        that are relevant to the interface.
    TypeError
        If `n` is not an integer

    Examples
    --------
    Examples should be written in doctest format, and should illustrate how
    to use the function.

    >>> print([i for i in example_generator(4)])
    [0, 1, 2, 3]

    """
    try:
        for i in range(n):
            yield i
    except TypeError as err:
        print('n must be an integer')
        raise err


class ExampleError(Exception):
    """Exceptions are documented in the same way as classes.

    The __init__ method may be documented in either the class level
    docstring, or as a docstring on the __init__ method itself.

    Either form is acceptable, but the two should not be mixed. Choose one
    convention to document the __init__ method and be consistent with it.

    Parameters
    ----------
    msg : str
        Human readable string describing the exception.
    code : :obj:`int`, optional
        Numeric error code.

    Attributes
    ----------
    msg : str
        Human readable string describing the exception.
    code : int
        Numeric error code.

    """

    def __init__(self, msg, code=None):
        self.msg = msg
        self.code = code

    # def __str__(self):
    #   return f'{self.msg}, {self.code}'


class ExampleClass(object):
    """The summary line for a class docstring should fit on one line.

    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration (see __init__ method below).

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes
    ----------
    attribute_string : :obj:`str`
        Description of `attribute_string`.
    attribute_list : :obj:`int`, optional
        Description of `attr2`.

    """

    # TODO - decide which init documentation method to follow
    # params in class docstring, or under init?

    def __init__(self, param1, param2, param3):
        """Docstring on the __init__ method.

        The __init__ method may be documented in either the class level
        docstring, or as a docstring on the __init__ method itself.

        Either form is acceptable, but the two should not be mixed. Choose one
        convention to document the __init__ method and be consistent with it.

        Parameters
        ----------
        param1 : str
            Description of `param1`.
        param2 : :obj:`list` of :obj:`str`
            Description of `param2`. Multiple
            lines are supported.
        param3 : :obj:`int`, optional
            Description of `param3`.

        """
        self.attribute_string = param1
        self.attribute_list = param2
        self.attribute_integer = param3  #: Doc comment *inline* with attribute

        #: list of str: Doc comment *before* attribute, with type specified
        self.attr4 = ['attr4']

        self.attr5 = None
        """str: Docstring *after* attribute, with type specified."""

    @property
    def attribute_string(self):
        """Get the attribute string.

        Getting or setting the attribute string value will verify the value
        is a string.
        """
        return self._attribute_string

    @attribute_string.setter
    def attribute_string(self, value):
        if type(value) != str:
            raise TypeError('param1 must be a string')
        self._attribute_string = value

    @property
    def attribute_list(self):
        """Get the attribute list.

        Getting or setting the attribute list value will verify the value
        is a list of strings.
        """
        return self._attribute_list

    @attribute_list.setter
    def attribute_list(self, value):
        if type(value) != list:
            raise TypeError('param2 must be a list of strings')
        else:
            for element in value:
                if type(element) != str:
                    raise TypeError('param2 must be a list of strings')
        self._attribute_list = value

    @property
    def attribute_integer(self):
        """Get the attribute integer.

        Getting or setting the attribute integer value will verify the value
        is an integer.
        """
        return self._attribute_integer

    @attribute_integer.setter
    def attribute_integer(self, value):
        if type(value) != int:
            raise TypeError('param3 must be an integer')
        self._attribute_integer = value

    @property
    def readonly_property(self):
        """str: Get readonly_property.

        Properties should be documented in their getter method.
        """
        return 'readonly_property'

    def example_method(self, param1, param2):
        """Class methods are similar to regular functions.

        Parameters
        ----------
        param1
            The first parameter.
        param2
            The second parameter.

        Returns
        -------
        bool
            True if successful, False otherwise.
        """
        return True

    def __special__(self):
        """By default special members with docstrings are not included.

        Special members are any methods or attributes that start with and
        end with a double underscore. Any special member with a docstring
        will be included in the output, if
        ``napoleon_include_special_with_doc`` is set to True.

        This behavior can be enabled by changing the following setting in
        Sphinx's conf.py::

            napoleon_include_special_with_doc = True

        """
        pass

    def __special_without_docstring__(self):  # noqa: D105
        pass

    def _private(self):
        """By default private members are not included.

        Private members are any methods or attributes that start with an
        underscore and are *not* special. By default they are not included
        in the output.

        This behavior can be changed such that private members *are* included
        by changing the following setting in Sphinx's conf.py::

            napoleon_include_private_with_doc = True

        """
        pass

    def _private_without_docstring(self):
        pass


if __name__ == '__main__':

    print('Running example numpy module')
    print(f'DEBUG constant set to: {DEBUG}')

    function_with_types_in_docstring(1, 2)
    function_with_types_in_docstring(1, 'test')
