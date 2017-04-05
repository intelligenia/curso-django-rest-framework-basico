# -.- coding: utf-8 -.-

## ----------------------------------------------------------------------------------------
## Módulo con parámetros de configuración por defecto para las aplicaciones
## ----------------------------------------------------------------------------------------
## Las variables aquí definidas se pueden sobreescribir con variables específicas en ell 
## sistema en producción. 
## 
## Todas las variables que se definan en el módulo intelligenia_local.intelligenia_settings_local 
## se importarán y/o sobreescribirán las que estén definidas en este, de manera que aquí 
## se pondrán los valores por defecto utilizados en el sistema de desarrollo y habrá que 
## comunicar al sysadmin cuáles son los valores que hay que definir para el sistema en 
## explotación (p. ej. DEBUG = False, credenciales para el acceso a la BD, cuenta de 
## email para notificaciones, etc). Esta sobreescritura se hace ejecutando un método al
## final de este fichero.
##
## Todas las variables de configuracion finales que utilizará el sistema serán las que
## se definan en el módulo elex.settings, así que para que los valores que indiquemos
## en elex.intelligenia_settings o en el módulo intelligenia_settings_local tengan
## efecto real, es necesario que en el módulo elex.settings dichos valores se
## referencien de la siguiente manera:
## 
## Fichero elex/settings.py
## -----------------------------
## DEBUG = intelligenia_settings.DEBUG
## MEDIA = intelligenia_settings.MEDIA
## ...
## 
## ----------------------------------------------------------------------------------------

import os.path
from intelligenia_util import deploy

## ----------------------------------------------------------------------------------------
## PARÁMETROS DE CONFIGURACIÓN
## ----------------------------------------------------------------------------------------


# URI raíz para los contenidos estáticos
BASE_URI = ""

ADMINS = (
	('Jose Carlos Calvo Tudela', 'josecarlos@intelligenia.com'),
)

# Dominio desde el que se sirve el contenido
DOMAIN = deploy.DOMAIN_NAME if deploy.IS_PRODUCTION else "localhost:8000"
ALLOWED_HOSTS = [ DOMAIN ]

# En caso de que se utilice la aplicación "Sites", con esta opción se identifica
# cuál es esta web.
# NOTA: Cada vez que se vaya a crear una nueva web, se deberá:
# 1- Establecer el SITE_ID oportuno
# 2- Actualizar la tabla django_site
# 3- Insertar tantas entrada en la tabla core_area_site como áreas diferentes tenga asociadas el sitio. 
SITE_ID = 1

# Parámentros de conexión a la BD
DBNAME = "apirest"
DBUSER = "root"
DBPASSWORD = "intelligenia"
DBHOST = ""
DBPORT = ""

SERVER_EMAIL = "mailer@intelligenia.com"
DEFAULT_FROM_EMAIL = "Mailer intelligenia"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "********"
EMAIL_HOST_PASSWORD = "*******"
EMAIL_USE_TLS = True

SMTP_CONFIG = {
	"default": {
		"host": EMAIL_HOST,
		"port": EMAIL_PORT,
		"username": EMAIL_HOST_USER,
		"password": EMAIL_HOST_PASSWORD,
		"use_tls": EMAIL_USE_TLS
	},
	"testing": {
		"host": "smtp.gmail.com",
		"port": 587,
		"username": "********",
		"password": "********",
		"use_tls": True
	}
}


################################################################################
################################################################################


USE_X_FORWARDED_HOST = False
SECURE_SSL_REDIRECT = False   # Django >= 1.8
SECURE_SSL_HOST = None        # Django >= 1.8


## ----------------------------------------------------------------------------------------
## FIN DE PARÁMETROS DE CONFIGURACIÓN
## ----------------------------------------------------------------------------------------
