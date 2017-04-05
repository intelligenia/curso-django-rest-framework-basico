# -.- coding: utf-8 -.-
from rest_framework import serializers, pagination
from rest_framework_recursive.fields import RecursiveField
from django.utils.formats import date_format
from django.contrib.auth.models import User
from django.db.models import Q
import datetime
import json
import pytz
from itertools import chain
from myapp.apps.core.models import *
from myapp.util.serializers import DynamicFieldModelSerializer

from location.models import *


class UserSerializer(DynamicFieldModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'first_name', 'last_name', 'email', 'username',)
				
class RegionSerializer(DynamicFieldModelSerializer):
	class Meta:
		model = Region
		fields = ('iso', 'name')
		
class ProvinceSerializer(DynamicFieldModelSerializer):
	town_count =  serializers.SerializerMethodField()
	
	
	def get_town_count(self, obj):
		return Town.objects.filter(province=obj).count()
	
	
	class Meta:
		model = Province
		fields = ('iso', 'name', 'town_count')
		
class TownSerializer(DynamicFieldModelSerializer):
	region = RegionSerializer(source="province.region",many=False, required=False, read_only=True)
	province = ProvinceSerializer(many=False, required=False, read_only=True)
	
	class Meta:
		model = Town
		fields = ('id', 'name', 'province', 'region')
		
