#!/bin/bash
# No ejecutar directamente este fichero. Invocar desde shell usando "source":
#
#   $ source start_venv.sh

[ ! -d venv ] && {
	echo "No se ha encontrado en venv. Puede crearlo con ./update_virtualenv.sh"
	exit 1
}

source ./venv/bin/activate
