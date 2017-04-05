# -*- coding: utf-8 -*-


from django.core.paginator import Paginator, InvalidPage


########################################################################
########################################################################


def paginate(request, object_list, per_page=10, page_param="page"):
	"""Pagina un listado de objetos"""
	
	paginator = Paginator(object_list, per_page)
	
	page_number = request.GET.get(page_param)
	
	try:
		page = paginator.page(page_number)
	except InvalidPage:
		page = paginator.page(1)
	
	return page


def check_parity(integer):
	"""
	Comprueba la paridad de un enetero pasado como parámetro.
	Devuelve True si es Par y False si es impar.
	No comprueba que lo que se pase sea un entero.
	"""
	return not (integer & 1)


def is_even(integer):
	"""Comprueba si el entero pasado como parámetro es par."""
	
	return check_parity(integer) is True


def is_odd(integer):
	"""Comprueba si el entero pasado como parámetro es impar"""
	
	return check_parity(integer) is False


def remove_duplicates(seq): 
	"""Elimina duplicados de un listado manteniendo el orden.
	
	No es la forma más eficiente de quitar los duplicados de una lista, pero sí
	la de hacerlo manteniendo el orden
	http://www.peterbe.com/plog/uniqifiers-benchmark
	
	Si no se desea conservar el orden, basta con hacer list(set(lista_original))
	para eliminar los duplicados.
	
	"""
	
	visited = {}
	result = []
	for item in seq:
		if not item in visited:
			visited[item] = 1
			result.append(item)
	return result
