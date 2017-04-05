# -*- coding: utf-8 -*-

import sys
from optparse import make_option

########################################################################

#~ from datetime import timedelta
from django.db import transaction
from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.utils import translation

########################################################################

from dateutil import relativedelta
from rest_framework import serializers

########################################################################

from elex.apps.core import models

########################################################################
########################################################################


class Command(BaseCommand):
	
	args = u'<period>'
	help = (u"Envía las comunicaciones que requieren comprobaciones a realizar cada intervalo de tiempo definido por <frecuencia>\n"
			u"  <frecuencia>      determina las funciones a ejecutar en función de su frecuencia [5minutes, hourly, daily, weekly, monthly, yearly]\n"
		)
	
	def handle(self, *args, **options):
		
		translation.activate(language='es')
		
		def uprint(unicodeobj): self.stdout.write(unicodeobj)
		
		if len(args) == 0:
			uprint(self.help)
			sys.exit(-1)
		
		period = args[0]
		
		if period == "5minutes":
			pass
		elif period == "hourly":
			pass
		elif period == "daily":
			pass
		elif period == "weekly":
			pass
		elif period == "monthly":
			pass
		elif period == "yearly":
			pass
