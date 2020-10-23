#!/usr/bin/env bash
EXIT_STATUS=0
export TEST_ENV=1
export GAIN_ENV=test
rm -f .coverage
pytest || EXIT_STATUS=$?

exit ${EXIT_STATUS}
