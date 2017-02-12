#!/usr/bin/env bash

if [[ $RUN_TESTS == true ]]
then
    echo -e "\n## Running unit tests"
    export PYTHONPATH="${PYTHONPATH}:$(realpath ~/google-cloud-sdk/platform/google_appengine)"
    export PYTHONPATH="${PYTHONPATH}:$(realpath ~/google-cloud-sdk/platform/google_appengine/lib/yaml/lib)"
    nosetests  --with-coverage --cover-package=cookomatic_api --exclude-dir=lib
fi
