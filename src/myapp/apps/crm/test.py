from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from models import *
from factories import *
from rest_assured.testcases import *


class CustomerTestCase(ReadWriteRESTAPITestCaseMixin, 
						BaseRESTAPITestCase):
	fixtures = ['location/fixtures/initial_data.xml']	
	base_name = 'customer'
	factory_class = CustomerFactory
	update_data = {'contact_person': 'Carlos Calvo'}
	attributes_to_check = ['id', 
							'company_name', 
							'contact_person', 
							'contact_phone', 
							'contact_email']
		
	def get_create_data(self):
		customer = factory.build(dict, FACTORY_CLASS=CustomerFactory)
		customer["town"] = customer["town"].id
		return customer

