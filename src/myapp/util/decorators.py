# -*- coding: utf-8 -*-

from functools import wraps

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test

from rest_framework import status
from rest_framework.response import Response

from elex.apps.core import models
from elex.util import authentication as util_authentication


########################################################################
########################################################################


def group_required(*group_names):
	"""Requiere que el usuario autenticado pertenezca a alguno de los grupos indicados.

	Los grupos (aunque sea sólo uno) deben pasarse como lista o tupla.
	
	"""
	
	def in_groups(u):
		if u.is_authenticated():
			if util_authentication.user_in_group(u, *group_names):
				return True
		return False
	return user_passes_test(in_groups)


def user_type_required(*types):
	"""Requiere que el usuario autenticado sea de alguno de los tipos indicados.
	
	Los tipos (aunque sea uno) deben pasarse como lista o tupla.
	
	"""
	
	def user_type(user):
		if user.is_authenticated():
			if user.type in types or user.is_superuser:
				return True
		return False
	return user_passes_test(user_type)


def rest_login_required(decorated_function):
	"""Decorador para servicios REST que comprueba si el usuario que ejecuta la
	petición está autenticado. Si no lo está devuelve un 403.
	
	Se implimenta ya que para los servicios REST no puede utilizarse el decorador
	login_required de django ya que hace una redirección a una URL determinada.
	
	"""
	
	# Un decorador recibe como parámetro la función decorada (para poder "decorarla",
	# de ahí su nombre).
	# Esta función interna (_wrapped_view) recibe los mismos parámetros que la
	# función decorada con este decorador ya que ésta reemplazará a la
	# decorada.
	# Como los decoradores se definen para ser utilizados con vistas de función,
	# para poder utilizarlos con vistas de clase hace falta utilizar el decorador
	# auxiliar de django "method_decorator", el cual hace la conversión
	@wraps(decorated_function)
	def _wrapped_view(request, *args, **kwargs):
		if not request.user.is_authenticated():
			return Response(status=status.HTTP_403_FORBIDDEN)
		else:
			return decorated_function(request, *args, **kwargs)
	return _wrapped_view


def rest_group_required(group_names):
	"""Decorador para servicios REST que comprueba si el usuario que ejecuta la
	petición pertenece a alguno de los grupos indicados (se pasan separados por comas).
	Al mismo tiempo comprueba que el usuario esté autenticado.
	Si no lo está devuelve un 403.
	
	Se implimenta ya que para los servicios REST no puede utilizarse
	user_passes_test de django ya que hace una redirección a una URL determinada.
	
	"""
	
	# Un decorador recibe como parámetro la función decorada (para poder "decorarla",
	# de ahí su nombre).
	# Esta función interna (_wrapped_view) recibe los mismos parámetros que la
	# función decorada con este decorador ya que ésta reemplazará a la decorada.
	# Este decorador recibe parámetros por lo que la función a devolver, la cual
	# será la función a la que pasará la función a decorada como parámetro
	# (por eso se añade un nuevo nivel "wrap" que recibe la función a ser decorada).
	# Como los decoradores se definen para ser utilizados con vistas de función,
	# para poder utilizarlos con vistas de clase hace falta utilizar el decorador
	# auxiliar de django "method_decorator", el cual hace la conversión
	def wrap(decorated_function):
		@wraps(decorated_function)
		def _wrapped_view(request, *args, **kwargs):
			
			if request.user.is_authenticated():
				if util_authentication.user_in_group(request.user, *group_names):
					return decorated_function(request, *args, **kwargs)
				
			return Response(status=status.HTTP_403_FORBIDDEN)
		
		return _wrapped_view
	return wrap


def rest_user_type_required(types):
	"""Decorador para servicios REST que comprueba si el usuario que ejecuta la
	petición es del tipo o tipos indicados (se pasan separados por comas).
	Al mismo tiempo comprueba que el usuario esté autenticado.
	Si no lo está devuelve un 403.
	
	Esto sólo podrá realizarse cuando se haya reemplazado al modelo de usuario
	por defecto de django "Users" por otro modelo en el que se incluya un campo
	"type" de texto (CharField) en el cual se indique el tipo de usuario.
	
	Se implimenta ya que para los servicios REST no puede utilizarse
	user_passes_test de django ya que hace una redirección a una URL determinada.
	
	"""
	
	# Un decorador recibe como parámetro la función decorada (para poder "decorarla",
	# de ahí su nombre).
	# Esta función interna (_wrapped_view) recibe los mismos parámetros que la
	# función decorada con este decorador ya que ésta reemplazará a la decorada.
	# Este decorador recibe parámetros por lo que la función a devolver, la cual
	# será la función a la que pasará la función a decorada como parámetro
	# (por eso se añade un nuevo nivel "wrap" que recibe la función a ser decorada).
	# Como los decoradores se definen para ser utilizados con vistas de función,
	# para poder utilizarlos con vistas de clase hace falta utilizar el decorador
	# auxiliar de django "method_decorator", el cual hace la conversión
	def wrap(decorated_function):
		@wraps(decorated_function)
		def _wrapped_view(request, *args, **kwargs):
			
			if request.user.is_authenticated():
				#~ if util_authentication.user_in_group(request.user, *group_names):
				if (request.user.type in types) | request.user.is_superuser:
					return decorated_function(request, *args, **kwargs)
				
			return Response(status=status.HTTP_403_FORBIDDEN)
		
		return _wrapped_view
	return wrap



#~ def decorator_a(decorated_function):
	#~ @wraps(decorated_function)
	#~ def _wrapped_view(request, *args, **kwargs):
		#~ print "A"
		#~ return decorated_function(request, *args, **kwargs)
	#~ return _wrapped_view
	#~ 
#~ def decorator_b(decorated_function):
	#~ @wraps(decorated_function)
	#~ def _wrapped_view(request, *args, **kwargs):
		#~ print "B"
		#~ return decorated_function(request, *args, **kwargs)
	#~ return _wrapped_view
