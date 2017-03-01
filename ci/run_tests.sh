#!/usr/bin/env bash

if [[ $RUN_TESTS == true ]]
then
    export PYTHONPATH="${PYTHONPATH}:$(realpath ~/google-cloud-sdk/platform/google_appengine)"
    export PYTHONPATH="${PYTHONPATH}:$(realpath ~/google-cloud-sdk/platform/google_appengine/lib/yaml/lib)"

    echo -e "\n## Running unit tests"
    nosetests  --with-coverage --cover-package=cookomatic_api --logging-level=INFO --exclude-dir=lib
fi
