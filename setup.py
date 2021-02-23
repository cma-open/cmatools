import setuptools

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
    package_dir={"" : "src"},
    # Legacy / Maintenance note: As the package dir is  specified, then don't need to also exclude the tests here
    # However being retained as a failsafe in case future tests are accidentally added in the main package
    packages=setuptools.find_packages(where="src", exclude=["*tests.*", "*tests"]),
    license="BSD",
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: BSD License',
        "Operating System :: OS Independent",
    ],
    # Set minimum python version to allow installation
    python_requires='>=3.9',
    # Set key dependency versions required to allow installation
    install_requires=[
       'scitools-iris>=3.0',  # Note the alternative name for iris when called via pip, c.f. conda-forge
       'numpy>=1.19'
    ],
    # include_package_data = True,

    # Register command line scripts from the relevant package module
    # These are added as command line options once the system is installed
    entry_points={
        'console_scripts': [
            # Name the tool, link to the package function
            'cli-hello='
            'cmatools.cli_hello_world:cli_entry_point',
                        ]
    }
)