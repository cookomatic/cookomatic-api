#!/usr/bin/env bash

if [[ $RUN_PYLINT == true ]]
then
    echo -e "\n### Running pylint"
    pylint cookomatic_server --ignore tests --disable=no-member --disable too-few-public-methods --disable unused-argument
    pylint cookomatic_server/tests --disable=no-member --disable too-few-public-methods --disable unused-argument --disable missing-docstring --disable protected-access --disable duplicate-code
fi
