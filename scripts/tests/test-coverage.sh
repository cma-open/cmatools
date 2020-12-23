#!/bin/bash

echo "--------------------------------"
echo "Test coverage"
testdir="$(dirname "$PWD")"
echo "$testdir"
echo "--------------------------------"

cd "$testdir"

# Discover and run tests on code path,  -v verbose flag, with coverage stats
coverage run -m pytest  $testdir
# Generate test report
coverage report -m
coverage html
# Open test coverage report with firefox
firefox  logs/tests/htmlcov/index.html