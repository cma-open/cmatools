# -*- coding: utf-8 -*-

"""NumPy style docstrings adapted to highlight the selected CMATOOLS style.

This module demonstrates documentation as specified by the `NumPy
Documentation HOWTO`_. Docstrings may extend over multiple lines. Sections
are created with a section header followed by an underline of equal length.

Example
-------
Examples formatting, including
literal blocks::

    $ python example_cmatools.py


Section breaks are created with two blank lines. Section breaks are also
implicitly created anytime a new section starts. Section bodies *may* be
indented:

Notes
-----
    This is an example of an indented section. It's like any other section,
    but the body is indented to help it stand out from surrounding text.

If a section is indented, then a section break is created by resuming
unindented text. See also notes in the wiki:
https://github.com/cma-open/cmatools/wiki/Naming-conventions

This file has been amended to include code style examples and further functional
code, so the module is well covered by tests.

See:

- :ref:`numpydoc:example`

- :ref:`numpydoc:format`

- :doc:`numpy:docs/howto_document`


"""

# standard library imports
from importlib.metadata import version

# third party imports
import numpy

# local app / lib imports
from cmatools.definitions import PACKAGE

# Document module level variables and constant with docstrings
# following the variable, not before.

DEBUG = True
"""int: Module level constant documented inline (Default: True)."""
CONSTANT = 21
"""int: Module level constant documented inline (Default: 21)."""
module_level_variable1 = 12345
"""int: Module level variable documented inline."""
module_level_variable2 = 98765
"""int: Module level variable documented inline.

The docstring may span multiple lines. The type may optionally be specified
on the first line, separated by a colon.
"""

# cmatools code style will use main module level docstring (after attribute)


def confirm_version() -> None:
    """Print package and numpy version numbers."""
    print(f'Numpy version: {numpy.__version__}')
    print(f'Package version: {PACKAGE} - {version(PACKAGE)}')


def function_with_pep484_type_annotations(param1: int, param2: str) -> bool:
    """Compare if param1 is greater than param2.

    Example function with PEP 484 type annotations.

    `PEP 484`_ type annotations are supported. If attribute, parameter, and
    return types are annotated according to `PEP 484`_, they do not need to be
    included in the docstring:

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

    Raises
    ------
    ValueError
        If `param2` is not a `str`.
    TypeError
        If `param1` is not an `int`
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


def module_level_function(param1, param2=None, *args, **kwargs) -> bool:
    """Verify is any parameter is greater than 100.

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

    Notes
    -----
    There is no distinction between positional and named params,
    but parameters can be noted within the docstring as optional.

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
        # check type
        if not isinstance(param2, str):
            error_message = 'param2 must be a string'
            print(error_message)
            raise ValueError(error_message)
        else:
            converted_param2 = int(param2)
            value_list.append(converted_param2)

    if args:
        for x in args:
            # check type
            if not isinstance(x, int):
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
    """Yield the next number.

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


class ExampleCMAError(Exception):
    """Example error class.

    Exceptions are documented in the same way as classes.

    The __init__ method should be documented in the class level
    docstring.

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
    coded_message : str
        The human readable string describing the exception, prefixed by the
        error code, as a string.

    Notes
    -----
    Do not include the `self` parameter in the ``Parameters`` section.
    """

    def __init__(self, msg, code=None):
        self.msg = msg
        self.code = code
        self.coded_message = f'{str(code)}: {msg}'

    # def __str__(self):
    #   return f'{self.msg}, {self.code}'


class SimpleClass(object):
    """Simple class object example.

    The summary line for a class docstring should fit on one line.

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

    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration (see __init__ method below).

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes
    ----------
    attribute_string : str
        Description of `attribute_string`.
    attribute_list : :obj:`int`, optional
        Description of `attrribute_list.

    Notes
    -----
    Do not include the `self` parameter in the ``Parameters`` section.

    """

    def __init__(self, param1, param2):
        self.attribute_string = param1
        self.attribute_list = param2

    @property
    def attribute_string(self):
        """Get attribute string.

        Getting or setting the attribute string value will verify the value
        is a string.
        """
        return self._attribute_string

    @attribute_string.setter
    def attribute_string(self, value):
        if not isinstance(value, str):
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
        if not isinstance(value, list):
            raise TypeError('param2 must be a list of strings')
        else:
            for element in value:
                if type(element) != str:
                    raise TypeError('param2 must be a list of strings')
        self._attribute_list = value


class ExampleCMAClass(object):
    """Example class.

    The summary line for a class docstring should fit on one line.

    The __init__ method should be documented in the class level
    docstring

    Parameters
    ----------
    param1 : str
        Description of `param1`.
    param2 : :obj:`list` of :obj:`str`
        Description of `param2`. Multiple
        lines are supported.
    param3 : :obj:`int`, optional
        Description of `param3`.


    Attributes
    ----------
    attribute_string : str
        Description of `attribute_string`.
    attribute_list : :obj:`int`, optional
        Description of `attr2`.
    attribute_integer : str
        Description of `attr1`.
    attr4 : :obj:`int`
        Description of `attr4`.
    attr5 : :obj:`int`, optional
        Description of `attr5`.
    quality :  str, optional
        Description of `quality`.
    metadata :  bool, optional
        Description of `metadata`.
    archive :  bool, optional
        Description of `archive`.
    uniqueid :  int
        Description of `uniqueid`.

    Notes
    -----
    Do not include the `self` parameter in the ``Parameters`` section.

    If the class has public attributes, they should be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration (see __init__ method below).

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    """

    def __init__(self, param1, param2, param3, quality, metadata, archive, uniqueid):
        self.attribute_string = param1
        self.attribute_list = param2
        self.attribute_integer = param3
        self.attr4 = ['attr4']
        self.attr5 = None
        self._quality = quality  # non-public attribute
        self._metadata = metadata  # non-public attribute
        self.archive = archive
        self.uniqueid = uniqueid

    @property
    def attribute_string(self):
        """Get the attribute string.

        Getting or setting the attribute string value will verify the value
        is a string.
        """
        return self._attribute_string

    @attribute_string.setter
    def attribute_string(self, value):
        if not isinstance(value, str):
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
        if not isinstance(value, list):
            raise TypeError('param2 must be a list of strings')
        else:
            for element in value:
                if not isinstance(element, str):
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
        if not isinstance(value, int):
            raise TypeError('param3 must be an integer')
        self._attribute_integer = value

    @property
    def readonly_property(self):
        """str: Get readonly_property.

        Properties should be documented in their getter method.
        """
        return 'readonly_property'

    @property
    def quality(self):
        """str: Get quality.

        Properties should be documented in their getter method.
        """
        # provide read-only attribute, immutable once object created
        return self._quality

    @property
    def metadata(self):
        """str: Get metadata.

        Properties should be documented in their getter method.
        The setter raises an exception if modification is attempted.
        """
        # provide read-only attribute, immutable once object created
        return self._metadata

    # setter used to raise custom exceptions if user attempts modification
    @metadata.setter
    def metadata(self, value):
        raise Exception('Metadata is read-only and cannot be modified')

    # set data as valid if object has metadata and quality is High
    @property
    def valid(self):
        """str: Get valid.

        Properties should be documented in their getter method.
        """
        if self.quality == 'High' and self.metadata is True:
            return 'valid'
        else:
            return 'invalid'

    @property
    def archive(self):
        """Get archive.

        Properties with both a getter and setter
        should only be documented in their getter method.

        If the setter method contains notable behavior, it should be
        mentioned here.
        """
        return self._archive

    @archive.setter
    def archive(self, value):
        if not isinstance(value, bool):
            raise TypeError('archive must be True or False')
        self._archive = value

    # read-write property
    # status is a useful attribute, does not need to be set during initialisation
    # system code may set dev status on the class
    # if status is set to certain values, the archive attribute is updated
    @property
    def status(self):
        """Get status.

        Properties with both a getter and setter
        should only be documented in their getter method.

        If the setter method contains notable behavior, it should be
        mentioned here.
        """
        if self.archive is True:
            return 'Production'
        else:
            return 'development'

    # if status is reset to development, then archive is modified
    @status.setter
    def status(self, value):
        if value not in ['development', 'Production']:
            raise ValueError('Status must be Production or development')
        if value == 'development':
            self.archive = False
        else:
            pass

    # write-only example (cant read or access, once created)
    @property
    def uniqueid(self):
        """Get unique ID.

        Properties with both a getter and setter
        should only be documented in their getter method.

        If the setter method contains notable behavior, it should be
        mentioned here.

        The setter method validates the value is an integer.
        The getter method raises an error. This attribute is write-only.
        """
        raise AttributeError('Unique ID is write-only')

    @uniqueid.setter
    def uniqueid(self, value):
        # check the value is an integer
        try:
            isinstance(value, int) is True
        except TypeError:
            raise TypeError('Unique Id must be an integer')
        # check the value is unique
        # TODO

    def example_method(self, param1: int, param2: int) -> bool:
        """Class methods are similar to regular functions.

        Parameters
        ----------
        param1
            The first parameter.
        param2
            The second parameter.

        Returns
        -------
        bool :bool
            True if successful, False otherwise.

        Notes
        -----
        Do not include the `self` parameter in the ``Parameters`` section.

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


class ExampleClassAnother(object):
    """An example class.

    The summary line for a class docstring should fit on one line.

    The __init__ method should be documented in the class level
    docstring.

    Parameters
    ----------
    param1 : str
        Description of `param1`.
    param2 : :obj:`list` of :obj:`str`
        Description of `param2`. Multiple
        lines are supported.
    param3 : :obj:`int`, optional
        Description of `param3`.


    Notes
    -----
    If the class has public attributes, they should be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section.

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes
    ----------
    attribute_string : str
        Description of `attribute_string`.
    attribute_list : :obj:`int`, optional
        Description of `attribute_list.
    attribute_integer : str
        Description of `attribute_integer`.
    """

    # Class attributes

    # Accessed e.g. by ExampleClassAnother.reference_period
    reference_period = '1990-2020'
    """str: Description of `reference_period` (class attribute)."""

    # Class attribute (convention indicates constant)
    QC_LEVEL = 'High'
    """str: Description of `QC_LEVEL`(class attribute: CONSTANT)."""

    def __init__(self, param1, param2, param3):
        self.attribute_string = param1
        self.attribute_list = param2
        self.attribute_integer = param3

    def example_method(self, param1: int, param2: int) -> bool:
        """Class methods are similar to regular functions.

        Parameters
        ----------
        param1
            The first parameter.
        param2
            The second parameter.

        Returns
        -------
        bool :bool
            True if successful, False otherwise.

        Notes
        -----
        Do not include the `self` parameter in the ``Parameters`` section.

        """
        return True
