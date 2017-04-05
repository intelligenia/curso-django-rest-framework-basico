# -*- coding: utf-8 -*-

import pytz

from django.conf import settings
from django.utils import dateparse

########################################################################
########################################################################


def localize_naive_datetime(datetime):
	"""Convierte un datetime "naive" en uno "aware" (en timezone UTC) con el 
	timezone especificado en settings"""

	server_tz = pytz.timezone(settings.TIME_ZONE)
	aware_datetime = server_tz.localize(datetime)
	return aware_datetime.astimezone(pytz.utc)


def localize_datetime_from_string(str_datetime):
	"""Convierte un datetime pasado como un string en un objeto datetime "aware"."""
	
	datetime = dateparse.parse_datetime(str_datetime)
	return localize_naive_datetime(datetime)


def get_datetime_range_from_date(date):
	"""A partir de un objeto "date" de tipo "naive" se devuelven los dos datetimes
	que definen el intervalo a utilizar para consultar esa fecha en BD en 
	un campo de tipo datetime. Ambos datetimes serán "aware" y en UTC
	
	Con un ejemplo:
	Queremos consultar en un campo de tipo datetime los elementos creados el día
	"2014-03-19". Para poder consultar con un BETWEEN (range en Django), 
	hay que consultar entre "2014-03-19 00:00:00" y
	"2014-03-19 23:59:59" pero como django almacena en BD los datetime convertidos
	a UTC, realmente hace falta consultar (en el caso de España) entre estas dos
	fechas: "2014-03-18 23:00:00" y "2014-03-19 22:59:59" (aquí varía una hora
	por la fecha seleccionada, pero pueden ser 2 si es horario de invierno).
	Estas fechas son las que se devuelven aquí.
	
	"""
	
	dt1 = "{} 00:00:00".format(date)
	dt2 = "{} 23:59:59".format(date)
	
	adt1 = localize_datetime_from_string(dt1)
	adt2 = localize_datetime_from_string(dt2)
	
	return (adt1, adt2)


def aware_datetime_to_utc(aware_datetime):
	"""Convierte un datetime aware, que esté en cualquier timezone, al timezone utc"""
	
	utc = pytz.utc

	return aware_datetime.astimezone(utc)


# CÓDIGOS DE EJEMPLO DE LA DOCUMENTACIÓN DE DJANGO Y OTROS SITIOS DE CÓMO OPERAR
# CORRECTAMENTE CON FECHAS


# A ESTE EJEMPLO LE FALTA LA CONVERSIÓN A UTC antes de realizar la consulta. 
# Creo que django la hace de forma
# implícita pero en la documentación recomiendan trabajar con fechas aware en UTC
# así que es mejor añadirla de forma explícita para asegurar.
# Se muestra cómo hacer una consulta sobre un campo de tipo datetime para seleccionar
# "cosas" registradas en un día determinado (se selecciona todo lo que está comprendido
# entre el primer segundo del día y el último).
#~ >>> 
#~ >>> import pytz
#~ >>> s1 = '2012-05-03 00:00:00' # start time
#~ >>> s2 = '2012-05-03 23:59:59' # end time, together covers 1 day
#~ >>> la = pytz.timezone('America/Los_Angeles')
#~ >>> n1 = parse_datetime(s1) # naive object
#~ >>> n2 = parse_datetime(s2)
#~ >>> aware_start_time = la.localize(n1) # aware object
#~ >>> aware_end_time = la.localize(n2)
#~ >>> MyModel.objects.filter(timestamp__range=(aware_start_time, aware_end_time))) # 'timestamp' is a datetime field


################################################################################

# Aquí se está convirtiendo un datetime "naive" en otro "aware" en el timezone
# de París y posteriormente se está convirtiendo al datetime de Nueva York
#~ >>> import datetime
#~ >>> import pytz
#~ >>> paris_tz = pytz.timezone("Europe/Paris")
#~ >>> new_york_tz = pytz.timezone("America/New_York")
#~ >>> paris = paris_tz.localize(datetime.datetime(2012, 3, 3, 1, 30))
#~ # This is the correct way to convert between time zones with pytz.
#~ >>> new_york = new_york_tz.normalize(paris.astimezone(new_york_tz))
#~ >>> paris == new_york, paris.date() == new_york.date()

################################################################################

# Varios ejemplos de trabajo con datetimes "aware"
#~ import pytz
#~ import datetime as DT
#~ 
#~ eastern = pytz.timezone('US/Eastern')
#~ utc = pytz.utc
#~ test = '2013-03-27 23:05'
#~ This is a "naive" datetime:
#~ 
#~ test2 = DT.datetime.strptime(test, '%Y-%m-%d %H:%M')   
#~ print(test2)
#~ # 2013-03-27 23:05:00

#~ This makes a timezone-aware datetime by interpreting test2 as if it were in the EST timezone: 
#~ print(eastern.localize(test2))
#~ # 2013-03-27 23:05:00-04:00

#~ This makes a timezone-aware datetime by interpreting test2 as if it were in the UTC timezone: 
#~ print(utc.localize(test2))
#~ # 2013-03-27 23:05:00+00:00

#~ Alternatively, you can convert one timezone-aware datetime to another timezone using the astimezone method: 
#~ test2_eastern = eastern.localize(test2)
#~ print(test2_eastern.astimezone(utc))
#~ # 2013-03-28 03:05:00+00:00
