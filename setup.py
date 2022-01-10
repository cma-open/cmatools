"""Setup for the cmatools package."""

import warnings

import setuptools

# TODO add log or better user warning re use of datadir and home directory

warnings.warn(
    "Warning: once installed and used this software will write to "
    "locations in the home directory"
)
warnings.warn(
    "Warning: edit the config.ini to use project specific directory "
    "names, if required"
)
warnings.warn("Info: see user documentation for more details")

# requires pip install . -v
# or python setup.py install


# Use text from the main repo readme for the package long description
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cmatools",
    version="0.0.1",
    author="Jonathan Winn",
    author_email="jonathan.winn@metoffice.com",
    description="Training example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cma-open/cmatools",
    # find and install all packages
    package_dir={"": "src"},
    # Legacy / Maintenance note:
    # As the package dir is  specified, then don't need to also exclude the tests here
    # However retained as a failsafe in case future tests are added in the main package
    packages=setuptools.find_packages(where="src", exclude=["*tests.*", "*tests"]),
    license="BSD",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    # Set minimum python version to allow installation
    python_requires=">=3.9",
    # Set key dependency versions required to allow installation
    install_requires=[
        "scitools-iris>=3.0",  # Note alt name for iris via pip, c.f. conda-forge
        "numpy>=1.19",
    ],
    # Include data files, as listed in MANIFEST.in (e.g. config.ini)
    include_package_data=True,
    # Register command line scripts from the relevant package module
    # These are added as command line options once the system is installed
    entry_points={
        # Name the tool, link to the package function
        "console_scripts": [
            # Name the simple analysis command
            "cli-simple-analysis=" "cmatools.cli_simple_analysis:cli_entry_point",
            # Set the data download command
            "cli-data-download="
            "cmatools.cli_data_download:cli_data_download_entry_point",
            # Set the copernicus data download command
            "cli-copernicus-download="
            "cmatools.cli_copernicus_download:cli_copernicus_download_entry_point",
            # Set function to write out current config to file
            "write-config=" "cmatools.common.write_config:write_config",
        ]
    },
)
