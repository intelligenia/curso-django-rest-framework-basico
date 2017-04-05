# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import *
from django.db import models
from django.db.models import Sum, Q, Min, Max , F
from django.db import connection
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

import datetime
from datetime import date
from dateutil import relativedelta

########################################################################

from myapp.util import models_base
from location import models as location_models

########################################################################
########################################################################

class Member(models_base.CommonModel):
	first_name = models.CharField(max_length=140)
	last_name = models.CharField(max_length=140)
	phone = models.CharField(max_length=15)
	email = models.EmailField(max_length=140)
	
	town = models.ForeignKey(location_models.Town, related_name="members", default=None, null=True)
	user = models.OneToOneField(User, related_name="member", null=True, on_delete=models.CASCADE)

	def save(self, *args, **kwargs):
		if self._state.adding:
			self.user = User.objects.create_user(self.email, password=self.email)

		super(Member, self).save(*args, **kwargs)
	
