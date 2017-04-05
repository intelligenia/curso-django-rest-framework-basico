import factory
from models import *
from location.models import *

class ProvinceFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Province
		django_get_or_create = ('iso',)
		
	iso = 'GR'	

