#!/usr/bin/env bash
VERSION=${PYTHON_VERSION:="3.7"}
echo "Installing with python $VERSION"
pipenv --rm
pipenv --python $VERSION
pipenv run pip install -r requirements.txt
