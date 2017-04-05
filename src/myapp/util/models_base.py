# -*- coding: utf-8 -*-

###########################################

## Importaciones de Django
from django.db import models

# Validadores de los modelos
from django.core.validators import *

########################################################################

## Modelo abstracto que todo otro modelo implementa
class CommonModel(models.Model):
	"""Modelo de los general para entidades del sistema de tickets"""

	creation_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación del objeto")
	last_update_datetime = models.DateTimeField(auto_now=True, verbose_name="Fecha de última actualización del objeto")
	#is_deleted = models.BooleanField(default=False, verbose_name="¿Eliminado?", help_text="Si lo marca se borrará el elemento.")

	## Metainformación sobre el modelo común
	class Meta:
		abstract = True

	def __unicode__(self):
		return "{0}".format(self.id)

	@classmethod
	def meta(cls):
		"""Obtiene la metainformación de objetos de este modelo."""
		return cls._meta

	@classmethod
	def get_table_name(cls):
		"""Obtiene el nombre de la tabla asociada al modelo."""
		return cls.meta().db_table

	def get_class(self):
		"""Obtiene el objeto clase de este modelo."""
		return self.__class__

	def get_class_name(self):
		"""Obtiene el nombre de la clase de objetos de este modelo."""
		return self.__class__.__name__

	def has_attribute(self, field):
		"""Comprueba si el atributo existe en el objeto."""
		return field in self.__dict__
