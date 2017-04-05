# -*- coding: utf-8 -*-
from django.db import models
from myapp.util import models_base
from location import models as location_models

########################################################################

class Customer(models_base.CommonModel):
	company_name = models.CharField(max_length=140)
	contact_person = models.CharField(max_length=140)
	contact_phone = models.CharField(max_length=15)
	contact_email = models.EmailField(max_length=140)
	
	town = models.ForeignKey(location_models.Town, related_name="customers", default=None, null=True)
	

