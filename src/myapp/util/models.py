# -*- coding: utf-8 -*-


class ModelBuffer(object):
	"""Clase auxiliar para ser utilizada como una cola temporal en la que introducir
	instancias de modelos de Django con idea de guardarlas en BD en lotes
	mediante el uso del método "bulk_create" cuando se alcanza un determinado
	número de elementos en la cola. Cada vez que se guardan los objetos en BD
	la cola se trunca.
	
	El número de elementos en el que se producirá la inserción se puede indicar
	al instanciar la cola.
	
	No se pueden introducir instancias de diferentes modelos.
	
	"""

	def __init__(self, length=100):
		self.buffer = []
		self.length = length
		self.type = None
		
	def push(self, model_instance):
		"""Introduce un elemento en la cola y realiza el guardado en BD si se
		alcanza la cifra máxima.
		
		"""
		
		if not self.type:
			self.type = type(model_instance)
		else:
			if type(model_instance) != self.type:
				raise TypeError(u"La instancia no es del tipo {}".format(self.type))
		
		self.buffer.append(model_instance)
		
		if len(self.buffer) == self.length:
			self.buffer[0].get_class().objects.bulk_create(self.buffer)
			self.buffer = []
			print "Guarda buffer"
	
	def flush(self):
		"""Método a ejecutar siempre en último lugar para guardar en BD los 
		elementos que queden en la cola y que no han podido ser guardados por
		no haberse alcanzado el límite del buffer.
		
		"""
		
		if len(self.buffer) > 0:
			self.buffer[0].get_class().objects.bulk_create(self.buffer)
			print "Guarda buffer flush"
