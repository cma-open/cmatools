import setuptools

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
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        #"License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    # include_package_data = True,
    # entry_points
)