# -*- coding: utf-8 -*-

##################################################
### Módulos de Python
# Módulo para sacar en JSON
import json
from django.http import HttpResponse

########################################################################
########################################################################


def get_request_body(request):
	"""Obtiene el cuerpo de la petición POST"""
	# Carga de los datos enviado por POST
	return json.loads(request.body)


########################################################################
########################################################################

def json_error_response(error_type, system, message, extra_attributes=None, status_code=200):
	"""Devuelve una respuesta HTTP con información de error en formato JSON"""
	error = {"status": "error", "error_type": error_type, "system": system, "msg": message}
	if extra_attributes is not None:
		for key in extra_attributes:
			error[key] = extra_attributes[key]
	json_with_error = json.dumps(error)
	return HttpResponse(json_with_error, status=status_code)


def response_not_allowed(system, message, extra_attributes=None, status_code=200):
	"""Devuelve una respuesta HTTP con información del error de permisos en formato JSON"""
	return json_error_response("not_allowed", system, message, extra_attributes, status_code)


def response_bad_request(system, message, extra_attributes=None, status_code=200):
	"""Devuelve una respuesta HTTP con información del error de petición mal formada en formato JSON"""
	return json_error_response("bad_request", system, message, extra_attributes, status_code)


def response_impossible_request(system, message, extra_attributes=None, status_code=200):
	"""Devuelve una respuesta HTTP con información del error de petición imposible en formato JSON"""
	return json_error_response("impossible_request", system, message, extra_attributes, status_code)

########################################################################
########################################################################


def response_ok_with_attrs(message=None, extra_attributes=None, status_code=200):
	"""Devuelve una petición correcta"""
	ok = {"status": "ok", "msg": message}
	if extra_attributes is not None:
		for key in extra_attributes:
			ok[key] = extra_attributes[key]

	json_ok = json.dumps(ok)
	return HttpResponse(json_ok, status=status_code)


def response_ok(content=None, status_code=200):
	if status_code == 204:
		return HttpResponse(status=status_code)
	json_ok = json.dumps(content)
	return HttpResponse(json_ok, mimetype="application/json", status=status_code)