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
from myapp.util import string as util_string
from location import models as location_models
from myapp.apps.crm.models import Customer
from myapp.apps.hr.models import Member

########################################################################
########################################################################


class Project(models_base.CommonModel):
	name = models.CharField(max_length=140)
	description = models.CharField(max_length=256)
	manager = models.ForeignKey(Member, related_name="projects_manager", null=True, default=None)
	
	members = models.ManyToManyField(Member, related_name="projects")
	customer = models.ForeignKey(Customer, related_name="projects", null=False)	
	
class FlowStep(models_base.CommonModel):
	project = models.ForeignKey(Project, related_name="flow_steps", null=False, on_delete=models.CASCADE)
	name = models.CharField(max_length=140)
	description = models.CharField(max_length=256)
	order = models.PositiveIntegerField("order", null=False, default=1)
	
	class Meta:
		ordering = ('order',)
	
	def save(self, *args, **kwargs):
		if self._state.adding:
			self.order = self.project.flow_steps.count()+1

		super(FlowStep, self).save(*args, **kwargs)
		
	def delete(self, *args, **kwargs):
		self.get_class().objects.filter(project=self.project,
			order__gt=self.order).update(order=F("order")-1)
			
		super(FlowStep, self).delete(*args, **kwargs)
		
	def down(self):
		next = self.get_class().objects.filter(project=self.project, order=self.order+1)
		if next.count()>0:
			next = next[0]
			next.order = self.order
			self.order = self.order+1
			next.save()
			self.save()
	
	def up(self):
		prev = self.get_class().objects.filter(project=self.project, order=self.order-1)
		if prev.count()>0:
			prev = prev[0]
			prev.order = self.order
			self.order = self.order-1
			prev.save()
			self.save()
		
class Task(models_base.CommonModel):
	flow_step = models.ForeignKey(FlowStep, 
									related_name="tasks", 
									null=False, 
									on_delete=models.CASCADE)
	name = models.CharField(max_length=140)
	description = models.CharField(max_length=256)
	order = models.PositiveIntegerField("order", null=False, default=1)
	deadline = models.DateField(null=True, default=None)
	members = models.ManyToManyField(Member, related_name="tasks")
	
	class Meta:
		ordering = ('order',)
	
	def save(self, *args, **kwargs):
		if self._state.adding:
			self.order = self.flow_step.tasks.count()+1

		super(Task, self).save(*args, **kwargs)
		
	def delete(self, *args, **kwargs):
		self.get_class().objects.filter(flow_step=self.flow_step,
			order__gt=self.order).update(order=F("order")-1)
			
		super(Task, self).delete(*args, **kwargs)

	def down(self):
		next = self.get_class().objects.filter(flow_step=self.flow_step, order=self.order+1)
		if next.count()>0:
			next = next[0]
			next.order = self.order
			self.order = self.order+1
			next.save()
			self.save()
	
	def up(self):
		prev = self.get_class().objects.filter(flow_step=self.flow_step, order=self.order-1)
		if prev.count()>0:
			prev = prev[0]
			prev.order = self.order
			self.order = self.order-1
			prev.save()
			self.save()
	
class Comment(models_base.CommonModel):
	task = models.ForeignKey(Task, related_name="comments", null=False, on_delete=models.CASCADE)
	member = models.ForeignKey(Member, related_name="comments", null=False, on_delete=models.CASCADE)
	
	comment = models.TextField(blank=False)
	
	class Meta:
		ordering = ('creation_datetime',)

