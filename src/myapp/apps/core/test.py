from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from models import *
from factories import *
from rest_assured.testcases import *


class ProvinceTests(ReadRESTAPITestCaseMixin, BaseRESTAPITestCase):
	fixtures = ['location/fixtures/initial_data.xml']	
	base_name = 'province'
	factory_class = ProvinceFactory
	lookup_field = 'iso'
	attributes_to_check = ['iso', 'name']
	
	def test_get_towns(self):
		"""
		Ensure we can get a town object.
		"""
		url = reverse('province-towns', args=[self.object.iso])
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(Town.objects.filter(province=self.object).count(), len(response.data), response.data)
	
	def test_get_towns_detail(self):
		"""
		Ensure we can get a town object.
		"""
		town = Town.objects.filter(province=self.object.iso)[0]
		url = reverse('province-towns', args=[self.object.iso])+town.id.__str__()+"/"
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK, url)
		self.assertEqual(town.name, response.data["name"], url)
	
		
