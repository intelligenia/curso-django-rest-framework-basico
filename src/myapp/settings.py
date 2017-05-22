# -*- coding: utf-8 -*-

# Django settings for MyAPP project.


import os

import intelligenia_settings
from intelligenia_util import deploy 
deploy.apply_intelligenia_settings_local()

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

DEBUG = deploy.IS_DEVELOPMENT
ENABLE_DEBUG_TOOLBAR=deploy.IS_DEVELOPMENT
TEMPLATE_DEBUG = DEBUG

#BASE_DIR se puede usar como ruta absoluta a la carpeta de inicio del proyecto Django
BASE_DIR = deploy.DEPLOYMENT_DIR

DOMAIN = intelligenia_settings.DOMAIN

# Para los enlaces de los emails, el TPV y demás, necesito componer URLs con el
# nombre de dominio utilizado en frontend. En la variable DOMAIN en explotación
# en dicha variable se almacena como dominio el de backend, lo cual no nos sirve.
if DEBUG:
	FRONTEND_DOMAIN = DOMAIN
else:
	FRONTEND_DOMAIN = "www.myapp.com"

ADMINS = intelligenia_settings.ADMINS

MANAGERS = ADMINS

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
		'NAME': intelligenia_settings.DBNAME, # Or path to database file if using sqlite3.

		'USER': intelligenia_settings.DBUSER,
		'PASSWORD': intelligenia_settings.DBPASSWORD,
		'HOST': intelligenia_settings.DBHOST, # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
		'PORT': intelligenia_settings.DBPORT, # Set to empty string for default.
		'OPTIONS': {
			'init_command': 'SET storage_engine=INNODB',
		}
	}
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = intelligenia_settings.ALLOWED_HOSTS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Madrid'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'es-es'

# En caso de que se utilice la aplicación "Sites", con esta opción se identifica
# cuál es esta web.
SITE_ID = intelligenia_settings.SITE_ID

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = False

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = deploy.MEDIA_ROOT

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
#~ MEDIA_URL = intelligenia_settings.BASE_URI + '/media/'
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'public_html/collectedstatic')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = intelligenia_settings.BASE_URI + '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
	# Put strings here, like "/home/html/static" or "C:/www/django/static".
	# Always use forward slashes, even on Windows.
	# Don't forget to use absolute paths, not relative paths.
	 os.path.join(BASE_DIR, "static/"),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#	'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'dfgh7873h3nnsnsxjxi9xij32n2309s9ksjaj1..22'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
#	 'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.middleware.locale.LocaleMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'myapp.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'apache.wsgi.application'

TEMPLATE_DIRS = (
	# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
	# Always use forward slashes, even on Windows.
	# Don't forget to use absolute paths, not relative paths.
	os.path.join(BASE_DIR, "templates/"),
)

INSTALLED_APPS = (
	#~ "django_extensions",
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	
	
	# Uncomment the next line to enable the admin:
	'django.contrib.admin',
	
	# Uncomment the next line to enable admin documentation:
	# 'django.contrib.admindocs',
	
	'myapp.apps.core',
	'myapp.apps.crm',
	'myapp.apps.hr',
	'myapp.apps.project',
	'rest_framework',
	'rest_framework_swagger',
	'location',
)

# CONTEXT_PROCESSORS
# La idea es que cada vez que se utilice RequestContext se añada el
# context_processor que incluye el "request" en el contexto de un template
# https://docs.djangoproject.com/en/1.4/ref/templates/api/#subclassing-context-requestcontext
# https://docs.djangoproject.com/en/1.4/ref/request-response/#django.http.HttpRequest

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
	'django.core.context_processors.request',
)

# Con esto se reemplaza el "logger" "django.request" que trae django por defecto
# para poder poner "propagate" a True y que se muestren los errores en consola.
# El handler y el filter definidos son los mismos que se encuentran en el array
# de configuración que trae django por defecto pero hay que ponerlos aquí 
# también para que no de error.
if DEBUG:
	LOGGING = {
		'version': 1,
		'disable_existing_loggers': False,
		'filters': {
			'require_debug_false': {
				'()': 'django.utils.log.RequireDebugFalse',
			},
		},
		'handlers': {
			'mail_admins': {
				'level': 'ERROR',
				'filters': ['require_debug_false'],
				'class': 'django.utils.log.AdminEmailHandler'
			}
		},
		'loggers': {
			'django.request': {
				'handlers': ['mail_admins'],
				'level': 'ERROR',
				'propagate': True,
			},
		}
	}


TEST_RUNNER = 'django.test.runner.DiscoverRunner'

################################################################################
################################################################################


LOGIN_URL = '/login/'

LOGOUT_URL = '/'

LOGIN_REDIRECT_URL = '/'


################################################################################
################################################################################


SERVER_EMAIL = intelligenia_settings.SERVER_EMAIL

# Configuración para envío de correos electrónicos
DEFAULT_FROM_EMAIL = intelligenia_settings.DEFAULT_FROM_EMAIL
EMAIL_HOST = intelligenia_settings.EMAIL_HOST
EMAIL_PORT = intelligenia_settings.EMAIL_PORT
EMAIL_HOST_USER = intelligenia_settings.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = intelligenia_settings.EMAIL_HOST_PASSWORD
EMAIL_USE_TLS = intelligenia_settings.EMAIL_USE_TLS

try:
	SMTP_CONFIG = intelligenia_settings.SMTP_CONFIG
	
	# En local, todos los envíos de correos se hacen desde la cuenta de pruebas
	if DEBUG:
		SMTP_CONFIG["default"] = SMTP_CONFIG["testing"]
		SMTP_CONFIG["eevid"] = SMTP_CONFIG["testing"]
		
		EMAIL_HOST = SMTP_CONFIG["testing"]["host"]
		EMAIL_PORT = SMTP_CONFIG["testing"]["port"]
		EMAIL_HOST_USER = SMTP_CONFIG["testing"]["username"]
		EMAIL_HOST_PASSWORD = SMTP_CONFIG["testing"]["password"]
		EMAIL_USE_TLS = SMTP_CONFIG["testing"]["use_tls"]
except:
	pass


################################################################################
################################################################################


# Número de elementos por página en los listados
DEFAULT_PAGE_COUNT = 20


################################################################################
################################################################################


REST_FRAMEWORK = {
	#~ 'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
	"PAGINATE_BY": DEFAULT_PAGE_COUNT,
	"DEFAULT_FILTER_BACKENDS": ("rest_framework.filters.DjangoFilterBackend", 
		"rest_framework.filters.SearchFilter")
}

if not DEBUG:
	REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = ('rest_framework.renderers.JSONRenderer',)


################################################################################
################################################################################


#~ MAX_UPLOAD_FILE_SIZE = 10485760 # Bytes (10MB)
#~ MAX_UPLOAD_IMAGE_SIZE = 5242880 # Bytes (5MB)
#~ IMAGE_EXTENSIONS = ("jpg", "jpeg", "png", "gif")
#~ FILE_EXTENSIONS = ("doc", "pdf", "docx", "odt")


################################################################################
################################################################################


# Modelo a utilizar para reemplazar al model Auth.User
# AUTH_USER_MODEL = 'Auth.User'


# Backends de autenticación que se consultarán para autenticar a un usuario
AUTHENTICATION_BACKENDS = (
	'django.contrib.auth.backends.ModelBackend',
)


################################################################################
################################################################################


LOCALE_PATHS = (
	os.path.join(BASE_DIR, 'locale/'),
)


################################################################################
################################################################################

# Vamos a definir aquí el listado de asuntos de los distintos emails que se
# envían desde la plataforma con la idea de no tenerlos repartidos en los
# distintos archivos
EMAIL_SUBJECTS = {
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

USE_X_FORWARDED_HOST = intelligenia_settings.USE_X_FORWARDED_HOST
SECURE_SSL_REDIRECT = intelligenia_settings.SECURE_SSL_REDIRECT   # Django >= 1.8
SECURE_SSL_HOST = intelligenia_settings.SECURE_SSL_HOST        	# Django >= 1.8
