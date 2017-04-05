#!/bin/bash

if ! [ -d venv ]; then
	virtualenv venv
fi

./venv/bin/pip install --upgrade pip
./venv/bin/pip install -r src/requirements.txt

