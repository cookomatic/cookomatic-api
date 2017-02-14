#!/usr/bin/env bash

if [[ $RUN_PYLINT == true ]]
then
    export PYTHONPATH="${PYTHONPATH}:$(realpath ~/google-cloud-sdk/platform/google_appengine)"
    export PYTHONPATH="${PYTHONPATH}:$(realpath ~/google-cloud-sdk/platform/google_appengine/lib/yaml/lib)"

    echo -e "\n### Running pylint"
    pylint cookomatic_api --ignore tests --disable=no-member --disable too-few-public-methods --disable unused-argument --disable invalid-name
    pylint cookomatic_api/tests --disable=no-member --disable too-few-public-methods --disable unused-argument --disable missing-docstring --disable protected-access --disable duplicate-code
fi
