# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url, include
from rest_framework import routers


from myapp.apps.crm.views import *

router = routers.DefaultRouter()
router.register(r'customer', CustomerView)

urlpatterns = patterns("",	
	url(r'^', include(router.urls)),
)
