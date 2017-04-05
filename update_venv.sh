#!/bin/bash

command -v virtualenv > /dev/null || {
	echo "Debe intalar el paquete 'python-virtualenv'"
	exit 1
}

[ ! -d venv ] && virtualenv venv
source ./venv/bin/activate
[ -f src/requirements.txt ] && pip install -r src/requirements.txt || echo "AVISO: No se ha encontrado el fichero src/requirements.txt, no se actualiza el venv"
