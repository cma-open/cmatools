"""Sphinx config settings."""

# Configuration file for the Sphinx documentation builder.
# This file only contains a selection of the most common options.
# For a full list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

import pkg_resources

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

sys.path.insert(0, os.path.abspath('../../src'))
sys.path.insert(0, os.path.abspath('../..'))


print('------------------')
print('System path:')
print(*sys.path, sep='\n')
print('------------------')

# tests is not installed by setup, therefore import here to ensure available
# by relative import path
import tests  # noqa: F401, E402 isort:skip
import cmatools  # noqa: F401, E402 isort:skip

# -- Project information -----------------------------------------------------

project = 'cmatools'
copyright = '2021, Jonathan Winn'
author = 'Jonathan Winn'
# Take the version nunmber from the package version in setup
release = pkg_resources.get_distribution('cmatools').version

# -- General configuration ---------------------------------------------------
# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    # 'sphinx_autodoc_typehints',  test this later # TODO
    'sphinx.ext.githubpages',
    # 'sphinx.ext.napoleon',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.autosummary',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.doctest',
    'sphinx.ext.coverage',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinxarg.ext',
    'sphinxcontrib.mermaid',
    'numpydoc'
]

# Allow todo panels to be highlighted in outputs docs
# Relates to the sphinx.ext.todo extension
todo_include_todos = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.
# See documentation for a list of builtin themes.
# A commonly used theme rtd (read the docs)
html_theme = 'sphinx_rtd_theme'
# html_theme = 'alabaster' # tested but decided against

numpydoc_attributes_as_param_list = False  # include attributes in a table
numpydoc_xref_param_type = True
numpydoc_xref_aliases = {
    'LeaveOneOut': 'sklearn.model_selection.LeaveOneOut',
}
# TODO add more custom refs here

# numpydoc_validation_checks = {"all"}
# TODO enable later

autosummary_generate = True
# autosummary_imported_members = True
autodoc_member_order = 'groupwise'
autodoc_default_flags = ['show-inheritance']
# autodoc_docstring_signature = True
autoclass_content = 'both'  # Add __init__ doc (ie. params) to class summaries

# TODO test later
add_module_names = False  # Remove namespaces from class/method signatures

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# copy to decision log
# decided numpydoc over napoloeon
# https://numpydoc.readthedocs.io/en/latest/install.html
# TODO check order of class methods and attributes, seem smixed up
# TODO - need to see how other config options impact output format

# Configuration for intersphinx
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'numpy': ('https://numpy.org/devdocs/', None),
    'sklearn': ('https://scikit-learn.org/stable/', None),
    'matplotlib': ('https://matplotlib.org/stable/', None),
}

# Refs
# https://stackoverflow.com/questions/2701998/sphinx-autodoc-is-not-automatic-enough
