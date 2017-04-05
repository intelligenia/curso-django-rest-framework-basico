# -*- coding: utf-8 -*-

import urllib

from django.conf import settings
from django.core import mail
from django.template import loader, Context, RequestContext


########################################################################
########################################################################


def get_text(template, context={}, request=None):
	""""""
	
	if request:
		context_class = RequestContext(request, context)
	else:
		context_class = Context(context)
	
	text = loader.get_template(u'{0}.txt'.format(template)).render(context_class)
	
	return text


def send_bulksms(to_number, template, context={}, request=None):
	"""Envío de un email mediante el servicio bulk_sms.
	
	El número de destino "to_number" debe de llevar el código del país antepuesto.
	Por ejemplo, para España, el número tiene que ser de la forma:
	"34666666666".
	
	"""

	text = get_text(template, context, request)
	
	url = "http://bulksms.vsms.net:5567/eapi/submission/send_sms/2/2.0"
	
	params = urllib.urlencode({
		'username': settings.BULKSMS_USER,
		'password': settings.BULKSMS_PASSWORD,
		'message': text,
		'msisdn': to_number
	})
	
	urllib.urlopen(url, params)
