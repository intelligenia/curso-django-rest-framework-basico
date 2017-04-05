# -.- coding: utf-8 -.-
from rest_framework import serializers, pagination
from rest_framework_recursive.fields import RecursiveField
from myapp.apps.hr.models import *
from myapp.util.serializers import DynamicFieldModelSerializer
from myapp.apps.core.serializers import TownSerializer

class MemberSerializer(DynamicFieldModelSerializer):
		
	town_data = TownSerializer(source="town",many=False, required=False, read_only=True, fields=("id","name"))
	
	class Meta:
		model = Member
		fields = (	'id',
					'first_name',
					'last_name',
					'phone',
					'email',
					'town','town_data'
				)
	
