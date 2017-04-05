#!/bin/bash

. ./start_venv.sh
pushd src
python ./manage.py test -v3
popd
