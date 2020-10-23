#!/usr/bin/env bash
#####################################################################
# travis won't pull tags which are needed by setuptools-git-version #
# not entirely clear why the below is needed here and not in        #
# other python library repos                                        #
git fetch --depth=10000 --tags                                      #
#####################################################################
git tag -l --points-at HEAD > VERSION
if [ ! -s VERSION ]; then
  echo "No version number specified. Not deploying."
  exit 0
fi
echo -n "Version number: "
cat VERSION
echo
python setup.py sdist
if [ $? -eq 111 ]
then
    echo "found no tags to publish python package for, exiting gracefully"
    exit 0
fi
pip install --upgrade twine
twine upload --repository-url https://pypi.fury.io/gain-bot/ --username "T9j6nuX7inNPGip1D3io" --password "" dist/*  # token is in username in encrypted travis env var
