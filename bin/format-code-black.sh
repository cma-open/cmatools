#!/bin/bash

codedir="$(dirname "$PWD")"
echo "$codedir"

black $codedir/cmatools
black $codedir/tests