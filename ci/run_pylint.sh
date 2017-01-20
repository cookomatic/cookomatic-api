#!/usr/bin/env bash

if [[ $RUN_PYLINT == true ]]
then
    echo -e "\n### Running pylint"
    pylint cookomatic_api --ignore tests --disable=no-member --disable too-few-public-methods --disable unused-argument
    pylint cookomatic_api/tests --disable=no-member --disable too-few-public-methods --disable unused-argument --disable missing-docstring --disable protected-access --disable duplicate-code
fi
