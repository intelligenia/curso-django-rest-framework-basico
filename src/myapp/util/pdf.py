# -*- coding: utf-8 -*-

import os
import urllib

########################################################################

from django.core import mail
from django.http import HttpResponse
from django.template import loader, Context, RequestContext

########################################################################

from wkhtmltopdf import pdfrenderer


def get_pdf(template, context={}, request=None, config={}):
	"""Devuelve el contenido binario del documento PDF generado."""
	
	if request:
		context_class = RequestContext(request, context)
	else:
		context_class = Context(context)
	
	html_content = loader.get_template(u'{0}.html'.format(template)).render(context_class).encode("utf-8")
	
	pdfs = []

	pdf = pdfrenderer.renderString(html_content, **config)
	
	# Abrir stream para lectura y borrar fichero PDF en disco
	pdf_content = open(pdf, 'rb')
	os.unlink(pdf)

	return pdf_content


def hptt_download_pdf(title, template, context={}, request=None, mode="download", config={}):
	"""Genera una respuesta HTTP para descarga de un PDF."""

	# Generamos el PDF a partir de los tickets cargados.
	pdf_content = get_pdf(template, context, request, config)
	
	if mode == "inline":
		mode_name = "inline"
	elif mode == "download":
		mode_name = "attachment"
	
	unicode_title = unicode(title)
	percentage_encoded_unicode_title = urllib.quote(unicode_title.encode("utf-8"))
	
	header = u'{mode}; filename={filename}.pdf; filename*=UTF-8\'\'{filename}.pdf;'.format(
		filename=percentage_encoded_unicode_title, mode=mode_name)
	
	response = HttpResponse(pdf_content, content_type='application/pdf')
	response['Content-Disposition'] = header
	
	# Devolvemos la respuesta con el PDF con los tickets
	return response
