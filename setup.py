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
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        #"License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    # include_package_data = True,

    # register command line scripts from the relevant package module
    entry_points={
        'console_scripts': [
            'cli-simple=cmatools.cli_simple:'
            'cli_simple_entry_point',

            'cli-analysis=cmatools.cli_analysis:'
            'cli_analysis_entry_point',
                        ]
    }
)