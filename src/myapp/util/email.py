# -*- coding: utf-8 -*-

from django.conf import settings
from django.core import mail
from django.template import loader, Context, RequestContext


########################################################################
########################################################################


def get_email(to_email, subject, template, from_email=settings.DEFAULT_FROM_EMAIL, context={}, request=None, smtp_config_name=None):
	"""Instancia un objeto de EmailMultiAlternative a partir de los datos recibidos."""
	
	if not isinstance(to_email, list) and not isinstance(to_email, dict):
		to_email = [to_email]
	
	if request:
		context_class = RequestContext(request, context)
	else:
		context_class = Context(context)
	
	# Si se recibe el nombre de una configuración SMPT a utilizar, creamos
	# una conexión con los datos indicados en la misma.
	# También intentamos obtener el from_email por si fuera diferente para
	# cada conexión.
	connection = None
	from_email = settings.DEFAULT_FROM_EMAIL
	
	print smtp_config_name
	
	try:
		smtp_config = settings.SMTP_CONFIG
	except:
		smtp_config = None
	
	if smtp_config and smtp_config_name and smtp_config_name in settings.SMTP_CONFIG:
		
		use_tls = False
		use_ssl = False
		
		if "use_tls" in settings.SMTP_CONFIG[smtp_config_name]:
			use_tls = settings.SMTP_CONFIG[smtp_config_name]["use_tls"]
		
		if "use_ssl" in settings.SMTP_CONFIG[smtp_config_name]:
			use_ssl = settings.SMTP_CONFIG[smtp_config_name]["use_ssl"]
		
		connection = mail.get_connection(
			host=settings.SMTP_CONFIG[smtp_config_name]["host"],
			port=settings.SMTP_CONFIG[smtp_config_name]["port"],
			username=settings.SMTP_CONFIG[smtp_config_name]["username"],
			password=settings.SMTP_CONFIG[smtp_config_name]["password"],
			use_tls=use_tls, use_ssl=use_ssl, fail_silently=False)
		
		if "from_email" in settings.SMTP_CONFIG[smtp_config_name]:
			from_email = settings.SMTP_CONFIG[smtp_config_name]["from_email"]
	
	text_content = loader.get_template(u'{0}.txt'.format(template)).render(context_class)
	html_content = loader.get_template(u'{0}.html'.format(template)).render(context_class)
	msg = mail.EmailMultiAlternatives(subject, text_content, from_email, to_email, connection=connection)
	msg.attach_alternative(html_content, "text/html")
	
	return msg


def send_email(to_email, subject, template, from_email=settings.DEFAULT_FROM_EMAIL, context={}, request=None, smtp_config_name=None):
	"""Envío de un email."""

	msg = get_email(to_email, subject, template, from_email, context, request, smtp_config_name)
	msg.send()


def send_emails(emails_config):
	"""Envío de varios emails haciendo uso de una única conexión."""
	
	if emails_config:
		
		connection = mail.get_connection()
		emails = [get_email(**email_config) for email_config in emails_config]
		connection.send_messages(emails)
