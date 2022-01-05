"""Selected functions, methods and command line tools for use by CMA projects.

The package should be imported directly, e.g.::

    import cmatools as cma

Modules include:

    :mod:`cmatools.analysis.simple_analysis`
        Holds several functions to assist with integer calculation
        :func:`~.analysis_max` , :func:`~.analysis_sum`  and :func:`~.analysis_product`
    :mod:`cmatools.examplesubpackage.example_cmatools`
        The :class:`~.ExampleClass` class contains default cma style docstrings as
        an example of the layout.
        The :meth:`~.ExampleClass.example_method` holds an example class method.
    :mod:`cmatools.io`
        Functions to assist with data input/ouput.

.. note ::
    This is not a full list of the cmatools package content. It is used to show
    active examples of the docstring and cross-reference links within the documentation.

.. note ::
    The documentation has further usage information, including
    a :ref:`userguide_label`

"""

# The example note above uses Sphinx refs to link from the python init to a
# pre-labeled section of the docs

# Some example package level docstrings:
# https://github.com/matplotlib/matplotlib/blob/main/lib/matplotlib/__init__.py
# https://github.com/pandas-dev/pandas/blob/master/pandas/__init__.py
# https://github.com/SciTools/iris/blob/main/lib/iris/__init__.py
# https://github.com/pydata/xarray/blob/main/xarray/__init__.py

# basic docs, exposes list of public API via __all__
# https://github.com/pytest-dev/pytest/blob/main/src/pytest/__init__.py

# basic
# https://github.com/sphinx-doc/sphinx/blob/4.x/sphinx/__init__.py


__version__ = '0.0.1'
