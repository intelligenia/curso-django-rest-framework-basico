# -.- coding: utf-8 -.-
from rest_framework import serializers, pagination
from rest_framework_recursive.fields import RecursiveField
from django.utils.formats import date_format
from django.db.models import Q
import datetime
import json
from myapp.apps.crm.models import *
from myapp.util.serializers import DynamicFieldModelSerializer
from myapp.apps.core.serializers import TownSerializer
from location.models import *

		
class CustomerSerializer(DynamicFieldModelSerializer):
		
	town_data = TownSerializer(source="town",many=False, required=False, read_only=True)
	
	class Meta:
		model = Customer
		fields = (	'id', 
					'company_name', 
					'contact_person', 
					'contact_phone',
					'contact_email',
					'town','town_data'
				)
		
