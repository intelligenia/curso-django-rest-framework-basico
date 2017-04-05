import factory
from models import *
from location.models import *

class CustomerFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Customer

	company_name = factory.Faker('company',locale='es_ES')
	contact_person = factory.Faker('name',locale='es_ES')
	contact_phone = "666777888"
	contact_email = "hola@hola.com"
	town = factory.Iterator(Town.objects.all())