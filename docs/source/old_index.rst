.. cmatools documentation master file, created by
   sphinx-quickstart on Tue May 12 15:49:37 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

CMATOOLS Documentation
======================

The CMATOOLS python package was developed for training use, not for production.

This package, and associated subpackages, provide a range of commonly used functions,for import and use in
CMA projects. The content and structure is initially sparse and basic and will be extended over time.

The package and the associated GitHub repository can also serve as a template project on which to start and
reconfigure new projects.


.. toctree::
   :maxdepth: 1

   userguide/gettingstarted
   userguide/userguide
   userguide/examplecode
   developersguide/developersguide
   changelog
   readme

CMATOOLS package
----------------

The content of the cmatools package, subpackages and modules.

.. autosummary::
   :toctree: _autosummary
   :template: custom-module-template.rst
   :recursive:

   cmatools
   tests


CMATOOLS cli
------------

The command line tools and options available from cmatools.

.. toctree::
   :maxdepth: 3

   cmd/cmd



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
