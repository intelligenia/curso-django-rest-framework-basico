# -*- coding: utf-8 -*-


from django.http import HttpResponse #, Http404, HttpResponseRedirect
from django.db.models import Q

from django.middleware import csrf

from django.shortcuts import render, render_to_response, get_object_or_404, redirect

from django.views.decorators.csrf import csrf_exempt, csrf_protect, ensure_csrf_cookie

from rest_framework import viewsets, generics, mixins
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework import status
from rest_framework.decorators import api_view, detail_route, list_route
from rest_framework.compat import View
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.renderers import JSONRenderer

from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib import auth

from myapp.apps.core.models import *
from myapp.apps.core.serializers import *
from myapp.util.util_json import *

import traceback

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import string
import random

VIEW_NAME = "Core"

## Devuelve el token CSRF
def get_csrf(request):
    return HttpResponse("{0}".format(csrf.get_token(request)), content_type="text/plain")


class RegionView(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
	queryset = Region.objects.all()
	serializer_class = RegionSerializer
	permission_classes = ()
	
	@detail_route(methods=['get', ])
	def provinces(self, request, pk=None):
		self.queryset = Province.objects.filter(region=pk)
		self.serializer_class = ProvinceSerializer
		return self.list(request)
	
class ProvinceView(mixins.ListModelMixin,
					mixins.RetrieveModelMixin, 
                    viewsets.GenericViewSet):
					
	"""
	list:
    Return the province list.
	
	towns:
    Return the towns in the selected province.
	
	town_detail:
    Return the town detail
    """				
					
	queryset = Province.objects.all()
	serializer_class = ProvinceSerializer
	
	@detail_route(methods=['get', ])
	def towns(self, request, pk=None):
		province_towns = Town.objects.filter(province=pk)
		serializer = TownSerializer(province_towns,many=True,fields=('id', 'name', ))
		return Response(serializer.data)
	
	@detail_route(url_path="towns/(?P<town_id>[0-9]+)", methods=['get', ])
	def town_detail(self, request, pk=None, town_id=None):
		town = Town.objects.get(id=town_id)
		serializer = TownSerializer(town)
		return Response(serializer.data)
	
	
class TownView(mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
	"""
    retrieve:
    Return the given town.

    """
	queryset = Town.objects.all()
	serializer_class = TownSerializer
	permission_classes = ()
	
	
