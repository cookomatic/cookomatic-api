#!/usr/bin/env bash

if [[ $RUN_TESTS == true ]]
then
    echo -e "\n## Running unit tests"
    nosetests  --with-coverage --cover-package=cookomatic_api --exclude-dir=lib
fi
