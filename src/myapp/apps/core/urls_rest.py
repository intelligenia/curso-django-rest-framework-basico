# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url, include
from rest_framework import routers


from myapp.apps.core.views import *

router = routers.DefaultRouter()
router.register(r'region', RegionView)
router.register(r'province', ProvinceView)
router.register(r'town', TownView)


urlpatterns = patterns("",
	
	url(r'^get_csrf/?$', "myapp.apps.core.views.get_csrf", name="get_csrf"),
	
	url(r'^', include(router.urls)),
)
