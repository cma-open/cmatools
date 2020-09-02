#!/bin/bash

testdir="$(dirname "$PWD")"
echo "$testdir"

# Discover and run tests on code path,  -v verbose flag
#pytest -r -l --tb=long  $testdir
#pytest --tb=long  $testdir
pytest -rA  $testdir/tests/integration
