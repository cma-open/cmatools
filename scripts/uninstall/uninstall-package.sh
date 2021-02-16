#!/bin/bash

######################################################################################################################
# Script for development use - uninstalls the package and deletes local files
# Ensures clean installs for testing
######################################################################################################################

# Set python package root dir as script constant
readonly CODE_DIR="$(dirname "$(dirname "${PWD}")")"
readonly PACKAGE="cmatools"

# Ask user if they want to continue?
echo ""
read -p "This script will remove the package from any local dev install and from site-packages. \
Continue? (Y/y to continue)" -n 1 -r
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    exit 1
else
  echo "---"
fi

# Check current install status
#if python -c "import pkgutil; exit(not pkgutil.find_loader(${PACKAGE}))"; then
if python -c 'import pkgutil; exit(not pkgutil.find_loader("cmatools"))'; then
    echo "Package: ${PACKAGE} is installed"
    PACKAGE_DIR=$(python -c 'import inspect; \
    import pathlib; import cmatools; \
    package = pathlib.Path(inspect.getfile(cmatools)); \
    print(str(package.parent)) \
    ')
    echo "Package installed: ${PACKAGE_DIR}"
    echo " --- "
    pip uninstall -y "${PACKAGE}"
else
    echo "---"
    echo "Package: ${PACKAGE} is not installed"
    echo "---"
    sleep 4
fi

# Also remove any remaining local files
echo "Removing local dev install files, if present at: ${CODE_DIR}"
echo "Removing .egg-info directory, if present"
rm -rf $CODE_DIR/cmatools.egg-info
echo "Removing build directory, if present"
rm -rf $CODE_DIR/build
echo "Removing dist directory, if present"
rm -rf $CODE_DIR/dist